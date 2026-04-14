---
name: varTFBridge
type: software_framework
source_bookmark: 138
preprint_url: https://www.biorxiv.org/content/10.64898/2026.03.03.708783v2
alphagenome_repo: https://github.com/google-deepmind/alphagenome
relevance_to_atlas: HIGH
integration_status: evaluated
evaluation_date: 2026-04-04
last_updated: 2026-04-04
---

# varTFBridge

## What It Does

varTFBridge is a framework that connects noncoding genetic variants to the transcription factors whose binding they disrupt and the genes whose expression they change. It does this by combining two technologies: FOODIE footprinting (which maps where transcription factors sit on DNA at near-base resolution using deaminase enzymes) and AlphaGenome (DeepMind's model that predicts functional effects of DNA sequence changes across 11 genomic modalities).

Applied to 490,640 UK Biobank genomes across 13 erythrocyte traits, varTFBridge identified 113 high-confidence regulatory variants (104 common, 9 rare) with 2,173 variant-TF-gene-trait linkages spanning 64 TFs and 108 genes.

## Evaluation for Atlas Integration

### What makes it valuable

This is the closest thing to a turnkey solution for our core problem: taking autism GWAS hits (all 5 of which are noncoding) and tracing them to specific TFs and target genes. The variant-TF-gene cascade output is exactly what the atlas needs to populate structured regulatory annotations.

### Critical dependency: AlphaGenome

AlphaGenome is available via API for non-commercial research (free). Code, weights and variant scoring implementations are on GitHub at google-deepmind/alphagenome. The API is designed for small-to-medium analyses (thousands of predictions, not millions), which fits our use case -- we have ~5 GWAS-significant loci plus credible sets from fine-mapping, not a whole-genome sweep.

Inputs: DNA sequences up to 1Mb, genomic intervals, variant positions (chr, pos, ref, alt), cell/tissue ontology terms, requested output types. Outputs: gene expression, splicing, chromatin features, contact maps at single-base resolution.

### Critical dependency: FOODIE footprints

FOODIE (FOOtprinting with DeamInasE) maps TF binding at near single-base resolution. It's been applied to mouse hippocampus (11,200 cells, 8 brain cell types) and human cell lines. The technique is cost-effective (thousands of cells, not millions like ChIP-seq).

The problem: there are no published FOODIE footprint maps for human brain tissue yet. The varTFBridge preprint used liver and erythroid FOODIE data. For autism, we would need either brain FOODIE data (doesn't exist yet) or a substitute.

### Feasibility assessment for autism

**What we can do now:**
1. Use AlphaGenome API directly to score all 5 ASD GWAS-significant noncoding variants plus fine-mapped credible sets from Grove et al. 2019. AlphaGenome accepts brain tissue ontology terms and can predict effects on gene expression, chromatin and splicing in neural cell types.
2. Use existing ATAC-seq footprints from PsychENCODE brain data as a substitute for FOODIE footprints. Tools like TOBIAS (github.com/loosolab/TOBIAS) can extract TF footprints from ATAC-seq, which is what varTFBridge's pipeline conceptually requires.
3. Cross-reference with brain eQTL data (PsychENCODE, GTEx brain regions, BrainSeq) to validate variant-gene linkages.

**What we cannot do now:**
1. Run the full varTFBridge pipeline as published -- no public code repository exists yet (preprint is from March 2026). The paper describes the method but the implementation code hasn't been released.
2. Generate brain FOODIE footprints -- requires wet-lab work on brain tissue/organoids.
3. Score rare noncoding variants at scale -- we'd need WGS cohort data (SPARK, MSSNG) with controlled access.

**Realistic path:**
Build a varTFBridge-like pipeline using the components that ARE available: AlphaGenome API for variant effect prediction + PsychENCODE ATAC-seq footprints for TF binding + existing brain eQTL/sQTL for gene linkage. This gets us 80% of what varTFBridge does for the specific autism use case, without waiting for the full tool release.

## Technical Details

- **Input:** Noncoding variants, TF footprint maps, genomic sequences
- **Output:** Variant-TF-gene-trait linkage cascades with effect sizes
- **Key dependencies:**
  - AlphaGenome API (available, free for non-commercial research)
  - FOODIE footprints (available for liver/erythroid; NOT yet for brain)
  - UK Biobank WGS (for population-level analysis; not needed for our targeted approach)
- **Paper:** Genome-wide maps of transcription factor footprints identify noncoding variants rewiring gene regulatory networks with varTFBridge. bioRxiv, March 2026. doi:10.64898/2026.03.03.708783
- **Code repository:** Not yet released as of April 2026.

## Integration Plan

### Phase 1 (Can start now)
Score ASD GWAS loci with AlphaGenome API using brain cell type ontology terms. Save variant effect predictions to structured/variants/. This gives us functional impact scores for all known GWAS-significant autism noncoding variants.

### Phase 2 (Requires PsychENCODE ATAC-seq data)
Extract TF footprints from PsychENCODE brain ATAC-seq using TOBIAS. Cross-reference with AlphaGenome predictions to identify which TFs are disrupted by autism risk variants.

### Phase 3 (When varTFBridge code is released)
Run full varTFBridge pipeline on autism GWAS data with brain-specific inputs. Validate against our Phase 1/2 results.

## Status

Evaluated. Phase 1 (AlphaGenome scoring) can begin immediately.
