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
