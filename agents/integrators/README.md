# Paper Integration Agent

The Paper Integration Agent generates wiki pages for autism genomics research papers that have been evaluated and marked for integration.

## Purpose

This agent:

1. Reads evaluation decisions from `logs/evaluation_decisions.jsonl`
2. For papers with status "INTEGRATE", loads the raw paper metadata from `raw/papers/{pmid}.json`
3. Generates structured markdown wiki pages in `wiki/findings/{pmid}.md`
4. Extracts and links:
   - Known autism/NDD genes (50+ genes in the reference set)
   - Dataset accessions (GEO, dbGaP, SFARI)
   - Relevant atlas concepts (receptor separation, convergence, noncoding variants)
5. Updates `wiki/index.md` with links to new findings
6. Logs all integrations to `logs/integration_log.jsonl`

## Usage

### Basic execution

```bash
python3 paper_integrator.py
```

This will read from the default location (`logs/evaluation_decisions.jsonl`) and process all papers with status "INTEGRATE".

### Dry-run mode (preview without writing)

```bash
python3 paper_integrator.py --dry-run
```

This shows what would be integrated without making any changes to the filesystem.

### Custom input file

```bash
python3 paper_integrator.py --input-file path/to/decisions.jsonl
```

### Custom base path

If the script is run from a different directory:

```bash
python3 paper_integrator.py --base-path /path/to/atlas
```

### Get help

```bash
python3 paper_integrator.py --help
```

## Output

### Wiki Pages

Generated at `wiki/findings/{pmid}.md` with:

- **YAML Front Matter:** title, PMID, DOI, publication date, journal, evidence tier (default "C"), relevance score, last update timestamp
- **Authors:** First 5 authors (et al. if more)
- **Abstract:** Full or summarized (first 500 chars)
- **Key Genes:** Extracted from abstract/title, matched against 50+ known autism genes
- **Datasets Referenced:** GEO accessions (GSE*), dbGaP accessions (phs*), SFARI mentions
- **Relevance to Atlas:** Links to concept pages (receptor separation, convergence, noncoding variants)
- **Related Genes:** Links to existing gene wiki pages with cross-references
- **Metadata:** PMID, relevance score, last update

### Index Update

`wiki/index.md` is updated to include new findings in the "## Findings" section:

```markdown
- [Title](./findings/pmid.md) -- PMID: pmid
```

Duplicates are detected and not re-added.

### Integration Log

`logs/integration_log.jsonl` records each integration:

```json
{
  "pmid": "35486828",
  "title": "Paper Title",
  "status": "success",
  "timestamp": "2026-04-04T11:54:55.345079",
  "details": {}
}
```

## Gene Reference Set

The script matches against 50+ known autism/NDD genes including:

**Transcription Factors:** MEF2C, FOXP1, TCF4, TBR1, HIVEP2, CREBBP, EP300, MECP2, FOXP2, KMT2A, ADNP, BCL11A, MYT1L, ARID1B, SETD5, RBBP5, ASH1L, POGZ, HDAC4, MBD5

**Ion Channels & Receptors:** SCN2A, SCN1A, CDKL5, KCNB1, KCNA1, KCNA2, CACNA1A, CACNA1G, CACNA1E, GRIN1, GRIN2A, GRIN2B, GRIA4, GRID2, GRIK1, GRIK2, GABRA1, GABRB2, GABRB3, GABRG2, PCDH19

**Network/Signaling Proteins:** SHANK3, SYNGAP1, DYRK1A, RBFOX1, DLX1, DLX2, DLX5

## Concept Matching

The script automatically links papers to relevant atlas concepts based on keyword matching in abstracts:

- **"GABA" or "glutamate"** → links to `concepts/receptor_type_separation.md`
- **"convergence" or "convergent"** → links to `concepts/convergence_phenomenon.md`
- **"noncoding", "regulatory", "enhancer", "GWAS", or "polygenic"** → links to `concepts/noncoding_variants_in_autism.md`
- **"organoid"** → detected for potential dataset page links

## Input Format

Evaluation decisions file (`logs/evaluation_decisions.jsonl`):

```json
{
  "pmid": "35486828",
  "title": "Paper title",
  "score": 39,
  "score_breakdown": {...},
  "status": "INTEGRATE",
  "timestamp": "2026-04-04T18:51:14.981749"
}
```

Raw paper JSON (`raw/papers/{pmid}.json`):

```json
{
  "pmid": "35486828",
  "title": "...",
  "authors": ["Author A", "Author B"],
  "abstract": "...",
  "journal": "Nature Neuroscience",
  "publication_date": "2022-05-15",
  "doi": "10.1038/..."
}
```

## Error Handling

- Missing paper files are logged and skipped
- Invalid JSON lines in evaluation file are skipped
- Failed wiki page generation is logged
- Index update failures are reported as warnings but don't block the run
- All errors are recorded in the integration log with details

## Dependencies

Python 3.6+ (stdlib only)

## No External Dependencies

The script uses only Python standard library:
- `json` - JSONL file parsing
- `os`, `pathlib` - File system operations
- `re` - Text pattern matching for genes and datasets
- `datetime` - Timestamping
- `argparse` - Command-line argument parsing

## Examples

### Process all papers and see summary

```bash
python3 paper_integrator.py
```

Output:
```
Reading evaluation decisions from .../logs/evaluation_decisions.jsonl
Loaded 5 decisions

[EXECUTE] Starting paper integration...

=== Integration Summary ===
Total decisions processed: 5
Papers to integrate: 2
Successfully integrated: 2
Skipped (not INTEGRATE status): 3
```

### Preview integration before running

```bash
python3 paper_integrator.py --dry-run
```

Output shows what would be integrated without making changes:
```
[DRY-RUN] Would integrate: 35486828 - Whole genome sequencing reveals autism risk variants...
[DRY-RUN] Would integrate: 36999999 - SCN2A mutations cause autism spectrum disorder
```

### Run from different directory

```bash
cd /home/user/project
python3 /path/to/paper_integrator.py --base-path /sessions/.../mnt/autism-data-atlas
```

## Notes

- The script is idempotent: running it multiple times on the same evaluation decisions won't create duplicates in the index
- Generated wiki pages can be manually edited after creation (they won't be overwritten on re-runs)
- The evidence tier defaults to "C" (descriptive) for auto-generated pages but can be manually edited to A/B/D in the generated markdown
- Relative paths in wiki cross-links use `./../../` for navigating between finding pages and gene/concept pages
