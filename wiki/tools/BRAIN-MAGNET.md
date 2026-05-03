---
title: BRAIN-MAGNET
type: tool
status: candidate (needs review)
last_updated: 2026-05-03
discovery_source: weekly_deep_scan
relevance: high
---

# BRAIN-MAGNET

A convolutional neural network for non-coding regulatory variant interpretation in brain disease. Authors trained the model on chromatin immunoprecipitation coupled with self-transcribing active regulatory region sequencing (ChIP-STARR-seq) data from human neural stem cells, then validated that the model's predictions match functional readouts.

## What it does

BRAIN-MAGNET takes a DNA sequence (or a variant in a sequence) and predicts whether the surrounding region functions as an active non-coding regulatory element in neural stem cells, plus how strongly. The authors pre-computed predictions for roughly 100 million SNPs across all NSC regulatory regions, so most users can look up a variant in a pre-scored table rather than running the model.

## Why it matters for this project

Autism GWAS hits are noncoding (Grove 2019), and ~49% of autism heritability comes from common inherited variants of mostly unknown function. A neural-stem-cell-trained activity model is a closer biological match for fetal-brain autism mechanisms than adult-tissue annotations like the ENCODE catalog. BRAIN-MAGNET fits beside AlphaGenome and varTFBridge in this atlas as a complementary, brain-specific predictor that can be used to triage Teagan-WGS noncoding variants and to fine-map GWAS loci.

## Status in the atlas

Candidate -- not yet integrated. Needs verification of GitHub repo activity (stars, last commit), accessibility of the pre-scored SNP table, and a head-to-head comparison with AlphaGenome on a shared variant set before adoption.

## Citation

Deng R et al. BRAIN-MAGNET: A functional genomics atlas for interpretation of non-coding variants. Cell. 2026;189(2):676-695.e24. PMID: 41265437. DOI pending verification before publication-grade citation.

## Repo

https://github.com/ruizhideng/BRAIN-MAGNET

## Outstanding questions

The published model is trained on neural stem cells, not differentiated cortical neurons or fetal cortical organoids -- whether NSC predictions transfer to the cell types most relevant to autism is an open question worth checking with the authors or via independent validation. Also unclear whether the pre-scored SNP table covers GRCh38 variants Teagan's WGS uses or requires a liftover.

## Related atlas pages

- [AlphaGenome](./AlphaGenome.md)
- [varTFBridge](./varTFBridge.md)
- [GET](./GET.md)
- [PARM](./PARM.md)
