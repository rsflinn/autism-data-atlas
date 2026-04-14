---
pmid: N/A
doi: 10.64898/2026.04.10.717844
title: "EVEE: Interpretable variant effect prediction from genomic foundation model embeddings"
authors: "Pearce MT et al."
journal: "bioRxiv"
date: 2026-04-11
relevance_score: 25
decision: INTEGRATE
genes_mentioned: []
concepts: [variant effect prediction, foundation model, ClinVar, VUS, pathogenicity, Evo 2]
evidence_tier: C
---

# EVEE: Interpretable variant effect prediction from genomic foundation model embeddings

## Key Findings
Evo 2 (7B-parameter genomic foundation model) embeddings enable SOTA variant pathogenicity prediction: 0.997 AUROC on 839k ClinVar SNVs, 0.991 AUROC zero-shot on indels. Outperforms all existing meta-predictors and protein models. Interpretable disruption profiles translated to natural language explanations. Pre-computed predictions for all 4.2M ClinVar variants available via EVEE web tool.

## Relevance to Atlas
Directly applicable to reclassifying VUS in autism-associated genes. The atlas's 49-gene set includes many genes with noncoding VUS that could be rescored through EVEE. Particularly relevant for the noncoding variant analysis track, where current tools (CADD, ChromBPNet) have known limitations. The foundation model approach may capture regulatory variant effects that sequence-conservation-based tools miss.

## Genes
Not gene-specific. Applicable to all 49 atlas genes for VUS reclassification, especially for noncoding variants in: MECP2, EP300, SCN2A, FOXP1, TCF4, CDKL5, MEF2C.

## Methods
Evo 2 foundation model embeddings + linear probe classifiers. Trained on ClinVar labels. Validated on deep mutational scanning datasets (BRCA1, BRCA2, TP53, LDLR). Interpretability via supervised annotation probes + LLM explanation generation.

## Cross-references
Related to ChromBPNet variant scoring pipeline. See chrombpnet/ directory for comparison. Could complement or replace CADD scores used in atlas variant prioritization.
