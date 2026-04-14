---
title: Evidence Tiers Classification System
last_updated: 2026-04-04
evidence_tier: C
type: concept
---

# Evidence Tiers Classification System

## Overview

The Evidence Tiers system classifies experimental findings by the rigor and specificity of the evidence supporting them. This classification helps distinguish between findings that are truly citable scientific claims versus observations that require further validation.

## Tier A: Properly Nulled

**Definition:** Tested against a meaningful null hypothesis AND survived the test.

**What This Means:**
- The finding is not just observed to be statistically significant
- An alternative explanation (null hypothesis) was explicitly tested
- The finding survived that test, demonstrating genuine distinctiveness or mechanism

**Citability:** Tier A findings are appropriate for direct citation in manuscripts and as evidence for mechanistic claims.

### Examples

**MEF2C ORC Dysregulation (Tier A):**
- Observation: MEF2C knockout causes ORC network dysregulation (6/16 genes, p=0.0003)
- Null hypothesis: Other NDD gene knockouts cause similar ORC dysregulation
- Test: Knocked out FOXP1, MYT1L, BCL11A, MECP2
- Result: None showed ORC-specific dysregulation
- Conclusion: MEF2C's effect is specific; claim is properly nulled and citable

**Common Variant Heritability (Tier A):**
- Observation: Common variants account for ~49% of autism liability
- Null hypothesis: Common variants contribute negligibly; heritability is from rare variants
- Test: Twin heritability studies, genetic correlation analyses
- Result: Null rejected; common variants explain more variance than rare variants
- Conclusion: Finding survives rigorous statistical testing; citable as high-confidence

## Tier B: Real but Not Specific

**Definition:** Statistically significant and reproducible in the reported dataset, but has NOT been tested for specificity or validated in an independent dataset.

**What This Means:**
- The finding is real within its context
- Rigorous statistical testing confirms non-random signal
- Either: (a) specificity not tested, or (b) not independently validated
- Suitable for hypothesis generation but requires caution in interpretation

**Citability:** Tier B findings can be cited as "found in Dataset X" but should not be claimed as universal or mechanistically established until validated.

### Examples

**SCN2A Autism Convergence (Tier B):**
- Observation: SCN2A is downregulated in CHOOSE when multiple autism genes are knocked out
- Statistical rigor: Yes, significant signal in CHOOSE
- Specificity test: Not done; no comparison to random targets
- Independent validation: Not done in Pasca or Jin datasets
- Status: Real in CHOOSE, unvalidated elsewhere
- Citation: "SCN2A shows convergent targeting in CHOOSE autism perturbation screen" (not "SCN2A is a convergent target of autism mutations")

**Receptor Type Separation (Tier B):**
- Observation: GABA receptors show rare variant burden in epilepsy; glutamate receptors in autism
- Statistical rigor: Yes, significant in Epi25 and CHOOSE
- Specificity test: Separation is meaningful but not mechanistically tested
- Independent validation: Not replicated in independent epilepsy and autism cohorts
- Status: Clean separation in Epi25+CHOOSE, untested in other datasets
- Citation: "In Epi25 and CHOOSE, GABA and glutamate receptors separate by condition" (not "GABA causes epilepsy and glutamate causes autism")

## Tier C: Descriptive

**Definition:** Observed in data without strong statistical claim; presents pattern or correlation worthy of investigation.

**What This Means:**
- No formal statistical test is claimed
- May be illustrative example, case study, or observed trend
- Valuable for hypothesis generation and visualization
- NOT suitable for causal claims or mechanistic interpretation

**Citability:** Tier C findings are appropriate in Methods sections, Results descriptions of exploratory analyses, and hypothesis generation sections. NOT appropriate as main evidence for mechanistic claims.

### Examples

**Convergence Phenomenon Observation (Tier C element):**
- Statement: "Multiple autism gene knockouts show overlapping transcriptional changes"
- Support: Described qualitatively across multiple studies
- Statistical test: Not formally applied (would need p-value, effect size)
- Status: Observed pattern; not statistically claimed
- Citation: Appropriate as "Convergence phenomenon has been observed across multiple studies" but not "The convergence phenomenon is statistically established at p<0.05"

**Ion Channel Dysregulation Pattern (Tier C element, though broader analysis is Tier B):**
- Statement: "Ion channels are commonly dysregulated in NDD gene knockouts"
- Support: Observed in multiple datasets qualitatively
- Statistical test: Need formal analysis (cross-correlation with p-values)
- Status: Observable pattern; level of rigor depends on statistical testing

## Tier D: Corrected/Withdrawn

**Definition:** Initially reported as significant but later corrected, retracted, or found to be non-robust.

**What This Means:**
- Finding was previously reported but has been superseded
- May have failed replication, had methodological errors, or been retracted
- Previous citations should note the correction

**Citability:** Should NOT be cited as evidence. If cited for historical context, must include note that finding was later corrected or withdrawn.

### Examples

**Hypothetical Example:**
- Initial report: "Gene X shows 5-fold upregulation in autism organoids, p=0.001"
- Later finding: Replication studies show no consistent upregulation; effect was artifact of batch
- Current status: Tier D (withdrawn)
- How to cite: "Gene X dysregulation was initially reported (Smith 2020) but not replicated in subsequent studies (Jones 2021, Brown 2022)"

## Tier Assignment Flowchart

```
Is the claim statistically tested?
├─ No → Tier C (Descriptive)
└─ Yes →
   ├─ Is there a null hypothesis test showing the finding survives challenge?
   │  ├─ Yes → Tier A (Properly Nulled)
   │  └─ No →
   │     ├─ Is there independent validation in a different dataset?
   │     │  ├─ Yes → Tier A or B (depends on consistency)
   │     │  └─ No → Tier B (Real but not specific)
   └─ Has the finding been contradicted?
      ├─ Yes → Tier D (Corrected/Withdrawn)
      └─ No → Continue evaluation
```

## Using Evidence Tiers in Practice

### In Manuscript Writing

- **Main evidence for claims:** Use Tier A findings
- **Supporting evidence:** Tier B is acceptable with appropriate caveats
- **Motivating hypotheses:** Tier C findings can motivate experiments
- **Never cite:** Tier D findings as evidence (only as historical context with corrections noted)

### In Atlas Curation

- **Gene pages:** Classify each finding by tier
- **Cross-links:** Include tier information when linking to dependent findings
- **Future work:** Flag Tier B findings needing validation
- **Methods:** Document what would be required to advance a Tier B finding to Tier A

### In Model/Algorithm Development

- **Training data:** Prefer Tier A findings
- **Features:** Tier B findings can be features if validated in independent test set
- **Hypothesis generation:** Tier C findings are appropriate
- **Validation:** Demonstrate that model predictions hold in independent data (Tier A validation)

## Cross-Links

**Related Concepts:**
- [Convergence Phenomenon](./convergence_phenomenon.md) -- Example Tier B finding awaiting validation
- [Receptor Type Separation](./receptor_type_separation.md) -- Example Tier B finding with clean patterns but no independent validation
- [Noncoding Variants in Autism](./noncoding_variants_in_autism.md) -- Example Tier A epidemiological findings

**Related Pages:**
- [MEF2C](../genes/MEF2C.md) -- Gene with Tier A mechanistic finding
- [SCN2A](../genes/SCN2A.md) -- Gene with Tier B findings

## Sources

This classification system is adapted from best practices in:
- Medical evidence grading (GRADE system)
- Replication science standards (Open Science Collaboration)
- Functional genomics validation standards

---

**Last Updated:** 2026-04-04
**Evidence Tier:** C (Descriptive classification system; not itself a empirical finding)
