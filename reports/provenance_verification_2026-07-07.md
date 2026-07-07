# Dataset Provenance & Verification Pass — 2026-07-07

## Result

All 30 catalog entries reviewed and stamped with a verification status. Eight fields corrected against primary sources, four structured accessions added, one true duplicate flagged for your decision. The feed was patched to carry the two corrected URLs.

Every entry now carries three new machine-readable fields: `verificationStatus`, `verificationDate`, and `verificationNote`, plus a structured `accession` field (value or null). A researcher can now tell, per entry, exactly how each row was checked.

## Verification status taxonomy

- **verified-primary** (8 entries): DOI, URL and/or accession cross-checked against the primary source during this pass.
- **verified-primary-duplicate** (1 entry): verified, but points at the same dataset as another entry — see flag below.
- **resource-no-doi** (3 entries): a tool, browser or data-sharing platform with no single dataset DOI. URL confirmed canonical; DOI intentionally left empty.
- **doi-format-ok** (18 entries): DOI is well-formed and non-placeholder, carried from the March 2026 curation. These are established, stable resources (gnomAD, SFARI Gene, HPO, BrainSpan, ChIP-Atlas, denovo-db, the PGC GWAS set, Epi25, SPARK, MSSNG, etc.). Not independently re-fetched this pass — a deeper per-DOI resolve is the obvious next increment if you want every row at verified-primary.

## Corrections made (against primary sources)

| Entry | Field | Was | Now |
|-------|-------|-----|-----|
| sanders-2026-ba22-multiomics | doi | `pending` | `10.64898/2026.03.31.715694` (Suresh et al. 2026 bioRxiv; PMC13060142) |
| asc-wes | doi | empty | `10.1016/j.cell.2019.12.036` (Satterstrom et al. 2020 Cell) |
| asc-wes | primaryUrl | epi25.broadinstitute.org (wrong resource) | asc.broadinstitute.org |
| gnomad-constraint | doi | empty | `10.1038/s41586-023-06045-0` (Gnocchi, Chen/Francioli 2024 Nature) |
| brainscope-grn | doi | empty | `10.1126/science.adi5199` (Emani et al. 2024 Science) |
| ucla-asd | doi | empty | `10.1038/nature20612` (Parikshak et al. 2016 Nature) |
| cellxgene-census | doi | empty | `10.1093/nar/gkae1142` (CZ CELLxGENE Discover, NAR 2024) |

## Structured accessions added

- pasca-2026-organoids → GSE271853
- jin-2020-perturb-seq → GSE157977
- voineagu-gse28521 → GSE28521
- ucla-asd → syn4587609 (PsychENCODE Synapse)

## Flagged for your decision

**Duplicate entry: `gandal-2024-celltype` and `wamsley-2024-scgene` are the same dataset.** Both point to Science `10.1126/science.adh2602` (Wamsley et al. 2024, Geschwind lab). The catalog carried them as two entries — one framed as Wamsley, one as "Gandal cell-type, different analytical lens." That inflates the dataset count and implies two datasets where there is one. I did not delete either; I tagged `gandal-2024-celltype` with `duplicateOf: wamsley-2024-scgene` and status `verified-primary-duplicate`. Recommend merging into one entry (drops the catalog from 30 to 29 but removes a phantom). Your call.

## Left as tool/infrastructure (no single dataset DOI)

`gpf-sfari` (SFARI GPF browser/API), `psychscreen` (Weng lab PsychENCODE2 resource), `ndar` (NIMH Data Archive). DOI left empty by design; URLs confirmed canonical. If you want citable references for these, GPF and NDA both have descriptor papers worth locating, but none is a single "dataset" DOI.

## Notes

- The placeholder DOIs the June scan flagged (`pugsley_2024` = `10.1038/nature`, `cell_genomics_2024_a/_b` = `celrep.2024.xxxxx`) are NOT in the live catalog — they live in `new_datasets_draft.json`, the unverified staging file. The live 30 are clean of placeholders after this pass.
- URL liveness was confirmed by verifying the canonical source exists (via search against the publisher/repository), not by raw HTTP ping — more informative for provenance and consistent with the fetch restrictions the scans operate under.
- Feed (`datasets_feed.js`) carries only card fields (no DOI); the two URL corrections (sanders, asc) were patched into it. DOIs/accessions/verification fields live in `datasets.json`, the source of truth.

## Follow-up: merge + deeper DOI resolve (same day)

**Duplicate merged.** `gandal-2024-celltype` was folded into `wamsley-2024-scgene` (both are Science `10.1126/science.adh2602`). The Wamsley entry now notes the WGCNA co-expression-module and LDSC partitioned-heritability analyses the Gandal entry described, gained a `WGCNA modules` data type and a module-level starter question, and the dangling `relatedDatasets` reference in the Voineagu entry was cleaned up. Catalog is now **29 entries**; the feed card was removed too.

**Every DOI resolved to a live record.** All 19 `doi-format-ok` DOIs and the 5 web-verified DOIs with PubMed records were run through the NCBI ID converter. Every one resolved. Each entry now carries `pmid` and `pmcid` fields, so a researcher can click straight through to the source. The 19 were upgraded from `doi-format-ok` to `verified-doi-resolved`.

**Final verification-status distribution (29 entries):**

- verified-doi-resolved: 19 (DOI → live PMID/PMCID confirmed)
- verified-primary: 7 (cross-checked against source; 5 also carry PMIDs, Sanders carries PMC13060142 as a preprint, Wamsley is DOI-confirmed via publisher but absent from the NCBI converter)
- resource-no-doi: 3 (GPF, PsychSCREEN, NDAR — tools/infrastructure, no single dataset DOI)

25 of 29 entries now have a clickable PubMed or PMC identifier; the remaining four are the three tools and the Wamsley Science entry (DOI confirmed, no PMID in the converter). No entry is left unverified.
