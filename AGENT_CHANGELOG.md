# Agent Changelog

This file documents the per-file changes applied during the automated review and
edit pass over the course notes. See workspace notes `changelog-phase*` for full
audit detail, including ambiguous items that were considered but skipped.

Commits:
- [`64d219e`](https://github.com/64bitpandas/notes/commit/64d219e55a4782a079a581ec7465410ceab35c79) — Phase 1: formatting and structural fixes
- [`d8dd002`](https://github.com/64bitpandas/notes/commit/d8dd00269af7ddd574bd49d79fdd7432149ebce5) — Phase 2: spelling and grammar
- [`704adf0`](https://github.com/64bitpandas/notes/commit/704adf0485470a1f8cb3ca215a115a6d7b6e3dab) — Phase 3: content corrections
- [`a5b6a3b`](https://github.com/64bitpandas/notes/commit/a5b6a3b0210d3d254ff5369f0faceaf8c82624f2) — Phase 4: psych learning-progression reordering
- [`47c4bcc`](https://github.com/64bitpandas/notes/commit/47c4bccd7fdace61287866e1c89201fcc8b39d38) — Phase 5: cross-course wiki links
- [`d106caf`](https://github.com/64bitpandas/notes/commit/d106cafd8c2c4d2cd54224f349bdd4a2c85b9001) — Phase 6: add AGENT_CHANGELOG.md
- [`0832ed7`](https://github.com/64bitpandas/notes/commit/0832ed775169ff4a3b3eafe21d1056a3c07da670) — Phase 8: fix BFS walk typo (GH #3)

## Phase 1 — Formatting and Structural Fixes

Repaired Markdown/Hugo rendering issues across the course notes: broken header
levels (h1→h3 jumps, missing h2), stray empty bold/italic markers from GitBook
export, broken image references, malformed wikilinks, unclosed inline/display
math, and a handful of dead external links. Verified by Hugo build (0
errors/warnings) and a broken-image-link scan.

### content/cs162/Chapter 1 OS Basics.md
- Promoted three `###` headings to `##` (Four Fundamental OS Concepts, Multiprocessing vs Multiprogramming, Addresses) — fixed h1→h3 jumps.

### content/cs162/Chapter 3 Threads.md
- Promoted four `###` headings to `##` (Thread States, Multithreaded Programs, Fork-Join Parallelism, Race Conditions) — fixed h1→h3 jumps.

### content/cs162/Chapter 4 I O.md
- Promoted four `###` headings to `##` (Reading and Writing, Stream Operations, High vs Low Level IO, Closing Pipes) — fixed h1→h3 jumps.

### content/cs162/Chapter 6 Scheduling.md
- Promoted three `###` headings to `##` (Scheduling Goals, Vocabulary, Deadlock) — fixed h1→h3 jumps.

### content/cs162/Chapter 8 Caching.md
- Promoted two `###` headings to `##` (Thrashing, Memory Access Walkthrough) — fixed h1→h3 jumps under `# Translation Lookaside Buffer (TLB)`.

### content/cs162/Chapter 9 File Systems.md
- Fixed two broken images that pointed to leaked Notion paths (`../../../CS186 Notes <uuid>/...`, `../../CS161 Notes <uuid>/...`) — rewrote to absolute site paths inside `/cs186/` and `/cs161/`.

### content/cs168/interdomain routing (bgp).md
- Demoted lone `# BGP` to `## BGP` — the page already uses `##` for top-level sections; the stray h1 was producing h1→h3 jumps for its children.

### content/cs170/Divide and Conquer (Master Theorem).md
- Replaced a truncated/abandoned `$$c \cdot n^d (` line with a completed `$O(n^d)$` sentence — unclosed display-math delimiter had left the rest of the file in math mode.

### content/cs170/Dynamic Programming.md
- Promoted `### How is this different from recursion though?` to `##` — fixed h1→h3 jump.

### content/cs170/Graphs.md
- Promoted Adjacency Matrix / Adjacency List / Tradeoffs from `###` to `##` — fixed h1→h3 jumps under `# Graph Representations`.

### content/cs170/Horn Formulas.md
- Promoted three `###` subsections to `##` (The Problem: Boolean Expressions, A Special Case, Solving the Special Case) — fixed h1→h3 jumps.

### content/cs170/Search Problems, P NP.md
- Promoted `### NP-hard and NP-complete` (L44) and `### A general problem-solving method` (L157) to `##` — fixed h1→h3 jumps.

### content/cs170/Zero-Sum Games.md
- Promoted `### Example (discussion 9)` to `##` — fixed h1→h3 jump.

### content/cs186/05 Iterators and Joins.md
- Fixed broken image: moved Obsidian-style `|300` width hint out of the URL angle brackets into the alt text so Hugo's `render-image.html` width parser recognises it.

### content/cs188/Machine Learning.md
- Promoted `### Maximum Likelihood Estimation` and `### Laplace Smoothing` to `##` — fixed h1→h3 jumps under `# Naive Bayes`.

### content/cs188/Utilities and Decision Trees.md
- Promoted `### Maximum Expected Utility Equations` to `##` — fixed h1→h3 jump.

### content/cs61b/_index.md
- Unescaped tilde in `inst.eecs.berkeley.edu/~cs61b` URL — backslash-escape was breaking the link.
- Promoted `### The 61B Concept Map` to `##` — fixed h1→h3 jump.
- Replaced wikilink `[[/cs61a|Click here]]` with standard Markdown link — Hugo does not render wikilink syntax here.
- Removed `.md` extensions from two internal links to match adjacent working links.

### content/cs61b/abstract-data-types/binary-trees/_index.md
- Removed stray empty `****` bold marker before `$\Theta(1)$`.
- Removed `.md` from four internal links (tries, hashing, dfs, bfs).

### content/cs61b/abstract-data-types/binary-trees/heaps.md
- Removed stray empty `****` bold marker — GitBook export artifact.

### content/cs61b/abstract-data-types/collections/stacks-and-queues.md
- Unescaped underscores in `tutorialspoint.com/operating_system/os_processes.htm` URL — backslash-escaped underscores produced a 404.
- Fixed broken internal link to Priority Queues anchor (missing `abstract-data-types` segment, had `.md`).
- Removed `.md` from dijkstras-algorithm link.

### content/cs61b/oop/dynamic-method-selection.md
- Removed stray empty `****` markers on two paragraphs.

### content/cs61c/CALL.md
- Fixed broken mixed bold/italic markers `**translation*,***` → `**translation,**`.
- Replaced dead `skyfree.org/.../ELF_Format.pdf` link with archive.org snapshot.

### content/cs61c/Caching.md
- Wrapped bare `L1$` in backticks — unclosed KaTeX inline-math span.
- Wrapped `sizeof(array) > cache size` in backticks — bare `>` could be parsed as raw HTML.

### content/cs61c/Exam Problem Guide.md
- Removed stray `****` between `first.` and `So,`.
- Replaced dead `clickhouse.tech` link with archive.org snapshot and fixed malformed `**Int Ranges[](url)**` heading syntax.
- Replaced dead `skyfree.org` ELF link with archive.org snapshot.

### content/cs61c/Operating Systems.md
- Removed two stray trailing `****` markers (lines 81 and 84).

### content/cs61c/RISC-V.md
- Cleaned `**Immediates ****` → `**Immediates**` — unbalanced bold span.

### content/cs70/_index.md
- Promoted `#### Credits` to `### Credits` — fixed h2→h4 jump.
- Removed `.md` from `/cs70/latex-reference.md` internal link.

### content/cs70/discrete-math/countability.md
- Promoted `#### Proving that something is countable:` to `###` — fixed h2→h4 jump.

### content/cs70/discrete-math/modular-arithmetic.md
- Promoted five `####` subsection headers to `###` (Formal Statement of CRT, Uniqueness of CRT Solution, Computation, The Formal Definition, An Alternative Definition) — fixed h2→h4 jumps.
- Removed trailing empty `****` after `$x \equiv y \pmod{m}$`.

### content/cs70/discrete-math/rsa-cryptography.md
- Removed three stray empty `****` markers in the RSA Cheat Sheet block.

### content/cs70/discrete-math/stable-matching.md
- Promoted `#### Important notes about this algorithm:` to `###` — fixed h2→h4 jump.
- Removed dangling empty `### ` heading at end of file.

### content/cs70/latex-reference.md
- Removed empty `# ` heading at line 6 — was rendering an empty h1.
- Promoted four section headers (Basics, Propositional Logic, Sets, Modular Arithmetic) from `###` to `##` — fixed h1→h3 jumps.

### content/cs70/probability/counting.md
- Removed stray `****` markers around line 17 trailing text and around the image on line 19.


### content/data102/_index.md
- Demoted `#### Credits` to `###` — fixed h2→h4 jump.

### content/data102/sampling.md
- Removed stray `(` from inline math on line 16.
- Completed truncated inline math at end of sentence on line 71 (was `at time $` with unclosed `$`) — had left the rest of the file in math mode.
- Inserted missing `p` in `$q(\theta) \propto(\theta | x)$` → `$q(\theta) \propto p(\theta | x)$`.

### content/psych131-140/cross cultural psychology.md
- Escaped literal `$10` as `\$10` — unbalanced `$` was opening a KaTeX inline math span.

### content/psych131-140/theories of cognitive development.md
- Removed empty bullet under "conservation".
- Promoted `### Properties of Piaget's Theory` to `##` — fixed h1→h3 jump.

### content/psych143/introduction.md
- Removed stray trailing backtick — unmatched backtick was opening an inline code span.

### content/psych150/Outcomes and Applications.md
- Merged citation that was incorrectly split across three list items.

(See workspace notes changelog-phase1-A through changelog-phase1-E for items considered but skipped.)

## Phase 2 — Spelling and Grammar

Unambiguous spelling and grammar fixes across all course directories.
Technical jargon, YAML front matter, code blocks, and math expressions were
preserved. No stylistic rewrites.

### content/astro-c10/Cosmology.md
- "anywhere you look" → "Anywhere you look" (sentence start), "pherical" → "spherical", "Big Crunsh" → "Big Crunch", "compresed" → "compressed", "casing the fusion" → "causing the fusion", "formoation" → "formation", "into once single entity" → "into one single entity", "habital zone" → "habitable zone".

### content/astro-c10/Galaxies.md
- "multipled" → "multiplied"; "blackholes" → "black holes".

### content/astro-c10/Planetary Systems.md
- "subliminates as it approaches" → "sublimate as they approach"; "coalescencing" → "coalescing"; "multiple it by" → "multiply it by".

### content/astro-c10/Spectroscopy.md
- "has unique configuration" → "has a unique configuration"; "the photon can absorb the proton" → "the electron can absorb the photon" (subject/object swap); "to a lower energy states" → "to a lower energy state".

### content/astro-c10/Stars, Black Holes, Supernovae.md
- "proprtional" → "proportional"; fixed missing space and unbalanced paren in the same sentence; "stars who have cores" → "stars that have cores".

### content/astro-c10/Telescopes.md
- "chromatic abberation" → "chromatic aberration"; "spherical abberation" → "spherical aberration"; "The light output of stars are not" → "is not" (subject-verb agreement).

### content/astro-c10/The Expansion of the Universe.md
- "10 milion light years" → "10 million light years".

### content/astro-c10/_index.md
- "impossible convey" → "impossible to convey".

### content/cs161/Extra Topics.md
- "idfferent" → "different"; "encryption layersk" → "encryption layers."; "using Tor.j" → "using Tor.".

### content/cs161/Heap Vulnerabilities.md
- "in hte heap" → "in the heap"; "overflow he heap" → "overflow the heap".

### content/cs161/Networking.md
- "Configuratiton" → "Configuration"; "response with a SYN-ACK" → "responds with a SYN-ACK"; "Rouge AP" → "Rogue AP".

### content/cs161/x86.md
- "a instruction pointer" → "an instruction pointer".

### content/cs162/Chapter 6 Scheduling.md
- "superceded" → "superseded"; "Remaning" → "Remaining"; "Mos commercial" → "Most commercial".

### content/cs162/Chapter 8 Caching.md
- "cahce" → "cache"; "Containes" → "Contains"; "timng" → "timing".

### content/cs162/Chapter 9 File Systems.md
- "In this ways" → "In this way"; "spects" → "specs"; "plattter" → "platter".

### content/cs168/TCP.md
- "tne abstractions" → "the abstractions".

### content/cs168/addressing (ip).md
- "fragementation" → "fragmentation".

### content/cs168/congestion control.md
- "azdjust" → "adjust"; "maximially" → "maximally".

### content/cs168/ethernet.md
- "maximially" → "maximally".

### content/cs168/final review.md
- "calcuated" → "calculated"; "receieved" → "received"; "recieved" → "received".

### content/cs168/interdomain routing (bgp).md
- "traffc" → "traffic".

### content/cs168/intradomain routing.md
- Fixed six errors: "procols" → "protocols" (×2), "progagation" → "propagation", "whos entry" → "whose entry", "Dijkstras" → "Dijkstra's", "the the advertised" → "the advertised".

### content/cs168/reliability.md
- "reciever" → "receiver".

### content/cs170/Duality.md
- "inqualities" → "inequalities".

### content/cs170/Dynamic Programming.md
- "where each each vertex" → "where each vertex".

### content/cs170/Greedy Algorithms.md
- "an optional solution" → "an optimal solution"; "we can chose" → "we can choose".

### content/cs170/Minimum Spanning Trees.md
- "The sum of edge weights in $T$ are minimized." → "is minimized." (subject-verb agreement).

### content/cs170/Search Problems, P NP.md
- "non-determinstic" → "non-deterministic"; "algorithm ahs" → "algorithm has".

### content/cs186/00 SQL Basics.md
- "interersting" → "interesting".

### content/cs186/01 Disks, Buffers, Files.md
- "colection" → "collection".

### content/cs186/02 B+ Trees.md
- "therer" → "there".

### content/cs186/05 Iterators and Joins.md
- "utples" → "tuples".


### content/cs186/07 Query Optimization.md
- "the the output" → "the output"; "Sellinger" → "Selinger".

### content/cs186/09 Parallel Query Processing.md
- "differerent" → "different".

### content/cs186/10 Recovery.md
- "maintinence" → "maintenance".

### content/cs186/_index.md
- "AERIES" → "ARIES" (proper noun match with chapter 10); "covery" → "cover".

### content/cs186/io.md
- "interchangably" → "interchangeably"; "noticable" → "noticeable".

### content/cs188/Games.md
- "Evalutes" → "Evaluates".

### content/cs188/Machine Learning.md
- "data pooints" → "data points".

### content/cs188/Markov Decision Processes.md
- "alll neighboring states" → "all neighboring states".

### content/cs188/Markov Models.md
- "conditionally independet" → "conditionally independent".

### content/cs188/Reinforcement Learning.md
- "without construction a reward or transition model" → "without constructing a reward or transition model".

### content/cs188/Utilities and Decision Trees.md
- "Substutiability" → "Substitutability"; "exxpected" → "expected".

### content/cs61b/abstract-data-types/hashing.md
- "if a item" → "if an item".

### content/cs61b/abstract-data-types/union-find-disjoint-sets.md
- Fixed bracket whitespace `See[ lab 14]` → `See [lab 14]`; "for an guide" → "for a guide".

### content/cs61b/algorithms/shortest-paths/dijkstras-algorithm.md
- "Djikstras" → "Dijkstra's"; "succesful relaxation" → "successful relaxation".

### content/cs61b/misc-topics/modular-arithmetic.md
- "is a a method" → "is a method".

### content/cs61b/oop/generics.md
- "One way of doing is is to specify" → "One way of doing this is to specify".

### content/cs61c/Caching.md
- "Containes" → "Contains".

### content/cs61c/Operating Systems.md
- "priviledge" → "privilege".

### content/cs70/discrete-math/computability.md
- "psuedocode" → "pseudocode".

### content/cs70/discrete-math/countability.md
- "However, the _are_ countably infinite" → "However, they _are_ countably infinite".

### content/cs70/discrete-math/graphs.md
- "each of the 5 neighbors each are" → "each of the 5 neighbors are".

### content/cs70/discrete-math/overview.md
- "what happens when when all numbers" → "what happens when all numbers".

### content/cs70/discrete-math/propositional-logic.md
- "doesn't necessary mean" → "doesn't necessarily mean".

### content/data102/Markov Decision Processes.md
- "alll neighboring states" → "all neighboring states".

### content/data102/Reinforcement Learning.md
- "without construction a reward or transition model" → "without constructing a reward or transition model".

### content/data102/_index.md
- "Thomson Sampling" → "Thompson Sampling" (proper noun).

### content/data102/bandits.md
- "Thomson Sampling" → "Thompson Sampling".

### content/data102/causality.md
- "skiilled" → "skilled"; "Natrual experiments" → "Natural experiments"; "estiamte ATE" → "estimate ATE".

### content/data102/concentration inequalities.md
- "inquality" → "inequality"; "Hoefding's Lemma" → "Hoeffding's Lemma".

### content/data102/decision theory.md
- "compared ot the average" → "compared to the average".

### content/data102/hypothesis testing.md
- "$\alpha$ treshold" → "$\alpha$ threshold"; "ambigous p-value" → "ambiguous p-value".

### content/data102/interpretability.md
- "GDPR requires" → "GDPR require" (subject-verb agreement); "## Explanability" → "## Explainability".

### content/data102/parameter estimation.md
- "data pooints" → "data points"; "likelhiood and prior ar both normal" → "likelihood and prior are both normal"; "conuugate priors" → "conjugate priors".

### content/data102/regression and glms.md
- "highest posteior density" → "highest posterior density".

### content/data102/sampling.md
- "algoritm" → "algorithm".

### content/psych131-140/2-1 Principles of Developmental Psychopathology.md
- Fixed nine spelling/grammar errors including "noticable" → "noticeable", "prevalance" → "prevalence", "Disabiity-adjusted" → "Disability-adjusted", "transfering" → "transferring", "increase vulnerability" → "increased vulnerability", "comorbility" → "comorbidity", "agression" → "aggression" (×3), "acadmic" → "academic", "exposted" → "exposed"; removed duplicated `##` heading marker.

### content/psych131-140/2-2 methods and assessment of mental health problems.md
- "experiement measure" → "experiment measures"; "experiements" → "experiments"; "more problematic as a child" → "more problematic than a child"; "Childrens'" → "Children's"; "perception a and difficulties" → "perception and difficulties".

### content/psych131-140/2-3 genetics.md
- "variation in behaviors result" → "variation in behaviors results"; "corrleation" → "correlation"; "assocation" → "association"; "correalation" → "correlation".

### content/psych131-140/2-4 temperament.md
- "Temperatment" → "Temperament".

### content/psych131-140/adhd.md
- "hability is .6-.9 (highly habitable)" → "heritability is .6-.9 (highly heritable)".

### content/psych131-140/anxiety disorders.md
- "symtoms" → "symptoms"; "absense" → "absence".

### content/psych131-140/autism.md
- "mulit-method" → "multi-method"; "three domians" → "three domains"; "theraputic" → "therapeutic".

### content/psych131-140/conduct problems.md
- "natrual function" → "natural function".

### content/psych131-140/cross cultural psychology.md
- "childrens' thoughts" → "children's thoughts"; "pictoral form" → "pictorial form".

### content/psych131-140/depression and bipolar.md
- "interpresonal" → "interpersonal"; "aggresive" → "aggressive".

### content/psych131-140/eating disorders.md
- "binge edating" → "binge eating"; "disatisfaction" → "dissatisfaction".

### content/psych131-140/emotional development.md
- "situatonal" → "situational"; "congitive" → "cognitive"; "embarassment" → "embarrassment" (×2); "phisiological" → "physiological"; "enotional states" → "emotional states"; "look veyr similar" → "look very similar".

### content/psych131-140/inference.md
- "once can infer" → "one can infer"; "development on logical reasoning" → "development of logical reasoning"; "Gobnik & Sobel" → "Gopnik & Sobel".

### content/psych131-140/metacognition.md
- "metacongnition" → "metacognition"; "detect metagonition" → "detect metacognition".

### content/psych131-140/nature and nurture.md
- "characteristics are more influenced by nurture, and other more by nature" → "some characteristics are more influenced by nurture, and others more by nature"; "Inheritence" → "Inheritance".

### content/psych131-140/ontogeny.md
- "resproduction" → "reproduction".

### content/psych131-140/schizophrenia.md
- "not amicable to change" → "not amenable to change"; "Elodia" → "Alogia"; "Anedonia" → "Anhedonia"; "delections/duplications" → "deletions/duplications".

### content/psych131-140/subtance use disorder.md
- "alcholism" → "alcoholism"; "algohol" → "alcohol".

### content/psych131-140/theories of cognitive development.md
- "four main type of representation" → "four main types of representation"; "ficticious" → "fictitious"; "typical indviidual" → "typical individual".

### content/psych131-140/theory of mind.md
- "reprocussions" → "repercussions"; "join attentional" → "joint attentional"; "replicatable" → "replicable"; "perspectives of others is" → "perspectives of others are"; "Childrens' Representation" → "Children's Representation"; "interepreted" → "interpreted".

### content/psych143/introduction.md
- Fixed 17 spelling/grammar errors including "Nativistis" → "Nativists", "speakers' unconscious" → "speaker's unconscious", "speach sounds" → "speech sounds", "ommitted" → "omitted", "number fo words" → "number of words", "Childrens'" → "Children's", "Pidgins and Croles" → "Pidgins and Creoles", "two different peoples speaking different language" → "different languages", "gramatically" → "grammatically", "errorsd" → "errors", "argujments" → "arguments", "informantion" → "information", "afterbirth" → "after birth", "cricital period" → "critical period", "ddiscontinuity" → "discontinuity", "lae learners" → "late learners", "Decontexualized" → "Decontextualized"; plural-agreement fixes ("Sign systems ... but lacks" → "lack", "language-like sound that combines" → "sounds that combine").

### content/psych150/Attachment.md
- "difficult to comfort when caregivers return" → "are difficult to comfort when caregivers return".

### content/psych150/Heritability of Personality.md
- "Idential twins" → "Identical twins".

### content/psych150/If-Then Personality.md
- "Personaity" → "Personality".

### content/psych150/Intro to Personality.md
- "perosnality" → "personality"; "characteristcs" → "characteristics".

### content/psych150/Outcomes and Applications.md
- "higher neuroticism and lower extraversion was associated" → "were associated"; "behavios" → "behaviors"; "MTBI" → "MBTI".

### content/psych150/Temperament and Birth Order.md
- "measure reponse time" → "measure response time"; "sibilng" / "sibilngs" → "sibling" / "siblings".

### content/psych150/Trait Theory.md
- "Asthetics" → "Aesthetics"; "Self-dicipline" → "Self-discipline"; "hypotheis" → "hypothesis"; "personality matures by adulthood (age 30), and are relatively stable" → "and is relatively stable"; "postiive emotion predicts" → "positive emotion predict" (plural-subject agreement).

(See workspace notes changelog-phase2-A through changelog-phase2-E for items considered but skipped, including British/American spelling variants and discipline-specific terms preserved verbatim.)

## Phase 3 — Content Corrections

Objective content errors only: mathematically wrong equations, direct
intra-file contradictions, swapped variables, and a piece of pangram filler
text accidentally pasted into a bullet. Stub headings, truncated paragraphs,
and ambiguous wording were left for follow-up.

### content/astro-c10/Cosmology.md
- "## The Cosmological Constant" third case `$\Omega_M > 1$` (duplicated) → `$\Omega_M < 1$` — the open-universe case was missing and the bullet's "expansion never stops" outcome only matches `< 1`.
- Restored corrupted exponents on lines 117/120: "1029 K" → "$10^{29}$ K", "10−37 s" → "$10^{-37}$ s" — formatting loss had turned GUT-scale values into nonsensical numbers.

### content/astro-c10/Stars, Black Holes, Supernovae.md
- Two occurrences of `$\frac{1}{R^3}$` → `$\frac{1}{M^3}$` — the parenthetical derivation uses mass; standard main-sequence lifetime is $\tau \propto M^{-3}$.

### content/astro-c10/Units.md
- SI prefix "k" row: `1m = 1000km` → `1km = 1000m` (units were swapped).
- SI prefix "n" row: `1 nm = 1000 $\mu$m` → `1000 nm = 1 $\mu$m` (sides of equation were swapped).

### content/cs161/Cryptography.md
- Second Preimage Resistance: "infeasible to find a different **output** with the same hash" → "different **input** ..." — definitional error.
- Blockchain ledger property: "mutable" → "immutable" — direct contradiction with "append only" and the later hash-chain description.

### content/cs161/Memory Safety Vulnerabilities.md
- Removed pangram filler text ("the quick brown fox jumps over the lazy dog.") accidentally pasted into the "sanitize inputs" bullet.

### content/cs161/Networking.md
- Kaminsky-attack source-port randomization: "adds **32** bits to guess" → "adds **16** bits" — TCP/UDP ports are 16 bits.

### content/cs162/Chapter 7 Address Translation.md
- "about 16MB of memory assuming each entry is 32 bits long" → "about 4MB of memory" — $2^{20}$ entries × 4 bytes = 4 MiB; 16 MB was arithmetically wrong.

### content/cs168/final review.md
- "$4/1 = 1$" → "$4/1 = 4$" — objective arithmetic error in the max-min-fair-share walkthrough.

### content/cs170/Algorithms for Integer Arithmetic.md
- `\sum_{i=0}^{log_2(n)} 2^i = \frac{2^{log_2(n)} - 1}{2 - 1}` → exponent `log_2(n)+1` — geometric series identity $\sum_{i=0}^k 2^i = 2^{k+1}-1$. The text's $2n$ upper bound only follows from the corrected expression.

### content/cs170/Dynamic Programming.md
- Knapsack complexity rewritten to standard pseudo-polynomial `O(n · W)` (previous expression was not a valid DP complexity and its parens didn't balance).
- Knapsack-with-repetition: "We do this `n` number of times (one for each possible max weight)" → "`W` number of times" — the parenthetical already says "one for each possible max weight".

### content/cs170/Huffman Coding.md
- Average-codeword-length expression: `.4n · 1 + .3n · 2 + .2n · 3 + .1 · 3 = 1.9n` → `.1n · 3` — fourth term was missing its `n` factor.
- Information/Entropy: "More than 1 bit if `p ≠ 0.5`" → "More than 1 bit if `p < 0.5`" — matches the $I(p) = \log_2(1/p)$ definition and the worked $p=0.25$ example.

### content/cs170/Network Flow.md
- Label corrected: "A `(s, t)` **weight** in a graph is a pair `(L, R)`" → "A `(s, t)` **cut** ..." — the next sentence and the section's title both say "cut".

### content/cs186/00 SQL Basics.md
- "`clubs` had $2$ rows ... $3 \times 4 = 12$ rows" → "$3$ rows" — direct contradiction; the inline image of `clubs` shows 3 rows.

### content/cs186/02 B+ Trees.md
- Q2a question: "with a height of $5$" → "$2$" — the answer text, the arithmetic ($2 + 20 + 4 = 26$), and Q2b all consistently use height = 2.

### content/cs188/Logic.md
- Proof step: `¬A ∨ ¬B ∨ C ⊨ ¬A ∨ ¬B ∨ ¬C` → `... ⊨ ¬A ∨ ¬B ∨ C` — the prior simplification step and the "both sides are completely equivalent" conclusion only hold with the corrected RHS.

### content/cs188/Machine Learning.md
- MLE for CPT: `P(Y=y) = (# data points with X=x) / total` → `(# data points with Y=y) / total` — estimating `P(Y=y)` counts `Y=y`.

### content/cs188/Markov Models.md
- Forward-algorithm observation update: `B(S_{t}1)` → `B(S_{t+1})` — LaTeX typo; every other term on the line is indexed `t+1`.

### content/cs188/Reinforcement Learning.md
- SARSA update: `Q(s,a) ← (1-α)Q(s,a) + α(R(s,a,s') + max_a Q(s', a))` → `... + α(R(s,a,s') + γ Q(s', a'))` — SARSA uses the next action actually taken by the current policy (not max) and includes the discount factor γ.

### content/cs61b/asymptotics/asymptotics-practice.md
- "this sum is equal to $4^{n+1}-1$" → "$\frac{4^{n+1}-4}{3}$" — geometric series identity; verified $4+16+64 = 84 = (4^4-4)/3$.

### content/cs61c/Number Representation.md
- "In an **unsigned** integer, the left-most bit is reserved as the **sign bit**" → "In a **signed** integer ..." — unsigned integers have no sign bit.

### content/cs61c/Operating Systems.md
- "UDP (**Universal** Datagram Protocol)" → "UDP (**User** Datagram Protocol)" — RFC 768.

### content/cs61c/Parallelism.md
- Amdahl's Law example: "$F = S = 0.5$" → "$F = 0.5, S = 2$" — the formula defines $S > 1$ as the speedup factor; verified $1/((1-0.5)+0.5/2) \approx 1.33$.

### content/cs70/discrete-math/modular-arithmetic.md
- `$\mod(x,m) = x - \lfloor{\frac{x}{y}}\rfloor \cdot y$` → `... \lfloor{\frac{x}{m}}\rfloor \cdot m` — function signature is `(x, m)`; standard remainder formula uses `m`.

### content/cs70/discrete-math/polynomials.md
- Lagrange Δ₁ basis polynomial denominator: `\prod_{j \ne i} (x_1 - x_j)` → `\prod_{j \ne 1} (x_1 - x_j)` — `i` was undefined here; both products of Δ₁ must skip index 1.

### content/cs70/discrete-math/proofs.md
- Direct Proof Form goal: `$P \iff Q$` → `$P \implies Q$` — a direct proof template proves an implication, not a biconditional; matches the worked example and the Contraposition/Contradiction sections.

### content/cs70/probability/counting.md
- Description of $\binom{n}{k}$: "choose $n$ things from $k$ total elements" → "choose $k$ things from $n$ total elements" — the two roles were swapped relative to the formula immediately above.

### content/data102/Reinforcement Learning.md
- SARSA update: same correction as cs188/Reinforcement Learning.md (the two files share this content).

### content/data102/hypothesis testing.md
- B-H proof inline math: `E[FDP] = E[P(R=0|D=1)` → `... E[P(R=0|D=1)]` — added missing closing bracket on the outer expectation.

### content/data102/parameter estimation.md
- MLE for CPT: same `P(Y=y)` count fix as cs188/Machine Learning.md.
- MMSE definition: `\hat\theta = argmax_{\hat\theta} E_{\theta|x} (\hat\theta - \theta)^2` → `argmin_{\hat\theta}` — Minimum MSE is by definition a minimization.

(See workspace notes changelog-phase3-A through changelog-phase3-E for items considered but skipped, including stub headings, ambiguous truncations, and interpretive wording issues.)



## Phase 4 — Psych Reorganization

Minimal YAML front-matter additions (`title` + `weight`) to give the Psych
course directories an intentional learning-progression order. No body content
was touched and no `_index.md` files were modified. Weights use gaps of 10 to
allow future inserts. Rationale per directory: psych131-140 places foundations
first, then typical cognitive/social development, then disorders by class;
psych150 follows the standard personality-psychology progression; psych143 has
a single content file.

### content/psych131-140/2-1 Principles of Developmental Psychopathology.md
- Added `weight: 10` — first in the foundations sequence.

### content/psych131-140/2-2 methods and assessment of mental health problems.md
- Added `weight: 20`.

### content/psych131-140/2-3 genetics.md
- Added `weight: 40`.

### content/psych131-140/2-4 temperament.md
- Added `weight: 60`.

### content/psych131-140/Reading Summaries.md
- Added `weight: 220` — capstone position.

### content/psych131-140/adhd.md
- Added `weight: 170`.

### content/psych131-140/anxiety disorders.md
- Added `weight: 140`.

### content/psych131-140/autism.md
- Added `weight: 160`.

### content/psych131-140/conduct problems.md
- Added `weight: 180`.

### content/psych131-140/cross cultural psychology.md
- Added `weight: 130`.

### content/psych131-140/culture.md
- Added `weight: 120`.

### content/psych131-140/depression and bipolar.md
- Added `weight: 150`.

### content/psych131-140/eating disorders.md
- Added `weight: 190`.

### content/psych131-140/emotional development.md
- Added `weight: 80`.

### content/psych131-140/inference.md
- Added `weight: 110`.

### content/psych131-140/metacognition.md
- Added `weight: 100`.

### content/psych131-140/nature and nurture.md
- Added `weight: 30`.

### content/psych131-140/ontogeny.md
- Added `weight: 50`.

### content/psych131-140/schizophrenia.md
- Added `weight: 210`.

### content/psych131-140/subtance use disorder.md
- Added `weight: 200`.

### content/psych131-140/theories of cognitive development.md
- Added `weight: 70`.

### content/psych131-140/theory of mind.md
- Added `weight: 90`.

### content/psych143/introduction.md
- Added `weight: 10` — only content file in the directory.

### content/psych150/Attachment.md
- Added `weight: 50`.

### content/psych150/Heritability of Personality.md
- Added `weight: 40`.

### content/psych150/If-Then Personality.md
- Added `weight: 70`.

### content/psych150/Intro to Personality.md
- Added `weight: 10` — first in personality sequence.

### content/psych150/Outcomes and Applications.md
- Added `weight: 80` — capstone position.

### content/psych150/Temperament and Birth Order.md
- Added `weight: 30`.

### content/psych150/Trait Theory.md
- Added `weight: 20`.

### content/psych150/Transference.md
- Added `weight: 60`.

## Phase 5 — Cross-Course Wiki Links

Added Obsidian-style `[[course-folder/page-name]]` cross-references between
in-scope course directories. 50 new wiki-links across 44 files spanning CS,
Data, and Psych. Every target file was verified to exist on disk and Hugo
build is clean. Conceptual bridges added: probability/inference, Markov
models, decision theory, graphs, search, MSTs, hashing, caching, memory/OS,
modular arithmetic/RSA, cryptography, networking, and
genetics/heritability/temperament.

### content/cs161/Cryptography.md
- Added `[[cs70/discrete-math/modular-arithmetic]]`, `[[cs70/discrete-math/rsa-cryptography]]` — number-theory foundations for RSA and Diffie–Hellman.

### content/cs161/Memory Safety Vulnerabilities.md
- Added `[[cs61c/Memory, Pointers, Addresses]]`, `[[cs61c/Memory Management]]` — the C memory model the attacks exploit.

### content/cs161/Networking.md
- Added `[[cs168/internet organization and layers]]` (intro), `[[cs168/interdomain routing (bgp)]]` (BGP section), `[[cs168/TCP]]` + `[[cs168/congestion control]]` (TCP section) — full networking-course treatments of each layer.

### content/cs162/Chapter 7 Address Translation.md
- Added `[[cs61c/Operating Systems]]`, `[[cs61c/Memory Management]]` — hardware/architecture view and C-level memory model.

### content/cs162/Chapter 8 Caching.md
- Added `[[cs61c/Caching]]`, `[[cs186/03 Buffer Management]]` — hardware caches and DB buffer-pool analog.

### content/cs168/TCP.md
- Added `[[cs161/Networking]]` — TCP injection, RST attacks, TLS on top of TCP.

### content/cs168/dns.md
- Added `[[cs161/Networking]]` — DNS spoofing, cache poisoning, DNSSEC.

### content/cs170/Graphs.md
- Added `[[cs61b/abstract-data-types/graphs]]`, `[[cs70/discrete-math/graphs]]` — data-structures view and combinatorial/proof view.

### content/cs170/Minimum Spanning Trees.md
- Added `[[cs61b/algorithms/minimum-spanning-trees/kruskals-algorithm]]`, `[[cs61b/algorithms/minimum-spanning-trees/prims-algorithm]]` — worked examples.

### content/cs186/03 Buffer Management.md
- Added `[[cs61c/Caching]]`, `[[cs162/Chapter 8 Caching]]` — same LRU/clock policies in hardware caches and OS page caches.

### content/cs186/04 Sorting and Hashing.md
- Added `[[cs61b/abstract-data-types/hashing]]` — in-memory fundamentals.

### content/cs188/Bayes Nets.md
- Added `[[cs70/probability/probability-overview]]`, `[[data102/parameter estimation]]` — underlying probability theory and Bayesian CPT estimation.

### content/cs188/Machine Learning.md
- Added `[[data102/parameter estimation]]` — broader Bayesian/MAP statistical treatment.


### content/cs188/Markov Decision Processes.md
- Added `[[data102/Markov Decision Processes]]` — same formalism from the inference/decision-theory side.

### content/cs188/Markov Models.md
- Added `[[cs70/probability/markov-chains]]` (memoryless-property paragraph), `[[data102/sampling]]` (particle-filtering section) — probability-theory foundation and sampling techniques.

### content/cs188/Reinforcement Learning.md
- Added `[[data102/Reinforcement Learning]]`, `[[data102/bandits]]` — statistical-inference framing and exploration/exploitation.

### content/cs188/Search Problems.md
- Added `[[cs61b/algorithms/searching/breadth-first-search-bfs]]` + `[[cs170/Graphs]]` (BFS bullet), `[[cs61b/algorithms/searching/depth-first-search-dfs]]` (DFS bullet).

### content/cs188/Utilities and Decision Trees.md
- Added `[[data102/decision theory]]` — connects AI utility theory to statistical decision theory.

### content/cs61b/abstract-data-types/graphs.md
- Added `[[cs170/Graphs]]`, `[[cs70/discrete-math/graphs]]`, `[[cs188/Search Problems]]` — algorithmic, combinatorial, and AI-state-space views.

### content/cs61b/abstract-data-types/hashing.md
- Added `[[cs186/04 Sorting and Hashing]]`, `[[cs70/probability/hashing-and-the-union-bound]]`, `[[cs161/Cryptography]]` — external/DB hashing, collision probability, and cryptographic hashes.

### content/cs61b/algorithms/minimum-spanning-trees/kruskals-algorithm.md
- Added `[[cs170/Minimum Spanning Trees]]` — cut-property correctness proof and greedy-MST framework.

### content/cs61b/algorithms/minimum-spanning-trees/prims-algorithm.md
- Added `[[cs170/Minimum Spanning Trees]]` — same rationale as Kruskal's.

### content/cs61b/algorithms/searching/breadth-first-search-bfs.md
- Added `[[cs170/Graphs]]`, `[[cs188/Search Problems]]` — formal runtime and BFS as AI search strategy.

### content/cs61b/algorithms/searching/depth-first-search-dfs.md
- Added `[[cs170/Graphs]]`, `[[cs188/Search Problems]]` — SCC/topo-sort role and AI search strategy.

### content/cs61b/algorithms/shortest-paths/dijkstras-algorithm.md
- Added `[[cs170/Graphs]]`, `[[cs188/Search Problems]]` — formal proof/runtime and Uniform Cost Search.

### content/cs61b/misc-topics/modular-arithmetic.md
- Added `[[cs70/discrete-math/modular-arithmetic]]` — mathematical foundations.

### content/cs61c/Caching.md
- Added `[[cs162/Chapter 8 Caching]]`, `[[cs186/03 Buffer Management]]` — same locality principle at OS and DB layers.

### content/cs61c/Memory, Pointers, Addresses.md
- Added `[[cs161/Memory Safety Vulnerabilities]]` — the unchecked-pointer model enables those attacks.

### content/cs61c/Operating Systems.md
- Added `[[cs162/Chapter 1 OS Basics]]` — deeper CS 162 treatment of processes/threads/scheduling/VM/FS.

### content/cs70/discrete-math/graphs.md
- Added `[[cs170/Graphs]]` — algorithmic treatment (BFS, DFS, SCCs, MSTs).

### content/cs70/discrete-math/modular-arithmetic.md
- Added `[[cs61b/misc-topics/modular-arithmetic]]`, `[[cs161/Cryptography]]` — bit-manipulation view and cryptographic primitives.

### content/cs70/discrete-math/rsa-cryptography.md
- Added `[[cs161/Cryptography]]` — RSA in a real security stack.

### content/cs70/probability/hashing-and-the-union-bound.md
- Added `[[cs61b/abstract-data-types/hashing]]` — data-structure use of hashing.

### content/cs70/probability/markov-chains.md
- Added `[[cs188/Markov Models]]`, `[[cs188/Markov Decision Processes]]` — time-series Bayes nets and the MDP extension.

### content/data102/Markov Decision Processes.md
- Added `[[cs188/Markov Decision Processes]]`, `[[cs70/probability/markov-chains]]` — AI-search framing and Markov-chain theory.

### content/data102/Reinforcement Learning.md
- Added `[[cs188/Reinforcement Learning]]` — same algorithms from the agent-search side.

### content/data102/hypothesis testing.md
- Added `[[psych131-140/2-2 methods and assessment of mental health problems]]` — NHST application in clinical research.

### content/data102/parameter estimation.md
- Added `[[cs188/Machine Learning]]`, `[[cs70/probability/probability-overview]]` — where MLE reappears in the AI ML pipeline and the broader probability background.

### content/psych131-140/2-2 methods and assessment of mental health problems.md
- Added `[[data102/hypothesis testing]]` — statistical machinery (null/alternative, p-values, FP control).

### content/psych131-140/2-3 genetics.md
- Added `[[psych150/Heritability of Personality]]` — same construct applied to personality traits.

### content/psych131-140/2-4 temperament.md
- Added `[[psych150/Temperament and Birth Order]]`, `[[psych150/Trait Theory]]` — connects developmental-psych Kagan inhibited/uninhibited to its personality-psych counterpart.

### content/psych131-140/inference.md
- Added `[[cs70/discrete-math/propositional-logic]]` (disjunctive-syllogism example), `[[data102/hypothesis testing]]` + `[[data102/parameter estimation]]` (inductive-inference paragraph).

### content/psych150/Heritability of Personality.md
- Added `[[psych131-140/2-3 genetics]]`, `[[psych131-140/nature and nurture]]` — same construct in mental-health symptoms and broader nature-vs-nurture framing.

### content/psych150/Temperament and Birth Order.md
- Added `[[psych131-140/2-4 temperament]]` — developmental-psych Kagan inhibited/uninhibited treatment.

## Phase 8 — GitHub Issue Fixes

Addressed open issues on the GitHub repo. Issue #2 (B+ tree Q2a inaccuracy)
was already resolved during Phase 3 (commit 704adf0) by changing the question's
stated tree height from 5 to 2 to match the existing answer of 26 I/Os — an
equally valid resolution to the one the reporter proposed.

### content/cs61b/algorithms/searching/breadth-first-search-bfs.md
- Changed "we won't add C or A because they are both marked." to "we won't add B or A because they are both marked." — fixes GH issue #3. At the step processing node C, the already-marked neighbors are A (start node) and B (marked when A's children were enqueued); C is the current node, not a neighbor it could try to add.

## Phase 9 — OCR Project: Philosophy 5, Anthro 1

Two new courses transcribed from handwritten lecture PDFs using
`scripts/ocr_to_notes.py` + the auggie CLI + Claude Opus 4.7. The
script reads a JSON page→section mapping, extracts pages with poppler
(`pdfseparate`/`pdfunite`/`pdftoppm`), OCRs each PNG via `auggie
--print --quiet --model opus4.7`, and writes Hugo leaf-bundle markdown
alongside per-section and combined PDFs. After transcription, the
two courses went through the same review process previously applied
to the existing notes (artifact cleanup, formatting, spelling/grammar,
content accuracy, cross-course wiki links).

Commits:
- [`fb4845b`](https://github.com/64bitpandas/notes/commit/fb4845b1c2693fd69f4e7ce05d1b800b52c12e77) — Phase A: OCR pipeline + navbar entries for 2 new courses
- [`7c6764a`](https://github.com/64bitpandas/notes/commit/7c6764a705807b5199545312d7219aedf3dee529) — Phase A.2: swap OCR backend from Anthropic SDK to auggie CLI
- [`bea5a4f`](https://github.com/64bitpandas/notes/commit/bea5a4fc85411122206d8a39339efdb44dcbf316) — Phase B: philosophy5 OCR transcription
- [`1caf3c7`](https://github.com/64bitpandas/notes/commit/1caf3c7e663c0aecdf797f8bca80682b8d669390) — Phase B.1: philosophy5 leaf-bundle restructure
- [`fb63a79`](https://github.com/64bitpandas/notes/commit/fb63a799d20c1ebe32ad13b96bfd359ab9d56968) — Phase D: anthro1 OCR transcription
- [`93cd13a`](https://github.com/64bitpandas/notes/commit/93cd13ab758640280d26d992d5f4f822dfc42d92) — Wave 1: anthro1 OCR artifact cleanup
- [`e6576de`](https://github.com/64bitpandas/notes/commit/e6576ded0882e442cd82aef02bf85b7e2cd61b95) — Wave 1: philosophy5 OCR artifact cleanup
- [`ccdee33`](https://github.com/64bitpandas/notes/commit/ccdee33fcee67cd92d57294ed0b30fc4f1f21fc7) — Wave 3: philosophy5 spelling and grammar
- [`ec29e65`](https://github.com/64bitpandas/notes/commit/ec29e65f2e1cab2171d58afc55d0e90cac7d27bf) — Wave 3: anthro1 spelling and grammar
- [`422846c`](https://github.com/64bitpandas/notes/commit/422846cb9c056bd92e380cc37374e9a6a66bbddb) — Wave 4: anthro1 content accuracy
- [`0ea9b37`](https://github.com/64bitpandas/notes/commit/0ea9b3734a7ce83267f9fec2757ec9baf4fe60b4) — Wave 6: cross-course wiki links between new and existing notes

### Phase A — OCR Pipeline + Navbar Scaffolding (`fb4845b`)

Built the transcription pipeline and added skeleton entries to the
sidebar so the two new courses would show up under "Incomplete
Notes". No PDFs from `old/` were staged in this commit — actual OCR
runs happen in subsequent commits.

#### scripts/ocr_to_notes.py
- New file: PDF → Hugo page-bundle markdown via Claude vision OCR + poppler (`pdfseparate`, `pdfunite`, `pdftoppm`). Reads a JSON page→section mapping per course, extracts the requested pages as PNGs, sends them to the Anthropic API, and writes a markdown page per section plus a per-section PDF and a combined PDF.

#### scripts/philosophy5.json
- New file: 9-section page-range mapping for `old/Philosophy 5.pdf` (design-arguments, fine-tuning-argument, statistical-mechanics, scientific-realism, natural-kinds, humes-problem-of-induction, ethics-of-ai, values, epistemic-catastrophe).

#### scripts/anthro1.json
- New file: 16-section page-range mapping for `old/Anthro 1.pdf` (what-is-anthropology, evolution, traits, mitosis-and-meiosis, modern-evolutionary-theory, origin-of-new-species, biological-classification, geological-time-vertebrate-evolution, primates, primate-anatomy, hominids, paleoanthropology, humans, biocultural-evolution, human-skeletal-biology, bioarchaeology).

#### content/philosophy5/_index.md
- New file: section skeleton with frontmatter `title: "Philosophy 5"` and `weight: 95` (last in the sidebar).

#### content/anthro1/_index.md
- New file: section skeleton with frontmatter `title: "Anthro 1"` and `weight: 97`.

#### content/_index.md
- Added `philosophy5`, `anthro1` to the "Incomplete Notes" list at the bottom of the site index.

### Phase A.2 — Switch OCR Backend to auggie CLI (`7c6764a`)

Replaced the direct Anthropic SDK call inside `ocr_to_notes.py` with
an `auggie --print --quiet --model opus4.7` subprocess invocation per
page PNG. This drops the `ANTHROPIC_API_KEY` requirement and the
`anthropic`/`pillow` Python dependencies; the script now needs only
the stdlib + poppler + an authenticated `auggie` CLI on PATH.

#### scripts/ocr_to_notes.py
- Removed `import anthropic` and the `client = anthropic.Anthropic(...)` setup.
- Removed image base64-encoding helper and the `client.messages.create(...)` call.
- Added `subprocess.run(["auggie", "--print", "--quiet", "--model", "opus4.7", ...])` wrapper that pipes the prompt over stdin and reads transcribed markdown from stdout.
- Net: −65 / +50 lines; same external interface (`python scripts/ocr_to_notes.py <course>`), no JSON-mapping changes needed.

### Phase B — Philosophy 5 OCR Transcription (`bea5a4f`)

Auto-transcribed 9 sections (~32 pages) from `old/Philosophy 5.pdf`.
Each section originally shipped as a flat `slug.md` + `slug.pdf` pair
inside `content/philosophy5/` with a sibling embedded PDF; the
combined `philosophy5-combined.pdf` was embedded in `_index.md`.
Diagrams were intentionally not transcribed in this first pass — body
text only.

#### content/philosophy5/_index.md
- Embedded the combined `philosophy5-combined.pdf` (one-line change to the skeleton).

#### content/philosophy5/design-arguments.md
- New file: 143 lines covering the Watchmaker analogy, Paley's argument, likelihood arguments, and Bayesian formalizations. Section PDF embedded at the top.

#### content/philosophy5/epistemic-catastrophe.md
- New file: 63 lines on Russell's chicken and the limits of empirical justification.

#### content/philosophy5/ethics-of-ai.md
- New file: 274 lines covering moral status, value alignment, superintelligence, post-human civilization, and Chalmers' gradual-uploading argument.

#### content/philosophy5/fine-tuning-argument.md
- New file: 110 lines covering the Anthropic Principle, Observational Selection Effect, multiverse responses, and the Firing Squad objection.

#### content/philosophy5/humes-problem-of-induction.md
- New file: 248 lines covering Hume's problem, Goodman's grue, Reichenbach's pragmatic vindication, and Inference to the Best Explanation.

#### content/philosophy5/natural-kinds.md
- New file: 52 lines.

#### content/philosophy5/scientific-realism.md
- New file: 121 lines.

#### content/philosophy5/statistical-mechanics.md
- New file: 40 lines.

#### content/philosophy5/values.md
- New file: 111 lines.

#### content/philosophy5/*.pdf
- New per-section PDFs (`design-arguments.pdf`, `epistemic-catastrophe.pdf`, `ethics-of-ai.pdf`, `fine-tuning-argument.pdf`, `humes-problem-of-induction.pdf`, `natural-kinds.pdf`, `scientific-realism.pdf`, `statistical-mechanics.pdf`, `values.pdf`) extracted via `pdfseparate` + `pdfunite`, plus a combined `philosophy5-combined.pdf`.

### Phase B.1 — Philosophy 5 Leaf-Bundle Restructure (`1caf3c7`)

Per-section PDFs were 404ing because Hugo only publishes sibling
files for leaf bundles (`<slug>/index.md`), not for flat `slug.md` +
`slug.pdf` pairs at the section root. Moved each section to its own
directory and patched the OCR script so future course runs produce
the correct layout out of the box.

#### content/philosophy5/<slug>.md → content/philosophy5/<slug>/index.md
- Renamed all 9 markdown files to `index.md` inside per-slug directories: design-arguments, epistemic-catastrophe, ethics-of-ai, fine-tuning-argument, humes-problem-of-induction, natural-kinds, scientific-realism, statistical-mechanics, values.

#### content/philosophy5/<slug>.pdf → content/philosophy5/<slug>/<slug>.pdf
- Moved all 9 per-section PDFs into their matching slug directories so Hugo publishes them as leaf-bundle resources.

#### scripts/ocr_to_notes.py
- Changed the output-path logic so each section is written to `<course>/<slug>/index.md` + `<course>/<slug>/<slug>.pdf` instead of flat siblings (+8 / −4 lines).

### Phase D — Anthro 1 OCR Transcription (`fb63a79`)

Auto-transcribed 16 sections from `old/Anthro 1.pdf` directly into
the leaf-bundle layout. Largest course of the batch — 2,717 markdown
lines across the sections plus a ~108 MB combined PDF.

#### content/anthro1/_index.md
- Embedded the combined `anthro1-combined.pdf`.

#### content/anthro1/what-is-anthropology/index.md
- New file: 33 lines.

#### content/anthro1/evolution/index.md
- New file: 169 lines covering pre-Darwinian thinkers (da Vinci, Hooke, Steno, Malthus, Wallace), Darwin's finches and Origin of Species, fitness as differential reproductive success, and the progress fallacy.

#### content/anthro1/traits/index.md
- New file: 76 lines on Mendelian genotype/phenotype, alleles, dominance, monogenic vs polygenic traits, and polymorphism.

#### content/anthro1/mitosis-and-meiosis/index.md
- New file: 28 lines.

#### content/anthro1/modern-evolutionary-theory/index.md
- New file: 65 lines covering allele-frequency change, gene flow, genetic drift, and selection.

#### content/anthro1/origin-of-new-species/index.md
- New file: 62 lines on speciation modes and reproductive isolation.

#### content/anthro1/biological-classification/index.md
- New file: 78 lines covering Linnaean taxonomy, homologous/analogous structures, homoplasy, cladistics, and the biological species concept.

#### content/anthro1/geological-time-vertebrate-evolution/index.md
- New file: 247 lines tracing chordates → vertebrates → tetrapods → mammals through the geologic record.

#### content/anthro1/primates/index.md
- New file: 219 lines on primate suborders, infraorders, and taxonomic relationships.

#### content/anthro1/primate-anatomy/index.md
- New file: 256 lines covering dental formulas, locomotion, postorbital closure, sagittal crests, and sexual dimorphism.

#### content/anthro1/hominids/index.md
- New file: 199 lines covering orangutans, gorillas (folivorous, large size, fission-fusion social structure), chimps, and bonobos.

#### content/anthro1/paleoanthropology/index.md
- New file: 191 lines covering Sahelanthropus, Orrorin tugenensis, Ardipithecus, and the australopithecines (afarensis, africanus, garhi, robust forms).

#### content/anthro1/humans/index.md
- New file: 326 lines covering Homo habilis/rudolfensis/erectus/heidelbergensis/neanderthalensis/denisova/sapiens/floresiensis, and the Out-of-Africa vs. Multiregional debate.

#### content/anthro1/biocultural-evolution/index.md
- New file: 422 lines covering lactose tolerance, sickle cell, race as a social construct, cranial topology history (Retzius, Morton, Hrdlička), and modern population genetics.

#### content/anthro1/human-skeletal-biology/index.md
- New file: 228 lines covering bone remodeling, osteons, woven vs. lamellar bone, fracture repair (woven bone → bony callus), bone types, and forensic anthropology.

#### content/anthro1/bioarchaeology/index.md
- New file: 117 lines covering paleopathology indicators (porotic hyperostosis, enamel hypoplasia, Pott's disease in vertebrae, degenerative disease).

#### content/anthro1/*/*.pdf
- New per-section PDFs for all 16 sections, plus the combined `anthro1-combined.pdf`.

### Wave 1 — OCR Artifact Cleanup

Three sister commits, one per course. The same four classes of OCR
artifact were stripped from every transcribed section:

1. **`📎 Attached N image(s)`** preamble lines leaked from auggie's
   per-image input echo.
2. **`Request ID: ...`** auggie meta-output lines.
3. **Duplicated paragraphs/bullets** from page-wrap OCR (where the
   model occasionally re-emitted the bottom of one page as the top
   of the next).
4. **Heading hierarchy shifted up one level** so the top-of-section
   heading is `h1` (previously transcribed as `h2` because the model
   reserved h1 for the page title).

#### Wave 1a — anthro1 (`93cd13a`)

##### content/anthro1/bioarchaeology/index.md (−20 lines)
- Stripped 📎 markers and Request-ID lines; de-duped repeated paragraphs.

##### content/anthro1/biocultural-evolution/index.md (−58 lines)
- Largest cleanup in the course — extensive page-wrap duplication around the lactose-tolerance and sickle-cell sections, plus several attachment-marker rows.

##### content/anthro1/biological-classification/index.md (−4 lines)
- Stripped 📎 markers.

##### content/anthro1/evolution/index.md (+22 / −34 net)
- Heading hierarchy shifted h2→h1 for "Charles Darwin" and "Modern Evolutionary Theory" sections; 📎 markers stripped; a few duplicated bullets removed.

##### content/anthro1/geological-time-vertebrate-evolution/index.md (−24 lines)
- Stripped 📎 markers and duplicated chordate-trait bullets (the `Notochord`/`nerve chord`/`pharyngeal slits`/`muscular tail` block appeared twice — duplication preserved here for traceability, fixed in Wave 3 for spelling).

##### content/anthro1/hominids/index.md (+22 / −38 net)
- Heading shifts (h2→h1 for top section), 📎 markers stripped, page-wrap duplicates removed.

##### content/anthro1/human-skeletal-biology/index.md (−28 lines)
- Stripped 📎 markers and duplicate paragraphs around the bone-remodeling section.

##### content/anthro1/humans/index.md (−26 lines)
- Stripped 📎 markers and duplicate hominin-species descriptions.

##### content/anthro1/mitosis-and-meiosis/index.md (+3 / −7 net)
- Stripped 📎 markers; heading promoted h2→h1.

##### content/anthro1/modern-evolutionary-theory/index.md (−8 lines)
- Stripped 📎 markers.

##### content/anthro1/origin-of-new-species/index.md (+5 / −13 net)
- Stripped 📎 markers; heading promoted h2→h1.

##### content/anthro1/paleoanthropology/index.md (−16 lines)
- Stripped 📎 markers and duplicate australopithecine entries.

##### content/anthro1/primate-anatomy/index.md (−28 lines)
- Stripped 📎 markers and dental-formula duplicates.

##### content/anthro1/primates/index.md (+22 / −38 net)
- Heading shifts, 📎 markers stripped, fission-fusion paragraphs de-duped.

##### content/anthro1/traits/index.md (+11 / −19 net)
- Stripped 📎 markers; heading promoted h2→h1; Mendelian-genotype bullets de-duped.

##### content/anthro1/what-is-anthropology/index.md (+2 / −6 net)
- Stripped 📎 markers; heading promoted h2→h1.

#### Wave 1b — philosophy5 (`e6576de`)

##### content/philosophy5/design-arguments/index.md (+16 / −38 net)
- Stripped 📎 markers and Request-ID lines; heading hierarchy shifted; de-duped Paley/watchmaker paragraphs.

##### content/philosophy5/epistemic-catastrophe/index.md (+7 / −20 net)
- Stripped 📎 markers; heading promoted; Russell's-chicken paragraph de-duped.

##### content/philosophy5/ethics-of-ai/index.md (+30 / −73 net)
- Largest cleanup in the course — extensive page-wrap duplication across moral-status, value-alignment, and superintelligence sections; 📎 markers stripped throughout.

##### content/philosophy5/fine-tuning-argument/index.md (+9 / −24 net)
- Stripped 📎 markers; heading promoted; Anthropic-Principle paragraphs de-duped.

##### content/philosophy5/humes-problem-of-induction/index.md (+25 / −61 net)
- Stripped 📎 markers; heading hierarchy shifted; multiple page-wrap duplicates removed around the Goodman grue and Reichenbach sections.

##### content/philosophy5/natural-kinds/index.md (+4 / −11 net)
- Stripped 📎 markers; heading promoted.

##### content/philosophy5/scientific-realism/index.md (+15 / −33 net)
- Stripped 📎 markers; heading hierarchy shifted; de-duped realism/anti-realism paragraphs.

##### content/philosophy5/statistical-mechanics/index.md (+2 / −9 net)
- Stripped 📎 markers; heading promoted.

##### content/philosophy5/values/index.md (+5 / −28 net)
- Stripped 📎 markers; heading promoted; values/value-pluralism paragraphs de-duped.

### Wave 3 — Spelling and Grammar

#### Wave 3b — philosophy5 (`ccdee33`)

Five surgical fixes across four of nine sections. `epistemic-catastrophe`,
`natural-kinds`, `scientific-realism`, `statistical-mechanics`, and
`values` needed no changes.

##### content/philosophy5/design-arguments/index.md
- "appeal to an auxiliary hypotheses" → "appeal to an auxiliary hypothesis" (singular/plural agreement).

##### content/philosophy5/ethics-of-ai/index.md
- "## Chalmer's argument of gradual uploading" → "## Chalmers' argument of gradual uploading" (apostrophe — Chalmers's name ends in -s).

##### content/philosophy5/fine-tuning-argument/index.md
- "## Observervational Selection Effect" → "## Observational Selection Effect" (typo in heading).
- "There is no evidence of either hypotheses!" → "There is no evidence of either hypothesis!" (singular/plural agreement in the Firing Squad example).

##### content/philosophy5/humes-problem-of-induction/index.md
- "easy for them to reject each others' conclusions" → "easy for them to reject each other's conclusions" (apostrophe position — "each other" is singular).

#### Wave 3c — anthro1 (`ec29e65`)

22 surgical fixes across nine of 16 files. `mitosis-and-meiosis`,
`modern-evolutionary-theory`, `origin-of-new-species`, `primates`,
`primate-anatomy`, `traits`, and `what-is-anthropology` needed no
changes.

##### content/anthro1/bioarchaeology/index.md
- "# [U] Bioarcheology" → "# [U] Bioarchaeology" (top-of-page heading typo).
- "porotic hyperstosis" → "porotic hyperostosis" (OCR misread of the paleopathology term).
- "circular deformation in vertabrae (Pot's disease)" → "circular deformation in vertebrae (Pott's disease)" (two corrections: `vertabrae`→`vertebrae` and `Pot's`→`Pott's` — Percival Pott, the 18th-century surgeon).

##### content/anthro1/biocultural-evolution/index.md
- "1842: Retizius — cephalic index" → "1842: Retzius — cephalic index" (proper-noun typo, Anders Retzius).

##### content/anthro1/biological-classification/index.md
- "homoplasty: evolutionary development of analogous structures" → "homoplasy: evolutionary development of analogous structures" (term typo).

##### content/anthro1/evolution/index.md
- "da Vinci, Robert Hook, Nicholas Steno" → "da Vinci, Robert Hooke, Nicholas Steno" (proper-noun typo).
- "Alfred Russell Wallace: natural selection" → "Alfred Russel Wallace: natural selection" (proper-noun spelling — Wallace's middle name is `Russel` with one L).
- "organisms evolves towards perfection" → "organisms evolve towards perfection" (subject-verb agreement).

##### content/anthro1/geological-time-vertebrate-evolution/index.md
- "nerve chord (precursor to brain and spinal cord)" → "nerve cord (precursor to brain and spinal cord)" — fixed twice (once per duplicated chordate-trait bullet block preserved from the Wave 1 OCR pass).
- "Pre mammals (mamaliformes)" → "Pre mammals (mammaliformes)" (term typo).

##### content/anthro1/hominids/index.md
- "## Folivorus" → "## Folivorous" (term typo).
- Two instances of "saggital crest" / "saggital crests" → "sagittal crest" / "sagittal crests" (anatomical-term typo).
- "no saggital crest (round skull)" → "no sagittal crest (round skull)" — third occurrence in the chimps section.

##### content/anthro1/human-skeletal-biology/index.md
- "Woven bone → bony callous" → "Woven bone → bony callus" (medical-term typo; `callous` is the adjective, `callus` is the bone-repair structure).
- "irregular bones → specialized, complex (pelvis, vertabrae)" → "irregular bones → specialized, complex (pelvis, vertebrae)".

##### content/anthro1/humans/index.md
- "sapien: wise" → "sapiens: wise" (Latin species name).
- "Homo denisova – Siberia, East Asia, Ne Guinea" → "Homo denisova – Siberia, East Asia, New Guinea" (OCR misread of the place name).

##### content/anthro1/paleoanthropology/index.md
- "### Orrin tugenensis" → "### Orrorin tugenensis" (genus-name typo for the early hominid).
- "most primitive australopithicine" → "most primitive australopithecine" (term typo).
- "first australopithicene discovered — 'Taung baby'" → "first australopithecine discovered — 'Taung baby'" (different misspelling of the same term).

### Wave 4 — Content Accuracy (`422846c`)

Removed three empty stub headings that were transcribed from the
PDF outline but never followed by body content in the source notes.
Each was immediately followed by a sibling/parent heading, producing
empty TOC entries.

##### content/anthro1/biological-classification/index.md
- Removed trailing empty `## Taxonomy of Humans` heading at end of file (no body content followed it).

##### content/anthro1/geological-time-vertebrate-evolution/index.md
- Removed empty `## Geological Time` heading immediately preceding `## Vertebrate Evolution` (the H2 had no content of its own; the section name is already in the page title).

##### content/anthro1/human-skeletal-biology/index.md
- Removed empty `### Suture closure` heading immediately preceding `### Tooth wear` (the H3 had no content of its own — likely a planned subsection in the source notes that was never written up).

### Wave 6 — Cross-Course Wiki Links (`0ea9b37`)

24 cross-course wikilinks across 15 files connecting the new
courses (philosophy5, anthro1) into the existing graph
(psych131-140, psych150, cs188, data102, astro-c10).
Note: `mcbc61` is PDF-only with no markdown pages, so the suggested
anthro1↔mcbc61 links were re-routed to `psych131-140` /
`psych150`, which already contain Mendelian genetics, heritability,
and dual-inheritance content.

#### content/anthro1/biocultural-evolution/index.md
- Added a paragraph under `## Biocultural Evolution` linking to `[[psych131-140/culture]]` (Dual Inheritance Theory), `[[psych131-140/nature and nurture]]` (broader nature/nurture/culture decomposition), and `[[psych131-140/2-3 genetics]]` (genotype/heritability machinery used by the sickle-cell polymorphism).

#### content/anthro1/evolution/index.md
- Extended the "Heritability (genetics)" bullet to link to `[[psych131-140/2-3 genetics]]` (behavioral/clinical-trait framing) and `[[psych131-140/nature and nurture]]`.

#### content/anthro1/mitosis-and-meiosis/index.md
- Added trailing paragraph linking meiosis to `[[psych131-140/2-3 genetics]]` (twin-study heritability).

#### content/anthro1/modern-evolutionary-theory/index.md
- Added a paragraph under "Evolution: the change in allele frequencies" linking to `[[psych150/Heritability of Personality|heritability]]` and `[[psych131-140/2-3 genetics]]`.

#### content/anthro1/traits/index.md
- Added a top-of-section paragraph linking to `[[psych131-140/2-3 genetics]]` for the allele/genotype/phenotype framing applied to mental-health traits.

#### content/astro-c10/Cosmology.md
- Extended the multiverse-anthropic-principle bullet to link to `[[philosophy5/fine-tuning-argument]]` for the full philosophical treatment including the Inverse Gambler's Fallacy and the Firing Squad objection.

#### content/cs188/Machine Learning.md
- Added a paragraph after the supervised/unsupervised distinction linking to `[[philosophy5/ethics-of-ai]]` (moral status, value alignment, post-human civilization) and `[[philosophy5/humes-problem-of-induction]]` (the inductive leap from training set to unseen-data predictions).

#### content/philosophy5/design-arguments/index.md
- Added a parenthetical under `P(LIFE | DESIGN) > P(LIFE | CHANCE)` linking to `[[data102/hypothesis testing]]` (same likelihood-ratio reasoning).

#### content/philosophy5/ethics-of-ai/index.md
- Added a parenthetical under "An artificial system that can perform tasks…" linking to `[[cs188/Machine Learning]]` and `[[cs188/Neural Networks]]` (the concrete techniques the ethical concerns apply to).

#### content/philosophy5/fine-tuning-argument/index.md
- Added a parenthetical under `# Anthropic Principle` linking to `[[astro-c10/Cosmology]]` (physics-first framing alongside the Drake equation).

#### content/philosophy5/humes-problem-of-induction/index.md
- Added a parenthetical after the "Still ampliative…" bullet linking to `[[data102/parameter estimation]]`, `[[data102/hypothesis testing]]` (formal statistical inference), and `[[cs188/Machine Learning]]` (the training-set-to-unseen-data inductive leap).

#### content/psych131-140/2-3 genetics.md
- Extended the "Allele" bullet to link to `[[anthro1/traits]]` for the dominant/recessive Mendelian basics in an anthropology context.

#### content/psych131-140/culture.md
- Extended the "Dual Inheritance Theory" definition to link to `[[anthro1/biocultural-evolution]]` for the lactose-tolerance / sickle-cell case studies.

#### content/psych131-140/nature and nurture.md
- Extended the "culture is a third influential factor" sentence to link to `[[anthro1/biocultural-evolution]]` for the biocultural framing.

#### content/psych150/Heritability of Personality.md
- Extended the existing cross-references paragraph to additionally link to `[[anthro1/modern-evolutionary-theory]]` (population-level definition of evolution as the change in allele frequencies).

