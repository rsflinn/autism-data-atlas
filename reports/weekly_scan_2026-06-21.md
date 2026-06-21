# Weekly Deep Scan — 2026-06-21

**Bottom line:** No new public datasets and no new tools this week. Cleaned one piece of retired terminology out of the wiki index, confirmed zero broken cross-references, refreshed the website feed date. Catalog holds steady at 30 datasets. One catalog data-quality issue surfaced that needs your eyes: a placeholder source URL on the Sanders 2026 BA22 entry.

Window scanned: 2026-06-14 to 2026-06-21. Paths note: the task file points at an old session ID (`friendly-serene-ride`); the atlas is mounted this session at `autism-data-atlas/`, which is what I used.

---

## New datasets discovered

None deposited and accessible this week.

Four PubMed queries returned a single in-window record, and it deposits nothing new:

- **PMID 42319587** — Akela et al., *Molecular Diversity*. Systems-biology / scRNA-seq reanalysis of ASD cortical development. It reuses an existing public dataset (GSE210960) and prioritizes RACK1 and NRXN1 as hub genes, then runs molecular docking of tretinoin against RACK1. No new deposit; the dataset it uses is already public and not autism-cohort-specific. Neither RACK1 nor NRXN1 is in the 27-gene atlas set. DOI: [10.1007/s11030-026-11612-4](https://doi.org/10.1007/s11030-026-11612-4) *(record retrieved via PubMed)*

bioRxiv: the autism single-cell/spatial preprints that surface in search (PRISMA imaging dataset, Jan 2026; STARMAPS developing-brain atlas / Wang et al., May 2026) are both outside the 7-day window. No in-window deposits to GEO, Zenodo, Synapse or dbGaP found.

## New catalog entries drafted

None. `new_datasets_draft.json` left unchanged — nothing verified to add. It still holds the same 5 unverified candidates from April (Alonso-Gonzalez TR, Cao NRXN1, Brudno H1/16p11.2, Forti TCF4 splicing, Lee Wac), four of which remain `[NEEDS VERIFICATION]` on their data-availability statements.

## Broken URLs found

None in the sample. Spot-checked 5 of 30 catalog entries; all live: denovo-db.gs.washington.edu, chip-atlas.org, gpf.sfari.org, brainspan.org, gnomad.broadinstitute.org.

Caveat: direct HTTP fetch is blocked by the fetch provenance restriction (same limitation logged in every recent scan), so liveness was confirmed via search-index existence, not a direct request.

**Separate catalog issue, not from the spot-check sample:** the `sanders-2026-ba22-multiomics` entry in `datasets.json` has `primaryUrl` set to the bare domain `https://www.biorxiv.org/` rather than the actual preprint URL. That is effectively a dead source link. I did not guess a replacement — the real preprint URL needs verification before it goes in. Flagging for a one-line fix. [NEEDS VERIFICATION]

## New tools found

None verifiably new. The GitHub scan surfaced only established repos already in the catalog or known: kundajelab/variant-scorer, kundajelab/chrombpnet, pinellolab/chorus, deepmind/alphagenome, getian107/PRScs. PRScs (continuous-shrinkage polygenic scoring) is a mature, widely used tool, not new — noted, not added.

## Wiki health issues

1. **Fixed: retired terminology in the index.** The MEF2C summary line in `wiki/index.md` described haploinsufficiency as dysregulating "ORC network members." Per CLAUDE.md the ORC cascade hypothesis is retired and "ORC" should not be used as active framing. Replaced with "NDD transcription-factor network members." "ORC" now appears nowhere in the wiki.
2. **Cross-references clean.** All 137 internal `.md` links in `index.md` resolve to existing files. Zero broken links.
3. **Unchanged, still needs your call: Receptor Type Separation concept page.** `wiki/concepts/receptor_type_separation.md` (and its one-line summary in the index) still states the class-level framing — "GABA receptors drive epilepsy, glutamate receptors drive autism convergence." The April 2026 reanalysis downgraded this to PARTIALLY FAILED: class-level separation didn't hold (epilepsy MWU p=0.189) and GRIN2A's significant epilepsy PTV burden breaks the glutamate=autism claim. Individual shared genes (SCN2A, KCNB1, PCDH19) are real; the receptor-class story is not. This is a science-framing decision, so I did not rewrite it. This is the third consecutive week it's been flagged.
4. **Missing gene pages (no change).** 18 of the 27-gene atlas set still lack pages: GRIN2B, SYNGAP1, RBFOX1, CACNA1A, KCNB1, SLC6A1, MECP2, MYT1L, EP300, BCL11A, ADNP, ARID1B, PCDH19, GRIN2A, STXBP1, WAC, AUTS2, RBBP5. No new in-set genes were introduced this week.

## Backfill progress

Phase 1 (10 critical datasets): **9 of 10 have wiki pages.** Mapped against `wiki/datasets/`: SPARK (spark-wgs), MSSNG (sfari-base), SSC (ssc), Epi25 (epi25-wes), ENCODE (encode), GTEx (gtex-brain), BrainSpan (brainspan), PsychENCODE (psychencode-grn), Allen Brain (allen-brain-atlas) all exist. The one gap is **ASC / Autism Speaks public cohort** — no dedicated page.

Data-quality note on the queue itself: `structured/backfill_queue.json` still marks every entry `not_started` and hasn't been touched since 2026-04-04, so it no longer reflects reality. Its metadata also disagrees with itself — `total_queued: 24` vs. a summary `total_entries: 29` (10+7+6+6). Worth a one-time status refresh.

Next 2–3 priorities to backfill:

1. **ASC / Autism Speaks dataset page** — the only missing Phase 1 page.
2. **SYNGAP1 gene page** — heavily referenced across findings, still missing; multiple new SYNGAP1 findings this spring.
3. **WAC gene page** — multiple findings this spring (DeSanto-Shinawi models, Boonpraman 2026), still missing.

Before any Phase 2 backfill, three entries carry placeholder DOIs and should be verified or dropped: `pugsley_2024` (`10.1038/nature`), `cell_genomics_2024_a` and `_b` (both `celrep.2024.xxxxx`).

## Website feed

`datasets_feed.js` regenerated from the 30 verified `datasets.json` entries; `last_updated` set to 2026-06-21. No content change beyond the date — no new datasets this week.

## Notable for you

- **The Sanders 2026 BA22 entry has a placeholder source URL** (`https://www.biorxiv.org/`). Small fix, but it's a broken provenance link sitting in the live catalog — worth correcting with the real preprint URL.
- **The receptor-type-separation concept page is still the one real inconsistency in the wiki.** Three weeks running. Recommend reframing it around the specific shared genes before it's cited anywhere downstream.
- Quiet week for primary data. The only on-topic literature item (Akela et al.) is a docking/reanalysis paper, not a data release.
