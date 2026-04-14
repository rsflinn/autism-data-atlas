---
id: spark-wgs
name: "SPARK Whole Genome Sequencing"
short_name: "SPARK WGS"
consortium: "Simons Foundation"
data_type: ["WGS", "WES", "phenotype", "clinical", "genotyping"]
sample_size: "330,000+ total participants; 123,444 with autism; 3,568 genomes and 34,164 exomes from individuals with ASD"
access_level: CONTROLLED
access_url: "https://www.sfari.org/resource/spark/"
wgs_available: true
wes_available: true
phenotype_depth: deep
has_noncoding_data: true
has_family_structure: true
has_iq_data: true
has_ados_data: true
backfill_phase: 1
atlas_integration_status: not_started
evidence_tier: C
last_updated: 2026-04-06
---

# SPARK Whole Genome Sequencing

## Overview

SPARK (Simons Foundation Powering Autism Research) represents the largest autism family cohort in the world, with over 330,000 participants including 123,444 individuals with autism spectrum disorder as of 2023. The cohort includes matched whole genome sequencing (WGS), whole exome sequencing (WES), and rich phenotypic data including behavioral assessments, IQ measurements, adaptive behavior ratings, and detailed medical histories. SPARK provides an unparalleled resource for studying the genetic basis of autism across diverse family structures and phenotypic presentations.

## Sample Structure

SPARK includes both simplex families (one affected child) and multiplex families (multiple affected members). The study was designed as a completely online, longitudinal research platform with rapid enrollment of families self-identifying through web-based recruitment. This design enables rapid scaling while maintaining detailed phenotypic data collection. Over 80% of enrolled families have genetic material from both parents and at least one unaffected sibling, optimizing power for family-based genetic analysis. The cohort spans the full age range (children to adults) and includes diverse US ethnic and racial populations.

## Available Data Types

### Genomic Data
- **Whole Genome Sequencing (WGS):** 3,568 genomes from individuals with ASD, averaging 30x coverage
- **Whole Exome Sequencing (WES):** 34,164 exomes from individuals with ASD
- **Genotyping Arrays:** 690,000 SNP array (Infinium Global Screening Array-24 v1.0) optimized for ethnically diverse cohorts, capturing common variants, structural variants, and copy-number variants
- **Total genomic data:** 81,172 SPARK participants with genomic data available

### Phenotypic Data
Comprehensive behavioral and clinical assessments available for 310,649 enrolled individuals:
- **Autism-Specific Measures:** Autism Diagnostic Observation Schedule (ADOS, subset), clinical ASD diagnosis confirmation
- **Developmental Assessments:** Vineland Adaptive Behavior Scales-3 (Vineland-3), Developmental Coordination Disorder Questionnaire (DCDQ)
- **Behavioral Questionnaires:** Adult Self Report (ASR), Child Behavior Checklist (CBCL), Repetitive Behavior Scale-Revised (RBS-R), Social Communication Questionnaire (SCQ), Social Responsiveness Scale-2 (SRS-2)
- **Cognitive Assessment:** IQ/Intelligence Quotient measurements (subset)
- **Medical History:** Comprehensive developmental and medical history including comorbidities, medications, and health conditions
- **Family Context:** Detailed parental and sibling phenotype data

## Noncoding Variant Relevance

SPARK's WGS data provides comprehensive coverage of noncoding variants critical for autism regulatory architecture. With 3,568 full genomes, researchers can systematically identify de novo noncoding mutations, inherited regulatory variants, and structural variants affecting regulatory elements. The combination of parent-child trios (optimal for de novo discovery) with detailed phenotypic data enables correlation of noncoding variant burden with phenotypic features. Early SPARK analyses using WGS have begun identifying de novo noncoding variants in regulatory regions and intronic sequences that may contribute to autism risk.

## Key Publications

1. **SPARK: A US Cohort of 50,000 Families to Accelerate Autism Research** (PMID: 29420931)
   - SPARK Consortium. Neuron. 2018; 97(3): 488-493. DOI: 10.1016/j.neuron.2018.01.015
   - Original SPARK cohort description at launch; foundational reference

2. **Validation of Autism Diagnosis and Clinical Data in the SPARK Cohort** (PMID: 34328611)
   - SPARK Consortium. Scientific Data. 2021. DOI: 10.1038/s41597-021-00924-1
   - Comprehensive validation of phenotypic data quality and autism diagnosis accuracy

3. **SPARK December 2022 Update: New Phenotypic Data Available** (SFARI, 2023)
   - Data release notes documenting phenotypic expansion to 310,649 individuals

## Access Instructions

### Registration and Account Setup
1. Navigate to https://www.sfari.org/resource/spark/ and log into SFARI Base
2. Create a SFARI Base account if you don't have one
3. Affiliate with your institution during account creation
4. If your institution is not yet registered, provide institution name and contact information for your Signing Official

### Data Access Request
1. Create a SFARI Base request specifying resource type (phenotype, genetic data, or both)
2. Indicate whether you need WGS, WES, or genotyping array data
3. SFARI science team reviews requests (typical timeline: 4-12 weeks)

### Data Availability and Embargoes
- **Phenotypic Data:** No embargo; available immediately upon approval
- **Genomic Data:** 6-month embargo from release date (allows SPARK team priority analysis)
- **Cloud Analysis:** Available through SFARI partnership; reduces need for local data download

## Atlas Integration Notes

### Priority Analyses for Phase 1
1. **De novo noncoding variant discovery:** Leverage WGS data from 3,568 probands to identify de novo noncoding mutations in regulatory regions, compare frequency to background rates
2. **Inherited regulatory variant burden:** Assess common and rare inherited variant burden in key autism genes vs. null-expectation
3. **Phenotype-genotype correlation:** Link genetic findings to specific SPARK phenotypes (IQ, adaptive behavior, comorbidities) to identify phenotypic specificity
4. **Family structure advantage:** Use parent-child trios and sibling comparisons to validate inheritance patterns and identify de novo events

### Data Harmonization Requirements
- Phenotype data needs standardization for cross-cohort comparison with MSSNG, SSC
- Genotyping array data requires lift-over to current genome build (GRCh38/hg38)
- Recommend working with SFARI-provided harmonized phenotype matrices

### Key Genes Already Identified
Across SPARK analyses, variants have been identified in validated autism genes including CHD8, SHANK3, PCDH19, and others, with additional novel genes identified through genome-wide analysis.

## Data Use Restrictions

SPARK data is available for Not-For-Profit Research Use. Publications must include appropriate acknowledgment of SPARK and Simons Foundation funding.

---

**Last Updated:** 2026-04-06
**Evidence Tier:** C (Dataset description; evidence for individual findings varies by analysis)
**Backfill Priority:** Phase 1
**Regulatory Relevance:** Comprehensive (WGS captures full regulatory landscape)
