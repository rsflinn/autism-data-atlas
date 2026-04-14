---
id: mssng
name: "MSSNG (Missing Genome) - Autism Speaks WGS Resource"
short_name: "MSSNG"
consortium: "Autism Speaks"
data_type: ["WGS", "phenotype", "structural_variants", "mitochondrial"]
sample_size: "5,100 individuals with autism + 6,212 family members (total 11,312), as of November 2022; continuously growing"
access_level: CONTROLLED
access_url: "https://research.mss.ng/"
wgs_available: true
wes_available: false
phenotype_depth: moderate
has_noncoding_data: true
has_structural_variants: true
has_family_structure: true
has_mitochondrial_data: true
backfill_phase: 1
atlas_integration_status: not_started
evidence_tier: C
last_updated: 2026-04-06
---

# MSSNG: Autism Speaks Whole Genome Sequencing Resource

## Overview

MSSNG (pronounced "missing") is the world's largest autism-focused whole genome sequencing resource, developed by Autism Speaks in partnership with Verily (formerly Google Life Sciences). The dataset comprises 5,100 individuals diagnosed with autism spectrum disorder and 6,212 family members (total 11,312 individuals as of November 2022), with WGS data hosted on the Google Cloud Platform. MSSNG is distinctive among major autism cohorts for its comprehensive structural variant characterization, cloud-based infrastructure with analytical tools, and free access to qualified international researchers. The project continues to grow as new batches of samples are processed.

## Sample Structure

MSSNG includes a mixture of simplex and multiplex families, with variable family member sequencing coverage. The international nature of the recruitment (with representation from Canada, USA, and other regions) provides greater population diversity than earlier primarily US-focused cohorts. While phenotypic data is more limited than cohorts like SPARK or SSC, the comprehensive structural variant characterization partially compensates by enabling variant-focused analyses.

## Available Data Types

### Genomic Data
- **Whole Genome Sequencing:** 5,100 individuals with autism, 6,212 family members; high-depth sequencing (typically 30x+)
- **Sequencing Platform:** Illumina sequencing with rigorous quality control
- **Comprehensive Variant Calling:**
  - Single nucleotide variants (SNVs): 52% of observed variants
  - Structural variants (SVs): 46% of observed variants, including:
    - Copy number variants (CNVs)
    - Inversions
    - Large insertions
    - Tandem repeat expansions
    - Uniparental isodisomies
  - Mitochondrial variants: 2% of observed variants
  - Polygenic risk scores: Calculated for subset

### Phenotypic Data
- **Limited phenotypic annotation** compared to SPARK or SSC
- **Medical history** and basic demographic information available
- No standardized behavioral assessment measures (unlike SSC/SPARK ADOS, Vineland)
- Focus is on genomic rather than phenotypic characterization

## Noncoding Variant Relevance

MSSNG's comprehensive structural variant calling makes it uniquely valuable for studying noncoding regulatory variation. The 46% of variants classified as structural variants include regulatory region disruptions not typically captured by SNV-only approaches. MSSNG data has revealed that structural variants account for a substantial portion of autism genetic architecture. With WGS of 5,100 affected individuals plus family members, MSSNG enables systematic discovery of de novo and inherited structural variants in regulatory regions, enhancing our understanding of noncoding autism biology.

## Key Publications

1. **Whole genome sequencing resource identifies 18 new candidate genes for autism spectrum disorder** (PMID: 28263302)
   - Yuen RK, et al. Nature Neuroscience. 2017; 20(4): 602-611. DOI: 10.1038/nn.4524
   - Initial MSSNG discovery paper establishing 18 new autism risk genes

2. **Genomic architecture of autism from comprehensive whole-genome sequence annotation** (PMID: 36368308)
   - Kaplanis J, et al. Cell. 2022; 185(24): 4409-4426. DOI: 10.1016/j.cell.2022.11.011
   - Comprehensive analysis of genomic architecture including extensive structural variant characterization
   - Defines variants contributing to autism across sequence-level, structural, and mitochondrial domains

3. **Long Read Genome Sequencing Elucidates Diverse Functional Consequences of Structural and Repeat Variation in Autism** (2024)
   - Advanced long-read sequencing revealing structural variant complexity missed by short-read approaches

## Access Instructions

### Registration and Data Access
1. Navigate to https://research.mss.ng/
2. Create a researcher account with your institutional affiliation
3. Complete a data access request (typically faster than SPARK/SSC due to no embargo)
4. Approval timeline: 4-8 weeks (variable by request type)

### Cloud-Based Analysis
- **Platform:** Google Cloud Platform (GCP)
- **Partner:** Verily Life Sciences
- **Cost:** Free access for qualified researchers
- **Analytical Tools:** Integrated analytical tools available directly on GCP platform
- **Infrastructure:** Researchers can spin up analysis environments without downloading multi-terabyte datasets locally

### International Access
- Available to 62 institutions across 18 countries
- Designed for global collaboration in autism research

## Atlas Integration Notes

### Priority Analyses for Phase 1
1. **Structural variant discovery:** MSSNG is the only major autism cohort with comprehensive SV characterization; prioritize SV-driven regulatory disruptions
2. **Noncoding regulatory variants:** Analyze structural variants disrupting enhancers, promoters, and other regulatory elements
3. **De novo SV burden:** Assess de novo SV contribution to autism (distinct from SNV burden documented in SSC)
4. **Population-specific variants:** Leverage MSSNG's international diversity to identify population-stratified regulatory variation

### Data Harmonization Requirements
- MSSNG phenotypic data is minimal; expect to integrate with SPARK/SSC for phenotype-genotype correlations
- Structural variant nomenclature and coordinates require standardization across datasets
- Recommend using MSSNG raw VCFs for maximum control over variant filtering

### Distinctive Advantages
- Only autism cohort with world-class structural variant characterization
- Free cloud-based access eliminates computation bottleneck
- International sample diversity
- Continuing to grow as new samples are processed

## Data Use Restrictions

MSSNG data is available for research use. Specific restrictions vary by access tier; generally restricted to non-commercial research. Publications must acknowledge Autism Speaks and Verily partnership.

## Research Impact

MSSNG has been accessed by 62 institutions in 18 countries and has contributed to major discoveries in autism genomic architecture. The 2022 Kaplanis et al. publication in Cell demonstrates the research potential of the resource with comprehensive variant characterization across multiple variant classes.

---

**Last Updated:** 2026-04-06
**Evidence Tier:** C (Dataset description; evidence for individual findings varies by analysis)
**Backfill Priority:** Phase 1
**Regulatory Relevance:** Comprehensive (WGS captures full regulatory landscape; SV focus is unique advantage)
**Distinctive Feature:** World-class structural variant characterization and cloud-based accessibility
