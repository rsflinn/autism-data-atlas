# Claude Design Brief — Autism Brain Atlas Homepage

A complete brief and prompt for Claude Design. Drop the attached files into the project, then paste the prompt below.

## Files to attach

- `brain-glass.png` — the transparent glass-brain image, the visual anchor
- `VOICE_AND_STYLE.md` — the editorial voice guide
- `ATLAS_ARCHITECTURE.md` — what the Atlas is and how it works
- `index.html` — the existing site structure the homepage must integrate with
- `papers_feed.js` — live paper feed data for the latest-additions card row
- `README.md` — the public-facing project description

---

## The prompt to paste

> Build the homepage for the Autism Brain Atlas — a free, public, daily-updated tool that does two things in one site. It is a wiki of every indexed autism genetics study, written in plain language. It is also a portal to the public datasets and tools that allow non-academics to run their own analyses. The site auto-updates from PubMed and preprint servers via scanning agents. It is built and maintained by an independent journalist; it is not affiliated with any institution.
>
> ### Audiences (in priority order)
>
> 1. Parents and family members of autistic people who want to understand the science
> 2. Citizen scientists and armchair researchers who want to run their own analyses
> 3. Journalists and policy people looking for grounded, citable material
> 4. Working researchers as a secondary audience
>
> ### Voice
>
> Wire-service journalism for a general audience. Plain English at high-school reading level. Active voice. Lead with the so-what. No jargon, no acronyms, no specific gene names like SCN2A unless the term itself is the news. Banned words: groundbreaking, revolutionary, novel, cutting-edge, paradigm-shifting, interestingly, importantly, notably. The attached `VOICE_AND_STYLE.md` is the canonical guide. Apply it to every word that ends up on the page.
>
> ### Locked copy
>
> Use these exact strings. Do not rewrite or paraphrase.
>
> - Brand wordmark in the nav: **Autism Brain Atlas**
> - Hero line: **Autism Brain Atlas: an open-source tool for exploring autism's genetic roots.**
> - Tagline below the hero: **Studies, datasets, findings.**
> - Primary CTA button: **Browse the studies**
> - Secondary CTA text link: **Explore the data →**
> - Search placeholder: **Search studies, genes, datasets, findings…**
> - Search filter chips: **All · Studies · Genes · Datasets · Findings**
> - Five example query chips below the search: **MEF2C · SCN2A · noncoding variants · cortical organoids · ChromBPNet**
> - Stats labels (in this order): **Studies indexed · Datasets cataloged · Genes profiled · Variants annotated**
> - Latest-additions strip label: **Recently added**
> - Footer credit (very bottom of page, small): **Built and maintained by Ryan Flinn, an independent journalist covering health and science. Free for anyone to use.**
>
> ### Design direction
>
> Modern research portal. Calm, confident, minimal. Reference points: AlphaFold Protein Structure Database, Stripe Press, DeepMind's homepage, the Anthropic homepage. The page must feel like a serious scientific resource, not a museum exhibit, not a brand site, not a clinical tool.
>
> **Background:** a single linear vertical gradient. Top to bottom — `#1860c4` (lapis) at 0%, `#0c3b8a` (cobalt) at 35%, `#0a2868` (deep) at 70%, `#051438` (abyss) at 100%. One linear-gradient, that is all. No radial glows, no diagonal light shafts, no fog overlays, no atmospheric effects.
>
> **What is forbidden:** marine-snow particles, drifting bubbles, volumetric fog, light shafts, glass-mask treatments on the brain, caustics, specular highlights, refraction halos, electrical sparks inside the brain, plate-style hairline borders around the viewport, Roman-numeral index marks, "Plate I" labels, italic Latin captions, "Pelagic Specimen" or any specimen-museum framing, any decorative ornament that does not serve content. None of these belong on this page.
>
> **The brain:** the attached transparent PNG sits as a quiet visual anchor on the right side of the hero. Roughly 700–900px wide on desktop, bleeding slightly off the right edge if needed. No frame around it. No caption beneath it. At most a soft `radial-gradient` halo in mist blue behind it, blurred. Subtle vertical floating bob (~8 second cycle) is acceptable. Nothing else animates on or inside the brain.
>
> **Layout:** 60/40 split hero. Left column carries everything textual. Right column is the brain. Top navigation runs full-width above. Footer credit and small links run full-width below.
>
> *Left column, top to bottom:*
> - Top navigation in left position: home · Studies · Genes · Datasets · Methods · Findings · Getting Started · About
> - Hero line in display-scale serif (Cormorant Garamond, 96–124px on desktop, single weight, letter-spacing tight)
> - Tagline below in italic Cormorant Garamond, around 24px, in cream
> - Search bar — input + button, with the placeholder text above; below the input, the five filter chips on one row, and the example query chips on the next row, smaller and in italic mist blue
> - CTA row: coral-filled primary button + secondary text link with arrow
> - Latest-additions strip: four cards in a horizontal row pulled from `papers_feed.js`, each card showing journal name, date, title (truncated to two lines), and gene tags
> - Stats row: four stats in a single-line horizontal grid with thin vertical dividers, animated counters
>
> *Right column:*
> - Brain image, large, anchored vertically centered. Nothing else.
>
> *Footer (full-width, bottom of page):*
> - Single line of small text containing the credit string above, in cream at low opacity
> - Beside it (or below on narrow viewports): three small text links — About · Contributing · Source code
>
> ### Palette (use only these)
>
> abyss `#051438` · deep `#0a2868` · cobalt `#0c3b8a` · lapis `#1860c4` · glow `#4ea3e8` · mist `#9bc4f5` · coral `#f76c4e` · amber `#f4a259` · cream `#fbecd1`
>
> Coral is the action color (primary button only). Amber is the hover-state and accent color. Cream is the typography color. Everything else is structural background.
>
> ### Typography
>
> - Cormorant Garamond — serif, used for the hero line, tagline, and any italic captions
> - Inter — sans-serif, used for navigation, search input, CTAs, stats, feed-card text, footer
>
> Use only these two families. Use light and regular weights for Inter; regular and italic for Cormorant Garamond. No other weights, no other faces.
>
> ### Success criteria
>
> A first-time visitor must, within three seconds of loading the page, know what the site is, what is inside it, and what they can do here. The page must feel like AlphaFold's database UI in mood — calm, confident, scientific — not a museum exhibit, not a marketing landing page, not a startup's product launch. The hierarchy must be: hero line first, search second, CTA third, latest additions fourth, stats fifth, brain as quiet visual companion. The brain must not compete with the text for attention.
>
> ### What to deliver
>
> A single self-contained HTML file with everything embedded. Real data wired from the attached `papers_feed.js` (top four most recent papers in the feed). Stats counters with realistic numbers (use the architecture document for guidance on counts; placeholders are fine if exact numbers are unclear). The footer credit must read exactly as locked above. Mobile-responsive — at viewports under 1024px the hero stacks vertically with the brain on top, content below; under 720px the feed cards stack to a single column.

---

## After Claude Design produces a result

Export as standalone HTML, drop it back in the autism-data-atlas folder. I'll integrate it with the existing `index.html` so the search and stats are wired to the real feeds, the navigation hooks into the existing tab structure, and the page becomes the actual homepage of the live site.

If the first iteration still has any of the forbidden elements (marine snow, plate frames, glass-mask brain, Latin captions), reply with a short follow-up: "Remove [specific elements]. Keep everything else." Don't restart the whole prompt.
