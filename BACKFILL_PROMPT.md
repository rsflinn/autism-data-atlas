# Prompt: Historical backfill of the Autism Data Atlas

Paste this into a fresh Claude session. It's self-contained — Claude should read the referenced files first, then execute. The session is meant to run as autonomous research work, not as a quick conversation.

---

## The job

The Autism Data Atlas is an open knowledge base mapping the genetic roots of autism for parents, citizen scientists, journalists and working researchers. It currently contains roughly 150-200 unique papers gathered by a daily scanning agent that started recently. We need a **historical backfill** — going back through twenty-plus years of autism research — so the corpus reflects the actual literature, not just what's been published this month.

You have two tasks. Do them in order. Both must be complete before you stop.

**Task 1 — Backfill.** Pull a substantial sample of historical autism research from PubMed and bioRxiv, score each paper against the atlas's existing relevance criteria, and add the qualifying ones to the corpus in the same format the daily agent uses. Target: at least 800 newly indexed papers covering the period 2005-present, weighted toward 2015-2024 where the field's productivity is highest.

**Task 2 — Synthesize.** Once the backfill is in place, write a short report that looks across the full corpus — original 150-200 plus the new 800+ — and identifies patterns: where the field has clustered, where it has gaps, which genes appear repeatedly across decades, where mechanism work outpaces treatment work, where preprints are clumped while trials are scarce, what the trajectory of the field looks like.

---

## Files to read before starting

In this exact order. Don't skip any.

1. `/Users/ryanflinn/Library/Mobile Documents/com~apple~CloudDocs/Personal/Teagan's genetic files/CLAUDE.md` — the project's master memory. It contains the Iron Laws (truth and writing rules) you must follow, the project's history including which hypotheses have been retired, and the user's role and preferences.

2. `/Users/ryanflinn/Library/Mobile Documents/com~apple~CloudDocs/Personal/Teagan's genetic files/autism-data-atlas/CLAUDE.md` — the atlas-specific memory. Same Iron Laws, with extra detail on what the atlas is and what's in it.

3. `/Users/ryanflinn/Library/Mobile Documents/com~apple~CloudDocs/Personal/Teagan's genetic files/autism-data-atlas/ATLAS_ARCHITECTURE.md` — the architectural vision for the atlas. Read the sections on the agent pipeline, the relevance scorer, the evidence tier system, and the backfill strategy. Phases 1 through 4 in that document define what to prioritize.

4. `/Users/ryanflinn/Library/Mobile Documents/com~apple~CloudDocs/Personal/Teagan's genetic files/autism-data-atlas/VOICE_AND_STYLE.md` — the editorial voice. Apply this to any summaries you write. Plain language. Active voice. Define every technical term in plain language on first use. Avoid gene names, accession codes, and acronyms unless they are the news.

5. `/Users/ryanflinn/Library/Mobile Documents/com~apple~CloudDocs/Personal/Teagan's genetic files/autism-data-atlas/raw/papers/` — the current paper corpus. Look at five or six JSON files to understand the schema you'll be writing to.

6. `/Users/ryanflinn/Library/Mobile Documents/com~apple~CloudDocs/Personal/Teagan's genetic files/autism-data-atlas/wiki/findings/` — the compiled findings. Look at three or four to understand the markdown schema.

7. `/Users/ryanflinn/Library/Mobile Documents/com~apple~CloudDocs/Personal/Teagan's genetic files/autism-data-atlas/structured/datasets_catalog.json` — the dataset catalog. Useful context for understanding what cohorts the corpus draws on.

---

## Iron Laws — non-negotiable

These come from the master CLAUDE.md and apply to every paper you score, every summary you write, every claim you make in the synthesis report.

**Truth.**

1. Never invent. No fabricated abstracts, citations, statistics, sample sizes, or findings. If you can't verify a paper exists and matches what you say about it, don't include it.

2. Never spin. If a paper's findings are ambiguous or null, say so. If a study is underpowered, say so. Soften nothing.

3. Three Gates before claiming any pattern in the synthesis report — what's the null, what would falsify it, what's the base rate. If a "trend" disappears under any of those three checks, drop it.

4. State dataset and methodological limits every time. Mouse-only findings noted. Single-cohort findings noted. Preprint-vs-peer-reviewed noted.

**Writing.**

5. Bottom line first. Every summary leads with what + why anyone should care. No buildup.

6. Plain language at high-school reading level. Define every technical term on first use. Avoid jargon, accession codes, gene names except where the gene is the news.

7. No honesty theater, no throat-clearing, no marketing language.

If at any point a rule on this page would push you to invent or pad, leave the rule. Drop the paper. Trim the summary. Skip the section.

---

## Task 1 — Backfill, in detail

### Source priority

Hit PubMed first via the E-utilities API or the connected PubMed MCP. Use queries derived from the four research tracks already in the atlas plus broader ones. Examples (combine with `AND ("autism" OR "ASD" OR "autism spectrum disorder")`):

- Genetic discovery: `("genome-wide" OR "GWAS" OR "exome" OR "whole-genome sequencing" OR "rare variant" OR "de novo")`
- Mechanism: `("brain organoid" OR "iPSC" OR "knockout" OR "haploinsufficiency" OR "synapse" OR "neuron" OR "ion channel")`
- Phenotype and comorbidity: `("epilepsy" OR "intellectual disability" OR "language" OR "regression" OR "comorbid")`
- Diagnosis: `("clinical exome" OR "diagnostic yield" OR "screening" OR "biomarker")`
- Treatment: `("clinical trial" OR "intervention" OR "therapy" OR "drug")`

For each query, paginate. Don't stop at the first 50 results. Aim for at least 200 papers per query, then de-duplicate at the end.

For bioRxiv preprints, hit the bioRxiv MCP if available, otherwise the bioRxiv API. Pull autism-tagged preprints from 2018 forward.

### Scoring

For every candidate paper, score it on the same 0-50 scale used by the existing scanner, with the same six axes. The schema is in any file in `raw/papers/` — autism_relevance (0-10), noncoding_regulatory (0-10), dataset_availability (0-10), novelty (0-10), cell_type_specificity (0-5), phenotype_severity (0-5).

The threshold from the architecture doc is: score >= 25 → INTEGRATE, 15-24 → REVIEW, <15 → SKIP. Apply that threshold. Do not include SKIP-tier papers in the corpus.

### De-duplication

Before integrating any paper, check existence by DOI, PMID, and bioRxiv DOI against the existing `raw/papers/` corpus. If the paper is already there, don't write a duplicate. Update the existing record only if you have substantively new metadata.

### Output format

For each new INTEGRATE-tier paper, write a JSON file to `raw/papers/{pmid_or_doi_safe}.json` with the same schema as the existing files. Required fields:

- `pmid` and/or `doi`
- `title`, `authors`, `journal`, `date` (YYYY-MM)
- `source` (`pubmed` or `biorxiv` or `medrxiv`)
- `url`
- `abstract` (the paper's actual abstract)
- `relevance_score` (integer 0-50)
- `score_breakdown` (object with the six axes)
- `decision` (`INTEGRATE` or `REVIEW`)
- `genes_mentioned` (array of HGNC symbols extracted from title and abstract)
- `summary` (one or two sentences in the atlas voice — plain language, lead with so-what)

For REVIEW-tier papers (score 15-24), write to a separate `raw/papers/review_queue/` subdirectory so they're flagged but not in the main feed.

### What the user explicitly cares about

The user is the parent of a profoundly autistic 18-year-old with drug-resistant epilepsy and a negative clinical exome. The atlas exists because this case is genetically undiagnosed despite obvious heritability. Prioritize:

- Studies on undiagnosed severe autism
- Studies on autism + epilepsy comorbidity
- Studies on noncoding and regulatory variants (since coding-only exomes miss them)
- Studies on oligogenic and polygenic models (multiple-small-effect rather than single-gene)
- Studies on the genes already in the atlas (see the gene list in `structured/datasets_catalog.json` and the project memory)

These get a small relevance boost in your scoring. Don't go overboard — a low-quality paper on a priority topic is still low-quality.

### What to skip

- Papers behind paywalls where you cannot retrieve the abstract
- Papers in non-English languages
- Conference abstracts and editorials
- Studies clearly about animal welfare, agriculture, etc., that surfaced incidentally

---

## Task 2 — Synthesis report

Once the backfill is in place, write `wiki/synthesis/state_of_autism_research_2026.md` covering the full combined corpus.

The report follows the atlas voice guide. Three paragraphs per section, the Bloomberg-derived structure: theme + so-what / details / nut graf. No quotation paragraph required.

Sections to cover:

1. **The shape of the corpus.** How many papers, what years, what kinds of studies. Where the productivity is concentrated.

2. **Gene-by-gene activity.** Which genes appear repeatedly across decades. Which ones spiked and fell. Which ones haven't been touched in years. Which ones are emerging.

3. **Where the field has converged and where it has diverged.** Are mechanism studies agreeing with each other? Where do treatment trials line up against the gene work that motivated them? Are there gene clusters that map to specific phenotypes?

4. **Trends in study type.** Computational and theoretical work vs. cellular vs. animal vs. human observational vs. trial. Where is the volume? Where are the bottlenecks?

5. **Gaps and quiet areas.** Conditions, populations, mechanisms, or genes that are notably under-studied relative to their importance. Be specific. "Severely affected adults" not "this needs more work."

6. **What's likely to land next.** Based on preprint clusters, registered trials, and recent funding patterns visible in the data.

The whole report should be 2,000-3,500 words. Cite specific paper counts and DOIs as evidence for every claim. If you can't cite, drop the claim.

---

## Stopping conditions

You're done when, in this exact order:

1. At least 800 new INTEGRATE-tier papers are in `raw/papers/` with valid schemas.
2. Each one is de-duplicated against prior corpus.
3. The REVIEW queue is populated with marginal papers.
4. The synthesis report is written, edited, and saved at the path above.
5. A brief progress log is appended to `logs/backfill_log.md` with: total papers added, breakdown by year, breakdown by source, time taken.

If you hit a soft block — API rate limits, missing abstracts, ambiguous duplicates — log it, work around it, keep going. Don't stop early because of one obstacle.

If you can't reach 800 because the search space is genuinely smaller than that (the field literally doesn't have that much material in the priority topics), document why in the progress log and proceed to the synthesis with whatever you have.

---

## When you're done

Tell the user:

- How many papers were added
- What years they span
- Where the synthesis lives
- One or two surprising findings from the synthesis (in the atlas voice — plain language, so-what first)

Then stop.
