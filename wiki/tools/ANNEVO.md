---
name: ANNEVO
type: model
source_bookmark: 12
url: https://www.nature.com/articles/s41592-026-03036-7
relevance_to_atlas: HIGH
integration_status: pending
last_updated: 2026-04-04
---

# ANNEVO

## What It Does

ANNEVO is a deep learning genome language model using mixture-of-experts architecture that performs accurate ab initio gene annotation across phylogenetically diverse species. It models sequence evolution and long-range dependencies from DNA sequences alone, eliminating the need for external evidence like RNA-seq or protein homology.

## Why It Matters for the Atlas

Precise gene annotation is essential for the autism regulatory atlas. ANNEVO enables high-confidence mapping of gene boundaries and structures purely from sequence context, which is crucial for correctly interpreting which variants fall within genes versus regulatory regions. This improves our ability to distinguish coding from noncoding variant effects in the atlas.

## Technical Details

- **Input:** DNA sequences from diverse species
- **Output:** Gene structure annotations (exons, introns, start/stop codons)
- **Dependencies:** Deep learning framework, genomic sequence databases
- **Paper:** Highly accurate ab initio gene annotation with ANNEVO. Nature Methods (2026)
- **Publication:** Published March 12, 2026 by Professor Ye Kai's team at Xi'an Jiaotong University

## Integration Plan

ANNEVO would be applied in the atlas pipeline to ensure all genes referenced in our noncoding regulatory variant analysis have accurate, high-confidence structural annotations. Its outputs would validate gene boundaries and improve the precision of variant-gene association calls.

## Status

Pending evaluation for gene annotation layer of the atlas
