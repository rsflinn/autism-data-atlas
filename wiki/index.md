---
title: Autism Genomics Atlas Wiki
last_updated: 2026-04-04
type: index
---

# Autism Genomics Atlas Wiki

Master index of all wiki pages with one-line summaries.

## Genes

- [MEF2C](./genes/MEF2C.md) -- Network hub whose haploinsufficiency specifically dysregulates ORC network members in organoids
- [SCN2A](./genes/SCN2A.md) -- Sodium channel at the autism-epilepsy comorbidity boundary; convergent target of multiple autism gene perturbations
- [FOXP1](./genes/FOXP1.md) -- Transcription factor; loss-of-function causes FOXP1 syndrome with universal autism, intellectual disability, and speech impairment
- [TCF4](./genes/TCF4.md) -- Transcription factor; mutations cause Pitt-Hopkins syndrome, the most severe syndromic autism phenotype
- [CDKL5](./genes/CDKL5.md) -- Developmental kinase; deficiency causes severe early-onset epilepsy with autism and neurodevelopmental encephalopathy
- [SHANK3](./genes/SHANK3.md) -- Postsynaptic scaffolding protein; loss-of-function causes Phelan-McDermid syndrome with 80% autism penetrance
- [CHD8](./genes/CHD8.md) -- Chromatin remodeler; haploinsufficiency causes syndromic autism with macrocephaly and distinctive facial features
- [DYRK1A](./genes/DYRK1A.md) -- Developmental kinase; loss-of-function causes DYRK1A syndrome with intellectual disability and autism

## Concepts

- [Receptor Type Separation](./concepts/receptor_type_separation.md) -- GABA receptors drive epilepsy signal, glutamate receptors drive autism convergence, shared genes predict comorbidity
- [Convergence Phenomenon](./concepts/convergence_phenomenon.md) -- Multiple autism gene knockouts produce overlapping downstream effects, but specificity is dataset-dependent
- [Noncoding Variants in Autism](./concepts/noncoding_variants_in_autism.md) -- Common inherited variants account for ~49% of autism liability; all GWAS-significant loci are regulatory
- [Evidence Tiers](./concepts/evidence_tiers.md) -- Classification system for experimental evidence quality (A: properly nulled; B: real but not specific; C: descriptive; D: corrected)

## Datasets

### Phase 1 Backfill Priority (Foundational Autism Cohorts)

- [SPARK Whole Genome Sequencing](./datasets/spark-wgs.md) -- Largest autism family cohort (330,000+ participants; 123,444 with autism) with comprehensive WGS, WES, deep phenotyping (ADOS, IQ, adaptive behavior)
- [MSSNG (Autism Speaks)](./datasets/sfari-base.md) -- World's largest autism WGS resource (5,100 with autism + 6,212 family members) with world-class structural variant characterization and free cloud-based access
- [Simons Simplex Collection (SSC)](./datasets/ssc.md) -- Gold-standard de novo discovery resource (2,600 simplex families; 6,383 individuals with WGS) with deepest phenotyping; foundation for most major autism gene discoveries

### Regulatory & Functional Genomics (Phase 1)

- [ENCODE Project](./datasets/encode.md) -- 2.37M candidate cis-regulatory elements with >90% experimental validation; comprehensive chromatin accessibility and transcription factor binding across hundreds of cell types
- [GTEx Brain Tissues](./datasets/gtex-brain.md) -- Gene expression and eQTL/sQTL mapping across 13 brain regions from 838 donors; tissue-specific variant effects on gene expression
- [Allen Brain Atlas](./datasets/allen-brain-atlas.md) -- 2.78M single-nucleus transcriptomes and spatial transcriptomics; comprehensive human brain cell-type taxonomy with 100+ distinct types

### Supporting Datasets

- [BrainSpan](./datasets/brainspan.md) -- Developmental brain expression atlas spanning prenatal to adult periods
- [PsychENCODE Gene Regulatory Networks](./datasets/psychencode-grn.md) -- Single-cell transcriptomics and regulatory annotations of developing and adult brain
- [Epi25 Whole Exome Sequencing](./datasets/epi25-wes.md) -- Large-scale epilepsy sequencing consortium essential for understanding autism-epilepsy comorbidity

## Methods

### Tools

- [varTFBridge](./tools/varTFBridge.md) -- Traces noncoding variants to transcription factors and genes, identifying regulatory variants rewiring gene networks
- [ANNEVO](./tools/ANNEVO.md) -- Deep learning model for accurate ab initio gene annotation from sequence alone
- [GET](./tools/GET.md) -- Foundation model predicting gene expression across human cell types from chromatin and sequence data
- [PARM](./tools/PARM.md) -- Deep learning model predicting promoter activity and regulatory effects of variants
- [Genotype-Phenotype Map](./tools/genotype_phenotype_map.md) -- Comprehensive database mapping genetic associations across 16K traits and 2.7M molecular measurements
- [AlphaGenome](./tools/AlphaGenome.md) -- Google DeepMind unified DNA sequence model; best-in-class regulatory variant effect prediction across chromatin, TF binding, and gene expression modalities (Nature 2026)

## Findings

(Placeholder for key findings synthesis pages)

- [So Fragile, So Human: Noncoding DNA Regions Orchestrating Gene Expression Involved in Neurodevelopmental Disorders and in Human Brain Evolution.](./findings/41898648.md) -- PMID: 41898648
- [Closing the Gap in Autism Genetics: Population-Specific Variants and the Imperative for Global Inclusion.](./findings/41921886.md) -- PMID: 41921886
- [Etiology of autism spectrum disorders: recent advances and emerging directions.](./findings/41542841.md) -- PMID: 41542841
- [Co-occurrence of rare variants implicates gene pairs in cytoskeletal pathways and is associated with increased severity in autism spectrum disorder.](./findings/41872878.md) -- PMID: 41872878
- [NLGN3 autism variants have distinct functional impact on synapses and sleep behavior in Drosophila](./findings/biorxiv_NLGN3_2026.md) -- bioRxiv 2026; variant-specific synaptic phenotypes in Drosophila NLGN3 model
- [Analysis of 14q12 microdeletions reveals novel regulatory loci for the neurodevelopmental disorder-related gene, FOXG1](./findings/biorxiv_FOXG1_regulatory_2026.md) -- bioRxiv 2026; noncoding SVs disrupting FOXG1 CREs cause NDD; highest-scoring new preprint this week
- [Assessing molecular gene by treatment interactions using a population of neural progenitors exposed to valproic acid and lithium](./findings/41935183.md) -- PMID: 41935183; VPA/lithium gene-treatment interactions mapped via chromatin accessibility in 83-donor neural progenitor population; psychiatric risk variant enrichment (score: 36)
- [Enhancer hubs govern chromatin topology and Th17 identity](./findings/biorxiv_enhancer_hubs_Th17_2026.md) -- bioRxiv 2026; enhancer hub framework for chromatin topology; methods-transferable to autism regulatory analysis (score: 16)
- [Brain cell type nuclei enrichment without fixative for nanoCUT&Tag and other omics approaches](./findings/biorxiv_brain_nuclei_nanoCUTTag_2026.md) -- bioRxiv 2026; fixative-free brain cell-type epigenomic profiling workflow applicable to autism variant characterization (score: 17)
---

**Last Updated:** 2026-04-09 (daily scan)

- [Pan et al. 2026 — Convergent genetic pathways linking neuropsychiatric and ocular disorders](findings/41947537.md) (2026-04-07, score 25)
- [Pedapati et al. 2026 — SPG601 BK channel activator in Fragile X syndrome](findings/41946887.md) (2026-04-07, score 23)
- [Sala-Gaston et al. 2026 — Proteasome dysfunction in HERC2-linked NDD](findings/41951624.md) (2026-04-08, score 19)
- [Qiu et al. 2026 — STEAM: Evolutionary transfer learning for mammalian enhancer landscapes](findings/10_64898_2026_04_07_717039.md) (2026-04-08, score 32)
- [Li et al. 2025 — FMRP regulates neuronal RNA granules containing stalled ribosomes](findings/10_1101_2025_02_21_639553.md) (2025-02-21, score 22)
- [Lolam & Roy 2026 — NF1 expression atlas in developing mouse brain](findings/10_64898_2026_03_22_713444.md) (2026-03-24, score 20)
- [Kumar et al. 2026 — Subunit-selective GABAA receptor modulation via neurosteroid DARTs](findings/10_64898_2026_03_23_713679.md) (2026-03-26, score 18)

## 2026-04-10 Daily Scan

### INTEGRATE (9 papers)
- [Distinct cellular DNA methylation mechanisms underlie common and rare genetic risk for brain disorders](findings/41959448.md) - Zhou et al. 2026 | Score: 43/50 | **Top pick**: mCG vs mCH distinct mechanisms for common vs rare noncoding ASD variants, 186 cell subtypes, replicated in 5,782 probands
- [ICePop: Linking Genetic Risk to Disease-Relevant Cellular States](findings/41959181.md) - Yuan et al. 2026 | Score: 35/50 | Metacell-resolution GWAS mapping, ASD risk in enteric neuron subtypes
- [SYNGAP1 Synchronizes Relative Neuronal Maturation](findings/41959404.md) - Golovin et al. 2026 | Score: 31/50 | SYNGAP1 haplo produces opposing cortical activity patterns via maturation timing
- [In vivo human embryonic spinal cord atlas reveals ASD spinal signatures](findings/biorxiv_2025.12.22.696129.md) - Gupta et al. 2025 | Score: 29/50 | ASD genes enriched in mechanosensory spinal interneurons
- [Cell-specific variant-to-gene mapping for sleep](findings/biorxiv_2026.04.07.715910.md) - Zimmerman et al. 2026 | Score: 23/50 | V2G methods applicable to ASD GWAS
- [Non-canonical Hif-1alpha roles in interneuron development](findings/41956077.md) - Li & Pasca 2026 | Score: 23/50 | GRIN2B interaction, Pasca lab
- [Base editing in AUTS2](findings/41958697.md) - Yan et al. 2026 | Score: 22/50 | iPSC allele-specific model for ASD gene
- [Proteasome dysfunction in HERC2-linked NDD](findings/41951624.md) - Sala-Gaston et al. 2026 | Score: 21/50 | Angelman-like, proteasome mechanism
- [Somatic RAS-MAPK variants in drug-resistant epilepsy](findings/biorxiv_2026.04.06.716727.md) - Warren et al. 2026 | Score: 21/50 | Hippocampal sclerosis genetic basis

### REVIEW (1 paper)
- ML functional connectomes in ASD (Grassia et al. 2026, PMID 41957158) - Score: 14/50 - fMRI deep learning, no genetics

### SKIP (4 papers)
- Sweet potato metabolomics (tangential autism mention)
- Pediatrician ASD screening barriers (qualitative)
- Literacy instruction for minimally verbal autism (no genetics)
- Family resilience interventions review (no genetics)

### 2026-04-12 Daily Scan

- **[PMID 41963441](findings/41963441.md)** (Score: 29) - Base editing restores CDKL5 expression and rescues neuronal deficits in a patient-derived model of CDKL5 deficiency disorder. *Genes: CDKL5*
- **[PMID 41964267](findings/41964267.md)** (Score: 15) - Reliability and stability of cerebral palsy classification scales for individuals with STXBP1- and SYNGAP1-related disorders. *Genes: STXBP1, SYNGAP1*
- **[DOI 10.1101/2024.05.26.595966](findings/10.1101_2024.05.26.595966.md)** (Score: 16) - Complementary vertebrate Wac models exhibit phenotypes relevant to DeSanto-Shinawi Syndrome. *Genes: WAC*

### 2026-04-13 Daily Scan

- [WAC / DeSanto-Shinawi Syndrome vertebrate models](findings/biorxiv_WAC_DeSanto_Shinawi_2026.md) — INTEGRATE (23/50). First mouse+zebrafish WAC knockouts showing GABAergic neuron impacts, seizures, autism-relevant behaviors.
- [EVEE: Variant effect prediction via Evo 2 foundation model](findings/biorxiv_EVEE_variant_prediction_2026.md) — INTEGRATE (25/50). SOTA variant pathogenicity prediction (0.997 AUROC), 4.2M ClinVar variants pre-scored.

## Daily Scan - 2026-04-14

| Score | Decision | Title | Source | Genes |
|-------|----------|-------|--------|-------|
| 29 | INTEGRATE | [Tic Disorders GWAS - 6 Risk Loci incl. HCN1](findings/10_64898_2026_04_09_26350245.md) | medRxiv | HCN1 |
| 28 | INTEGRATE | [Federated single-cell QTL meta-analysis](findings/10_64898_2026_01_20_700519.md) | bioRxiv | - |
| 26 | INTEGRATE | [FKH-7/FOXP1 in C. elegans chemosensory neurons](findings/41974488.md) | Genetics | FOXP1 |
| 26 | INTEGRATE | [De novo mutation timing in male germline](findings/10_64898_2026_04_09_26350474.md) | medRxiv | - |
| 23 | INTEGRATE | [Cortical morphology x psychiatric disorders](findings/10_64898_2026_04_10_26349224.md) | medRxiv | - |
| 18 | INTEGRATE | [ASD Genetic Architecture Review](findings/41977462.md) | Int J Mol Sci | SHANK3, MECP2+ |
| 18 | INTEGRATE | [CK2alpha OCNDS variant characterization](findings/41978434.md) | FEBS J | CSNK2A1 |
| 10 | REVIEW | Nrp2 deletion - autism/seizure behaviors (letter) | Mol Psychiatry | NRP2 |
| 10 | REVIEW | Cytoskeletal dynamics in SZ and ASD | Biology | SHANK3 |

## Daily Scan - 2026-04-15

| Score | Decision | Title | Source | Genes |
|-------|----------|-------|--------|-------|
| 16 | INTEGRATE | [Drug-resistant early-onset epilepsy genetics](findings/41982969.md) | Transl Pediatr | KCNQ2, SCN2A |
| 19 | INTEGRATE | [Neanderthal alleles and present-day brain morphology](findings/10_64898_2026_04_14_718380.md) | bioRxiv | - |
| 15 | INTEGRATE | [Rare variant pleiotropy across biobank phenotypes](findings/10_1101_2024_10_01_614806.md) | bioRxiv | - |
| 14 | REVIEW | Somatic mutation landscape from urine iPSCs (Vaccarino lab) | bioRxiv | - |
| 12 | REVIEW | Nrp2 interneuron deletion - autism/seizure (response letter) | Mol Psychiatry | NRP2 |
| 6 | SKIP | VR adaptive game for joint attention in ASD (tech paper) | Int J Dev Neurosci | - |
| 4 | SKIP | Swallowing in speech-delayed children (excluded autism) | Int J Lang Commun Disord | - |

*Note: FOXP1/FKH-7 (score 27), federated sc-QTL (score 30), ASD genetic architecture review (score 20), CK2α OCNDS (score 17), and EVEE (score 25) were already captured in prior scans.*

## Daily Scan - 2026-04-16

| Score | Decision | Title | Source | Genes |
|-------|----------|-------|--------|-------|
| 33 | INTEGRATE | [Cis-regulatory variation in brain enhancers (PD cohort)](findings/10_64898_2026_03_15_711881.md) | bioRxiv | - |
| 32 | INTEGRATE | [MAGEB16 epigenetic timing regulator in ASD](findings/41988164.md) | EXCLI J | MAGEB16 |
| 21 | INTEGRATE | [SynGAP C2 domain missense mutations impair membrane diffusion](findings/41983718.md) | Protein Sci | SYNGAP1 |
| 20 | INTEGRATE | [NeuroPathX imaging-genetics framework (ASD validated)](findings/41988634.md) | MICCAI | - |
| 19 | INTEGRATE | [Polygenic origins of uneven NDD cognitive profiles](findings/41987674.md) | Dev Sci | - |
| 14 | REVIEW | Regulatory logic of neuronal differentiation in Drosophila | bioRxiv | - |
| 6 | SKIP | Social ABCs group program evaluation | Autism | - |
| 3 | SKIP | Parental resilience and ASD behavioral profiles | Psychol Res Behav Manag | - |
| 3 | SKIP | AVATA Cure digital therapeutics for ASD | Psychiatry Investig | - |
| 2 | SKIP | VR adaptive game for joint attention in ASD | Int J Dev Neurosci | - |

*Top pick: Sigalova et al. brain enhancer cis-regulatory variation modeling (score 33) -- methodology directly applicable to autism GWAS noncoding loci. Also notable: MAGEB16 paper (score 32) proposes X-linked epigenetic timing mechanism for ASD susceptibility.*

## 2026-04-17 Daily Scan Findings

- [Histone H1 Variants Regulate Neurodevelopmental Transcriptional Programs in Autism with 16p11.2 deletion](./findings/10.64898_2026.04.15.718682.md) -- score 37; Brudno R et al. (bioRxiv, 2026-04-16); no atlas genes
- [Modeling cis-regulatory variation in human brain enhancers across a large Parkinson's Disease cohort](./findings/10.64898_2026.03.15.711881.md) -- score 30; Sigalova OM et al. (bioRxiv, 2026-04-16); no atlas genes
- [Cell-type-resolved NRXN1 isoforms across human brain tissues and hiPSC cortical organoids](./findings/10.1101_2025.11.11.687875.md) -- score 30; Cao L et al. (Brennand, Roussos labs) (bioRxiv, 2026-04-17); NRXN1
- [Disrupted glial-mediated synaptic refinement in Fragile X syndrome](./findings/41993264.md) -- score 24; Starr L et al. (bioRxiv, 2026-04-11); FMR1
- [MAGEB16 as an epigenetic timing regulator linking X-chromosome biology to neurodevelopmental vulnerability in Autism Spe](./findings/41988164.md) -- score 20; Gaspar JA et al. (EXCLI J, 2026-03-06); MAGEB16
- [Examining Genetic Variants Associated with FOXP1 Syndrome through Molecular Dynamics of Its DNA-Binding Domain and Self-](./findings/41992872.md) -- score 20; Motta S et al. (J Chem Inf Model, 2026-04-17); FOXP1
- [Learning Explainable Imaging-Genetics Associations Related to a Neurological Disorder](./findings/41988634.md) -- score 18; Wang J et al. (MICCAI (LNCS), 2025-09-20); no atlas genes
- [EVEE: Interpretable variant effect prediction from genomic foundation model embeddings](./findings/10.64898_2026.04.10.717844.md) -- score 17; Pearce MT et al. (bioRxiv, 2026-04-16); no atlas genes
- [Instability of Alpha Oscillatory States in Autism and Familial Liability: Evidence from Burst-Resolved High-Density EEG](./findings/41993350.md) -- score 16; Vanneau T et al. (bioRxiv, 2026-04-07); no atlas genes
- [Causal effects of single-carbon metabolism and vitamin levels on autism spectrum disorder risk: a bidirectional Mendelia](./findings/41992357.md) -- score 15; Zhu J et al. (Ital J Pediatr, 2026-04-16); no atlas genes

**Last Updated:** 2026-04-18 (daily scan)

- [Vermudez et al. 2026 — Increasing MeCP2 in Pitt-Hopkins (Tcf4) mice does not fix myelination but generates astrocytes](findings/41997465.md) (2026-04-15, score 27)
- [Parasar et al. 2026 — Whole-genome 3D architectural screen of brain DNA structure (Plate-C)](findings/10.64898_2026.04.15.718501.md) (2026-04-17, score 25)
