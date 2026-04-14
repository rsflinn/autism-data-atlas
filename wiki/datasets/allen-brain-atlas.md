---
id: allen-brain-atlas
name: "Allen Brain Atlas - Human Brain Gene Expression and Cell Types"
short_name: "Allen Brain Atlas"
data_types: ["single-cell RNA-seq", "spatial transcriptomics (MERFISH)", "single-nucleus RNA-seq", "multiomics"]
access_level: PUBLIC
access_url: "https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas, https://brain-map.org/bkp/explore/abc-atlas"
regulatory_relevance: indirect (functional context for cell types expressing autism genes)
cell_types: "All human brain cell types (100s of types across MTG, DFC, and other regions)"
backfill_phase: 1
atlas_integration_status: not_started
evidence_tier: A
last_updated: 2026-04-06
---

# Allen Brain Atlas - Human Brain Gene Expression and Cell Types

## Overview

The Allen Institute for Brain Science has created the most comprehensive **human brain cell-type atlas** to date. The Allen Brain Cell (ABC) Atlas integrates:

- **2.78 million single-nucleus transcriptomes** from middle temporal gyrus (MTG) and dorsolateral prefrontal cortex (DFC) from 84 donors
- **Largest spatial transcriptomics dataset** in human brain (MERFISH) with 24 SEA-AD (Seattle Alzheimer's Disease) donors
- **100s of distinct cell types** with comprehensive gene expression profiles
- **Multiomics integration**: RNA-seq, ATAC-seq, and protein expression in the same cells
- **Standardized cell-type taxonomy** enabling cross-study comparison

The Allen Brain Atlas answers: "Which cell types express my gene of interest?" and "What are the molecular signatures of specific brain cell types?"

## Available Data Types

### Single-Cell/Nucleus RNA-seq
- **snRNA-seq (single-nucleus)**: Most comprehensive coverage (~2.78M nuclei from MTG + DFC)
- **scRNA-seq (single-cell)**: Fresh cell data (lower throughput but higher quality)
- **10x Genomics platform**: ~16,000-20,000 genes per cell
- **Full transcriptome coverage**: Protein-coding and noncoding RNA quantification
- **Cell quality metrics**: Doublet detection, cell cycle scoring, quality control
- **Donor metadata**: Age, sex, postmortem interval, batch information

### Spatial Transcriptomics
- **MERFISH (Multiplexed error-robust FISH)**: Single-cell resolution spatial location
- **MTG and DFC coverage**: 24 donors with spatial information
- **~200 gene probes per brain section**: Targeted spatial measurement
- **High-resolution images**: Spatial coordinates linked to cell type
- **Colocalization data**: Which cell types are neighbors, spatial organization

### Multiomics (Joint Measurement)
- **RNA + ATAC**: Gene expression + chromatin accessibility in same cells
- **RNA + protein**: Gene expression + surface/intracellular protein (CITE-seq or similar)
- **Enables causal inference**: Connects regulatory state to transcriptional output

### Developing Annotations
- **Cell type taxonomy**: Standardized classification across experiments
- **Marker genes**: Genes defining each cell type (statistically tested)
- **Co-expression modules**: Gene sets correlated across the cell type
- **Transcription factor activity**: Predicted TF activity per cell type

## Brain-Specific Resources

### Human Brain Regions Covered

**Current Release**:
- **Middle Temporal Gyrus (MTG)**: Primary sensory/associational cortex (~1.5M nuclei)
- **Dorsolateral Prefrontal Cortex (DFC)**: Executive function/higher cognition (~1.2M nuclei)
- **Other regions**: Expanding (basal ganglia, hippocampus, cerebellum in development)

**SEA-AD (Seattle Alzheimer's Disease) Cohort**:
- 24 donors with spatial transcriptomics (MERFISH)
- Includes cognitively normal and early Alzheimer's pathology cases
- Enables disease-relevant cell-type characterization

### Cell-Type Taxonomy (100s of types)

The ABC Atlas identifies cell types at multiple levels of resolution:

**Major Cell Classes**:
- Glutamatergic neurons (excitatory)
- GABAergic neurons (inhibitory, with multiple subtypes)
- Astrocytes
- Oligodendrocytes
- Oligodendrocyte precursor cells (OPCs)
- Microglia
- Endothelial cells
- Pericytes
- Other cell types

**Neuron Subtypes** (key for autism):
- **Excitatory pyramidal neurons** (layer-specific): L2/3, L5, L6
- **GABAergic interneurons** (30+ subtypes): VIP+, SST+, PV+, and others
- **VIP-positive neurons**: Often inhibitory to inhibitory (disinhibitory role)
- **Parvalbumin-positive neurons**: Fast-spiking interneurons (critical for gamma oscillations)
- **Somatostatin-positive neurons**: Regular-spiking interneurons
- **Non-fast-spiking interneurons**: Other subtypes with distinct connectivity

**Glial Cell Subtypes**:
- Astrocyte subtypes (morphology and function specialized)
- Oligodendrocyte subtypes (myelin-forming)
- Microglial subtypes (activation states)
- Vascular associated subtypes

## Autism-Relevant Features

### Excitatory-Inhibitory Balance Context
The detailed cell-type taxonomy enables exploration of autism-relevant hypotheses:
- Which GABAergic neuron subtypes express autism candidate genes?
- Are there E/I imbalance signatures in glutamate vs. GABA neuron expression?
- How are neurotransmitter receptor genes distributed across neuron types?

### Receptor Type Separation Application
The ABC Atlas directly supports the receptor type separation framework by providing:
- Gene expression across glutamatergic neuron subtypes
- Gene expression across all GABAergic interneuron subtypes
- Quantitative comparison of expression patterns
- Marker genes for neurophysiological classification

Example use: "Is this autism gene preferentially expressed in VIP+ neurons (disinhibitory) vs. PV+ neurons (fast-spiking)?"

## Noncoding Variant Annotation Use

For the Autism Genomics Atlas, Allen Brain Atlas data enables:

### 1. Cell-Type Expression Profiling
- **Map which cell types express each autism candidate gene**
- For example: "FOXP1 is highly expressed in L5 pyramidal neurons and SST+ GABAergic interneurons"
- Identify cell types where regulatory variants might have functional impact

### 2. Regulatory Element Interpretation (with ENCODE/Roadmap)
- **Integrate with ENCODE chromatin data** to understand which cell types show regulatory effects
- "This enhancer is chromatin-open in SST+ neurons and contains an autism-associated SNP"
- Direct link: variant → accessible regulatory element → cell type expressing gene

### 3. Co-expression and Gene Regulatory Networks
- **Identify which genes are co-expressed** in cell types expressing autism genes
- Build cell-type-specific networks from ABC Atlas expression data
- Compare with PsychENCODE GRN to validate predicted regulatory links

### 4. Disease Relevance Prediction
- **Identify disease-vulnerable cell types** by finding those expressing highest numbers of autism genes
- "L2/3 pyramidal neurons express 47 autism genes; GABAergic neurons express 52" → need both in mechanistic model
- Prioritize cell types for experimental validation

### 5. Cross-Species Comparison
- **Human-mouse alignment** in ABC Atlas enables translational research
- Identify conserved vs. human-specific cell types and expression patterns
- Test autism variant effects in equivalent mouse cell types

## Key Publications

- "A brain cell atlas integrating single-cell transcriptomes across human brain regions." Nature Medicine (2024). Hodge et al. (Allen Institute). DOI: 10.1038/s41591-024-03150-z -- Primary ABC Atlas release paper
- "A multimodal cell census and atlas of the mammalian primary motor cortex." Nature (2021). Yao et al. (Allen Institute). DOI: 10.1038/s41586-021-03950-0 -- Methods and M1 cortex atlas (similar methodology)
- "Seattle Alzheimer's Disease Brain Cell Atlas (SEA-AD): A high-resolution genomic and spatial atlas of Alzheimer's disease pathology." Preprint (2023) -- SEA-AD cohort documentation

## Access Instructions

### Option 1: Interactive Web Browser
1. Navigate to https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas
2. Select cell type of interest from taxonomy
3. View:
   - Canonical marker genes (cell type-defining genes)
   - Gene expression violin plots (across cell types)
   - Spatial location (if available in MERFISH data)
   - Donor information and metadata
4. **Search by gene**: Enter gene name to find which cell types express it
5. **No download required** - interactive visualization

### Option 2: Alternative Interface (ABC Explorer)
1. Navigate to https://brain-map.org/bkp/explore/abc-atlas
2. Different visualization interface for the same data
3. Allows browsing cell-type taxonomy
4. View cell-type marker genes and expression levels

### Bulk Download: GitHub Repository
1. Navigate to https://alleninstitute.github.io/abc_atlas_access/intro.html
2. Instructions for programmatic access via Python/R
3. Download options:
   - Raw count matrices (full data)
   - Normalized expression files (processed)
   - Cell metadata and annotations
   - Reference mapping files (for integrating new datasets)

### Data Access Methods

**Raw Data**:
- Download from AWS S3 (public bucket, no authentication required)
- Estimated size: 100+ GB for complete single-nucleus data
- Files available in Zarr format (compressed, efficient for large datasets)
- h5ad format (standard single-cell analysis format)

**Metadata**:
- Cell type annotations (CSV/H5AD)
- Donor metadata (age, sex, brain region, etc.)
- Quality metrics per cell

## Atlas Integration Notes

**Status**: not_started

**Integration Plan**:
- Phase 1: Download and parse ABC Atlas cell-type taxonomy and gene expression
- Phase 2: Map autism candidate genes to cell-type expression profiles
- Phase 3: Integrate with ENCODE/GTEx to connect variants→regulatory elements→cell types
- Phase 4: Build cell-type-specific prediction models for noncoding variant effects

**Data Processing**:
- Extract gene expression for all autism candidate genes across cell types
- Generate heatmaps: genes × cell types (identify cell-type specificity)
- Calculate cell-type expression specificity scores (how specific is expression to that cell type)
- Cross-reference with PsychENCODE GRN to identify cell-type-specific regulatory links

**Computational Approach**:
- Differential expression analysis: autism genes vs. background genes
- Cell-type enrichment: which cell types are enriched for autism genes?
- Co-expression network: build networks within specific cell types
- Trajectory analysis: if developmental data available, order cell states

**Expected Outputs**:
- Annotated table: autism genes with cell-type expression profiles
- Cell-type expression specificity for each autism gene
- Cell-type-specific regulatory networks (TF→target gene)
- Integration with spatial transcriptomics (if MTG/DFC-specific analysis needed)

**Technical Challenges**:
- Large data volume (~100 GB+)
- Computational resources needed for expression analysis
- Multiple cell-type definitions/taxonomies (standardization needed)
- Limited coverage of some brain regions (only MTG + DFC for comprehensive single-nucleus data)

**Developmental Limitation**:
- ABC Atlas currently covers **adult brain only**
- No developmental data in current release
- Must combine with **BrainSpan** for developmental trajectory
- Future: developing mouse brain atlas (methods-compatible)

**Dependencies**:
- ENCODE (for chromatin accessibility context)
- GTEx (for adult tissue eQTL context)
- PsychENCODE GRN (for regulatory network validation)
- BrainSpan (for developmental trajectory)

## Expanding Coverage

The Allen Brain Atlas is actively expanding:
- **Basal Ganglia**: Human and cross-species (Human-Mammalian Brain Basal Ganglia, ~2M cells)
- **Hippocampus**: In development
- **Cerebellum**: Planned
- **Developmental brain**: Methods being extended to fetal/early postnatal tissue

Future releases will provide comprehensive coverage of relevant autism-implicated regions.

## Related Tools and Resources

- **Cell Types Database (older version)**: https://celltypes.brain-map.org/ (superseded by ABC Atlas)
- **BrainSpan Integration**: Many ABC cell types can be matched to BrainSpan developmental expression
- **BICCN Resources**: Brain Initiative Cell Census Network (related large single-cell efforts)
- **Spatial Transcriptomics Data**: SEA-AD MERFISH spatial maps available separately

---

**Last Updated**: 2026-04-06
**Evidence Tier**: A (Large-scale, high-quality single-cell atlas)
