---
title: MEF2C Gene
last_updated: 2026-04-04
evidence_tier: A
type: gene
---

# MEF2C

## Overview

MEF2C (Myocyte Enhancer Factor 2C) is a transcription factor that acts as a network hub with a unique topological position in autism-related gene networks. Its loss reverberates through multiple neurodevelopmental disorder (NDD) transcription factors, making it a critical node in autism-associated regulatory circuits.

## Role and Function

**Network Hub:** MEF2C occupies a central position in NDD transcription factor networks, suggesting it coordinates regulation of downstream gene expression programs.

**Cascading Effects:** Perturbation of MEF2C affects expression of multiple related NDD transcription factors, indicating its role as an upstream regulator.

## Key Findings

### MEF2C-Specific ORC Network Dysregulation

**Finding:** MEF2C haploinsufficiency in patient-derived organoids preferentially dysregulates ORC (Oligodendrocyte Regulation Circuit) network members.

**Effect Size:**
- ORC network members dysregulated: 6/16 (37.5%)
- Non-ORC NDD genes dysregulated: 4/107 (3.7%)
- Fisher's exact p = 0.0003

**Mechanism:** All ORC hits show compensatory upregulation in neuronal cell types, suggesting a coordinated regulatory response.

### MEF2C-Specific Effect

This dysregulation pattern is **MEF2C-specific**. Other tested NDD genes do not produce the same cross-regulation pattern:

- FOXP1 knockout: Does NOT show ORC-specific dysregulation
- MYT1L knockout: Does NOT show ORC-specific dysregulation
- BCL11A knockout: Does NOT show ORC-specific dysregulation
- MECP2 knockout (CHOOSE dataset): Does NOT show ORC-specific dysregulation

This specificity indicates that MEF2C's role in ORC regulation is not a general feature of NDD transcription factor perturbations.

## Evidence Quality

**Evidence Tier: A** -- Properly nulled finding. The dysregulation pattern was tested against the null hypothesis that other NDD gene knockouts would show similar effects. MEF2C's specificity survived this test and is citable as evidence of genuine mechanistic distinctiveness.

## Datasets

- [Lipton 2024](../datasets/Lipton_2024.md) -- Patient-derived organoids with MEF2C haploinsufficiency
- [Paulsen 2023 CHOOSE](../datasets/CHOOSE.md) -- Multiplexed perturbation screen including MEF2C
- [Pasca 2026](../datasets/Pasca_2026.md) -- Organoid validation cohort

## Cross-Links

**Directly interacting genes:**
- [SCN2A](./SCN2A.md) -- Convergent target of MEF2C and other autism gene perturbations
- [FOXP1](./FOXP1.md) -- Related NDD transcription factor; does NOT show MEF2C-like ORC dysregulation
- [TCF4](./TCF4.md) -- Related transcription factor in autism networks
- [BCL11A](./BCL11A.md) -- NDD transcription factor; tested and negative for ORC-specific effects
- [MYT1L](./MYT1L.md) -- NDD transcription factor; tested and negative for ORC-specific effects
- [CDKL5](./CDKL5.md) -- Related NDD gene in broader autism-epilepsy network

**Related Concepts:**
- [Evidence Tiers](../concepts/evidence_tiers.md) -- How this finding achieved Tier A status
- [Convergence Phenomenon](../concepts/convergence_phenomenon.md) -- Why MEF2C's specificity matters for understanding network effects

## Sources

- Lipton, J. et al. (2024). MEF2C haploinsufficiency and ORC network dysregulation in autism patient-derived organoids. *Nature Neuroscience*.
- Paulsen, B. et al. (2023). CHOOSE: Large-scale multiplexed perturbation screen of autism risk genes. *Cell Genomics*.
- Pasca, S. P. et al. (2026). Organoid validation of autism transcription factor networks. (in preparation)

---

**Last Updated:** 2026-04-04
**Evidence Tier:** A (Properly nulled)
