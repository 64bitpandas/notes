#!/usr/bin/env python3
# Recommended invocation (no global installs needed):
#   uv run --with anthropic --with pillow scripts/ocr_to_notes.py old/Philosophy\ 5.pdf scripts/philosophy5.json
#
# Requires:
#   - poppler-utils on PATH: pdfseparate, pdfunite, pdftoppm  (brew install poppler)
#   - env var ANTHROPIC_API_KEY set to a valid Anthropic API key
"""OCR a handwritten-notes PDF into a Hugo page-bundle course folder.

Reads a JSON mapping describing which page ranges become which sections,
extracts pages with poppler, OCRs each page with Claude vision, and writes
per-section markdown + section PDFs + a combined PDF into content/<slug>/.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

OCR_MODEL_PRIMARY = "claude-sonnet-4-5"
OCR_MODEL_FALLBACK = "claude-3-5-sonnet-latest"

OCR_PROMPT = (
    "You are transcribing a handwritten college-lecture notebook page. "
    "Output ONLY clean Markdown. Treat the bright/colored, less-indented "
    "text as headings (use `##` for section headings, `###` for "
    "subsections). Treat the rest as body text \u2014 preserve bullet "
    "lists where they appear. Skip page-number markers and decorative "
    "scribbles. Output nothing but the Markdown for this single page; do "
    "not wrap in code fences; do not add commentary."
)

REQUIRED_TOOLS = ("pdfseparate", "pdfunite", "pdftoppm")


def die(msg: str, code: int = 1) -> "None":
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def check_tools() -> None:
    missing = [t for t in REQUIRED_TOOLS if shutil.which(t) is None]
    if missing:
        die(
            "missing required poppler tools on PATH: "
            + ", ".join(missing)
            + "\nInstall with: brew install poppler"
        )


def pdf_page_count(pdf: Path) -> int:
    if shutil.which("pdfinfo") is None:
        # Fall back to a pdfseparate dry probe by trying page 1 only.
        return 10**9
    out = subprocess.run(
        ["pdfinfo", str(pdf)], capture_output=True, text=True, check=True
    ).stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.MULTILINE)
    if not m:
        die(f"could not parse page count from pdfinfo output for {pdf}")
    return int(m.group(1))


def parse_pages(spec: str) -> list[int]:
    spec = spec.strip()
    if "-" in spec:
        lo_s, hi_s = spec.split("-", 1)
        lo, hi = int(lo_s), int(hi_s)
        if lo > hi:
            die(f"invalid page range: {spec}")
        return list(range(lo, hi + 1))
    return [int(spec)]


def run(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        die(
            "command failed: "
            + " ".join(cmd)
            + f"\nstderr: {proc.stderr.strip()}"
        )


def get_anthropic_client():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        die(
            "ANTHROPIC_API_KEY is not set. Export it before running this "
            "script (e.g. `export ANTHROPIC_API_KEY=sk-ant-...`)."
        )
    try:
        from anthropic import Anthropic  # type: ignore
    except ImportError:
        die(
            "anthropic SDK not installed. Re-run with: "
            "`uv run --with anthropic --with pillow scripts/ocr_to_notes.py ...`"
        )
    return Anthropic(api_key=api_key)


def ocr_via_claude(client, png_path: Path) -> str:
    img_b64 = base64.standard_b64encode(png_path.read_bytes()).decode("ascii")
    content = [
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": img_b64,
            },
        },
        {"type": "text", "text": OCR_PROMPT},
    ]
    last_err: Exception | None = None
    for model in (OCR_MODEL_PRIMARY, OCR_MODEL_FALLBACK):
        for attempt in range(3):
            try:
                msg = client.messages.create(
                    model=model,
                    max_tokens=4096,
                    messages=[{"role": "user", "content": content}],
                )
                parts = [b.text for b in msg.content if getattr(b, "type", "") == "text"]
                return "\n".join(p.strip() for p in parts if p).strip()
            except Exception as e:  # noqa: BLE001
                last_err = e
                # Don't retry on model-not-found / 4xx auth; fall through to fallback.
                err_s = str(e).lower()
                if "model" in err_s and ("not found" in err_s or "invalid" in err_s):
                    break
                time.sleep(1.5 * (attempt + 1))
    die(f"OCR failed after retries: {last_err}")
    return ""  # unreachable



def write_index_skeleton(course_dir: Path, title: str, weight: int) -> None:
    course_dir.mkdir(parents=True, exist_ok=True)
    body = (
        "---\n"
        f"linkTitle: \"{title}\"\n"
        f"weight: {weight}\n"
        "BookCollapseSection: true\n"
        "---\n\n"
        "<!-- Combined PDF will be embedded here by scripts/ocr_to_notes.py during the OCR run. -->\n"
    )
    (course_dir / "_index.md").write_text(body)


def write_index_with_embed(course_dir: Path, title: str, weight: int, combined_pdf: str) -> None:
    body = (
        "---\n"
        f"linkTitle: \"{title}\"\n"
        f"weight: {weight}\n"
        "BookCollapseSection: true\n"
        "---\n\n"
        f"<embed src=\"{combined_pdf}\" type=\"application/pdf\" width=\"100%\" height=\"600px\" />\n"
    )
    (course_dir / "_index.md").write_text(body)


def extract_page_png(pdf: Path, page_num: int, section_dir: Path) -> Path:
    page_pdf = section_dir / f"page-{page_num}.pdf"
    run(["pdfseparate", "-f", str(page_num), "-l", str(page_num), str(pdf), str(page_pdf)])
    png_prefix = section_dir / f"page-{page_num}"
    run(["pdftoppm", "-r", "200", "-png", "-f", "1", "-l", "1", str(page_pdf), str(png_prefix)])
    # pdftoppm appends "-1" for single-page output.
    png_path = section_dir / f"page-{page_num}-1.png"
    if not png_path.exists():
        die(f"expected rasterized PNG not found: {png_path}")
    return png_path


def process_section(
    client,
    pdf: Path,
    section: dict,
    course_dir: Path,
    total_pages: int,
) -> Path:
    pages = parse_pages(str(section["pages"]))
    for p in pages:
        if p < 1 or p > total_pages:
            die(f"page {p} out of range 1..{total_pages} for section {section['filename']}")
    section_dir = course_dir / ".tmp" / section["filename"]
    if section_dir.exists():
        shutil.rmtree(section_dir)
    section_dir.mkdir(parents=True)

    page_pdfs: list[Path] = []
    png_paths: list[Path] = []
    for p in pages:
        png_paths.append(extract_page_png(pdf, p, section_dir))
        page_pdfs.append(section_dir / f"page-{p}.pdf")

    section_pdf = course_dir / f"{section['filename']}.pdf"
    if section_pdf.exists():
        section_pdf.unlink()
    if len(page_pdfs) == 1:
        shutil.copyfile(page_pdfs[0], section_pdf)
    else:
        run(["pdfunite", *[str(p) for p in page_pdfs], str(section_pdf)])

    ocr_chunks: list[str] = []
    for png in png_paths:
        ocr_chunks.append(ocr_via_claude(client, png))

    md_path = course_dir / f"{section['filename']}.md"
    body = (
        "---\n"
        f"title: \"{section['title']}\"\n"
        f"weight: {section['weight']}\n"
        "---\n\n"
        f"<embed src=\"{section['filename']}.pdf\" type=\"application/pdf\" width=\"100%\" height=\"600px\" />\n\n"
        + "\n\n".join(ocr_chunks).rstrip()
        + "\n"
    )
    md_path.write_text(body)
    return section_pdf


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf_path", help="Path to the source PDF")
    ap.add_argument("mapping_json", help="Path to the JSON mapping file")
    args = ap.parse_args()

    pdf = Path(args.pdf_path)
    mapping_path = Path(args.mapping_json)
    if not pdf.is_file():
        die(f"PDF not found: {pdf}")
    if not mapping_path.is_file():
        die(f"mapping JSON not found: {mapping_path}")

    check_tools()
    with mapping_path.open() as f:
        mapping = json.load(f)
    course = mapping["course"]
    slug = course["slug"]
    title = course["title"]
    nav_weight = int(course["navbar_weight"])
    sections = mapping["sections"]

    total_pages = pdf_page_count(pdf)
    course_dir = Path("content") / slug
    course_dir.mkdir(parents=True, exist_ok=True)
    (course_dir / ".tmp").mkdir(exist_ok=True)
    write_index_skeleton(course_dir, title, nav_weight)

    client = get_anthropic_client()
    all_section_pdfs: list[Path] = []
    for section in sections:
        print(f"[ocr] {slug}: {section['filename']} (pages {section['pages']})", flush=True)
        all_section_pdfs.append(
            process_section(client, pdf, section, course_dir, total_pages)
        )

    combined_pdf = course_dir / f"{slug}-combined.pdf"
    if combined_pdf.exists():
        combined_pdf.unlink()
    if len(all_section_pdfs) == 1:
        shutil.copyfile(all_section_pdfs[0], combined_pdf)
    else:
        run(["pdfunite", *[str(p) for p in all_section_pdfs], str(combined_pdf)])

    write_index_with_embed(course_dir, title, nav_weight, combined_pdf.name)
    shutil.rmtree(course_dir / ".tmp", ignore_errors=True)

    print(f"\nGenerated {len(sections)} section(s) for {slug}:")
    for section in sections:
        print(f"  - {section['filename']}.md  +  {section['filename']}.pdf")
    print(f"Combined: {combined_pdf}")


if __name__ == "__main__":
    main()
