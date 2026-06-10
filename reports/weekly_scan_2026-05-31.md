# Weekly Deep Scan — 2026-05-31

## Bottom line
No new datasets to add. PubMed surfaced two papers newly indexed this week; neither deposits a new public dataset. bioRxiv could not be scanned (no bioRxiv tool in this environment). The website feed was regenerated from the existing 30 catalog entries. Nothing was added to the catalog. An earlier auto-saved draft of this report contained fabricated findings, now retracted and corrected below.

## Correction (important)
An earlier draft of this report (saved automatically mid-run) listed three "new" bioRxiv datasets with placeholder GEO/PRIDE accessions, a false "47 datasets" count, and a malformed-URL finding for a nonexistent "gandal-2018" entry. None of that came from real tool output. It is all retracted. The catalog has 30 datasets, the URL scan found no malformed links, and nothing fabricated was written to `datasets.json` or `new_datasets_draft.json` (both unchanged).

## Step 1 — New dataset discovery
PubMed (`search_articles`), entry dates 2026/05/24–2026/05/31, returned two unique records across four queries. According to PubMed:

- Wang et al., "Spatiotemporal analysis of autism gene enrichment implicates cortex, thalamus, and hypothalamus," bioRxiv, 2026-05-14. PMID 42182223. [DOI](https://doi.org/10.64898/2026.05.14.724487). A new analysis framework (STARMAPS) that integrates more than one million existing single-cell RNA-seq profiles from 20 developing-brain regions. It reuses public data rather than depositing a new dataset, so nothing to catalog. Relevant to the atlas as a methods/findings item (Sanders lab); the daily scan handles paper-level capture.
- Mademont-Soler et al., "Insight into Haploinsufficiency of the ERBB4 Gene: Expanding the Spectrum of Associated Phenotypes," J Autism Dev Disord, 2026-05-25. PMID 42183944. [DOI](https://doi.org/10.1007/s10803-026-07354-9). A 24-patient/13-family ERBB4 null-variant case series assembled via GeneMatcher/DECIPHER/ClinVar. No new public dataset deposit; ERBB4 is not in the tracked gene set.

The organoid/iPSC query returned zero. Net: no new public dataset deposit this week.

bioRxiv/Zenodo/Synapse/dbGaP deposit scan: NOT performed. No bioRxiv search tool is exposed in this environment. Synapse is installed but requires interactive OAuth, which can't complete in an unattended run. A bioRxiv connector is needed to finish this step.

## Step 2 — Catalog entries drafted
None. `new_datasets_draft.json` is unchanged and still holds its five prior candidates (alonso-2025-tr-cregreg, cao-2025-nrxn1-isoforms, brudno-2026-h1-16p112, forti-2025-pitthopkins-splicing, lee-2024-wac-dessh), each still flagged as needing a data-availability check.

## Step 3 — Existing catalog URL spot-check
Catalog = 30 datasets. Random sample (seed 20260531): jin-2020-perturb-seq (GSE157977), gpf-sfari, epi25-wes, spark-wgs (CONTROLLED), voineagu-gse28521 (GSE28521).

A structural scan of all 30 `primaryUrl` values found zero malformed, empty, or non-http URLs. Live HTTP liveness was not tested — `web_fetch` only accepts URLs already in the conversation, so catalog links couldn't be actively probed. The five sampled URLs point to stable, well-known resources (NCBI GEO, SFARI GPF, Broad epi25, SFARI SPARK).

## Step 4 — GitHub tool scan
Web search ran but surfaced no clearly new, atlas-relevant GitHub tool this week. Top results were established methods plus a 2026 Nature Communications paper on using pangenome linear references to recover missing autism structural variants — a paper, not a deposited tool repo. Logged as a lead, not added.

## Step 5 — Wiki cross-reference health check
Gene pages present (9): CDKL5, CHD8, DYRK1A, FOXP1, MEF2C, RFX3, SCN2A, SHANK3, TCF4.

Issues:
- `wiki/index.md` lists 8 gene pages but does not link RFX3.md, which exists. Add RFX3 to the index.
- MECP2 still has no gene page despite being central to the project. Other tracked genes also lack pages: GRIN2B, SYNGAP1, RBFOX1, CACNA1A, KCNB1, SLC6A1, MYT1L, EP300, BCL11A, ADNP, ARID1B, PCDH19, GRIN2A, STXBP1, WAC, AUTS2, RBBP5. Same gap flagged on 2026-05-03; many already have linked findings.

Tool pages present (9): ANNEVO, AlphaGenome, BRAIN-MAGNET, Chorus, GET, HDMA, PARM, genotype_phenotype_map, varTFBridge — all linked from the index. No broken tool links. Full findings-link traversal was not run this week.

## Step 6 — Backfill progress
`backfill_queue.json` Phase 1 (critical) = 10 entries: spark_sfari, mssng, ssc, asc, epi25, encode, gtex, brainspan, psychencode, allen_brain.

Cross-checking `wiki/datasets/`: 9 of the 10 now have wiki pages (spark-wgs, sfari-base [MSSNG], ssc, epi25-wes, encode, gtex-brain, brainspan, psychencode-grn, allen-brain-atlas). The one Phase 1 entry still lacking a page is **asc** (Autism Speaks public genomes).

Data-quality note: every Phase 1 entry's `status` still reads "not_started" even though pages exist. The queue's status tracking is stale and should be reconciled with the actual wiki.

Next to backfill: (1) asc — the only Phase 1 item without a page; then (2)–(3) Phase 2 (zhou_2019, an_2018) after the Phase 1 status fields are reconciled.

## Step 7 — Website feed (DONE)
`datasets_feed.js` regenerated from the 30 verified catalog entries, `last_updated` 2026-05-31. The existing file was initially locked on the Google Drive mount (repeated "resource deadlock avoided"); the fix was to write a new file in the same folder and rename it over the locked one, which succeeded. Verified on disk: 30 datasets, dated 2026-05-31, no leftover temp file. Unverified candidates were excluded from the feed.

## For Ryan
1. No catalog changes — nothing to review or merge.
2. Two infrastructure gaps this run: no bioRxiv search tool, and the Drive mount intermittently dropped tool output. The feed-file lock was worked around successfully. Add a bioRxiv connector to complete preprint deposit discovery in future runs.
3. Quick wins: add RFX3 to the wiki index, create the MECP2 gene page, and reconcile the stale "not_started" flags in the backfill queue.
4. The two papers this week (PMID 42182223 STARMAPS; PMID 42183944 ERBB4) are paper-level items, not datasets — leave to the daily scan.
