---
title: RFX3 Gene
last_updated: 2026-04-10
evidence_tier: B
type: gene
---

# RFX3

## Overview

RFX3 (Regulatory Factor X3) is a transcription factor that has emerged as a central regulatory hub in autism, particularly in speech-related brain regions. It enhances CREB binding at the promoters of immediate early genes (IEGs), connecting chromatin accessibility to activity-dependent transcription. RFX3 is independently established as an autism gene through rare variant exome burden testing (FDR 3x10-7).

## Role and Function

**Transcription Factor:** RFX3 belongs to the RFX family of winged-helix transcription factors. In neurons, it enhances CREB-mediated transcription of immediate early genes -- the rapid-response genes that activate when neurons fire and are critical for learning and memory.

**CREB/CREBBP Connection:** RFX3 works through CREB binding, linking it to CREBBP (CREB binding protein), which is the functional partner of EP300. This places RFX3 upstream of an established autism gene network: RFX3 -> CREB/CREBBP -> EP300 -> activity-dependent transcription.

**Cell-Type Specificity:** RFX3's effects are concentrated in excitatory neurons, particularly deep-layer intratelencephalic (IT) neurons (L4/5 IT, L2/3 IT) in speech-related cortex (BA22). These are cortico-cortical projection neurons that integrate sensory input and distribute information across cortical networks.

## Key Findings

### RFX3 as Most Consistent Differentially Accessible Motif in Autism (Sanders BA22 2026)

**Finding:** In single-nucleus multiomics of BA22 from 100 donors, RFX3 motif accessibility was the most consistently altered signal across cell types.

**Details:**
- Increased RFX3 motif accessibility in cases vs controls (FDR < 0.05 in 6 cell types; P < 0.05 in 13 additional)
- RFX3 gene expression also increased in excitatory neurons
- Strongest effects in L4/5 IT1 and L2/3 IT neurons
- Consistent across all three comparisons: All cases, NDD/ASD only, ASD only

### Paradoxical IEG Downregulation

**Finding:** Despite increased RFX3 expression and motif accessibility, downstream immediate early genes (IEGs) are enriched among DEGs but many are downregulated.

**Interpretation:** This mirrors the compensatory pattern seen in Pasca 2026 idiopathic ASD organoids, where regulatory machinery was upregulated without downstream rescue. RFX3 may be attempting to compensate for reduced activity-dependent signaling, but the downstream programs remain disrupted.

### Verbal vs Non-Verbal Phenotype Association

**Finding:** RFX3 regulatory activity varies within the autism cohort by language phenotype.

**Details:**
- Differential eRegulon activity between verbal and non-verbal individuals in L2/3 IT3, L2/3 IT4, and L5 ET2 neurons
- Coordinated changes in RFX3 RNA expression, motif accessibility, and eRegulon activity
- Regulatory regions associated with these differences enriched in human-gained enhancers (HGEs) and primate-conserved regions linked to language

**Caveat:** Small sample sizes (~20-26 donors with verbal phenotype data). Interpret cautiously.

## Genetic Evidence

- **Rare variant burden:** FDR 3x10-7 in autism exome sequencing (Satterstrom/Fu et al., Nature Genetics 2022)
- **Gene family:** Other RFX members (RFX2, RFX4, RFX5) also show altered motif accessibility in NDD/ASD, though less consistently than RFX3

## Evidence Quality

**Evidence Tier: B** -- Real signal in a well-powered study (100 donors, ~500K nuclei, split-control design to avoid correlation inflation). The RFX3 motif accessibility finding is robust across comparisons and cell types. The verbal/non-verbal association is preliminary (small Ns). Not yet independently replicated in a second cohort.

## Datasets

- [Sanders BA22 2026](../../datasets.json) -- Primary source: BA22 multiomics, 100 donors
- [Satterstrom/Fu 2022](https://doi.org/10.1038/s41588-022-01104-0) -- Exome sequencing establishing RFX3 as autism gene

## Cross-Links

**Directly connected genes:**
- [EP300](./EP300.md) -- Connected through CREB/CREBBP pathway
- [MEF2C](./MEF2C.md) -- Both are upstream regulators with cell-type-specific effects in neurons
- [FOXP1](./FOXP1.md) -- Both show increased expression in NDD/ASD donors in BA22

**Related Concepts:**
- [Convergence Phenomenon](../concepts/convergence_phenomenon.md) -- RFX3 dysregulation is shared across genetically diagnosed and undiagnosed autism
- [Receptor Framework](../../structured/receptor_framework.json) -- RFX3 effects are concentrated in excitatory (glutamatergic) neurons

## Sources

- Suresh V, Wigdor EM, Hao Y, et al. Molecular dynamics of Brodmann Area 22 in development and autism. bioRxiv preprint, 2026.
- Satterstrom FK, et al. Exome sequencing of autism families. Nature Genetics. 2022;54:1104.
- RFX3 as regulator of IEGs via CREB: bioRxiv 2025.02.27.640588v1.

---

**Last Updated:** 2026-04-10
**Evidence Tier:** B (Real but requires replication)
