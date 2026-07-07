---
title: Receptor Type Separation Model
last_updated: 2026-07-07
evidence_tier: D-partial
type: concept
status: PARTIALLY FAILED -- reframed around specific shared genes
---

# Receptor Type Separation Model

## Status: the clean class-level separation did not survive retesting (April 2026)

The original claim on this page -- GABA receptors drive epilepsy, glutamate receptors drive autism, as receptor *classes* -- did not hold up when tested properly. What survives is narrower and more defensible: a small set of *specific* genes carry signal in both conditions. The receptor-class story is retired as active framing; the individual shared-gene overlaps are real.

Do not cite the class-level separation downstream. Cite the specific shared genes.

## What was originally claimed (for history)

Cross-condition comparison of Epi25 rare-variant burden against CHOOSE autism-perturbation convergence appeared to show a clean split: GABA receptor genes (GABRB3, GABRG2, GABRA1) loaded on epilepsy with zero autism convergence, glutamate receptor genes (GRIK1/2, GRIA4, GRID2) loaded on autism convergence with zero epilepsy burden, and a handful of shared genes explained comorbidity. This was filed as Tier B in April 2026.

## What retesting showed (April 2026 reanalysis)

The separation was tested as a class-level property, with a stated null: if receptor *class* predicts condition, epilepsy burden should separate GABA from glutamate genes and autism association should separate the reverse. It did not.

- Epilepsy side, class-level: Mann-Whitney U p=0.189. Not significant. GABA vs glutamate genes do not separate on epilepsy burden as classes.
- Autism side, class-level: SFARI odds ratio 3.39, p=0.113. Not significant.
- The falsifier fired: GRIN2A, a glutamate receptor gene, carries significant epilepsy protein-truncating-variant burden (p=0.009). That directly breaks the "glutamate = autism, not epilepsy" claim.
- The apparent separation was driven by 4 specific genes, not by receptor class membership.

Base-rate note: with only a few genes per receptor class, a handful of strong individual genes can create the visual impression of class-level separation. Once tested against the null of "class predicts nothing beyond the individual genes," the class effect disappears.

## What survives: specific shared genes span both conditions

These individual genes carry real signal in both epilepsy and autism datasets. This is the defensible finding.

| Gene | Epilepsy signal | Autism signal |
|------|-----------------|---------------|
| SCN2A | DEE damaging-missense p=4.2e-4 (Epi25) | Convergent target (CHOOSE) |
| KCNB1 | DEE p=1.3e-3 / PTV p=4.6e-4 (Epi25) | Ion-channel convergence set |
| PCDH19 | PTV p=1.4e-3 / DEE PTV p=1.4e-5 (Epi25) | Convergent target (CHOOSE) |
| GRIN2A | PTV p=8.6e-3 / NAFE p=0.01 (Epi25) | Glutamate receptor family |

The claim these support is gene-specific, not class-specific: mutations in these particular genes are compatible with autism, epilepsy, or both. GRIN2A in particular sits on the glutamate side yet carries epilepsy burden, which is why the class framing fails.

## What would change this back

A clean class-level separation would need to replicate in an independent epilepsy cohort AND an independent autism perturbation screen, with the class effect surviving after removing the 4 driver genes. Until then, treat any "GABA = epilepsy / glutamate = autism" statement as unsupported.

## Evidence quality

Evidence Tier: D (partial) -- initially significant as Tier B, corrected in April 2026 when the class-level tests came back non-significant. The specific shared-gene overlaps remain Tier B (real in Epi25 + CHOOSE, not independently replicated).

## Datasets
- [Epi25 Consortium](../datasets/Epi25.md) -- rare variant burden in epilepsy
- [Paulsen 2023 CHOOSE](../datasets/CHOOSE.md) -- multiplexed perturbation screen in autism risk genes

## Cross-Links
- [SCN2A](../genes/SCN2A.md), [PCDH19](../genes/PCDH19.md), [KCNB1](../genes/KCNB1.md), [GRIN2A](../genes/GRIN2A.md) -- the specific shared genes that survive
- [Convergence Phenomenon](./convergence_phenomenon.md)
- [Evidence Tiers](./evidence_tiers.md)

## Sources
- Epi25 Collaborative. (2024). Exome sequencing of 20,979 individuals with epilepsy and 33,444 controls. *Nature Neuroscience*.
- Paulsen, B., Velasco, S., et al. (2023). Single-cell brain organoid screening identifies developmental defects in autism. *Nature* 621:788-797.
- Internal reanalysis, April 2026 (class-level separation test).

---
**Last Updated:** 2026-07-07
**Evidence Tier:** D (partial) -- class-level separation corrected; specific shared genes survive
