# Design brief: negative-exome reframe

Pre-flight design gate (APPLIER). Locks the principles before any HTML. Pairs with REFRAME_PLAN_2026-07.md.

Decisions locked: keep the "Autism Brain Atlas" name; add a "Start Here" button; the father-daughter journey is the narrative spine, written de-identified ("my daughter," never the name). Build order: start-here.html first.

## The governing principle: story, not inventory

The site's spine is one question a parent carries the day the result lands — "the test found nothing, so is there nothing to find?" — and the arc from that dead end to a map of real next roads. Every section has to advance that story. The moment a section starts *listing what the site contains*, it has failed.

Concrete consequences:
- The stat wall (953 studies / 29 datasets / 59 genes / 1,025 variants) reads like a SaaS metrics flex. It gets cut from the headline role, or reframed into the story ("more than a thousand studies read so you don't have to"). It is not a hero moment.
- Section decks stop describing contents ("Search every study, gene and dataset") and start speaking to the reader's situation ("Check any gene or claim someone has told you about").
- No "everything you need in one place" hero, no row of three identical feature cards presented as the point. Those are the tells of the cookie-cutter look you're avoiding.

## The one device that already makes this site non-generic

The homepage gradient runs blue → violet → red → orange → navy as you scroll. Reuse it as the emotional arc, not just decoration: cool and uncertain at the top (the dead end), warming through the middle (the next roads, the active part), resolving to deep navy at the bottom (honest limits, footing). Color carries meaning here — warmth = action, cool = uncertainty. That mapping is the throughline that ties both pages together and it's already half-built.

## APPLIER — six phases

1. **Purpose & audience.** Three-second takeaway: "A negative exome isn't the end of the road — here's where to look next, from someone who walked it." The action that follows is one click: Start Here. If a section doesn't serve that, it moves below the fold or goes.

2. **Structure.** Keep the existing frame: 1440px max, 56px margins, single-column editorial scroll. The page is read top-to-bottom like a feature story, not scanned like a dashboard. Type scale stays as built (League Spartan display clamp, Inter body). Don't introduce new ratios.

3. **Typography.** Two families already in place — League Spartan for display, Inter for body. Add nothing. Body stays ≥17px. Display headlines carry story beats ("The test came back clear. That's the common result.") not labels ("Features"). First person where the journey speaks; plain third person for the science.

4. **Composition & hierarchy.** One focal point per screen. Hero focal is the glass-brain-flowers image plus a human sentence — not the wordmark, not a button cluster. On start-here, each next avenue is a scene with one dominant element, read as a single column. Eye flow is a deliberate left-aligned vertical narrative. No centered-everything.

5. **Color.** Dominant violet, accents red/orange, navy as the neutral resolve, cream paper for reading passages. Already within the ≤3-saturated rule. Add no new colors. Any text set over the flower art gets a contrast plate or scrim behind it.

6. **Technical.** Semantic sections, sequential heading order (one h1, then h2/h3), 44px minimum tap targets, legible at 320px and 1440px, real illustration over icons wherever emotion is doing the work.

## Where the journey lives

Not as an "about me" block. It's connective tissue: an opening first-person beat that sets the stakes ("Two years ago my daughter's exome came back negative. I'm a journalist, not a scientist. This is what I learned looking for what it missed."), then it reappears as the human voice between the science sections and again in the honest-limits close. De-identified throughout. It earns the reader's trust precisely because it's not a brochure.

## Homepage vs. start-here, as story structure

- **Homepage = the trailer.** Hook (the daughter line) → the turn (negative doesn't mean nothing) → Start Here CTA → then the atlas, graph and replication ledger framed as "and here's the evidence room, open to you." Existing sections stay; their copy and order serve the arc.
- **Start-here = the full story.** The dead end → why an exome misses things → the roads (each next avenue as a scene, with honest yield) → how not to get fooled (the ledger) → honest limits. The navy resolve closes it.

## CHECKER status

CHECKER is the post-flight gate — it runs against the actual rendered pages at build time, not now. Every deliverable in this reframe ships with an explicit Design QA: PASS / PASS-with-notes / FAIL line before it goes to you. Recorded here so it isn't skipped.
