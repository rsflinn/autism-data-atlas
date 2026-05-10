---
type: tool-page
id: hdma
name: HDMA (Human Development Multiomic Atlas)
discovered: 2026-05-10
status: candidate
last_updated: 2026-05-10
---

# HDMA -- Human Development Multiomic Atlas

Paired single-cell chromatin accessibility (snATAC-seq) and gene expression (snRNA-seq) from 817,740 fetal cells across 12 organs, 203 cell types, with more than 1 million candidate cis-regulatory elements (cCREs). Greenleaf Lab, Stanford. Published in Nature 2026 (Liu*, Jessa*, Kim*, Ng*, et al.; doi 10.1038/s41586-026-10326-9). Preprint on bioRxiv April 2025 (10.1101/2025.04.30.651381).

Repo: https://github.com/GreenleafLab/HDMA
Companion site: https://greenleaflab.github.io/HDMA/
Data: https://zenodo.org/communities/hdma

## Why it matters here

The atlas's central noncoding question is which fetal-brain regulatory elements matter and which transcription factors bind them. Adult brain (GTEx, ENCODE) doesn't capture the developmental window where most autism heritability acts. HDMA gives per-cell-type cCRE calls and per-cell-type ChromBPNet models for fetal tissue, including brain.

That maps directly onto a finding already in the project memory: 12 of 39 NDD genes do have fetal-brain eQTLs in BrainVar (notably MECP2 and EP300), and those eQTLs are invisible in adult GTEx because they reverse postnatally. HDMA is the kind of resource that lets us follow up on those signals at cell-type resolution.

## What it gives us

* 1M+ fetal cCREs across 12 organs, 203 cell types
* Per-cell-type ChromBPNet models for accessibility prediction
* Composite-motif syntax: which TF pairs cooperate, with what spacing constraints
* WashU Genome Browser tracks for visual inspection
* Zenodo deposit for downloadable BED files and model weights

## Caveats

This is a reference resource, not a case-control dataset. It tells us which cCREs exist and which cell types they're active in -- it does not tell us which are perturbed in autism.

A million cCREs is a large multiple-testing burden if running variant-enrichment tests. Any analysis needs an explicit null and an explicit FDR strategy.

The ChromBPNet models predict accessibility, not transcription. Same caveats as ChromBPNet generally.

## Open questions

* Do Teagan-WGS noncoding variants overlap HDMA fetal-brain cCREs at higher rate than expected from a matched random-variant sample?
* Among the 12 NDD genes with prenatal-trending eQTLs (MECP2, EP300, others), which fetal-brain cell types show their cCREs as accessible?
* Does HDMA's composite-motif syntax explain effect-size variation across the 5 GWAS-significant ASD loci?

## Status

Candidate. Saved metadata to `raw/tools/HDMA.json`. Repo and Zenodo content not yet downloaded or run against Teagan WGS.
