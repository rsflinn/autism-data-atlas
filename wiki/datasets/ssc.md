---
id: ssc
name: "Simons Simplex Collection"
short_name: "SSC"
consortium: "Simons Foundation"
data_type: ["WGS", "WES", "genotyping", "phenotype", "deep_phenotype"]
sample_size: "Approximately 2,600 simplex families; WGS available for 6,383 individuals across 2,274 families"
access_level: CONTROLLED
access_url: "https://www.sfari.org/resource/simons-simplex-collection/"
wgs_available: true
wes_available: true
phenotype_depth: deep
has_noncoding_data: true
has_family_structure: true
has_simplex_design: true
has_iq_data: true
has_ados_data: true
has_vineland_data: true
has_medical_history: true
backfill_phase: 1
atlas_integration_status: not_started
evidence_tier: C
last_updated: 2026-04-06
---

# Simons Simplex Collection (SSC)

## Overview

The Simons Simplex Collection (SSC) is the foundational resource for de novo mutation discovery in autism. Comprising approximately 2,600 families with a simplex design (one affected child with autism spectrum disorder, unaffected parents, and an unaffected sibling in 80% of families), the SSC is uniquely optimized for identifying de novo variants that drive autism risk. The resource includes whole genome sequencing for 6,383 individuals across 2,274 families, alongside the deepest phenotyping of any major autism cohort, including autism diagnostic measures (ADOS), cognitive assessment (IQ via Wechsler scales), adaptive functioning (Vineland), and comprehensive medical and developmental history. Since 2010, the SSC has been the primary discovery resource underlying the majority of autism gene discoveries, including landmark de novo variant studies by Iossifov (2014), Sanders (2015), and more recent noncoding variant analyses (2024).

## Sample Structure: Simplex Family Design

The SSC's defining feature is its simplex family design, which is optimal for de novo variant discovery:

- **Family Structure:** One affected child with autism (proband) + unaffected biological parents + unaffected sibling (in 80%+ of families)
- **Total Families:** ~2,600 simplex families
- **Total Individuals:** 10,000+ with deep phenotyping
- **WGS Individuals:** 6,383 individuals from 2,274 families

This design is critical because:
1. **De novo discovery:** Parent-child trio structure enables definitive identification of de novo mutations (variants in proband absent in both parents)
2. **Null hypothesis testing:** Unaffected siblings provide internal controls for variant filtering
3. **Reduced confounding:** Simplex design reduces genetic heterogeneity from multiple affected family members carrying different mutations
4. **Power for association:** Enrichment of de novo variants in affected vs. unaffected siblings provides robust statistical evidence

The SSC achieves this population through rigorous recruitment criteria ensuring each family has exactly one diagnosed autistic child with unaffected parents (no parental autism history beyond screening questions).

## Available Data Types

### Genomic Data
- **Whole Genome Sequencing (WGS):** 6,383 individuals from 2,274 families; 30x average coverage
- **Whole Exome Sequencing (WES):** Complete WES available for all SSC individuals
- **Genotyping Arrays:** SNP arrays for genome-wide association studies (GWAS)
- **Sequencing Platform:** Illumina sequencing with quality control validation

### Deep Phenotyping
The SSC is legendary for rigorous, standardized phenotyping across multiple domains:

- **Autism Diagnosis Confirmation:**
  - Autism Diagnostic Interview (ADI): Semi-structured parent interview capturing developmental history
  - Autism Diagnostic Observation Schedule (ADOS): Standardized behavioral observation protocol
  - Clinical diagnosis confirmation by experienced clinicians

- **Cognitive and Adaptive Assessment:**
  - Wechsler Intelligence Scales (full IQ assessment)
  - Vineland Adaptive Behavior Scales (adaptive functioning and daily living skills)
  - Captures both intellectual ability and functional independence

- **Developmental and Medical History:**
  - Comprehensive developmental milestones
  - Medical comorbidities (seizures, gastrointestinal issues, sleep disorders, etc.)
  - Medication history
  - Family psychiatric history (for unaffected parents and siblings)

- **Behavioral Assessment:**
  - Symptom severity measurements
  - Language and communication skills
  - Motor development
  - Adaptive behavior in daily living

## Noncoding Variant Relevance

The SSC's WGS data, combined with its optimal family structure and deep phenotyping, makes it uniquely powerful for noncoding variant discovery:

- **De novo noncoding variants:** Recent analysis (2024) identified de novo noncoding variants contributing to approximately 4.3% of autism cases
- **Regulatory element disruption:** WGS captures variants in enhancers, promoters, silencers, and other regulatory regions
- **Intronic and intergenic variants:** Complete genome coverage enables discovery beyond coding regions
- **Family-based validation:** Parent-child trios and unaffected sibling comparisons provide definitive validation of noncoding mutations
- **Phenotype correlation:** Deep phenotyping enables assessment of whether noncoding variants show phenotypic specificity (e.g., contributing to intellectual disability, language impairment, seizure risk)

## Key Publications: Foundational De Novo Discoveries

1. **The Simons Simplex Collection: A Resource for Identification of Autism Genetic Risk Factors** (PMID: 20955926)
   - Fischbach GD, Lord C. Neuron. 2010; 68(2): 192-195. DOI: 10.1016/j.neuron.2010.05.014
   - Original SSC resource paper establishing the cohort, design rationale, and phenotyping protocol
   - Foundational reference for understanding why simplex design is optimal

2. **The contribution of de novo coding mutations to autism spectrum disorder** (PMID: 25363768)
   - Iossifov I, et al. Nature. 2014; 515(7526): 216-221. DOI: 10.1038/nature13908
   - Landmark study: First large-scale exome sequencing of SSC families (>2,500 families)
   - **Key findings:** 30% of simplex autism driven by de novo mutations; 45% in affected females
   - Established that different genes contribute to autism in males vs. females
   - Gene discovery: Identified key autism genes through de novo enrichment

3. **Insights into Autism Spectrum Disorder Genomic Architecture and Biology from 71 Risk Loci** (PMID: 26364307)
   - Sanders SJ, et al. Neuron. 2015; 88(6): 1226-1239. DOI: 10.1016/j.neuron.2015.09.029
   - TADA (Transmission And De novo Association) analysis combining SSC and ASC data
   - Identified 71 high-confidence autism risk loci
   - Definitive list of genes meeting genome-wide significance for autism association
   - **Most widely cited list of core autism genes**

4. **Identifying associations of de novo noncoding variants with autism through integration of gene expression, sequence, and sex information** (2024)
   - Recent WGS analysis of SSC noncoding variants
   - De novo noncoding variants identified in ~4.3% of cases
   - Integration with gene expression data and sex-specific effects
   - Demonstrates SSC utility for contemporary noncoding variant research

## Access Instructions

### Registration and Account Setup
1. Navigate to https://www.sfari.org/resource/simons-simplex-collection/
2. Log into SFARI Base; create account if needed
3. Affiliate with your institution
4. Register your institution if not already registered (provide Signing Official contact)

### Data Access Request
1. Create a SFARI Base request specifying:
   - Resource type (WGS, WES, phenotype, or combination)
   - Planned research use
   - Data analysis location (local download vs. cloud)
2. SFARI science team reviews (typical timeline: 4-12 weeks)
3. No embargo on SSC data; access granted immediately upon approval

### Data Formats and Delivery
- **WGS:** VCF files with variant calls
- **Phenotype:** Structured databases with phenotypic variables
- **Integration Tools:** Can request pre-harmonized phenotype matrices for cross-dataset analysis

## Atlas Integration Notes

### Priority Analyses for Phase 1

1. **De novo noncoding variant discovery:** SSC's optimal family structure is unmatched for de novo identification
   - Identify de novo variants in regulatory regions, intronic sequences
   - Compare frequency to background expectation
   - Assess enrichment in regulatory domains

2. **Gene discovery:** SSC remains the gold standard for autism gene validation
   - Use de novo burden analysis to identify high-confidence candidate genes
   - Combine with SPARK and MSSNG data for increased power

3. **Sex-stratified analysis:** SSC data shows striking sex differences in genetic architecture
   - De novo variants contribute 45% of female diagnoses vs. 30% overall
   - Prioritize sex-specific noncoding variant analyses

4. **Phenotype-genotype correlation:** Leverage deep phenotyping for mechanistic insight
   - Link specific noncoding variants to intellectual disability, language impairment, seizure risk
   - Identify phenotypic specificity of different variant classes

### Data Integration with SPARK and MSSNG
- **De novo discovery:** Combine SSC (family-validated de novos) with SPARK (larger sample) for power
- **Structural variants:** Integrate SSC WES-detected SVs with MSSNG WGS comprehensive SV calls
- **Phenotypic specificity:** Use SSC deep phenotyping as benchmark for validating associations found in larger but less phenotyped cohorts

### Key Genes Already Validated in SSC
The Sanders 2015 list of 71 high-confidence autism risk genes includes:
CHD8, FOXP1, PCDH19, GRIN2B, SHANK3, CACNA1C, TBR1, DYRK1A, RBBP5, MECP2, CDKL5, POGZ, GRIN2A, ASXL3, PLCB1, DCHS1, KIF1A, and 54 others

## De Novo Contribution Estimates

Based on SSC analysis:
- **Coding de novo mutations:** Account for ~30% of simplex autism cases overall
- **Female-specific de novo burden:** 45% of affected females have contributory de novo mutations vs. ~17% of affected males
- **Noncoding de novo mutations:** Recent analysis identifies additional 4.3% of cases with de novo noncoding variants
- **Total estimated de novo contribution:** 34-39% of simplex diagnoses

## Data Use Restrictions

SSC data is available for Not-For-Profit Research Use. Publications must acknowledge the Simons Foundation and SSC contribution. No commercial use without specific arrangement.

## Research Impact

The SSC has been the discovery resource underlying the vast majority of autism genetic findings from 2010 onwards:
- 70+ published studies using SSC data
- Foundation for all major autism gene lists and panels
- Standard benchmark for validating newly discovered genes
- Continues to be actively used in 2024-2026 for noncoding variant research

---

**Last Updated:** 2026-04-06
**Evidence Tier:** C (Dataset description; evidence from individual analyses varies)
**Backfill Priority:** Phase 1
**Regulatory Relevance:** Comprehensive (WGS captures full regulatory landscape; simplex design is gold standard for de novo discovery)
**Distinctive Features:** Simplex family design (optimal for de novo discovery) and deepest phenotyping of any major autism cohort

## Cross-Links

- [SPARK Whole Genome Sequencing](./spark-wgs.md) -- Largest cohort; use for power in larger-sample analyses
- [MSSNG](./sfari-base.md) -- Complementary structural variant expertise and cloud accessibility
- [Evidence Tiers](../concepts/evidence_tiers.md) -- Understanding how SSC discoveries are validated
