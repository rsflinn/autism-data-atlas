---
type: tool-page
id: chorus
name: Chorus
discovered: 2026-05-10
status: candidate
last_updated: 2026-05-10
---

# Chorus

One unified Python interface for six genomic deep-learning models -- Enformer, Borzoi, ChromBPNet/BPNet, Sei, LegNet, and AlphaGenome -- with the same five lines of code running each oracle. Author lab: pinellolab (Luca Pinello, MGH/Broad). Released 2026.

Repo: https://github.com/pinellolab/chorus

## Why it matters here

The atlas already lists AlphaGenome, ChromBPNet (variant-scorer), and BRAIN-MAGNET as standalone tools. Chorus is the first wrapper that makes head-to-head comparison straightforward. For a Teagan-WGS noncoding variant of interest, you can ask AlphaGenome, ChromBPNet, and BRAIN-MAGNET about the same site and see whether they agree. Disagreement isn't necessarily a problem -- the models are trained on different cell types and different output modalities -- but it is a useful sanity check.

The percentile-ranking against ~10K random SNPs and ~30K cCREs is the more interesting feature. It directly addresses Iron Law #3 (what's the base rate?) by giving every prediction a built-in null distribution rather than just a raw effect size.

## Caveats

The percentile is against random SNPs, not against ASD cases vs controls. A variant in the 99th effect-percentile is "predicted to be unusually strong", not "more common in autism patients." Don't conflate the two.

The 22-tool MCP server bundled with Chorus may or may not work inside Cowork mode -- needs verification before relying on it.

Repo creation date and license were not verified during this scan. Treat as candidate until confirmed.

## Open questions

* For the current Teagan-WGS noncoding variant shortlist, does AlphaGenome agree with ChromBPNet on direction and magnitude?
* What's the agreement rate between BRAIN-MAGNET (NSC-trained) and Borzoi (RNA-seq-trained) on the autism GWAS noncoding loci?
* Does a percentile-rank cutoff (top 1%, top 5%) materially change which Teagan variants stay on the candidate list?

## Status

Candidate. Saved metadata to `raw/tools/chorus.json`. No analyses run yet.
