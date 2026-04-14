---
name: Genotype-Phenotype Map
type: database
source_bookmark: 128
url: https://gpmap.opengwas.io/
relevance_to_atlas: HIGH
integration_status: pending
last_updated: 2026-04-04
---

# Genotype-Phenotype Map (GPMap)

## What It Does

The Human Genotype-Phenotype Map is a comprehensive open-access database that integrates genetic associations across 15,997 complex traits and 2.7 million molecular measurements (gene expression, protein expression, splicing, methylation). It maps colocalizing variants that are shared across different phenotypes, revealing pleiotropic effects where a single variant influences multiple traits.

## Why It Matters for the Atlas

The GPMap provides crucial context for understanding the broader phenotypic consequences of autism-associated noncoding variants. By linking variants to their effects across all complex traits and molecular phenotypes, the GPMap helps us identify which regulatory networks are autism-specific versus shared with other conditions, supporting mechanistic hypothesis generation about autism biology.

## Technical Details

- **Input:** User queries with SNP identifiers; option to upload custom GWAS summary statistics
- **Output:** Colocalization groups showing shared genetic signals, pleiotropy maps, tissue-specific effects
- **Coverage:** 15,997 complex traits + 2.7M molecular measurements from diverse tissues and cell types
- **Methods:** Fine mapping, colocalization analysis, rare variant annotation
- **Website:** https://gpmap.opengwas.io/
- **Documentation:** https://ieureka.blogs.bristol.ac.uk/2026/03/11/genotype-phenotype-map/
- **Publication:** Building The Human Genotype-Phenotype Map to Harness Pleiotropy and Refine Disease Mechanisms (medRxiv 2026)

## Integration Plan

The GPMap serves as a reference resource for contextualizing atlas variants. For each autism-associated regulatory variant, we can query GPMap to identify all colocalized traits and molecular phenotypes, enriching the atlas annotation with pleiotropy data and revealing shared biological pathways between autism and other disorders.

## Status

Pending integration as reference resource and colocalization validation layer
