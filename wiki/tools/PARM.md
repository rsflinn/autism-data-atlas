---
name: PARM
type: model
source_bookmark: 70
url: https://github.com/vansteensellab/PARM
relevance_to_atlas: HIGH
integration_status: pending
last_updated: 2026-04-04
---

# PARM (Promoter Activity Regulatory Model)

## What It Does

PARM is a cell-type-specific deep learning model that predicts promoter activity directly from DNA sequence using convolutional neural networks trained on massively parallel reporter assays (MPRA). It learns both simple transcription factor binding motifs and complex regulatory grammar including TF-TF interactions.

## Why It Matters for the Atlas

Promoter activity is a key functional consequence of regulatory variants affecting autism genes. PARM enables rapid in silico prediction of how noncoding variants alter promoter strength and activity in multiple cell types, providing quantitative functional scores for variants in the atlas without requiring expensive experimental validation.

## Technical Details

- **Input:** DNA sequences (genomic fragments or promoter regions)
- **Output:** Predicted promoter activity scores, transcription factor contributions, in silico mutagenesis effects
- **Dependencies:** Cell-type-specific MPRA training data
- **Available cell types:** AGS, HAP1, HCT116, HEK293, HepG2, K562, LNCaP, MCF7, U2OS
- **Paper:** Regulatory grammar in human promoters uncovered by MPRA-based deep learning. Nature (2025)
- **Repository:** https://github.com/vansteensellab/PARM

## Integration Plan

PARM should be applied to functionally score all autism-associated noncoding variants falling within or near promoter regions. Its predictions would annotate each variant with quantitative promoter activity effects, enabling prioritization of likely deleterious regulatory variants for the atlas resource.

## Status

Pending evaluation for variant scoring pipeline
