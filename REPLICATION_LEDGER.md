# Autism Regulatory Variant Atlas — Replication Ledger

Every major claim this project tested, with where it was first seen, where it was retested, whether it held, and its current evidence tier. Records failures and corrections as first-class entries. Literature anchors (published findings not tested here) are labeled sourceType='literature-anchor'.

_Last updated: 2026-07-07_

**Evidence tiers:** A = properly nulled, survives · A- = survives with caveats · B = real but not gene-set-specific · C = descriptive · D = corrected/falsified · E = inconclusive/underpowered · established = published anchor.

## Survived testing

| Claim | Category | First observed | Replication result | Tier | Takeaway |
|---|---|---|---|---|---|
| Gene pairs with a direct regulatory edge are more co-disrupted in ASD brain than other NDD gene pairs. | regulatory edge | GSE28521 / ASD postmortem cortex — cross-reg pairs rho=0.158 vs non-cross-reg NDD 0.082 | same, permutation null: HELD (MWU p=0.006, permutation p=0.021) | A | The strongest surviving finding. Specific regulatory wiring, not just NDD membership, predicts co-disruption. |
| Individual regulatory edges between NDD transcription factors and ion-channel genes are stronger than both random genes and other NDD genes for the same targets. | regulatory edge | TruthSeq (internal, on Replogle K562 + comparators) — 5/10 edges supported, mean 77.5th pctl vs null 25-26th | vs 7,639 random knockdowns: HELD (p=0.0) · vs 18 other NDD genes: HELD (p=0.0) · K562 expression-confound check: HELD (n_sig p=0.82, median|Z| p=0.60 — confound ruled out) | A | Tests individual edge strength, NOT network-level convergence. The wiring between specific gene pairs is real and specific; a coordinated cascade is a separate, unproven claim. |
| The FOXP2/HDAC4 regulatory module carries excess de novo variants in autism. | common/rare variant burden | denovo-db — 6 observed / 1.908 expected = 3.15x | 10K permutations + leave-one-out + controls: HELD (p=0.0001, leave-one-out robust, 0 in controls) | A | Independent of the GPF signal that later collapsed (uses denovo-db). |
| A TCF4 enhancer variant is supported as regulatory by multiple independent methods. | regulatory element | multi-tool (Hi-C, FLARE, ENCODE4 rE2G, Evo2, BRAIN-MAGNET, AlphaGenome) — 6 methods converge (FLARE 98.5th, BRAIN-MAGNET 98.8th, rE2G 0.797) | each method independent: HELD (6/6 concordant) | A | Convergent orthogonal support; the single best-validated regulatory element in the project. |
| MEF2C haploinsufficiency preferentially dysregulates other NDD transcription factors in patient organoids. | cross-dataset convergence | Lipton/Trudler 2024 MEF2C organoids — 6/16 network genes vs 4/107 non-network, Fisher p=0.0003, permutation p=0.0002 | Paulsen 2023 CHOOSE (36 KOs): FAILED (MEF2C-specific; knocking out FOXP1/MYT1L/BCL11A/MECP2 does NOT reproduce the cross-regulation) | A | Real and properly nulled, but it is MEF2C-specific — a topological property of where MEF2C sits, not a general cascade among the genes. |

- **Gene pairs with a direct regulatory edge are more co-disrupted in ASD ** — sources: Voineagu 2011 GSE28521 (PMID 21614001)  
- **Individual regulatory edges between NDD transcription factors and ion-** — sources: TruthSeq project (internal)  
- **The FOXP2/HDAC4 regulatory module carries excess de novo variants in a** — sources: denovo-db (PMID 27899662)  
- **A TCF4 enhancer variant is supported as regulatory by multiple indepen** — sources: ENCODE / brainSCOPE context (PMID 38781369)  
- **MEF2C haploinsufficiency preferentially dysregulates other NDD transcr** — sources: Lipton/Trudler 2024 (PMID 39349966); Paulsen 2023 CHOOSE (PMID 37704762)  

## Real but not specific to the gene set

| Claim | Category | First observed | Replication result | Tier | Takeaway |
|---|---|---|---|---|---|
| Ion-channel disruption is a common downstream endpoint across many autism/NDD gene knockouts. | cross-dataset convergence | mouse perturb-seq / 22 syndrome genes — rho=0.314, p<0.0001 | Pasca/Geschwind 2026: HELD (KCNA2 hit by 7/9 mutations at Day 25; multiple Ca/Na channels early) · specificity check: FAILED (not specific to any particular upstream gene set) | B | Robust and replicated as a convergence endpoint, but it happens for essentially any NDD gene knockout — it does not single out a special upstream network. |
| MECP2 is a common downstream casualty of diverse upstream autism mutations. | cross-dataset convergence | Pasca/Geschwind 2026 — 5/9 mutations disrupt MECP2 at Day 25, mostly down | specificity check: HELD (real cross-mutation signal, but not specific to any particular gene set) | B | MECP2 goes down regardless of which upstream gene is hit — a convergent casualty, not evidence for a specific cascade. |
| The core network genes are disrupted together in ASD postmortem brain. | cross-dataset convergence | Wamsley scGENE 2024 (ASD brain) — network genes disrupted, p=0.032 vs random | vs other NDD TF sets: FAILED (other NDD TF sets show equal/greater convergence with the same ion-channel targets) | B | Real disruption, but nothing distinguishes this network from other NDD gene sets. 'Consistent with,' not 'validates.' |
| The core network is preferentially disrupted in dup15q organoids. | cross-dataset convergence | Perez dup15q 2025 — 83% direction match with idiopathic ASD | breadth test: FAILED (network at 52nd percentile — not preferentially disrupted) | B | Direction concordance is real but the network is not preferentially hit; it sits at chance for breadth. |

- **Ion-channel disruption is a common downstream endpoint across many aut** — sources: Pasca/Geschwind 2026 (PMID 41611887)  
- **MECP2 is a common downstream casualty of diverse upstream autism mutat** — sources: Pasca/Geschwind 2026 (PMID 41611887)  
- **The core network genes are disrupted together in ASD postmortem brain.** — sources: Wamsley scGENE 2024 (10.1126/science.adh2602)  
- **The core network is preferentially disrupted in dup15q organoids.** — sources: Perez dup15q 2025 (PMID 40615364)  

## Partially failed

| Claim | Category | First observed | Replication result | Tier | Takeaway |
|---|---|---|---|---|---|
| Predicted downstream effects match observed direction in CHOOSE inhibitory-lineage neurons. | cross-dataset convergence | Paulsen 2023 CHOOSE — 10/11 predictions match, p=0.019 | same, full sign test: PARTIAL (overall 13/27 p=0.72; excitatory shows opposite direction) | A-minus | Signal is real only in the inhibitory lineage; the excitatory lineage points the other way, so the overall prediction does not hold. |
| The core gene set is enriched for common ASD GWAS signal. | common variant / heritability | iPSYCH-PGC ASD GWAS (Grove 2019) — 11.57% vs 6.81% baseline, 1.70x, p=0.019 | 13-gene set / gene-set swap: PARTIAL (weakens to p=0.061; 5-gene swap flips significance) | A-minus | Gene-set-sensitive — the result flips depending on which genes are included. Classic fragility. |
| The core genes are unusually developmentally co-expressed in fetal brain. | developmental co-expression | BrainSpan — mean coupling 99.1st percentile | 10K permutations of high-pLI brain genes + BH correction: PARTIAL (p=0.018, fragile under BH across 8 findings; subset selection unclear) | A-minus | Borderline and fragile; the 5-gene subset selection may be post-hoc. Demoted A→A- in the April 2026 audit. |
| GABA receptors drive epilepsy and glutamate receptors drive autism, as receptor classes. | receptor-type separation | CHOOSE + Epi25 cross-condition — glutamate convergent in autism, GABA burdened in epilepsy, apparent zero overlap | class-level test (Epi25): FAILED (epilepsy MWU p=0.189) · class-level test (autism): FAILED (OR=3.39, p=0.113) · falsifier: GRIN2A: FAILED (GRIN2A (glutamate) significant epilepsy burden p=0.009 — breaks glutamate=autism) | D | The class-level separation did not hold. What survives is a small set of specific shared genes (SCN2A, KCNB1, PCDH19, GRIN2A) that span both conditions. Reframed accordingly. |

- **Predicted downstream effects match observed direction in CHOOSE inhibi** — sources: Paulsen 2023 CHOOSE (PMID 37704762)  
- **The core gene set is enriched for common ASD GWAS signal.** — sources: Grove 2019 (iPSYCH-PGC) (PMID 30804558)  
- **The core genes are unusually developmentally co-expressed in fetal bra** — sources: BrainSpan (PMID 24695229)  
- **GABA receptors drive epilepsy and glutamate receptors drive autism, as** — sources: Epi25 (PMID 38212586); Paulsen 2023 CHOOSE (PMID 37704762)  

## Failed to replicate / corrected

| Claim | Category | First observed | Replication result | Tier | Takeaway |
|---|---|---|---|---|---|
| Multiple autism-gene knockouts converge on the same specific downstream bottleneck genes (KCNIP4, DLGAP1, GRIK1, etc.). | cross-dataset convergence | Paulsen 2023 CHOOSE — 65 genes hit by 5+ perturbations, 9/65 neuro-signaling, OR=9.36 p<0.0001; glutamate receptors OR=45.7 | Pasca/Geschwind 2026: FAILED (OR=1.01, p=0.52 — zero of 10 key genes reached significance) · Jin 2020: FAILED (all controlled p>0.64 — no specificity vs other neuronal genes) | D | The convergence PHENOMENON is real in all three datasets, but the SPECIFIC genes that converge differ every time. There is no universal bottleneck gene list. This is the project's central negative result. |
| Population-level regulatory-variant enrichment validates the core network (3.4x, p=0.00055). | common/rare variant burden | GPF / SFARI genotype browser — 3.4x enrichment, p=0.00055 | CADD rescoring: FAILED (0/9 families survive; driven by an HDAC4 + chromatin-loop artifact) | D | Collapsed entirely on rescoring. An artifact, not a signal. One of the project's key confirmation-bias corrections. |
| CUX1 is a master regulator driving the autism cell-type program. | regulatory topology | brainSCOPE GRN / cell-type DEGs — drives 64% of key cell-type DEGs | genome-wide + LDSC: FAILED (targets 17.8% of ALL genes; LDSC p=0.31 — not a specific autism regulator) | D | The 64% figure reflects CUX1's enormous target breadth, not autism specificity. Its breadth could still be mechanistically relevant, but the 'master autism regulator' claim is falsified. |
| MEF2C regulates roughly half of all autism genes (a uniquely powerful hub). | regulatory topology | brainSCOPE GRN — presented as dominant hub | ranked vs all TFs: FAILED (#259/644 TFs (1.30x); 4 other TFs cover more) | D | MEF2C is unremarkable by raw target count. Its importance is topological (where it sits), not quantitative — a distinction the project now keeps strict. |
| The proband carries pathogenic coding variants in MEF2C / DYRK1A / EP300. | proband variant | GeneDx WES + WGS re-read — reported frameshifts / deletion | population frequency + zygosity check: FAILED (MEF2C 'frameshifts' both intronic (one AF 42%); DYRK1A variant homozygous in father; EP300 deletion part of a common haplotype) | D | All were common or benign. Reinforces the project's starting point: the proband's exome is negative, and inherited/common variation is where the model lives. |
| Seven shared transcription factors regulate all five core genes. | regulatory topology | PsychENCODE GRN — 7 TFs regulate all 5 | brain expression check: FAILED (only 1 (TBX20) shows the expected brain pattern; 4/7 not expressed) | D | Most of the 'shared regulators' are not expressed in brain. Computational inference without an expression filter. |
| Molecular disruption magnitude tracks clinical autism severity. | phenotype | multiple datasets, 16 metrics — tested across 16 metrics | 16 metrics: FAILED (all p>0.10) | B | A clean, publishable negative: molecular disruption magnitude does not predict severity across any of 16 metrics tested. |

- **Multiple autism-gene knockouts converge on the same specific downstrea** — sources: Paulsen 2023 CHOOSE (PMID 37704762); Pasca/Geschwind 2026 (PMID 41611887); Jin 2020 (PMID 33243861)  
- **Population-level regulatory-variant enrichment validates the core netw** — sources: GPF / SFARI  
- **CUX1 is a master regulator driving the autism cell-type program.** — sources: brainSCOPE (PMID 38781369)  
- **MEF2C regulates roughly half of all autism genes (a uniquely powerful ** — sources: brainSCOPE (PMID 38781369)  
- **The proband carries pathogenic coding variants in MEF2C / DYRK1A / EP3** — sources: Genetic re-eval 2026-06 (internal)  
- **Seven shared transcription factors regulate all five core genes.** — sources: PsychENCODE GRN (PMID 30545857)  
- **Molecular disruption magnitude tracks clinical autism severity.** — sources: Internal severity analysis  

## Inconclusive (underpowered / proxy)

| Claim | Category | First observed | Replication result | Tier | Takeaway |
|---|---|---|---|---|---|
| Cross-regulatory wiring creates compounding (amplifying) vulnerability across the network. | cascade | CHOOSE + perturbation modeling — presented as compounding vulnerability | 62 perturbations: INCONCLUSIVE (p=0.31; ~33% power at d=0.5; CHOOSE 86% zeros (uninformative); right experiment not done) | E | Tested three times, never demonstrated — but the data are too underpowered to call it falsified. The proper experiment (multi-gene partial knockdown in a sensitized background) has not been run. |
| The core genes are uniquely co-regulated by shared upstream factors. | regulatory topology | brainSCOPE / SFARI permutations — 77th percentile vs random SFARI sets | SFARI permutation: INCONCLUSIVE (p=0.24; positive trend, not significant; proxy tests 'more shared TFs' not 'coordinated regulation') | E | A positive trend that never reaches significance, using a proxy for the real question. Not support, not falsification. |
| The core regulatory programs carry common-variant ASD heritability. | common variant / heritability | GWAS summary stats + regulon annotations — tested per gene program | LDSC: INCONCLUSIVE (TCF4 p=0.84, MEF2C p=0.93, EP300 p=0.29 — all null, but LDSC underpowered for small gene-set annotations) | E | All null, but LDSC needs thousands of SNPs to have power; small gene-set annotations can't be tested this way. A method-power limit, not demonstrated absence. |

- **Cross-regulatory wiring creates compounding (amplifying) vulnerability** — sources: Paulsen 2023 CHOOSE (PMID 37704762)  
- **The core genes are uniquely co-regulated by shared upstream factors.** — sources: brainSCOPE (PMID 38781369)  
- **The core regulatory programs carry common-variant ASD heritability.** — sources: Grove 2019 GWAS (PMID 30804558)  

## Descriptive

| Claim | Category | First observed | Replication result | Tier | Takeaway |
|---|---|---|---|---|---|
| Common regulatory-variant burden at NDD genes is correlated/structured in the population (and elevated in the proband). | common variant / heritability | 1000 Genomes (633 Europeans), ChromBPNet scoring — 3,490 LD-pruned variants across 20 gene regions | binomial/pathway null: FAILED (burden segregates independently (obs/exp 1.0-1.6x); pathway rho ~0.01; proband 0/10 genes in bottom 5%) | C | Negative in this specific design, but the design had no ASD cases, used monogenic (not GWAS) genes, adult brain models, and a tiny sample. Does NOT weigh against common noncoding variants in autism — see literature anchors below. |

- **Common regulatory-variant burden at NDD genes is correlated/structured** — sources: ChromBPNet population scoring (internal)  

## Literature anchors (not tested here)

| Claim | Category | First observed | Replication result | Tier | Takeaway |
|---|---|---|---|---|---|
| Common inherited variation accounts for the majority of autism heritability (~52% of liability). | common variant / heritability | Gaugler et al. 2014, Nature Genetics — narrow-sense h2 ~52%; common inherited ~49% of variance; rare de novo ~2.6% | published, widely cited: HELD (established) | established | The anchor for why the project studies inherited/common variation. Rare de novo variants have large individual effect but small population contribution; common inherited variation carries the bulk of heritability. |
| All genome-wide-significant ASD GWAS loci are noncoding/regulatory. | common variant / heritability | Grove et al. 2019, Nature Genetics (18,381 ASD cases) — 5 genome-wide-significant loci, all noncoding; SNP-h2 explains ~12% of liability so far | published, larger GWAS ongoing: HELD (established; implicated genes (KCNN2, KMT2E, PTBP2, MACROD2) do not overlap the monogenic NDD set) | established | Supports a regulatory/noncoding architecture for common ASD risk, and shows the common-variant genes differ from the monogenic NDD genes the project's own tests focused on. |
| Most monogenic NDD genes are eQTL-free in developing brain, but a subset carries prenatal-specific, expression-reducing regulatory variation. | common variant / heritability | BrainVar / Werling 2020 (176 DLPFC samples) — 27/39 NDD genes zero eQTLs; 12 have prenatal-specific/trending, expression-reducing eQTLs (e.g. MECP2 prenatal p=6.25e-5 beta=-0.371; EP300 p=8.87e-7 beta=-0.41) | project analysis of BrainVar: HELD (prenatal effects invisible in adult GTEx) | established | Marks the 12 genes where rare (monogenic) and common (regulatory) mechanisms both plausibly operate, and shows adult-brain models (like the project's ChromBPNet test) miss prenatal effects. |

- **Common inherited variation accounts for the majority of autism heritab** — sources: Gaugler et al. 2014, Nat Genet (PMID 25038753)  
- **All genome-wide-significant ASD GWAS loci are noncoding/regulatory.** — sources: Grove et al. 2019, Nat Genet (PMID 30804558)  
- **Most monogenic NDD genes are eQTL-free in developing brain, but a subs** — sources: Werling et al. 2020, Cell Reports (BrainVar) (PMID 32937128)  
