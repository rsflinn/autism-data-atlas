---
id: encode
name: "ENCODE Project (Encyclopedia of DNA Elements)"
short_name: "ENCODE"
data_types: ["ChIP-seq", "ATAC-seq", "DNase-seq", "Hi-C", "candidate cis-regulatory elements (cCREs)", "STARR-seq", "reporter assays"]
access_level: PUBLIC
access_url: "https://www.encodeproject.org/, https://screen.wenglab.org/"
regulatory_relevance: direct
cell_types: "Multiple (see brain-specific note)"
backfill_phase: 1
atlas_integration_status: not_started
evidence_tier: A
last_updated: 2026-04-06
---

# ENCODE Project (Encyclopedia of DNA Elements)

## Overview

The ENCODE Consortium provides the most comprehensive functional annotation of the human genome to date. As of January 2026, ENCODE has cataloged **2.37 million candidate cis-regulatory elements (cCREs)** across the human genome, with >90% functionally validated through STARR-seq, massively parallel reporter assays, CRISPR perturbation, and transgenic mouse studies. This represents a threefold expansion from ENCODE Phase 3 (0.9 million cCREs) and covers hundreds of unique cell and tissue types.

The ENCODE Phase 4 registry provides the foundation for understanding which regulatory elements control gene expression in human cells and tissues, directly enabling interpretation of noncoding variants in autism and other diseases.

## Available Data Types

### Chromatin Accessibility and Occupancy
- **ATAC-seq**: Open chromatin regions in hundreds of cell types
- **ChIP-seq**: Transcription factor binding sites and histone modifications
- **DNase-seq**: Hypersensitive sites marking regulatory regions
- **MNase-seq**: Nucleosome positioning

### Three-Dimensional Chromatin Structure
- **Hi-C**: Chromosome folding and enhancer-promoter interactions
- **4C-seq/5C-seq**: Chromosome conformation capture variants
- **Micro-C**: High-resolution chromatin structure

### Regulatory Element Validation
- **STARR-seq**: Massively parallel reporter assays for enhancer activity
- **Luciferase assays**: Individual regulatory element validation
- **CRISPR perturbation**: Functional testing of cCRE effects
- **Transgenic mouse assays**: In vivo regulatory validation

### RNA-seq
- Expression quantification across tissues and cell types
- Small RNA sequencing (miRNA, lncRNA)
- Total RNA-seq for comprehensive transcriptome coverage

## Brain-Specific Resources

ENCODE includes substantial coverage of **brain-derived cell types and tissues**:

- Primary human brain cells (neurons, glia, oligodendrocytes, astrocytes)
- Differentiated neural cells from iPSCs
- Brain tissue samples across developmental stages
- Cell-type specific chromatin accessibility and transcription factor binding

The SCREEN portal (Search Candidate cis-Regulatory Elements by ENCODE) provides interactive access to brain-specific regulatory annotations, allowing queries like:
- "Which regulatory elements are open in neurons vs. astrocytes?"
- "Which transcription factors bind in brain tissue?"
- "What regulatory variants affect this enhancer?"

### Developmental Brain Coverage

ENCODE includes data from:
- Prenatal brain development (8 PCW through 40 years)
- Adult brain from multiple donors
- Primary fetal brain cells
- Neural progenitor cells

## Noncoding Variant Annotation Use

For the Autism Genomics Atlas, ENCODE data enables:

### 1. Regulatory Element Annotation
- Identify which genomic regions are regulatory elements (enhancers, silencers, promoters)
- Distinguish functional from non-functional noncoding variants
- Map tissue and cell-type specificity of regulatory effects

### 2. Variant Effect Prediction
- Determine if noncoding variants disrupt transcription factor binding sites (ChIP-seq peaks)
- Assess whether variants affect chromatin accessibility (ATAC-seq signal)
- Predict impact on long-range enhancer-promoter interactions (Hi-C data)

### 3. Cell-Type Specific Interpretation
- Brain-specific chromatin accessibility (which cells are affected)
- Brain-specific transcription factor binding (which regulatory proteins are involved)
- Neuron vs. glia specificity of regulatory effects

### 4. GWAS Fine-Mapping
- Collocalize GWAS variants with ENCODE regulatory elements
- Identify likely causal regulatory variants from associated SNP clusters
- Connect GWAS signals to cell-type specific mechanisms

## Data Integration in Atlas

The Autism Genomics Atlas will integrate ENCODE by:

1. **Filtering cCREs for brain relevance**: Focus on regulatory elements active in brain tissues, particularly those matching autism-relevant cell types (cortical neurons, GABAergic interneurons)

2. **Variant prioritization**: Score noncoding variants by their overlap with ENCODE-defined regulatory elements and experimentally validated cCREs

3. **Cell-type specificity**: Combine ENCODE brain cell-type chromatin maps with autism candidate genes to identify cell-type-specific mechanisms

4. **Annotation confidence**: Use ENCODE's functional validation data (STARR-seq, CRISPRi) to prioritize high-confidence regulatory elements

## Key Publications

- "An expanded registry of candidate cis-regulatory elements." Nature (2026). Lead authors: Zhiping Weng, Jill Moore (UMass Chan). DOI: 10.1038/s41586-025-09909-9 -- Publication of ENCODE Phase 4 with 2.37M human cCREs
- "Expanded encyclopaedias of DNA elements in the human and mouse genomes." Nature (2020). ENCODE Consortium. DOI: 10.1038/s41586-020-2493-4 -- ENCODE Phase 3, foundational for current atlas development
- "Regulatory transposable elements in the encyclopedia of DNA elements." Nature Communications (2024). DOI: 10.1038/s41467-024-51921-6 -- Regulatory TEs as cis-regulatory elements

## Access Instructions

### Option 1: ENCODE Portal (All Data)
1. Navigate to https://www.encodeproject.org/
2. Filter by:
   - **Assay type**: ATAC-seq, ChIP-seq, DNase-seq, Hi-C, RNA-seq
   - **Organism**: Homo sapiens
   - **Tissue/Cell Type**: Brain (multiple options available)
3. Download processed files (BAM, BED, bigWig formats available)
4. All ENCODE Phase 4 data is **public access** (no authentication required)

### Option 2: SCREEN Portal (cCRE Search)
1. Navigate to https://screen.wenglab.org/
2. Search by:
   - Genomic region (chromosome:start-end)
   - Gene name (finds regulatory elements for that gene)
   - Cell type (filter to brain cell types)
3. View:
   - cCRE coordinates and classification (enhancers, silencers, promoters, proximal/distal)
   - Chromatin accessibility (ATAC-seq) across cell types
   - Transcription factor binding profiles
   - Validation evidence (STARR-seq scores, CRISPR results)
4. **Interactive visualization** - no data download required for initial exploration

### Option 3: Bulk Download
- Contact ENCODE portal for bulk download assistance
- Estimated storage: 80+ GB for complete human brain ATAC and ChIP-seq datasets
- Alternative: Access via Google Cloud (requester pays model)

## Atlas Integration Notes

**Status**: not_started

**Data Processing Plan**:
- Phase 1: Identify all ENCODE brain-derived cell types and assays (completeness check)
- Phase 2: Filter cCRE catalog for brain-specific regulatory elements
- Phase 3: Cross-reference with autism candidate genes and noncoding variants
- Phase 4: Build annotation pipeline for new variants using ENCODE profiles

**Computational Approach**:
- Use ENCODE ChIP-seq/ATAC-seq peaks as ground truth for regulatory elements
- Apply variant effect scoring (e.g., DeepSEA, Enformer) trained on ENCODE data
- Generate brain-specific regulatory element annotations (BED/VCF format)
- Create cell-type-specific variant impact predictions

**Expected Outputs**:
- Annotated catalog of autism noncoding variants with ENCODE regulatory evidence
- Cell-type-specific regulatory effect predictions (high-confidence via STARR-seq/CRISPR validation)
- Integration with PsychENCODE GRN for transcription factor→target gene links

**Technical Challenges**:
- Large data volume (~80+ GB for relevant experiments)
- Cell type nomenclature differs across ENCODE datasets (standardization needed)
- Requires mapping ENCODE cell types to autism-relevant circuit nodes

**Dependencies**:
- GTEx v8 (for tissue-level validation of predictions)
- PsychENCODE GRN (for transcription factor connection)
- Allen Brain Atlas (for cell-type taxonomy)

## Related Resources

- **ENCODE Project**: https://www.encodeproject.org/
- **SCREEN Portal**: https://screen.wenglab.org/
- **Portal Alternative**: https://screen.encodeproject.org/ (older interface)
- **cCRE GitHub**: https://github.com/weng-lab/ENCODE-cCREs
- **ENCODE Standards**: https://www.encodeproject.org/data/annotations/

---

**Last Updated**: 2026-04-06
**Evidence Tier**: A (Comprehensive, experimentally validated functional annotations)
