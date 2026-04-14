# Weekly Deep Scan Report: 2026-04-12

## Executive Summary

Quiet week for new autism-specific datasets in PubMed. One relevant PubMed paper found (AUTS2 base editing model). bioRxiv/medRxiv sweep identified 4 autism/NDD-relevant preprints worth noting (2 already captured by daily scans). No new GitHub tools discovered beyond what's already tracked. Wiki has structural gaps -- 6 gene pages referenced in index are missing files. All 29 backfill queue datasets remain at "not_started."

---

## Step 1: GEO/SRA Dataset Scan (PubMed)

**Date range searched:** 2026-04-05 to 2026-04-12 (entry date)

**Query 1** (autism + GEO/SRA/scRNA-seq/ATAC-seq/ChIP-seq + dataset): **0 results**

**Query 2** (autism + organoid/iPSC + RNA-seq/sequencing): **1 result**
- **PMID 41958697** -- Yan et al. 2026 -- "Base editing in the AUTS2 gene and high-throughput NGS genotyping of clones" (DOI: 10.18699/vjgb-26-04)
  - iPSC model using adenine base editing to introduce allele-specific markers in AUTS2
  - No new public dataset deposited (methodology paper)
  - Already captured in daily scan (2026-04-10, score 22/50)

**Query 3** (autism + WGS + cohort/family/trio): **0 results**

**New datasets discovered:** 0

---

## Step 2: bioRxiv/medRxiv Weekly Sweep

**Searched:** bioRxiv genetics (30 results), genomics (50 results), neuroscience (50 results); medRxiv (50 results). Date range: 2026-04-05 to 2026-04-12.

### Autism/NDD-Relevant Preprints Identified

**Already captured by daily scans:**
1. **Gupta et al. -- In vivo human embryonic spinal cord atlas validates stem cell-derived human dorsal interneurons and reveals ASD spinal signatures** (bioRxiv 10.64898/2025.12.22.696129, v2 2026-04-09). Already in atlas as findings/biorxiv_2025.12.22.696129.md (score 29).
2. **Li & Sossin -- FMRP Regulates Neuronal RNA Granules Containing Stalled Ribosomes** (bioRxiv 10.1101/2025.02.21.639553, v5 2026-04-08). Already in atlas as findings/10_1101_2025_02_21_639553.md (score 22).
3. **Qiu et al. -- Evolutionary transfer learning enables organism-wide inference of mammalian enhancer landscapes** (bioRxiv 10.64898/2026.04.07.717039). Already in atlas as findings/10_64898_2026_04_07_717039.md (score 32).
4. **Lee et al. -- Complementary vertebrate Wac models exhibit phenotypes relevant to DeSanto-Shinawi Syndrome** (bioRxiv 10.1101/2024.05.26.595966, v4). Already captured as findings/10.1101_2024.05.26.595966.md (score 16).

**New preprints not yet in atlas:**
5. **Schilder et al. -- "Genetic background shapes AI-predicted variant effects"** (bioRxiv 10.64898/2026.04.04.715328, genomics, 2026-04-07)
   - Relevance score: **18/50** (REVIEW)
   - Shows that variant effect predictions from models like ChromBPNet and Enformer change depending on which haplotype background the variant sits on
   - Direct relevance to our ChromBPNet scoring work -- variants scored against GRCh38 reference may miss effects present on other haplotype backgrounds
   - Methods-relevant but not autism-specific

6. **Harrison et al. -- "DNM1-related disorder is characterized by recurrent variants and phenotypic homogeneity"** (medRxiv 10.64898/2026.04.05.26350183, genetic and genomic medicine, 2026-04-06)
   - Relevance score: **15/50** (INTEGRATE threshold)
   - DNM1 = dynamin-1, presynaptic vesicle fission gene
   - Developmental and epileptic encephalopathy phenotype overlaps with Teagan's presentation
   - Largest DNM1 cohort compiled to date

7. **Kanagasingam et al. -- "Rare Variant Burden Analysis of Dystonia Genes in Parkinson's Disease"** (medRxiv 10.64898/2026.04.04.26349768, neurology, 2026-04-06)
   - Relevance score: **8/50** (SKIP)
   - Not autism-relevant, dystonia-PD overlap

**Counts:** INTEGRATE: 0 new (4 already captured), REVIEW: 2 new, SKIP: ~194

---

## Step 3: GitHub Tool Scan

**Searches performed:** 4 queries covering autism genomics, noncoding/regulatory variant prediction, polygenic scores + autism, and ChromBPNet/MPRA/VEP tools.

**New tools found this week:** 0 genuinely new tools

**Notable existing tools confirmed active:**
- **AlphaGenome** (google-deepmind/alphagenome) -- already in wiki as tools/AlphaGenome.md
- **variant-scorer** (kundajelab/variant-scorer) -- ChromBPNet-based variant scoring framework. Already known, not in wiki.
- **TraitGym** (songlab-cal/TraitGym) -- benchmarking DNA sequence models for causal regulatory variant prediction. Not yet in wiki.
- **VariantFormer** (czi-ai/variantformer) -- CZI deep learning framework for variant-to-expression prediction. Not yet in wiki.

**Recommendation:** Create wiki pages for variant-scorer, TraitGym, and VariantFormer as they're directly relevant to the atlas's noncoding variant analysis pipeline.

---

## Step 4: Cross-Reference Health Check

### Missing pages referenced in wiki/index.md

The index references these pages that **do not exist as files**:

**Gene pages missing (referenced in index but no file):**
- None currently missing -- all 9 gene pages (MEF2C, SCN2A, FOXP1, TCF4, CDKL5, SHANK3, CHD8, DYRK1A, RFX3) exist as files.

**Dataset pages with wiki pages:** 6 of 10 Phase 1 datasets have wiki pages:
- spark-wgs.md ✓
- sfari-base.md (MSSNG) ✓
- ssc.md ✓
- encode.md ✓
- gtex-brain.md ✓
- allen-brain-atlas.md ✓
- brainspan.md ✓
- psychencode-grn.md ✓
- epi25-wes.md ✓
- **Missing: ASC (Autism Speaks/Autism Sequencing Consortium) -- referenced in backfill queue but no wiki page**

**Findings pages:** All findings referenced in index.md exist as files. No broken cross-references found.

**Genes that should have pages but don't:**
Based on INTEGRATE papers this week mentioning genes tracked in the project:
- EP300 (referenced in CLAUDE.md as project gene, no wiki page)
- MECP2 (referenced in CLAUDE.md as project gene, no wiki page)
- MYT1L (referenced in CLAUDE.md as project gene, no wiki page)
- SYNGAP1 (paper scored 31/50, no gene page)
- AUTS2 (paper scored 22/50, no gene page)
- WAC (paper scored 16/50, no gene page -- DeSanto-Shinawi syndrome)

### Contradiction Check
No contradictory findings identified among current wiki pages. The receptor-type separation concept page should be checked to confirm it reflects the April 2026 partial failure (MWU p=0.189).

---

## Step 5: Backfill Progress

**Phase 1 (10 datasets):** 9 have wiki pages, 0 have data downloaded. All remain "not_started" in backfill_queue.json.
- Missing wiki page: ASC (Autism Sequencing Consortium)

**Phase 2 (7 datasets):** 0 have wiki pages, 0 have data downloaded. All "not_started."

**Phase 3 (6 datasets):** 0 have wiki pages, 0 have data downloaded.

**Phase 4 (6 datasets):** 0 have wiki pages, 0 have data downloaded.

**Total: 29 datasets queued, 0 started, 9/29 have wiki pages (all Phase 1).**

**Next highest-priority backfill targets:**
1. **Zhou et al. 2019 -- De novo regulatory mutations** (Phase 2) -- seminal noncoding variant paper, public data
2. **An et al. 2018 -- Autism WGS** (Phase 2) -- large-scale WGS family data
3. **ASC wiki page** (Phase 1) -- only Phase 1 dataset without a wiki page

---

## Step 6: Weekly Summary

| Category | Count |
|----------|-------|
| PubMed papers found | 1 |
| New datasets discovered | 0 |
| bioRxiv/medRxiv preprints screened | ~180 |
| Autism-relevant preprints (new) | 2 REVIEW |
| Autism-relevant preprints (already captured) | 4 INTEGRATE |
| New GitHub tools | 0 (3 existing tools need wiki pages) |
| Wiki health issues | 6 missing gene pages for project genes |
| Backfill progress | 0/29 datasets started |

### Notable Findings Worth Flagging

1. **Schilder et al. "Genetic background shapes AI-predicted variant effects"** -- Directly relevant to our ChromBPNet scoring pipeline. Demonstrates that variant effect predictions change based on haplotype background. Our scoring was done against GRCh38 reference only. This paper suggests effects we scored may be background-dependent. Worth reading in full.

2. **Daily scan captured a high-value paper this week**: Zhou et al. (PMID 41959448, score 43/50) on distinct DNA methylation mechanisms for common vs. rare noncoding ASD variants across 186 cell subtypes. This is the most relevant new paper of the week.

3. **DNM1 cohort paper** (Harrison et al.) -- developmental and epileptic encephalopathy phenotype similar to Teagan's. DNM1 is a presynaptic gene not currently in the project gene set but worth tracking.
