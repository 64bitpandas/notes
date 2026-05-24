#!/usr/bin/env python3
"""Count words across all .md files in content/, excluding YAML frontmatter."""

import re
import sys
from pathlib import Path

# Word count of the MCB C61 PDF (not included in markdown sources).
MCBC61_PDF_WORDS = 10981

# Repo-relative content directory.
CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"


def strip_frontmatter(text: str) -> str:
    """Remove a leading YAML frontmatter block delimited by '---' lines."""
    if text.startswith("---"):
        # Match the opening '---' on its own line, then everything up to the
        # next '---' on its own line.
        match = re.match(r"^---\s*\n.*?\n---\s*\n", text, flags=re.DOTALL)
        if match:
            return text[match.end():]
    return text


def count_words(text: str) -> int:
    # Split on any whitespace; filter out empties.
    return sum(1 for tok in text.split() if tok.strip())


def main() -> int:
    if not CONTENT_DIR.is_dir():
        print(f"error: {CONTENT_DIR} does not exist", file=sys.stderr)
        return 1

    per_dir: dict[str, int] = {}
    total = 0
    file_count = 0

    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        try:
            text = md_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = md_path.read_text(encoding="utf-8", errors="replace")

        body = strip_frontmatter(text)
        words = count_words(body)

        rel = md_path.relative_to(CONTENT_DIR)
        top = rel.parts[0] if len(rel.parts) > 1 else "(root)"
        per_dir[top] = per_dir.get(top, 0) + words
        total += words
        file_count += 1

    print(f"Markdown files scanned: {file_count}")
    print()
    print("Words per top-level section:")
    for name in sorted(per_dir):
        print(f"  {name:<20} {per_dir[name]:>8}")
    print()
    print(f"Markdown total:        {total:>10}")
    print(f"MCB C61 PDF (const):   {MCBC61_PDF_WORDS:>10}")
    print(f"Grand total:           {total + MCBC61_PDF_WORDS:>10}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
