---
title: AlphaGenome
type: tool
category: variant_effect_prediction
relevance: HIGH
date_added: 2026-04-04
source: weekly_tool_scan
---

# AlphaGenome

Google DeepMind's unified DNA sequence model for regulatory variant effect prediction. Published in Nature, January 2026.

## What It Does

Takes up to 1 Mb of DNA sequence as input and outputs predictions at single base-pair resolution across multiple functional genomic modalities:

- Gene expression
- Transcription initiation
- Chromatin accessibility (ATAC-seq / DNase-seq equivalent)
- Histone modifications
- Transcription factor binding
- Chromatin contact maps
- Splice site usage and junction strength

Trained on human and mouse genomes. Matches or exceeds the strongest prior models in 25 of 26 variant effect prediction evaluations.

## Why It Matters for the Atlas

AlphaGenome provides the most comprehensive single-model solution currently available for scoring noncoding autism variants. It directly addresses the atlas's core task: linking regulatory variants to disrupted gene expression. Unlike earlier models that predict one or two modalities, AlphaGenome integrates the full chain from chromatin accessibility to TF binding to gene expression — reducing the need to chain multiple tools.

It is directly complementary to [varTFBridge](./varTFBridge.md), which traces TF-to-gene consequences; AlphaGenome handles the upstream step of predicting which TF binding sites are disrupted.

## Access

- Research code and model weights: [github.com/google-deepmind/alphagenome_research](https://github.com/google-deepmind/alphagenome_research)
- API access (noncommercial): [https://deepmind.google.com/science/alphagenome](https://deepmind.google.com/science/alphagenome)
- Python SDK: [github.com/google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome)

## Publication

Jumper et al. "Advancing regulatory variant effect prediction with AlphaGenome." *Nature* (2026). PMID: 41606153. DOI: 10.1038/s41586-025-10014-0

## Integration Status

Not yet integrated into atlas pipelines. Recommended as the primary variant effect scoring engine for the noncoding variant analysis workflow. Priority: HIGH.

## Related Tools

- [varTFBridge](./varTFBridge.md) — downstream TF-to-gene consequence tracing
- [PARM](./PARM.md) — promoter activity prediction
- [GET](./GET.md) — gene expression across cell types from chromatin data

---
**Added:** 2026-04-04 (weekly tool scan)
