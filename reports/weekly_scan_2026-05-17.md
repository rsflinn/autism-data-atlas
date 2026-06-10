---
type: weekly-deep-scan-report
date: 2026-05-17
window_start: 2026-05-10
window_end: 2026-05-17
agent: atlas-weekly-deep-scan
---

# Atlas Weekly Deep Scan -- 2026-05-17

## Headline

Quiet week. No new public autism dataset deposits in the 7-day window. No new GitHub tools relevant to the atlas. Five datasets URL-spot-checked, all reachable. Two new PubMed hits in the dataset queries -- both use existing data, neither deposits new data. The 18-gene wiki gap and 0/7 Phase 2 backfill flagged 2026-05-03 remain open with no progress this week.

## Step 1 -- New dataset discovery (PubMed)

Four PubMed queries run with edat 2026/05/10 to 2026/05/17.

Q1 (autism + GEO/SRA/scRNA-seq/ATAC-seq/ChIP-seq + dataset): 1 hit -- PMID 42129508 (Liu and Shimogori, Commun Biol 2026, [DOI](https://doi.org/10.1038/s42003-026-10045-x)). Spatiotemporal brain transcriptomics analysis using existing bulk and single-cell data across 15 neuropsychiatric traits. No new dataset deposit; analysis paper on prior data.

Q2 (autism + organoid/iPSC + RNA-seq/sequencing): 0 hits.

Q3 (autism + WGS + cohort/family/trio): 1 hit -- PMID 42135523 (Jung et al., Mol Psychiatry 2026, [DOI](https://doi.org/10.1038/s41380-026-03637-w)). Postpartum psychosis genetic architecture using existing Swedish registers, All of Us, and BioMe Biobank. Not autism per se; not a new deposit.

Q4 (neurodevelopmental disorder + scRNA-seq/spatial/epigenomics + data availability): 0 hits.

bioRxiv/medRxiv 7-day scans (genetics, genomics, neuroscience) surfaced one autism-adjacent preprint of note: Wang et al. 2026, bioRxiv 10.64898/2026.05.14.724487v1 -- STARMAPS framework for spatiotemporal enrichment of risk genes, integrating ~1 million previously deposited single-cell profiles from developing human brain. Analysis paper on existing data. No new deposit. Authors include Roeder and Sanders, so it will likely move into the daily-scan INTEGRATE stream when peer-reviewed.

## Step 2 -- Catalog drafts

No new entries drafted. `new_datasets_draft.json` retains the five prior unverified candidate entries from earlier weeks (Alonso-Gonzalez 2025, Cao 2025 NRXN1, Brudno 2026 H1/16p11.2, Forti 2025 PTHS splicing, Lee 2024 Wac models). These remain awaiting Ryan review.

## Step 3 -- URL spot-check (5 random catalog entries)

Positions 5, 6, 11, 14, 15 in datasets.json:

* `wamsley-2024-scgene` -- `https://doi.org/10.1126/science.adh2602` resolves. Paper title verified.
* `gandal-2024-celltype` -- same DOI as wamsley-2024-scgene (intentional sister entry from same Science paper covering a different analytical view). Both reachable. Worth noting: the citation strings are nearly identical, and a future cleanup could merge or clearly distinguish them.
* `pgc-cross-disorder` -- `https://pgc.unc.edu/for-researchers/download-results/` reachable. PGC summary statistics still posted without restriction; commercial use requires DAC approval.
* `gpf-sfari` -- `https://gpf.sfari.org/` reachable. Same access model (public for de novo + gene-level statistics; protected for raw SSC/SPARK data).
* `sfari-gene` -- `https://gene.sfari.org/` reachable. Q1 2026 report posted; database actively maintained.

No broken URLs. One structural redundancy to consider: `wamsley-2024-scgene` and `gandal-2024-celltype` could be a single entry with two analytical views noted in `description`, or renamed to clearly distinguish them (e.g., "...-cells" vs "...-modules").

## Step 4 -- GitHub tool scan

Four web searches for new repositories from the past week. No new tools surfaced relevant to the atlas.

The week's autism-genomics-related news coverage (the Pasca/Geschwind organoid convergence paper in Nature) refers to work already cataloged as `pasca-2026-organoids`. No new code repository identified for it in this scan.

Tools already in the catalog: BRAIN-MAGNET, AlphaGenome, ChromBPNet, variant-scorer, ANNEVO, Chorus, HDMA, PARM, GET, varTFBridge, genotype-phenotype-map.

## Step 5 -- Cross-reference health check

`wiki/index.md` link check: 117 unique link targets, 0 broken.

Atlas gene-page coverage: 9 of 27 atlas genes have wiki pages (MEF2C, SCN2A, FOXP1, TCF4, CDKL5, SHANK3, CHD8, DYRK1A, RFX3). 18 still missing: ADNP, ARID1B, AUTS2, BCL11A, CACNA1A, EP300, GRIN2A, GRIN2B, KCNB1, MECP2, MYT1L, PCDH19, RBBP5, RBFOX1, SLC6A1, STXBP1, SYNGAP1, WAC. Identical list to 2026-05-03 -- no gene-page backfill done in the past two weeks.

The `wiki/datasets/sfari-base.md` filename/content mismatch flagged on 2026-05-03 (file holds MSSNG entry per its frontmatter `id: mssng`) also remains unresolved.

## Step 6 -- Backfill progress

Phase 1 (10 critical datasets): 9 of 10 have wiki pages. Missing: `asc` (Autism Speaks Powered by Amazon WGS), distinct from MSSNG and from the ASC exome browser. No change from 2026-05-03.

Phase 2 (7 high-priority published studies): 0 of 7 have wiki pages. No change. Two of the Phase 2 entries (`cell_genomics_2024_a`, `cell_genomics_2024_b`) have placeholder DOIs (`10.1016/j.celrep.2024.xxxxx`) and need to be replaced with real citations before they can be backfilled.

Phases 3-4: not started.

Next 3 highest-priority backfills (unchanged from last week):
1. `asc` -- closes the Phase 1 gap.
2. `zhou_2019` -- foundational for the noncoding hypothesis still active in this project.
3. `pugsley_2024` -- recent and directly relevant to the noncoding-architecture question.

## Step 7 -- Website dataset feed

`datasets_feed.js` regenerated with 30 entries from `datasets.json`. Timestamp 2026-05-17. No content changes since no new datasets were added; the regenerated file is identical in structure to the 2026-05-03 version.

## Step 8 -- Notable

Two structural issues now appearing in consecutive weekly scans and worth flagging for a dedicated cleanup session:

1. **Wiki gene-page gap**: 18 missing pages, same list two weeks running. Several of these genes (SYNGAP1, MECP2, WAC, GRIN2A, AUTS2) already have multiple linked findings in the daily-scan stream.
2. **Phase 2 backfill stalled**: 0 of 7 entries done; 2 of the 7 have placeholder DOIs that block backfill until replaced.

Neither will resolve itself.

## Files written

* `datasets_feed.js` (regenerated, timestamp 2026-05-17)
* `reports/weekly_scan_2026-05-17.md` (this file)

No new tool, dataset, or wiki pages created this week.
