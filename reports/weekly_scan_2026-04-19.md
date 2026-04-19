---
title: Atlas Weekly Deep Scan
date: 2026-04-19
type: weekly_report
run_by: atlas-weekly-deep-scan (scheduled)
session: epic-gallant-cori
---

# Weekly Deep Scan -- 2026-04-19

## Bottom line

Three new candidate datasets flagged for manual verification. All 5 spot-checked catalog URLs resolve. Wiki has 22 broken internal cross-references and is missing 18 of 27 project-list gene pages. `datasets_feed.js` regenerated from 30-entry `datasets.json`. Phase 1 backfill has 9 of 10 wiki pages but only 1 of 10 formal catalog entries.

## 1. Dataset discovery (PubMed + bioRxiv, last 7 days)

Three ASD/NDD-relevant bioRxiv preprints surfaced in the genomics/genetics/neuroscience feeds. PubMed returned nothing new that was both dataset-linked and on-topic. All three are abstract-only; bioRxiv is blocked by the workspace egress allowlist, so Data Availability statements could not be fetched directly. Per Iron Laws, no accessions were invented — candidates are saved with `verificationStatus: "UNVERIFIED"` and flagged for Ryan.

Candidate files: `raw/datasets/candidate_*.json` (3 files).

Draft catalog entries appended to `new_datasets_draft.json` (preserves the 2 prior April 6 entries, adds 3 new ones):

- `brudno-2026-h1-16p112` -- Histone H1 regulation in 16p11.2 deletion ASD model
- `forti-2025-pitthopkins-splicing` -- RBFOX/NOVA splicing in TCF4/Pitt-Hopkins
- `lee-2024-wac-dessh` -- WAC DESSH mouse/zebrafish model v4 update

Next step for Ryan: open each bioRxiv PDF, pull the Data Availability statement, and (for any that disclose an accession) promote from `new_datasets_draft.json` into `datasets.json`.

## 2. Catalog updates

No direct edits to `datasets.json`. `new_datasets_draft.json` now contains 5 candidate entries (2 pre-existing + 3 new this week), all unverified.

## 3. URL spot-check (5 random catalog entries)

Deterministic sample (seed=20260419) from 30-entry catalog:

| ID | URL | Status |
|----|-----|--------|
| sfari-gene | https://gene.sfari.org/ | LIVE (indexed, last site update Jan 14, 2026) |
| ipsych-pgc-asd-gwas | https://pgc.unc.edu/for-researchers/download-results/ | LIVE |
| spark-wgs | https://www.sfari.org/resource/spark/ | LIVE |
| pgc3-scz | https://pgc.unc.edu/for-researchers/download-results/ | LIVE (duplicate URL with iPSYCH-PGC entry) |
| lipton-2024-mef2c | https://doi.org/10.1038/s41380-024-02761-9 | LIVE (resolves to nature.com) |

No broken links this week. Note the duplicate URL between `ipsych-pgc-asd-gwas` and `pgc3-scz` -- both point to the PGC download hub. That is accurate (it's the consortium's single distribution page) but the `downloadUrls` field on each entry should distinguish the specific summary-stats archive for that analysis. Low-priority cleanup.

## 4. GitHub tool scan

No brand-new releases this week. Existing tools already covered by the wiki (`tools/AlphaGenome.md`, `tools/varTFBridge.md`, etc.) remain the state of the art. Adjacent tools worth considering for future wiki coverage:

- `kundajelab/variant-scorer` -- ChromBPNet variant scoring framework (methods adjunct to our ChromBPNet work; reference-worthy)
- `pinellolab/chorus` -- wraps ChromBPNet + Enformer for variant-to-gene prediction
- `ciceklab/deepnd` -- DeepND cross-disorder NDD gene risk (ASD+ID multitask)
- `jchow32/EarlyPredictionSNN` -- NDD classifier, low-FPR design
- `PGScatalog/pgsc_calc` -- PGS Catalog reproducible scoring pipeline

Recommend wiki `tools/` entries for `variant-scorer` and `chorus` next — both are directly referenced in the AlphaGenome benchmarking we use.

## 5. Wiki cross-reference health check

91 wiki files scanned. Found **22 broken internal links across 15 files** (2 additional index-level targets and 5 gene-page pointers are the most consequential).

Category A: missing gene pages linked from existing pages.

- `genes/MEF2C.md` -> `BCL11A.md`, `MYT1L.md` (both missing)
- `genes/SHANK3.md` -> `GRIN2B.md`, `SYNGAP1.md` (both missing)
- `genes/RFX3.md` -> `EP300.md` (missing)
- `concepts/receptor_type_separation.md` -> `PCDH19.md`, `KCNB1.md`, `GRIN2A.md` (all missing)

Category B: missing dataset pages linked from concepts/gene pages.

- `concepts/convergence_phenomenon.md` -> `CHOOSE.md`, `Pasca_2026.md`, `Jin_2020.md`
- `concepts/receptor_type_separation.md` -> `Epi25.md`, `CHOOSE.md` (the Epi25 page exists under the slug `epi25-wes.md`; this is a naming-drift bug, not a missing page)
- `genes/MEF2C.md` -> `Lipton_2024.md`, `CHOOSE.md`, `Pasca_2026.md`

Category C: missing concept pages linked from findings.

- Four findings files link to `concepts/noncoding_variants_in_autism.md` with a malformed relative path (`./../../` instead of `../../`). The page exists; the paths are wrong.
- `findings/41935183.md` uses absolute-root paths (`/wiki/concepts/chromatin_accessibility.md`) that don't resolve in static-site rendering. Need `chromatin_accessibility.md` and `environmental_risk.md` concept stubs.
- `findings/biorxiv_brain_nuclei_nanoCUTTag_2026.md` and `biorxiv_enhancer_hubs_Th17_2026.md` have the same absolute-path bug.

Category D: gene-page gap vs. project gene list.

Present (9): CDKL5, CHD8, DYRK1A, FOXP1, MEF2C, RFX3, SCN2A, SHANK3, TCF4.

Missing (18): GRIN2B, SYNGAP1, RBFOX1, CACNA1A, KCNB1, SLC6A1, MECP2, MYT1L, EP300, BCL11A, ADNP, ARID1B, PCDH19, GRIN2A, STXBP1, WAC, AUTS2, RBBP5.

Recommendation: next wiki sprint stubs out the 5 genes that are actively linked from existing pages (BCL11A, MYT1L, GRIN2B, SYNGAP1, EP300, PCDH19, KCNB1, GRIN2A) before starting on the rest. Fix the 4 malformed `./../../` relative-path findings links (one-line sed). No `index.md` broken links this scan (all 83 link targets resolve).

## 6. Backfill queue progress

Phase 1 (10 critical entries): 9 of 10 have wiki pages. The gap is ASC (Autism Sequencing Consortium) -- no wiki, no catalog entry. ASC underpins the canonical Satterstrom 2020 gene list and is probably the single highest-value backfill remaining.

Catalog coverage for Phase 1 is much weaker: only BrainSpan has a formal `datasets.json` entry. SPARK, MSSNG, SSC, Epi25, ENCODE, GTEx, PsychENCODE and Allen Brain Atlas each have wiki pages but no catalog entry (so they don't show up in the website feed). This is the bigger gap to close.

Phases 2-4 (19 entries): none have wiki pages or catalog entries.

Suggested next 3 backfills, in order:
1. ASC -- both wiki page and catalog entry
2. SPARK catalog entry -- wiki page already exists
3. MSSNG catalog entry -- wiki is folded into `sfari-base.md`, may want its own catalog row

## 7. datasets_feed.js regenerated

Rebuilt from `datasets.json` (30 entries, up from 0 placeholders in the prior file). Output: `datasets_feed.js`, 31 KB. `last_updated` field now reflects 2026-04-19.

## 8. Summary

| Item | Count |
|---|---|
| New candidate datasets flagged | 3 (all UNVERIFIED) |
| Spot-checked URLs | 5 of 5 live |
| GitHub tools worth adding | 5 (variant-scorer, chorus, deepnd, EarlyPredictionSNN, pgsc_calc) |
| Wiki broken internal links | 22 across 15 files |
| Missing project-list gene pages | 18 of 27 |
| Phase 1 backfill -- wiki pages | 9 of 10 |
| Phase 1 backfill -- catalog entries | 1 of 10 |
| datasets_feed.js entries | 30 |

Nothing here blocks current analytical workstreams. The wiki hygiene items (broken paths, missing gene stubs) are the most tractable low-hanging fruit; the catalog/Phase-1 gap is the larger structural deficit.
