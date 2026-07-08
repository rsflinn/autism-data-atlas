# Reframe plan: from "atlas" to a tool for negative-exome families

Draft for approval. No HTML changes until you sign off. Decisions you flagged: keep all three audiences (families, journalists, researchers) but make the negative-exome family the front door; tone decided per section (I've marked where I'd caveat hard vs. lightly).

## The one-line shift

Today the site says "here is a searchable atlas of autism genetics." The reframe makes it say "your exome came back negative — here is what that means, why it happens, and the real next avenues to investigate — plus the research library to check any claim yourself."

Same visual system, same data feeds, same research pages. What changes is the front door and the framing around it.

## Who the reader is now

Front door: a parent or self-advocate who just got a negative exome and typed "autism exome negative what next" into a search bar. Non-scientist. Wants direction, not a lecture. The journalist and researcher stay served by the existing atlas, graph, ledger and timeline — they're one click deeper, not gone.

## What "negative exome" reframing has to get right (honesty spine)

Two hard-caveat facts anchor the whole thing, and both need a cited source before they go live:

- A negative exome is the *common* outcome, not a failure. Clinical exome diagnostic yield in autism/neurodevelopmental disorders is roughly a quarter to a bit under half. [NEEDS VERIFICATION — I'll pull a current yield figure with a citation during build, not from memory.]
- Most next steps still end without a diagnosis today. The honest promise is "better odds over time and concrete avenues," not "we'll find your answer."

The research-frontier material (regulatory/noncoding work this project does) gets labeled research-stage, not clinical, every time it appears. That's a hard-caveat section.

## Page map

### 1. Homepage (`index.html`) — reframed, not rebuilt

Keep the layout and aesthetic. Change copy and add one band.

- Hero: retitle the tagline and CTAs toward the family. Wordmark can stay "Autism Brain Atlas" or shift — see open questions. New tagline direction: "Your exome came back negative. Here's what that means, and where to look next." Primary CTA "Start here" → new pathway page; secondary "Browse the research" → atlas/graph.
- New band directly under the hero: "Got a negative exome? Start here." Three-to-five step preview of the pathway with a button into the full page. This is the funnel.
- "Where to begin" cards (currently 6 topic doorways): re-point from explainer topics to next-steps topics — Why exomes miss things · Ask for a reanalysis · Whole-genome sequencing · Research studies you can join · Common vs. rare causes · What's still unknown. Lightly caveated, action-first copy.
- Search, knowledge graph, recently-added feed, stats: keep as-is functionally; rewrite the section decks so they address the family reader ("check any gene or claim you've been told about") rather than a researcher. Light touch.
- Menu + footer: add "Start here" as the first nav item.

### 2. New page: `start-here.html` — the actual tool

This is the deliverable that makes the site "useful," structured as a walkthrough:

1. What a negative exome actually means — plain language, base-rate framing. Hard caveat.
2. Why an exome can miss a cause — noncoding/regulatory variants, structural/copy-number changes, repeat expansions, mosaicism, genes not yet linked to autism, and plain interpretation limits. Each defined in one sentence by what it does.
3. Next avenues — the core. Each as a card with four fixed fields: what it is · who it's for · how to pursue it · honest yield. Planned avenues:
   - Ask for periodic reanalysis of the exome you already have
   - Trio / parental testing if it wasn't done
   - Whole-genome sequencing (WGS)
   - Join a research study — SPARK, GREGoR / Undiagnosed Diseases Network, MSSNG (links verified at build)
   - Deep phenotyping where a comorbidity points somewhere (e.g. epilepsy → EEG/MRI re-read)
   - The regulatory/noncoding frontier — what this project explores, labeled research-stage, links into the atlas. Hard caveat.
4. How to read a research claim — short literacy section funneling to the replication ledger and evidence tiers, so a family can sanity-check anything a forum or a preprint tells them.
5. Limits box — not a diagnostic tool, talk to a genetic counselor, most reanalysis still finds nothing today. Hard caveat, and it closes the page rather than opening it.

### 3. Existing pages — unchanged this pass

`replication_ledger.html`, `study-timeline.html`, `brain-explorer.html` stay as-is. The reframe just points more traffic to them and frames them as "check the claims yourself" tools. The replication ledger is genuinely the differentiator here — it's the honesty layer a scared, googling parent almost never gets.

## Copy direction

- Bottom line first, plain language, define terms on first use, no honesty theater — same rules as the project's writing standard.
- Every avenue and every frontier claim states the honest yield or research-stage status inline. No result framed as more certain than it is.
- Keep the flower / glass-brain art and the violet→red→orange type system. No redesign.

## Things I'll verify during build (not assert from memory)

- Current exome diagnostic-yield figure for autism/NDD, with citation.
- Live enrollment links and eligibility for SPARK, GREGoR/UDN, MSSNG.
- Whether any yield/timeline claims in the reframed decks need a source.

## Open questions for you

1. Wordmark: keep "Autism Brain Atlas," or rename to something that says "start here" more plainly (e.g. "Autism Genetics: Next Steps")? I lean keep-the-name, reframe-the-tagline.
2. New page as a standalone `start-here.html`, or an anchored section on the homepage? I recommend a standalone page funneled from a homepage band — keeps the homepage clean, gives the tool room.
3. the proband's story as the motivating example on the start-here page? It's powerful but the proband name is still in the public GitHub repo/history even though it's scrubbed from the live site. If yes, I'd write it de-identified. Your call.
4. Build order once approved: I'd do `start-here.html` first (the substance), then wire the homepage band + nav + deck rewrites to it.
