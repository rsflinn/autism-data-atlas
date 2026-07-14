# Decision record — the Autism Brain Atlas

**Last updated: 2026-07-13.** This document supersedes `REFRAME_PLAN_2026-07.md` and `DESIGN_BRIEF_REFRAME_2026-07.md` where they conflict. Read this first. If a decision below is contradicted anywhere else in the repo, this document wins.

This file exists because these decisions kept getting remade. They were settled in conversation and never written down, so every new working session re-litigated them from scratch. That stops here.

---

## 1. What the site is for

**A person points the tool at their own genomic data. The tool pulls their variants and searches them against what is publicly known — is this variant rare, has it been seen in autism, does it sit in anything that matters.** A custom search against published and public data, run on a real person's scan.

The audience, in order: a family that just got a negative exome and has nowhere to go; an independent researcher; a journalist.

The gap it addresses: clinical labs read the ~1–2% of the genome that codes for protein and leave the other 98% uninterpreted. There is no ClinVar for regulatory variants. Families get "negative exome" and nothing else.

## 2. What the site is NOT for

**Not a project to validate or replicate published research.** Retired 2026-07-13. That work can't be done better here than by the groups publishing it, and it serves neither families nor independent researchers.

The replication ledger (`replication_ledger.*`) stays live as an internal record of this project's own testing. It is **not the differentiator and not the product.** `REFRAME_PLAN_2026-07.md` calls it "genuinely the differentiator" — that line is stale and wrong.

**Do not propose replication or validation features.**

## 3. Privacy — the load-bearing constraint

**No one ever uploads their genome to this site. Not to a server, not to an API, not to a third party. Ever.**

This is not negotiable and not a nice-to-have. It removes HIPAA and compliance exposure entirely, and it is the only defensible posture for a one-person project handling other people's children's genomes.

Consequences that follow, and they are not optional:

- **The analysis runs on the user's machine.** Delivery mechanism: **browser-local (WebAssembly)** — the site loads the code, the user selects their file, the file is read locally by the browser and never transmitted. No install, no terminal, no upload. Decided 2026-07-13.
- **No live API calls on user variants at runtime.** The current pipeline in `reanalysis_2026-07/` calls the Ensembl VEP REST API and the AlphaGenome API per variant. **That architecture cannot ship.** Sending a family's variant coordinates to Ensembl is an upload, whatever we call it.
- **Annotation must be precomputed and served as static data.** We host frequency, consequence, regulatory-overlap and score data for a bounded set of autism-relevant regions. The browser fetches those static files and joins them to the user's variants locally.
- **Bounding the region set is therefore not a scoping choice, it's a physical requirement.** Genome-wide precomputed CADD is ~300 GB. A curated set of autism gene regions plus flanks and brain regulatory elements is a few hundred megabytes and shardable.

## 4. The honesty spine — this is the differentiator

Every consumer genetics product on earth is built to make you feel like it found something. This one is built to tell you when it didn't.

Three features carry that, and they are the product:

- **The base rate, always.** Everyone carries thousands of rare noncoding variants. A result is meaningless without the control distribution beside it: *"you carry 31 rare noncoding variants in these regions; a typical person carries 25–40."* No count is ever shown without its comparison.
- **Artifact flagging.** In the July scan, ~23 of 29 "rare" hits were indels in homopolymer and repeat runs — the standard signature of sequencing error, not biology. A naive tool shows those as findings. This one flags and demotes them.
- **Every score shown, no black-box number.** Rarity, consequence, regulatory overlap, CADD, SpliceAI, predicted brain effect, gene relevance — displayed side by side. They disagree with each other, and that disagreement is information. Collapsing them into one "autism score" would hide real uncertainty and would be dishonest.

"Nothing strong here" must be a valid, common, well-designed output. It will be the most frequent one.

### 4a. The control is not optional — added 2026-07-13, learned the hard way

The first working scan reported the proband at 10,135 rare noncoding variants against a European baseline of 442 — the 100th percentile, 23x normal. It was entirely false. Running her father through the identical pipeline returned 9,375. He is the control, and he is the only reason we know the tool was broken rather than the child.

The bug: rarity was defined against a filtered reference panel, so "absent from the panel" was silently read as "rare." That inflates every genome equally. Without a second genome to compare against, the error is invisible — it looks exactly like a finding.

**Therefore: the scan must never report a user's count without simultaneously running a control genome through the identical pipeline and reporting both.** Not a stored baseline number — a live control. If the tool cannot produce a sane control result, it must refuse to report the user's result at all.

This is not a nicety. A tool that tells a parent their child carries 23x the normal burden of rare variants in autism genes will send that family down months of a blind alley. We were one unrun control away from shipping exactly that.

### 4b. The metric is a ratio, not a count — established 2026-07-13 after three failed rebuilds

Three separate rebuilds of the scan, each fixing a real bug, each still failing the control gate: 23x → 4.4x → 2.0x. The conclusion is structural, not a bug to be found.

**Absolute rare-variant counts are not portable across sequencing pipelines.** A genome called with DRAGEN yields more variants than one called with GATK, and every public control cohort is GATK. In the final run the control's count of *real, catalogued, non-artifact* rare variants exceeded the entire median of the control cohort. No choice of reference panel repairs that, because the reference was never the problem — the count is dominated by whose software wrote the VCF.

**Therefore the headline metric must be a within-genome ratio:** rare-variant density in the autism gene regions divided by density in matched control genes, scored from the same VCF, same caller, same run. The pipeline effect appears in both terms and cancels. Only then is the number comparable between people.

A user's genome is never comparable to a public cohort on raw counts. It is only ever comparable to itself.

## 5. What every result must say

No score in this tool was trained on autism. They are trained on general pathogenicity or evolutionary conservation. **A high score means "generically interesting," never "autism-causing."** This is research-stage, not clinical. It appears on every result, every time.

## 6. Front door

`start-here.html` — the negative-exome pathway, as specified in `REFRAME_PLAN_2026-07.md` section 2. That plan's page structure and the design gate in `DESIGN_BRIEF_REFRAME_2026-07.md` (keep the "Autism Brain Atlas" name; the father-daughter journey as narrative spine, de-identified; gradient as emotional arc; build start-here first) **remain in force.** Only the ledger-as-differentiator framing is retired.

## 7. Build order

Decided 2026-07-13: **the scan pipeline first**, then the front door.

1. Define the region set the scan covers (bounds everything downstream).
2. Compute the control base-rate distribution from 1000 Genomes high-coverage genomes.
3. Generalize the pipeline off the hardcoded VCF and six genes — any VCF in, ranked cards out, artifact filtering and base-rate comparison built in, no live API calls.
4. Verify: rerun on the known case; it must reproduce the July result and must report that case as unremarkable against the base rate.
5. Port to browser (WASM) + precomputed static annotation shards.
6. `start-here.html` and the homepage reframe.

## 8. Standing sources for the current state

- Working pipeline seed: `reanalysis_2026-07/` in the genetics project folder.
- Ranking-tool survey: `NONCODING_RANKING_TOOLKIT.md` — CADD v1.7, SpliceAI, ncER, gnomAD, RegulomeDB, AlphaGenome, ChromBPNet, Open Targets. Effectively the v1 annotation spec.
- Known-case result to verify against: `reanalysis_2026-07/CANDIDATE_REPORT.md`.
- Site deploy: manual zip-drop to Netlify, not git-connected. See `DEPLOY_STATE.md`.
