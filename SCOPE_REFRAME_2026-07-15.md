# Scope reframe: who the tool is for and the idea that organizes it
2026-07-15. Companion to DESIGN_BRIEF_REFRAME_2026-07.md (which locks the visual/narrative
design). This locks the *scientific scope* — the population and the spine — behind it.

## The sharpening

The reframe so far said "negative exome isn't the end of the road." True, but too broad —
a negative exome covers a huge, heterogeneous population. The three subtyping/regulatory
papers read this cycle let us narrow to the group the literature has actually left behind,
and the group this project knows from the inside.

**Target population: nonspeaking or minimally speaking (profound) autism, negative after
exome or genome sequencing.**

That is a real, defined clinical entity (Lancet Commission), roughly a quarter to a third
of autistic people, and — critically — the group with the *highest* rate of an underlying
genetic cause and therefore the highest rate of a cause that current tests can't yet see.
It is also the population that none of the current landmark subtyping papers actually study:
Litman's SPARK cohort skews verbal, Pagani's fMRI cohort is average-IQ ABIDE data. Profound
exome-negative autism is the gap in the literature, not its subject. That gap is the opening.

## The hallmark is presentation, not IQ

Define the group by what is observable and non-inferential: nonspeaking or minimally
speaking, high support needs, common comorbidities such as epilepsy. **Do not define it by
IQ or "intellectual disability."** Two reasons, both defensible:

1. Standard IQ tests require motor or verbal responses that nonspeaking people often can't
   produce, so a very low tested score in this group is partly a measurement artifact, not a
   clean read of cognitive ability. The field's own "profound autism" definition leans on
   language and support needs precisely because those are observable.
2. It's the honest position given real disagreement about how to measure cognition in
   nonspeaking individuals.

**On assisted-communication methods (spelling-to-communicate and similar): the site stays
out of it.** It is a genuinely contested area with professional-body position statements
against it. The tool's framing — "nonspeaking does not mean non-thinking, and tested IQ is
unreliable here" — is well supported on its own and does not require taking any position on
S2C. Keep it that way. No advocacy, no anecdote, no method claims.

## The spine: developmental timing, not gene identity

The organizing scientific idea, and the thing that makes the tool more than a lookup box:
**profound autism is better understood as disruption that acts early and in specific
developmental windows than as a broken gene.** Two independent papers converge on this from
opposite directions:

- Litman 2025 (phenotype → genetics): the more severe classes correspond to earlier-acting
  affected genes. Timing tracks outcome.
- Dominguez-Alonso 2026 (coding-negative regulatory sequencing, the on-target one): in
  exome-negative trios, de novo noncoding variants land on dynamically-expressed,
  stage-specific genes and at CTCF chromatin boundaries; inherited ones land on
  constitutively-expressed genes. Timing separates the two classes of hit.

So the tool organizes a person's noncoding variants not just by "is this rare / does it hit
an autism gene" but by *when and where the target gene is active in brain development.* A
variant near a gene that fires briefly in mid-fetal cortex reads differently from one near a
housekeeping gene. That framing is defensible, current, and it's what distinguishes this
from a generic annotation dump.

## In scope

- Interpret a person's own variants against public data: rarity, overlap with known ASD
  genes, regulatory context, and — the new layer — the developmental timing / cell-type
  activity of the target gene.
- Always surface the base rate. Everyone carries thousands of rare noncoding variants; a hit
  is a lead, not a finding. This is non-negotiable and is the project's credibility spine.
- Precomputed, browser-local (WASM) annotation only. No uploads, no server-side processing
  of a person's variants (per DECISION_RECORD).
- Serve two readers: the parent who got "negative exome and nothing else," and the
  independent researcher who wants a control-anchored regulatory lens.

## Out of scope (say so plainly)

- Diagnosis. The tool surfaces leads; it does not diagnose or claim causation.
- Validation / replication of published research (retired 2026-07-13).
- IQ or cognitive-ability claims about any individual.
- Any position on assisted-communication methods.
- Treatment or clinical advice.

## Honest limits (these go on the site, not just in this doc)

- No profound, nonspeaking, exome-negative *reference cohort* exists yet. The subtyping
  papers don't cover this group, so the tool interprets against adjacent data, not a matched
  population. Every lead carries that caveat.
- For any one person this is n=1. Leads are hypotheses, not answers.
- Inherited-vs-de novo and transmission can't be resolved without both parents' DNA — the
  single biggest missing input, and the reason so many leads stay open.

## What changes vs. the existing brief

The visual/narrative design brief still holds — story over inventory, the gradient as
emotional arc, start-here first. This adds two things underneath it: the audience narrows
from "negative exome" to "profound/nonspeaking, negative exome," and the science gets a spine
(developmental timing) instead of a flat gene/variant lookup. The parent line becomes more
specific and more honest: "The test found nothing. For a child like mine — nonspeaking, high
needs — that's common, and it doesn't mean there's nothing to find. Here's where the newest
science says to look, and how not to fool yourself."

## Sources
- Litman et al., Nat Genet 2025, DOI 10.1038/s41588-025-02224-z
- Dominguez-Alonso et al., Res Sq 2026 (preprint), DOI 10.21203/rs.3.rs-9650619/v1
- Pagani et al., Nat Neurosci 2026, DOI 10.1038/s41593-026-02287-z
- Lancet Commission profound-autism definition; CDC 2023 prevalence (~27%)
