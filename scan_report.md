# Atlas Daily Scan Report — 2026-04-13

## Search Summary

**PubMed**: API returned 500 errors on all 4 queries. Fell back to web search, which surfaced one recently-indexed paper (PMID 40790933).

**bioRxiv**:
- Genetics: 5 results, 0 relevant
- Neuroscience: 20 results, 1 relevant (WAC/DeSanto-Shinawi)
- Genomics: 11 results, 1 relevant (EVEE variant prediction)

**medRxiv**: 0 results (empty for last 1-2 days)

## Papers Scored

| Paper | Score | Decision |
|-------|-------|----------|
| EVEE: Variant effect prediction via Evo 2 (bioRxiv) | 25/50 | INTEGRATE |
| WAC/DeSanto-Shinawi vertebrate models (bioRxiv) | 23/50 | INTEGRATE |
| FOXP1/SYNGAP1/DOCK4 SNPs in Turkish ASD/BD (PubMed) | 11/50 | REVIEW |

**Total: 3 papers found, 2 INTEGRATE, 1 REVIEW, 0 SKIP**

## Notable Findings

**EVEE (score 25)**: Most actionable finding. Evo 2 foundation model achieves 0.997 AUROC on ClinVar variant pathogenicity prediction -- outperforms all existing tools. Pre-computed predictions for 4.2M ClinVar variants available via web tool. Directly applicable to reclassifying VUS in the atlas's 49 NDD genes. Could complement or replace CADD/ChromBPNet scoring in variant prioritization pipeline.

**WAC models (score 23)**: WAC is not in the 49-gene atlas set, but the GABAergic neuron phenotype with dual autism+epilepsy presentation connects to the atlas's receptor-type work. Transcriptional profiling data from Wac-null mice may be useful for cross-referencing with existing NDD TF perturbation datasets (Lipton, Paulsen CHOOSE).

**FOXP1/SYNGAP1 study (score 11)**: Negative result from severely underpowered study (n=200). Two atlas genes (FOXP1, SYNGAP1) tested but findings not informative given sample size.

## Issues

- PubMed NCBI E-utilities API consistently returned 500 errors. This may have caused missed papers. Recommend retry tomorrow or manual PubMed check.
- medRxiv returned zero results for 1-2 day window, which may indicate API lag rather than zero submissions.

## Files Updated

- `raw/papers/10.1101_2024.05.26.595966.json`
- `raw/papers/10.64898_2026.04.10.717844.json`
- `logs/evaluation_decisions.jsonl` (+3 entries)
- `wiki/findings/biorxiv_WAC_DeSanto_Shinawi_2026.md`
- `wiki/findings/biorxiv_EVEE_variant_prediction_2026.md`
- `wiki/index.md` (appended)
- `papers_feed.js` (regenerated)
