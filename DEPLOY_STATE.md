# Atlas deploy state

## Live URL
**https://autism-brain-explorer.netlify.app**

## Live homepage
- File: `index.html` (this is the v2 homepage, renamed from `index-v2.html` on 2026-05-01)
- Old homepage preserved at `index-legacy-2026-04.html` for rollback
- `_redirects` is cleared (just a comment); Netlify default static serving handles `/`

## Hosting
- Netlify project `autism-brain-explorer`
- Site ID `8d2a0cb0-4fce-48f0-bb70-adb59f713d3f`
- Team ID `697d4a072f57c91078fd0725`
- Admin: https://app.netlify.com/projects/autism-brain-explorer

## Last deploy
- Deploy ID `69f4d8f2ecbd5f6283e12a47`
- State `ready`, published 2026-05-01T16:46:59Z

## How to deploy a new build

The atlas folder lives in iCloud Drive. Running the Netlify deploy from a Linux sandbox fails with `Error: Unknown system error -35, read` because iCloud serves placeholder stubs to non-Mac processes. Deploy from the Mac side instead.

Reusable script at the outputs folder of any active session, copied here for reference:

```bash
#!/bin/bash
set -e
export PATH=/usr/local/bin:/usr/bin:/bin:$PATH
cd "/Users/ryanflinn/Library/Mobile Documents/com~apple~CloudDocs/Personal/Teagan's genetic files/autism-data-atlas"
/usr/local/bin/npx -y @netlify/mcp@latest \
  --site-id 8d2a0cb0-4fce-48f0-bb70-adb59f713d3f \
  --proxy-path "<proxy-path-from-netlify-mcp-deploy-site-call>"
```

The `proxy-path` is returned by calling the Netlify MCP `deploy-site` tool — it carries auth, so it's session-scoped. Get a fresh one via the Netlify MCP each time.

## Homepage visual conventions (locked, do not break casually)

- Hero image: `Glass Brain Flowers.png` (transparent glass head, vase shape, violet/red/orange flowers)
- Hero title: League Spartan with violet→red→orange ombre via `background-clip:text`
- Below the hero, four sections in a continuous color flow:
  1. **Search** — gradient navy-grey `#5A6E76` to violet `#9B5BA0`
  2. **Knowledge Graph** — violet `#9B5BA0` through `#B05078` to red `#E94835`
  3. **Browse by Topic** — red `#E94835` through `#E76540` to orange `#E5824A`
  4. **Recently Added** — orange `#E5824A` through rust to navy `#1F2A36`, meeting the footer
- Section titles on saturated sections are cream, not the tri-color ombre (would be invisible on matching backgrounds)
- Topic cards are white stamps with a colored top bar in their section's hue
- Search bar stays white
- Stats section sits on navy and bridges to the dark navy footer

## Homepage stats source files

- Studies indexed (953): `raw/papers/*.json` top-level only (excludes `review_queue/`)
- Datasets cataloged (29): entries in `structured/datasets_catalog.json`
- Genes profiled (59): distinct symbols in `genes_mentioned` field across all 953 papers
- Variants annotated (1,025): lines in `structured/variants/valone2026_variants.jsonl`

If you change the corpus and want the homepage stats to update, change the `data-target` attributes inside `<div class="stats" id="stats">` in `index.html`. The animated counter reads `parseFloat(el.dataset.target)` and renders integers via `toLocaleString()`.

## Voice and style

`VOICE_AND_STYLE.md` is the canonical guide. Apply it to every word that goes on the live page. Wire-service journalism, plain language, no jargon, no acronyms, no gene names unless the gene itself is the news. Banned words listed in the guide.
