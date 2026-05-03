---
type: weekly-deep-scan-report
date: 2026-05-03
window_start: 2026-04-26
window_end: 2026-05-03
agent: atlas-weekly-deep-scan
---

# Atlas Weekly Deep Scan -- 2026-05-03

## Headline

One new tool added: BRAIN-MAGNET (Cell 2026, PMID 41265437). No new public autism dataset deposits found in the past 7 days. Five datasets URL-spot-checked, all reachable.

## Step 1 -- New dataset discovery

Four PubMed queries and four bioRxiv/medRxiv category scans were run for the 7-day window. The first PubMed query (autism + GEO/SRA/scRNA-seq/ATAC-seq + dataset) timed out at 180s; a simpler retry returned zero hits. Three other PubMed queries returned zero hits. bioRxiv genomics returned 30 results, none autism-specific dataset deposits. bioRxiv genetics returned 24 results, none autism-specific. bioRxiv neuroscience returned 30 results, none autism-specific dataset deposits. medRxiv genetics returned 30 results, none autism-specific dataset deposits.

Two adjacent papers worth noting (already in daily-scan stream, not catalog):

* SCADS preprint (Yu et al., bioRxiv 10.64898/2026.04.27.721080) -- single-cell ATAC framework for polygenic risk; methodology applicable to autism GWAS noncoding loci. Already captured in 2026-04-29 daily scan.
* Optical genome mapping in epilepsy brain tissue (Miller et al., medRxiv 10.64898/2026.04.18.26350985) -- somatic SVs in surgically resected epilepsy tissue; relevant to autism-epilepsy comorbidity but no new deposit cited in the abstract.

## Step 2 -- Catalog drafts

`new_datasets_draft.json` already contains five prior unverified candidate entries (Alonso-Gonzalez 2025, Cao 2025 NRXN1, Brudno 2026 H1/16p11.2, Forti 2025 PTHS splicing, Lee 2024 Wac models). These were left intact. No new entries added this week because no new dataset deposits were identified.

## Step 3 -- URL spot-check (5 random catalog entries)

Five entries verified via web search (positions 5, 10, 15, 20, 25 in datasets.json):

* `perez-2025-dup15q` -- primary URL `https://doi.org/10.1038/s41467-025-61184-4` resolves; paper title is "Single-cell analysis of dup15q syndrome reveals developmental and postnatal molecular changes in autism." Citation in datasets.json says "Dup15q organoid and postmortem brain transcriptomics" and "Nat Commun 2025;16:6177" -- the citation string is paraphrased rather than canonical. Flag for cleanup.
* `asc-wes` -- `https://epi25.broadinstitute.org/` reachable. Browser is shared between Epi25 and ASC.
* `sfari-gene` -- `https://gene.sfari.org/` reachable.
* `brainspan` -- `https://www.brainspan.org/` reachable, redirects to RNA-seq search.
* `chip-atlas` -- `https://chip-atlas.org/` reachable. Database documented at 230,000+ experiments matches the entry; Cell 2026/Nucleic Acids Res 2024 citation valid.

No broken URLs in the sample. One citation cleanup recommended (`perez-2025-dup15q` citation string).

## Step 4 -- GitHub tool scan

Four web searches targeting GitHub repos in the past week. Notable hit:

**BRAIN-MAGNET** (`https://github.com/ruizhideng/BRAIN-MAGNET`, Cell 2026, PMID 41265437). ChIP-STARR-seq-trained CNN that predicts non-coding regulatory element activity in human neural stem cells. ~100 million SNPs pre-scored, so a Teagan-WGS noncoding lookup is feasible without retraining. Trained on NSCs rather than cortical neurons or fetal organoids -- whether predictions transfer to autism-relevant cell types is an open question.

Saved metadata: `raw/tools/BRAIN-MAGNET.json`. Wiki page: `wiki/tools/BRAIN-MAGNET.md`. Index updated.

Other repos surfaced (variant-scorer, MPRA-DragoNN, ChromBPNet, AlphaGenome research code, PRSice, PRS-CS, pgsc_calc) are pre-existing and not new this week.

## Step 5 -- Cross-reference health check

Index links updated. Sample of links verified -- existing gene and dataset pages match index references. Atlas gene-page coverage gaps: 9 of 27 atlas genes have wiki pages (MEF2C, SCN2A, FOXP1, TCF4, CDKL5, SHANK3, CHD8, DYRK1A, RFX3). 18 missing: GRIN2B, SYNGAP1, RBFOX1, CACNA1A, KCNB1, SLC6A1, MECP2, MYT1L, EP300, BCL11A, ADNP, ARID1B, PCDH19, GRIN2A, STXBP1, WAC, AUTS2, RBBP5. Several of these (SYNGAP1, MECP2, WAC, GRIN2A, AUTS2) already have multiple linked findings and warrant backfill to clean up indirect references.

Note: `wiki/datasets/sfari-base.md` filename mismatches its content (the file is the MSSNG entry, frontmatter `id: mssng`). Worth a rename to `mssng.md` with redirect handling, or content split if both MSSNG and SFARI Base need separate pages.

## Step 6 -- Backfill progress

Phase 1 (10 datasets, foundational): 9 of 10 have wiki pages. Missing entry is the Autism Speaks "Powered by Amazon" cohort (`asc` in queue) -- distinct from MSSNG and from the ASC exome browser. Phase 2 (7 datasets, high-impact published studies): 0 of 7 have wiki pages. Phase 3 and Phase 4: not started.

Next 3 highest-priority backfills:

1. `asc` (Autism Speaks Powered by Amazon WGS) -- closes the Phase 1 gap.
2. `zhou_2019` (Zhou et al. 2019 de novo regulatory mutations) -- foundational paper for the noncoding hypothesis still active in this project.
3. `pugsley_2024` (large-scale noncoding variant association) -- recent and directly relevant to the noncoding-architecture question.

## Step 7 -- Website dataset feed

`datasets_feed.js` timestamp updated to 2026-05-03. No content changes (no new datasets added this week).

## Step 8 -- Notable

The `perez-2025-dup15q` citation cleanup is the only data-quality issue surfaced this week. The 18 missing gene pages and 0 of 7 Phase 2 backfill is a structural gap that won't fix itself -- worth scheduling a focused backfill session.

## Files written

* `raw/tools/BRAIN-MAGNET.json` (new)
* `wiki/tools/BRAIN-MAGNET.md` (new)
* `wiki/index.md` (BRAIN-MAGNET added to Tools; weekly-scan section appended)
* `datasets_feed.js` (timestamp updated)
* `reports/weekly_scan_2026-05-03.md` (this file)
