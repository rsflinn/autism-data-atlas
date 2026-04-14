---
title: AlphaGenome Scoring of ASD GWAS Noncoding Loci
date: 2026-04-06
type: analysis
tool: AlphaGenome
variants_scored: 5
variants_pending: 0
evidence_tier: B
last_updated: 2026-04-06
---

# AlphaGenome Scoring of ASD GWAS Noncoding Loci

## Overview

Scored all 5 genome-wide significant noncoding variants from the ASD GWAS (Grove et al. 2019, Nature Genetics) using DeepMind's AlphaGenome model. AlphaGenome returned 19 output tracks per variant, spanning gene expression, chromatin accessibility, histone marks, contact maps and splicing predictions. All 5 variants scored successfully.

## Results (ranked by predicted functional impact)

### 1. rs142920272 (17q21.31, near KANSL1) -- Largest predicted effect

- GWAS p-value: 4.58e-08
- Track 16 max effect: **15,024**
- Track 16 mean effect: 2,031
- All 19 tracks returned data (no empty tracks)
- This is the 17q21.31 inversion region containing KANSL1 and MAPT. Deletions here cause Koolen-de Vries syndrome (intellectual disability, seizures). The large predicted effect is consistent with this being one of the most functionally potent autism risk loci.

### 2. rs201910565 (1p21.3, near PTBP2) -- Second largest

- GWAS p-value: 2.48e-08
- Track 16 max effect: **7,033**
- Track 16 mean effect: 1,328
- 4 empty splice/junction tracks (tracks 9-12)
- PTBP2 regulates alternative splicing in neurons. It's a master switch for neuronal RNA processing. The strong predicted effect here aligns with its known role in brain development.

### 3. rs910805 (20p11.22, near KIF3B) -- Moderate effect

- GWAS p-value: 2.04e-09 (strongest GWAS signal)
- Track 16 max effect: **5,620**
- Track 16 mean effect: 1,394
- All 19 tracks returned data
- Near KIF3B, involved in intracellular transport. Despite having the strongest GWAS p-value, its functional effect prediction is mid-range, suggesting the statistical signal may come from a large effect on liability spread across many regulatory positions rather than one dramatic disruption.

### 4. rs10099100 (8p23.1, near XKR6) -- Moderate effect

- GWAS p-value: 1.07e-08
- Track 16 max effect: **4,899**
- Track 16 mean effect: 887
- 4 empty splice/junction tracks
- Near XKR6, involved in cell signaling. Credible SNPs at this locus were enriched in fetal brain enhancer marks in the original GWAS.

### 5. rs13188074 (5q21.2, near NUDT12) -- Smallest predicted effect

- GWAS p-value: 3.48e-08
- Track 16 max effect: **3,775**
- Track 16 mean effect: 944
- 4 empty splice/junction tracks
- Near NUDT12. Smallest predicted functional effect of the five, though still substantially nonzero.

## What this means

All 5 autism GWAS variants show predicted functional effects, which is consistent with them tagging real regulatory changes rather than being false positives. The ranking by predicted effect does not match the ranking by GWAS p-value -- rs910805 has the strongest statistical association but only the third-largest predicted disruption. This is expected: GWAS p-values reflect sample size and allele frequency as much as biological effect.

The standout is rs142920272 at the 17q21.31 inversion. Its predicted effect is roughly 2x larger than the next variant and 4x larger than the weakest. This region is already clinically established through Koolen-de Vries syndrome. The second-ranked variant near PTBP2 is also notable because PTBP2 is a known neuronal splicing regulator.

## Limitations

Without a null distribution from matched control variants, we cannot formally test whether these effect sizes are unusually large. All five could be typical for common variants, or all five could be outliers. Establishing that baseline is the next step. These are also model predictions, not experimental measurements -- evidence tier B.

## Next steps

1. Score 100 matched control variants (common SNPs not associated with any trait, matched by allele frequency and LD) to build a null distribution
2. Identify which specific tracks correspond to which genomic modalities (the track numbering is not self-documenting in the current API output)
3. Cross-reference with GTEx brain eQTLs and PsychENCODE data
4. Score the full set of ~380 credible SNPs from GWAS fine-mapping, not just the 5 lead SNPs

## Methods

AlphaGenome API (non-commercial research license, Google DeepMind) with 1,048,576 bp (2^20) windows centered on each variant. Default scoring mode returned 19 AnnData tracks per variant. Some tracks returned empty arrays for variants not near splice sites (tracks 9-12). NaN values in contact map tracks (tracks 7-8) were excluded from summary statistics. Scored April 6, 2026 via Google Colab.

## Cross-references

- [Noncoding Variants in Autism](../../concepts/noncoding_variants_in_autism.md)
- [varTFBridge](../../tools/varTFBridge.md)

## Source

Grove J, Ripke S, Als TD, et al. Identification of common genetic risk variants for autism spectrum disorder. Nature Genetics. 2019;51(3):431-444. doi:10.1038/s41588-019-0344-8
