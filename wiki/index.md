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
- [BRAIN-MAGNET](./tools/BRAIN-MAGNET.md) -- ChIP-STARR-seq-trained CNN that predicts non-coding regulatory element activity in neural stem cells; ~100M pre-scored SNPs for variant lookup (Cell 2026; PMID 41265437) -- candidate, needs verification
- [Chorus](./tools/Chorus.md) -- Unified Python interface for six genomic deep-learning models (Enformer, Borzoi, ChromBPNet, Sei, LegNet, AlphaGenome); percentile-ranking against ~10K random SNPs gives a built-in null for any single-variant prediction (pinellolab, 2026) -- candidate
- [HDMA (Human Development Multiomic Atlas)](./tools/HDMA.md) -- Paired snATAC + snRNA from 817,740 fetal cells across 12 organs, 203 cell types, 1M+ cCREs, with per-cell-type ChromBPNet models (Greenleaf Lab; Liu*, Jessa* et al., Nature 2026; doi 10.1038/s41586-026-10326-9) -- candidate

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

## 2026-04-20 Daily Scan

### INTEGRATE (7 papers)
- [Forti et al. 2026 — RBFOX/NOVA splicing dysregulation at NRXN3 in monogenic ASD](findings/10_1101_2025_10_02_680092.md) - bioRxiv | Score: 31/50 | Splicing regulator dysfunction drives aberrant NRXN3 splicing; directly relevant to RBFOX1 + neurexin genes in core set
- [Wagner et al. 2026 — Neonatal cerebellar functional connectivity impacted by sex and autism polygenic liability](findings/10_64898_2026_04_17_26351076.md) - medRxiv | Score: 31/50 | Common noncoding variants shape cerebellar circuits from infancy
- [Pato et al. 2026 — Multiplex Portuguese families show shared genetic architecture of SZ/mood/ASD](findings/42006790.md) - medRxiv | Score: 30/50 | WGS of founder population reveals rare large-effect variants crossing diagnostic boundaries
- [Castro et al. 2026 — Novel HCFC1 variants (including noncoding) in ASD/ADHD with brain malformations](findings/42004903.md) - Mol Genet Metab Rep | Score: 27/50 | One noncoding HCFC1 variant identified; phenotypic expansion beyond cblX
- [Oostland et al. 2026 — Cerebellar Purkinje cell disruption accelerates learning in autism mouse model](findings/41999601.md) - Cell Reports | Score: 23/50 | Links cerebellum to sensory salience and weak coherence
- [Cheung 2026 — Developmental taxonomy of autism: early vs late-diagnosed subtypes](findings/42006518.md) - Cureus | Score: 23/50 | Single-author conceptual review; Failure to Build vs Failure to Refine
- [Sejd et al. 2026 — PSD3 identified as direct NUAK1 substrate regulating dendritic spines](findings/10_64898_2026_04_16_718295.md) - bioRxiv | Score: 22/50 | Chemical genetics links ASD-associated kinase to synaptic maturation

### REVIEW (5 papers)
- Shin et al. 2026 (PMID 42006949) - Dementia risk neuroanatomy in ASD | Score: 16/50 | Imaging only
- Wen et al. 2026 (PMID 42001626) - Comorbidity-aware transfer learning for NDD diagnosis | Score: 14/50 | fMRI classifier
- Awad et al. 2026 (PMID 42004618) - Nose-to-brain CBD micelles for ASD | Score: 13/50 | Drug delivery
- Dalvi-Garcia et al. 2026 (PMID 42001525) - ASD invisibility in Brazilian suicide records | Score: 12/50 | Epidemiology
- Licona et al. 2026 (PMID 42004682) - Spanish PRT autism early intervention | Score: 10/50 | Behavioral

### SKIP (3 papers)
- Lenker et al. 2026 (PMID 41999360) - Sleep intervention qualitative study
- Xia et al. 2026 (PMID 42004597) - Algae polysaccharide VPA model neuroprotection
- Hejlesen & Jensen 2026 (PMID 42006339) - Arts on prescription (autism tangential)

### Notes
- bioRxiv genomics category search timed out twice; coverage may be incomplete for that category.


## 2026-04-22 Daily Scan

### INTEGRATE (3 papers)
- [Muntane et al. 2026 — Genetic overlap and shared risk loci between ASD and cardiometabolic traits](findings/42009985.md) - Mol Psychiatry | Score: 33/50 | MiXeR+pleioFDR identify 100 shared loci/124 genes between ASD and cardiometabolic GWAS
- [Bazbaz et al. 2026 — Nitric oxide inhibition ameliorates cortical proteomic changes in Cntnap2 and Shank3 ASD mouse models](findings/42010670.md) - Mol Autism | Score: 24/50 | nNOS inhibition reverses convergent cortical proteomic changes across two ASD models
- [Liu et al. 2026 — SHANK3 phase-separated condensates recruit CaMKII during LTP](findings/42009682.md) - Nat Commun | Score: 20/50 | Autism-linked SHANK3 InsG3680 mutation disrupts condensate dynamics and PSD remodeling

### REVIEW (1 paper)
- Joo et al. 2026 (PMID 42011000) - Korean ID psychiatric comorbidity trends 2012-2021 | Score: 11/50 | Epidemiology only, no variant data

### SKIP (2 papers)
- Bereda et al. 2026 (PMID 42016254) - Camel milk review (tangential autism mention)
- Vahamaki et al. 2026 (PMID 42010886) - Finnish Fuchs corneal dystrophy TCF4 (ocular, not NDD)

### Notes
- bioRxiv/medRxiv searches for recent_days=1 returned zero results across all four categories (genetics, neuroscience, genomics, medrxiv).

## 2026-04-23 Daily Scan

### INTEGRATE (1 paper)
- [Wang et al. 2026 — Cell-type-specific genetic architecture of neuropsychiatric disorders (sc-eQTL + SMR, includes ASD)](findings/42020718.md) - Mol Psychiatry | Score: 37/50 | 345 cell-type-specific risk genes across 6 disorders; brain risk genes more cell-type specific than blood; shared synaptic + immune pathways

### SKIP (1 paper)
- Bereda et al. 2026 (PMID 42016254) - Camel milk functional food review (tangential autism mention, no genetics)

### Notes
- bioRxiv/medRxiv searches for recent_days=1 returned zero results across all four categories (genetics, neuroscience, genomics, medrxiv).
- Only 2 PubMed hits total across all four queries for the 24-hour window.


## Daily Scan -- 2026-04-24

- [A single-cell multiomic analysis identifies molecular and gene-regulatory mechanisms dysregulated in developing Down syndrome neocortex](./findings/42024758.md) -- Vuong CK et al., Science 2026-04-23 (score 42)
- [Autism Spectrum Disorder Caused by a Novel De Novo SCN2A Mutation: A Case Report](./findings/42023993.md) -- Gao J et al., Int J Dev Neurosci 2026-04 (score 19)
- [Linked origins but distinct roles for extreme length and sequence variation at a tandem repeat in CACNA1C](./findings/10.64898_2026.04.23.720446.md) -- Song J et al., bioRxiv 2026-04-23 (score 29)
- [Pubertal development and hypothalamic-pituitary-gonadal axis are altered in male mice lacking Mecp2](./findings/10.1101_2025.08.19.671012.md) -- Martin-Sanchez A et al., bioRxiv 2026-04-24 (score 18)
- [Tbx1 Heterozygosity in the Oligodendrocyte Lineage Shifts Myelinated Axon Composition in the Mouse Fimbria Without Behavioral Impairments](./findings/10.64898_2025.12.30.697076.md) -- Wells AM et al., bioRxiv 2026-04-24 (score 17)
- [The landscape of regional missense mutational intolerance quantified from 730,947 exomes](./findings/10.1101_2024.04.11.588920.md) -- Wang L et al., bioRxiv 2026-04-23 (score 21)

## Daily Scan -- 2026-04-29

- [Connecting polygenic disease risk to cell states and regulatory programs through single-cell chromatin accessibility (SCADS)](./findings/10.64898_2026.04.27.721080.md) -- Yu L et al., bioRxiv 2026-04-28 (score 30)
- [Identification of a Novel Homozygous SCN1B Splice-Site Variant in a Consanguineous Families With Early-Onset Epilepsy](./findings/42046183.md) -- Muhammad A et al., Mol Genet Genomic Med 2026-05 (score 23)

## Weekly Deep Scan -- 2026-05-03

New tool added: [BRAIN-MAGNET](./tools/BRAIN-MAGNET.md) (Cell 2026, PMID 41265437) -- candidate flagged for review.

No new public autism dataset deposits identified across PubMed and bioRxiv genomics/genetics/neuroscience + medRxiv genetics queries (window 2026-04-26 to 2026-05-03).

URL spot-check (5/30 entries verified): all primary URLs reachable -- chip-atlas.org, brainspan.org, gene.sfari.org, epi25.broadinstitute.org, dx.doi.org/10.1038/s41467-025-61184-4. No broken links in this sample.

Wiki gene-page gaps flagged (atlas gene set vs. existing pages): missing pages for GRIN2B, SYNGAP1, RBFOX1, CACNA1A, KCNB1, SLC6A1, MECP2, MYT1L, EP300, BCL11A, ADNP, ARID1B, PCDH19, GRIN2A, STXBP1, WAC, AUTS2, RBBP5. Several have multiple findings already linked to them and warrant backfill.

## Recent Findings (Daily Scan)

*Updated 2026-05-06*

- [A framework to infer de novo exonic variants when parental genotypes are missing enhances association studies of autism.](./findings/42082430.md) -- Random Draw framework infers de novo exonic variants in autism cohorts when parental data are missing; increases gene discovery power.
- [Prefrontal Cortex 5-HT1A Receptor-Coupled Inwardly Rectifying Potassium Channels Decreased Seizure Susceptibility in Rat](./findings/42084135.md) -- In a VPA rat ASD model, 5-HT1A activation reduces seizure susceptibility through Kir3 channel-mediated hyperpolarization in PFC.
- [Reduced dorsal CA1 Activity Limits Retention of the Temporal Component of Declarative Memory in the Cntnap2 Knockout Mou](./findings/10.1101_2024.10.29.620866.md) -- Cntnap2 KO mice show reduced dorsal CA1 activity that limits temporal memory retention; cell-type-specific functional consequence of CNTNAP2
- [Multi-omics profiling reveals MAGEL2-driven defects in human corticogenesis shared across Prader-Willi and Schaaf-Yang s](./findings/10.64898_2026.05.01.722223.md) -- Multi-omics shows MAGEL2 drives shared corticogenesis defects across PWS and Schaaf-Yang; latter has high autism penetrance.
- [Pten Orchestrates Neurogenic Radial Glia Lineage Progression and Tunes Neocortical Astrocyte Production](./findings/10.64898_2026.05.01.722191.md) -- PTEN orchestrates radial glial progenitor lineage and tunes neocortical astrocyte production; cell-type context for PTEN-autism syndrome.
- [Neural signatures of impaired semantic contextualization in Autism Spectrum Disorder](./findings/10.64898_2026.03.16.712048.md) -- Intracranial recordings show impaired semantic contextualization in ASD, supporting predictive coding/contextual integration models.
- [The contribution of short tandem repeats to splicing variation in the human cortex](./findings/10.64898_2026.05.04.721407.md) -- STRs contribute to splicing variation in human cortex; an underexplored class of noncoding regulatory variants relevant to psychiatric disea
- [Determinants of functional burden pleiotropy and gene dosage responses across human traits](./findings/10.1101_2025.02.25.25322833.md) -- Cross-trait analysis of gene dosage effects relevant to comorbidities in pediatric and psychiatric disorders.
- [Cell-type-resolved genetic regulatory variation shapes inflammatory bowel disease risk](./findings/10.1101_2025.06.24.25330216.md) -- cis-eQTL mapping across 2.2M single cells in IBD shows cell-type-resolved regulatory effects of noncoding variants; methodological template 

## Daily scan 2026-05-08
- [42093631](findings/42093631.md) -- Glessner et al. 2026, *Brain*. CNV burden in GRM-interacting networks (DLG2, NRXN1, SHANK3, SYNGAP1) enriched in ADHD with comorbid NDDs vs. ADHD-only. (INTEGRATE, score 35)
- [42100732](findings/42100732.md) -- Shadrina et al. 2026, *Front Neurosci*. CNTN6 review: CNV/GWAS associations across ASD, ID, TS, SCZ; cell adhesion / neurite guidance functions. (INTEGRATE, score 19)

## Daily scan 2026-05-13

### INTEGRATE (3 papers)
- [42124619](findings/42124619.md) -- Jiang J et al. 2026, *bioRxiv*. SYNGAP1 PDZ ligand motif disruption accelerates iPSC-derived GABAergic neuron differentiation; extends SYNGAP1 phenotype to inhibitory neurons. (INTEGRATE, score 30) | Genes: SYNGAP1
- [42123666](findings/42123666.md) -- Vinci M et al. 2026, *Int J Mol Sci*. Trio WES case report of ASD+epilepsy female; likely-pathogenic de novo USP24 variant plus 2 paternally inherited VUS; cumulative-variant model. (INTEGRATE, score 22)
- [42125456](findings/42125456.md) -- Miyahara K et al. 2026, *Front Psychiatry*. Postmortem brain study tests ASD-PRS/ADHD-PRS against antipsychotic responsiveness in schizophrenia; trends did not survive multiple-testing correction. (INTEGRATE, score 22)

### REVIEW (6 papers)
- PMID 42119734 -- Rodulfo-Cardenas et al. 2026, *Neurotoxicology*. Postnatal PM exposure alters Grin2b/Reln expression in apoE3/apoE4 mice; sex- and genotype-dependent. (Score 14) | Genes: GRIN2B
- PMID 42119900 -- Li et al. 2026, *Behav Brain Res*. LDSC+MR identifies TCF4 and DCC in shared MCP-MDD genetic architecture. (Score 13) | Genes: TCF4
- PMID 42116390 -- Luo et al. 2026, *Medicine*. RCT of trampoline exercise vs resistance training reduces anxiety in mild-to-moderate ASD. (Score 13)
- PMID 42125453 -- Wang et al. 2026, *Front Psychiatry*. Own-name ERP atypicalities in ASD toddlers. (Score 13)
- PMID 42124397 -- Raji et al. 2026, *Autism Res*. Longitudinal eye-tracking visual search in ASD; lower accuracy at 3-year follow-up. (Score 12)
- PMID 42119675 -- Koutourlou et al. 2026, *J Neurosci Methods*. Adapted in ovo RNAi protocol for chicken cerebellum NDD gene studies. (Score 10)

### SKIP (1 paper)
- PMID 42125771 -- Murtough et al. 2026, *Br J Clin Pharmacol*. ACKR1/Duffy-null clozapine pharmacogenomic guideline (not autism). (Score 4)

### Notes
- PubMed query "autism AND epilepsy AND (GABA OR glutamate OR ion channel) AND genetics" returned zero results in the 24-hour window.
- bioRxiv/medRxiv direct API access was blocked in this run; preprint coverage limited to those indexed via PubMed (1 bioRxiv preprint captured: SYNGAP1 paper PMID 42124619).
