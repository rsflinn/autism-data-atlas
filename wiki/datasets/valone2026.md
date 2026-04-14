---
dataset: Valone et al. 2026
source: medRxiv 10.1101/2025.09.12.25335653 (also Mol Psychiatry, PMID 41935183)
system: 83 genotyped human neural progenitor cell lines (hNPCs)
treatments: Vehicle, VPA 1mM, LiCl 1.5mM, 48h
assays: ATAC-seq + RNA-seq
ingested: 2026-04-06
---

# Valone et al. — population-scale GxT chromatin/expression in hNPCs

## What's here
Tier 1 data ingested into `structured/datasets/valone2026/`:
- `twas_asd_epi_relevant.jsonl` — 642 TWAS hits (FDR<0.1) for ASD, Epilepsy, EA, Intelligence, BP, SA, ST, TH
- `twas_ndd_gene_hits.jsonl` — 18 hits at NDD/folate genes (see below)
- `response_caQTLs.jsonl` — 794 r-caQTLs (779 VPA, 15 LiCl)
- `response_eQTLs.jsonl` — 229 r-eQTLs
- `eQTLs_ndd_genes.jsonl` — 19 eQTLs at NDD/folate genes across all 3 conditions
- `caQTL_summary.json` — counts only; full caQTL table not ingested (~80K rows)

## Key NDD/folate-pathway TWAS hits

Folate one-carbon metabolism dominates the EA2022 signal in VPA-treated cells:
- MTHFD1: Z=-6.09, FDR=8.6e-08 (VPA only — not in vehicle)
- MMACHC: Z=4.24, FDR=5.7e-04
- MTRR: Z=-4.22, FDR=6.0e-04
- DHFR2: Z=3.40, FDR=0.009
- MMUT: Z=-2.69, FDR=0.054
- MTFMT: Z=2.64, FDR=0.060

Other VPA-conditional hits:
- SUPT7L: Z=4.07 (Intelligence), Z=5.40 (TH) — VPA only
- AS3MT: Z=3.54 (EA), Z=4.40 (BP, LiCl) — context-dependent

## Why this matters for the atlas
This is the first population-scale dataset directly linking environmental exposure (VPA, an anticonvulsant and known autism-risk teratogen) to genetic regulatory variation in a neural cell type. The folate pathway TWAS hits emerge ONLY in drug-treated conditions, which is exactly the GxT signal the atlas is designed to capture.

## Atlas integration
- Variants: r-caQTL/r-eQTL SNPs → `structured/variants/` candidates for AlphaGenome scoring
- Regulatory elements: r-caQTL peaks → `structured/regulatory_elements/` (hNPC, drug-responsive)
- Gene-phenotype: TWAS hits → `structured/gene_phenotype_links/` (ASD/Epi/EA/Intelligence)

## Caveats
- hNPC ≠ mature neuron; missing cell-type-specific late effects
- VPA at 1mM is supra-physiological vs. therapeutic plasma levels (~0.3-0.7mM)
- N=83 lines is well-powered for caQTL/eQTL but underpowered for r-eQTL (only 15 LiCl)
- Stein lab cohort skews European ancestry
