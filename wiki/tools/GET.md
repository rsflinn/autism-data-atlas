---
name: GET
type: model
source_bookmark: 55
url: https://www.nature.com/articles/s41586-024-08391-z
relevance_to_atlas: HIGH
integration_status: pending
last_updated: 2026-04-04
---

# GET (General Expression Transformer)

## What It Does

GET is a foundation model that predicts gene expression across 213 human fetal and adult cell types using only chromatin accessibility data and DNA sequence information. It learns regulatory grammars—the rules governing how transcription factors and chromatin structure control gene expression—that generalize across cell types and conditions.

## Why It Matters for the Atlas

GET provides a unifying framework for understanding how noncoding regulatory variants affect gene expression in the relevant cell types for autism (neurodevelopmental tissues, neural precursors, mature neurons). Its ability to predict cell-type-specific expression from sequence enables us to infer the functional impact of autism-associated regulatory variants in specific neuronal contexts.

## Technical Details

- **Input:** Chromatin accessibility (ATAC-seq), transcription factor motifs, DNA sequences
- **Output:** Gene expression predictions across cell types, regulatory element annotations, TF interaction networks
- **Dependencies:** sc-ATAC-seq atlas, motif databases
- **Paper:** A foundation model of transcription across human cell types. Nature (2024)
- **Repository:** https://github.com/OmicsML/awesome-foundation-model-single-cell-papers
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11244937/

## Integration Plan

GET should be applied to predict how autism-associated noncoding variants alter gene expression in neuronal cell types. Its regulatory grammar outputs would help identify which transcription factor networks are disrupted by variants at each atlas locus, providing mechanistic insight into autism etiology.

## Status

Pending evaluation for regulatory prediction component of the atlas
