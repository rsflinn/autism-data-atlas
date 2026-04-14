---
id: gtex-brain
name: "GTEx (Genotype-Tissue Expression) - Brain Tissues"
short_name: "GTEx Brain"
data_types: ["bulk RNA-seq", "eQTL", "sQTL", "genotype data"]
access_level: MIXED (dbGaP for protected; public for processed)
access_url: "https://www.gtexportal.org/, https://www.gtexportal.org/home/datasets"
regulatory_relevance: direct
cell_types: "Brain tissue (bulk, not cell-type resolved)"
backfill_phase: 1
atlas_integration_status: not_started
evidence_tier: A
last_updated: 2026-04-06
---

# GTEx (Genotype-Tissue Expression) - Brain Tissues

## Overview

The GTEx Consortium provides **multi-tissue gene expression and quantitative trait loci (QTL) mapping** from postmortem human tissues. The current v8 release includes **838 donors, 15,201 samples across 54 tissues**, with **13 distinct brain regions** sampled. GTEx is the reference resource for understanding **tissue-specific gene expression and how genetic variants affect expression levels** (eQTLs) and RNA splicing (sQTLs) in humans.

For autism research, GTEx brain tissues provide the critical link between noncoding variants and gene expression changes in relevant tissues. eQTL mapping reveals which variants regulate which genes in each brain region, enabling prediction of functional effects of noncoding variants.

## Available Data Types

### Expression Data
- **Bulk RNA-seq**: Gene-level quantification across all 13 brain regions
- **Strand-specific**: Proper strand attribution for accurate strand-specific effects
- **Multiple normalization formats**: Raw counts, TPM, RPKM available
- **Transcriptome coverage**: All protein-coding and noncoding genes

### QTL Data (Expression and Splicing)

#### eQTL (Expression Quantitative Trait Loci)
- **cis-eQTLs**: Variants affecting expression of nearby genes (±1 Mb window)
- **Effect sizes**: Per-variant and per-gene estimates
- **Significance**: FDR-adjusted q-values
- **Fine-mapping**: Posterior probability of causality for lead variants
- **Scope**: Tested in all 13 brain regions for cross-tissue comparison

#### sQTL (Splicing Quantitative Trait Loci)
- **Intron excision variants**: Variants affecting splicing ratios
- **Exon inclusion**: Variants affecting which exons are included in transcripts
- **Developmental relevance**: Splicing changes often more sensitive to variants than overall expression

### Genotype Data
- **Common and rare variants**: SNPs, indels
- **Linkage disequilibrium**: Fine-mapping supports to identify likely causal variants
- **Population allele frequencies**: For filtering and interpretation

## Brain-Specific Resources

### GTEx v8 Brain Tissues (13 regions)

The 13 distinct brain regions profiled in GTEx v8 are:

1. **Brain - Amygdala** (105 samples)
2. **Brain - Anterior Cingulate Cortex (ACC)** (104 samples)
3. **Brain - Caudate** (113 samples)
4. **Brain - Cerebellar Hemisphere** (111 samples)
5. **Brain - Cerebellum** (121 samples) [subset duplicates with Cerebellar Hemisphere]
6. **Brain - Cortex** (132 samples)
7. **Brain - Frontal Cortex** (137 samples)
8. **Brain - Hippocampus** (118 samples)
9. **Brain - Hypothalamus** (87 samples)
10. **Brain - Nucleus Accumbens** (116 samples)
11. **Brain - Putamen** (105 samples)
12. **Brain - Spinal Cord** (83 samples)
13. **Brain - Substantia Nigra** (80 samples)

**Sampling Notes**:
- All brain tissues from postmortem donors (median time to autopsy: ~8.5 hours)
- Dissections performed at University of Miami Brain Endowment Bank
- Age range: 18-80 years (predominantly adult; limited fetal samples)
- Limited developmental coverage (not comparable to BrainSpan)

### Cell-Type Limitation (Important for Interpretation)

**Critical Note**: GTEx provides **bulk brain tissue data** without cell-type resolution. Brain regions are heterogeneous, containing:
- Multiple neuron subtypes (pyramidal neurons, GABAergic interneurons, etc.)
- Glia (astrocytes, oligodendrocytes, microglia)
- Vascular endothelial cells
- Other cell types

Expression changes in eQTLs may reflect effects in any cell type in the tissue. For **cell-type-specific interpretation**, GTEx must be combined with:
- PsychENCODE single-cell data
- Allen Brain Atlas cell-type taxonomy
- Single-cell eQTL studies (emerging)

## Noncoding Variant Annotation Use

For the Autism Genomics Atlas, GTEx brain data enables:

### 1. Variant-to-Expression Mapping
- **Identify which noncoding variants affect which genes** in brain tissues
- For example: "rs12345 is an eQTL for FOXP1 in frontal cortex (p=1e-15, effect=-0.2 SD)"
- Direct evidence that noncoding variant affects expression of autism candidate gene

### 2. Brain-Region Specificity
- **Determine tissue-level specificity** of regulatory effects
- "Gene X eQTL in frontal cortex but not cerebellum" suggests cortex-specific regulation
- Prioritize variants affecting expression in regions enriched for autism genes

### 3. Effect Size Quantification
- **Measure the strength of regulatory effects** (how much does allele frequency change expression?)
- Effect size for autism prioritization: larger effect variants more likely to be functional
- Fine-mapping posterior probabilities help identify likely causal variants

### 4. Integration with GWAS
- **Colocalize GWAS variants with eQTL signals**
- If GWAS SNP and eQTL SNP are the same or in high LD, likely shared causal variant
- Indicates expression effect as likely mechanism for GWAS association

### 5. Developmental Gap-Filling
- **Adult expression baseline** for comparison with BrainSpan developmental data
- Identify genes with developmental trajectory (BrainSpan) and adult eQTL regulation (GTEx)
- Build complete developmental→adult regulatory model

## Key Publications

- "The GTEx Consortium atlas of genetic regulatory effects across human tissues." Science (2020). GTEx Consortium. DOI: 10.1126/science.aaz1776 -- v7 release, still primary reference for methodology
- "Large eQTL meta-analysis reveals differing patterns between cerebral cortical and cerebellar brain regions." Scientific Data (2020). DOI: 10.1038/s41597-020-00642-8 -- Brain-specific eQTL analysis
- "Genome-wide association study of autism spectrum disorder." Nature Genetics (2019). Grove et al. DOI: 10.1038/s41588-019-0344-8 -- Demonstrates colocalizing GWAS signals with GTEx eQTLs

## Access Instructions

### Quick Option 1: Interactive Portal
1. Navigate to https://www.gtexportal.org/
2. Select **"Search eQTLs"** from the main menu
3. Enter gene name (e.g., "FOXP1")
4. Select **"Brain - Frontal Cortex"** (or other brain regions)
5. View:
   - Variant IDs and chromosomal positions
   - eQTL effect sizes (slope, allele substitution effect)
   - p-values and q-values
   - Download top 1000 hits per gene per tissue

### Quick Option 2: eQTL Dashboard
1. Navigate to https://www.gtexportal.org/home/eqtlDashboardPage
2. Filter by:
   - Gene name or variant ID
   - Tissue (select brain tissues)
   - Effect size threshold
3. Explore tissues with strongest regulatory effects

### Bulk Download Option 1: Portal Downloads
1. Navigate to https://www.gtexportal.org/home/downloads/adult-gtex/qtl
2. Download formatted eQTL files for each brain tissue
3. Files available in tab-delimited format (easy to parse)
4. **Access Level**: PUBLIC (no authentication required)

### Bulk Download Option 2: Google Cloud Bucket
1. For **all variant-gene associations** (not just top 1000):
   - Access: https://console.cloud.google.com/storage/browser/gtex-resources
   - Location: `gtex-resources/GTEx_Analysis_v10_eQTL_all_associations/`
   - Size: ~260 GB for complete dataset
   - Cost: Requester pays (Google Cloud charges for data transfer)

### Raw Data Access
1. **Protected data** (raw RNA-seq, genotypes, full metadata):
   - Via dbGaP: https://www.ncbi.nlm.nih.gov/gap/ (accession phs000424)
   - Requires approval (but standard approval process for academic researchers)
2. **Documentation**: https://www.gtexportal.org/home/documentationPage

### Video Tutorial
- Broad Institute tutorial: https://www.broadinstitute.org/videos/gtex-portal-downloading-open-access-files-gtex-portal

## Atlas Integration Notes

**Status**: not_started

**Integration Plan**:
- Phase 1: Extract all eQTL associations for autism candidate genes in brain tissues
- Phase 2: Fine-map eQTLs to identify likely causal variants
- Phase 3: Integrate with ENCODE regulatory elements to link variants→regions→genes
- Phase 4: Cross-reference with PsychENCODE GRN for transcription factor mechanisms

**Data Processing**:
- For each autism candidate gene: extract eQTLs from all 13 brain regions
- Generate effect size heatmap (tissues × genes) to show tissue specificity
- Fine-mapping: Use GTEx posterior probabilities + LD to identify 95% credible sets
- Merge with GWAS: Identify SNPs that are both GWAS-significant and eQTLs

**Computational Approach**:
- Colocation analysis with autism GWAS (e.g., using eCAVIAR, fastENLOC)
- Multi-tissue conditional analysis (tissue-specific eQTLs vs. ubiquitous)
- Integration with single-cell data (when available) to predict cell types of eQTL effect

**Expected Outputs**:
- Table: autism genes × brain tissues, showing eQTL signals and effect sizes
- Prioritized variant list: eQTL variants affecting autism genes with tissue specificity
- Fine-mapped credible sets for each eQTL signal (likely causal variants)
- Tissue-specificity annotations (cortex-specific, ubiquitous, etc.)

**Technical Challenges**:
- Large file sizes for bulk download
- Limited sample size for some brain regions (83-137 samples per tissue)
- Adult-only samples (limited developmental trajectory data)
- Lack of cell-type resolution

**Dependencies**:
- ENCODE (for linking eQTL variants to regulatory elements)
- PsychENCODE GRN (for TF→target gene links)
- Autism GWAS data (for colocation)
- BrainSpan (for developmental context)

## Related Datasets for Brain Interpretation

- **PsychENCODE**: Single-cell expression and GRN (cell-type resolution)
- **BrainSpan**: Developmental expression (temporal dynamics)
- **Allen Brain Atlas**: Cell-type taxonomy and spatial transcriptomics
- **Roadmap Epigenomics**: Brain chromatin landscape

---

**Last Updated**: 2026-04-06
**Evidence Tier**: A (Large-scale, well-powered QTL study; standard reference for human genetics)
