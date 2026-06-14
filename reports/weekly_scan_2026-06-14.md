# Weekly Deep Scan — 2026-06-14

**Bottom line:** No new public datasets and no new tools to add this week. Caught and fixed two orphaned wiki pages, refreshed the website dataset feed, and flagged one concept page that contradicts a tested result. Catalog holds steady at 30 datasets.

Window scanned: 2026-06-07 to 2026-06-14. Paths note: the task file points at an old session ID (`friendly-serene-ride`); the atlas is mounted this session at `autism-data-atlas/`, which is what I used.

---

## New datasets discovered

None deposited and accessible this week.

Four PubMed queries returned three unique records, none with a newly deposited public dataset:

- **PMID 42281968** — Dominguez-Alonso et al., *Research Square* preprint. Targeted sequencing of 85,394 cCREs in 200 coding-negative ASD trios; noncoding regulatory variants disrupt CTCF domains. Highly relevant to the project's noncoding-regulatory focus, but it reuses existing data (snRNA-seq from a prior cohort, Broad Cortical Organoid Atlas) and deposits no accessible dataset. Already captured by the 2026-06-13 daily scan. DOI: 10.21203/rs.3.rs-9650619/v1
- **PMID 42286492** — Reka et al., *BMC Psychiatry*. Retrospective CMA of 234 pediatric ASD patients; no public deposit. Already captured 2026-06-13. DOI: 10.1186/s12888-026-08263-y
- **PMID 42256340** — Al-Younis et al., *Front Genet*. Single DYRK1A case report; no dataset. DOI: 10.3389/fgene.2026.1813300

bioRxiv/medRxiv: the two autism single-cell preprints that surfaced (Wang et al. integrative developing-brain atlas; Young et al. spatial transcriptomics) are dated May 14–15, outside the 7-day window. No new deposits in-window.

*Attribution: PubMed records above retrieved via PubMed.*

## New catalog entries drafted

None. `new_datasets_draft.json` left unchanged — nothing verified to add.

## Broken URLs found

None. Spot-checked 5 of 30 catalog entries, all live: denovo-db.gs.washington.edu, psychscreen.wenglab.org, chip-atlas.org, brainscope.gersteinlab.org, gpf.sfari.org.

Caveat: full HTTP fetch is blocked by the fetch provenance restriction (same limitation logged in recent daily scans), so liveness was confirmed via search-index existence rather than a direct request. A true reachability check needs the URL passed in directly or a different fetch path.

## New tools found

None verifiably new. The GitHub scan surfaced only established repos already in the catalog: kundajelab/chrombpnet, kundajelab/variant-scorer, pinellolab/chorus, deepmind/alphagenome_research. One older third-party repo (rwang916/PEPSI, splicing-variant prediction) is not clearly new and not a priority; noted, not added.

## Wiki health issues

1. **Two orphan pages fixed.** `wiki/genes/RFX3.md` and `wiki/datasets/valone2026.md` existed but weren't linked from `wiki/index.md`. Both are now linked in their sections.
2. **Concept page contradicts a tested result — needs your review.** `wiki/concepts/receptor_type_separation.md` still states the class-level framing ("GABA receptors drive epilepsy, glutamate receptors drive autism convergence"). The April 2026 reanalysis downgraded this to PARTIALLY FAILED: class-level separation didn't hold (epilepsy MWU p=0.189), and GRIN2A's significant epilepsy PTV burden breaks the glutamate=autism claim. Individual shared genes (SCN2A, KCNB1, PCDH19) are real; the receptor-class story is not. I did not rewrite the page — the reframing is a science-framing call for you.
3. **Missing gene pages (no change this week).** 18 of the 27-gene atlas set still lack pages: GRIN2B, SYNGAP1, RBFOX1, CACNA1A, KCNB1, SLC6A1, MECP2, MYT1L, EP300, BCL11A, ADNP, ARID1B, PCDH19, GRIN2A, STXBP1, WAC, AUTS2, RBBP5. SYNGAP1 and WAC each have multiple findings already linked and are the strongest backfill candidates. No new in-set genes were introduced by this week's papers (the new CTCF preprint implicates POGZ, NFIB, ROCK2 — not in the atlas set).

## Backfill progress

Phase 1 (10 critical datasets) is effectively complete: 9 have wiki pages and the 10th (ASC / Autism Speaks public cohort) is the only gap. Note: `structured/backfill_queue.json` still marks every entry `not_started` — it hasn't been updated since 2026-04-04 and no longer reflects reality. Worth a one-time status refresh.

Next 2–3 priorities to backfill:

1. **SYNGAP1 gene page** — heavily referenced across findings, still missing.
2. **WAC gene page** — multiple findings this spring (DeSanto-Shinawi models, Boonpraman 2026), still missing.
3. **Zhou et al. 2019 de novo regulatory mutations** (Phase 2 top entry) — directly on the noncoding-regulatory thesis. Several other Phase 2 entries carry placeholder DOIs (`10.1038/nature`, `celrep.2024.xxxxx`) and should be verified or dropped before any backfill.

## Website feed

`datasets_feed.js` regenerated from the 30 verified `datasets.json` entries; `last_updated` set to 2026-06-14. No content change beyond the date — no new datasets this week.

## Notable for you

- The Dominguez-Alonso CTCF preprint (PMID 42281968) is the most on-thesis item this week even though it isn't a dataset: noncoding regulatory variants in coding-negative ASD trios disrupting CTCF boundaries, with maternal transmission bias on inherited variants. If they later deposit the targeted-sequencing data, it would be worth cataloging.
- The receptor-type-separation concept page is the one real inconsistency in the wiki right now. Recommend reframing it around specific shared genes before it's cited anywhere downstream.
