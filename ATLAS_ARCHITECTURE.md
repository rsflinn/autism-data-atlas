# Autism Regulatory Variant Atlas -- Self-Learning Architecture

## What This Is

A self-learning knowledge base that continuously discovers, evaluates, and integrates autism genomics data -- datasets, papers, tools, and methods -- into a structured, AI-queryable atlas. Built on the Karpathy knowledge-base pattern: raw data ingested into `raw/`, compiled by LLM agents into a structured wiki/database, queryable and self-improving over time.

The goal: become the most comprehensive, structured, publicly available resource mapping noncoding regulatory variants to autism phenotypes, organized by cell type, severity, and comorbidity profile.

## Architecture Overview

```
SCANNING AGENTS (continuous)          EVALUATION AGENTS (on trigger)
  |                                     |
  PubMed scanner                        Relevance scorer
  bioRxiv/medRxiv scanner               Novelty detector
  GEO/SRA dataset scanner               Quality assessor
  GitHub repo scanner                   Integration planner
  Twitter/X bookmark ingester           |
  |                                     v
  v                               INTEGRATION AGENTS (approved)
raw/                                    |
  papers/                               Dataset downloader
  datasets/                             Format standardizer
  tools/                                Annotation pipeline
  methods/                              Cross-reference linker
  |                                     |
  v                                     v
KNOWLEDGE GRAPH (compiled wiki)    STRUCTURED DATA (machine-readable)
  concepts/                             variants.jsonl
  genes/                                gene_regulatory_map.jsonl
  datasets/                             phenotype_links.jsonl
  methods/                              cell_type_annotations.jsonl
  findings/                             receptor_separation.jsonl
  index.md                              evidence_tiers.jsonl
```

## Directory Structure

```
autism-data-atlas/
  raw/                          # Unprocessed ingested material
    papers/                     # Downloaded PDFs, extracted text
    datasets/                   # Dataset metadata + download scripts
    tools/                      # Tool descriptions, READMEs
    bookmarks/                  # Twitter/X bookmarks, web clips
    scan_logs/                  # What was scanned, when, results

  wiki/                         # LLM-compiled knowledge base (.md files)
    index.md                    # Master index with summaries
    concepts/                   # Biological concepts (polygenic risk, noncoding variants, etc.)
    genes/                      # Per-gene pages (MEF2C.md, SCN2A.md, etc.)
    datasets/                   # Per-dataset pages (SPARK.md, MSSNG.md, etc.)
    methods/                    # Analytical methods (ChromBPNet.md, MPRA.md, etc.)
    findings/                   # Key findings across papers
    tools/                      # Software tools and models
    receptor_separation/        # Our receptor-type separation framework
    evidence_tiers/             # What's validated vs. hypothesis

  structured/                   # Machine-readable data (JSON-LD, TSV)
    variants/                   # Noncoding variant annotations
    regulatory_elements/        # Enhancers, promoters, insulators by cell type
    gene_phenotype_links/       # Gene -> phenotype -> severity -> comorbidity
    datasets_catalog.json       # All known autism datasets (extends current datasets.json)
    receptor_framework.json     # Glutamate/GABA/shared separation model

  agents/                       # Agent configurations and scripts
    scanners/                   # Scanning agent configs
    evaluators/                 # Evaluation agent configs
    integrators/                # Integration agent configs
    scheduler.py                # Orchestration / scheduling

  logs/                         # Audit trail
    scan_history.jsonl
    evaluation_decisions.jsonl
    integration_log.jsonl
```

## Agent Pipeline

### Layer 1: Scanning Agents (Discovery)

These run on a schedule (daily or weekly) and find new material.

**PubMed Scanner**
- Query: autism + (noncoding OR regulatory OR enhancer OR promoter OR polygenic OR GWAS OR "whole genome")
- Also: epilepsy + (GABA OR glutamate OR "ion channel") + genetics
- Also: specific gene names (MEF2C, SCN2A, FOXP1, etc.) + new publications
- Tool: PubMed MCP (already connected) or Entrez API
- Output: paper metadata -> raw/papers/{pmid}.json

**bioRxiv/medRxiv Scanner**
- Same queries as PubMed but for preprints
- Tool: bioRxiv MCP (already connected) or API
- Output: preprint metadata -> raw/papers/{doi}.json

**GEO/SRA Dataset Scanner**
- Query: autism OR ASD + (RNA-seq OR scRNA-seq OR WGS OR ATAC-seq OR ChIP-seq)
- Specifically look for: new organoid datasets, new WGS cohorts, new CRISPR screens
- Tool: GEO API via Entrez
- Output: dataset metadata -> raw/datasets/{accession}.json

**GitHub Scanner**
- Query: autism genomics, noncoding variant, regulatory variant, polygenic score
- Also track repos from key labs (Geschwind, Sanders, Daly, State)
- Tool: GitHub API
- Output: repo metadata -> raw/tools/{repo}.json

**Bookmark Ingester**
- Reads from Twitter bookmarks spreadsheet (manual export or API)
- Filters for HIGH usefulness + Science Findings / Research Tools categories
- Output: bookmark metadata -> raw/bookmarks/{id}.json

### Layer 2: Evaluation Agents (Triage)

When a scanning agent finds something new, an evaluation agent scores it.

**Relevance Scorer** (runs on every new item)
- Input: paper/dataset/tool metadata + abstract/description
- Scoring criteria:
  - Direct autism relevance (0-10)
  - Noncoding/regulatory variant relevance (0-10)
  - Dataset availability (public vs. controlled vs. unavailable) (0-10)
  - Novelty vs. what's already in the atlas (0-10)
  - Cell-type specificity information present? (0-5)
  - Phenotype/severity data present? (0-5)
- Output: relevance_score (0-50) + reasoning
- Threshold: score >= 25 goes to Integration queue; 15-24 goes to Review queue; <15 logged and skipped

**Novelty Detector**
- Compares new item against existing wiki/ entries
- Flags: new gene not yet covered, new dataset for existing gene, contradicts existing finding, new method applicable to existing data
- Output: novelty_type + affected_wiki_pages

**Quality Assessor** (for papers)
- Checks: sample size, statistical methods, replication, preprint vs. peer-reviewed
- Maps to our evidence tier system (A/B/C/D)
- Output: quality_tier + caveats

### Layer 3: Integration Agents (Action)

Items that pass evaluation get integrated by specialized agents.

**Dataset Integrator**
- Downloads public metadata (not raw data -- that's too large for auto-download)
- Extracts: genes covered, sample sizes, phenotype data available, data access requirements
- Creates structured entry in datasets_catalog.json
- Creates wiki page in wiki/datasets/
- Cross-references against existing gene pages

**Paper Integrator**
- Extracts key findings, methods, gene lists, variant lists
- Updates relevant wiki/ pages (adds new findings, citations)
- If paper contains variant-level data: extracts to structured/variants/
- Maps findings to receptor separation framework where applicable

**Tool Integrator**
- Tests if tool is installable/runnable
- Documents: what it does, input/output formats, dependencies
- Evaluates: could this improve our annotation pipeline?
- Creates wiki page in wiki/tools/

**Cross-Reference Linker**
- After any new integration, updates backlinks across wiki
- Checks: does this new dataset validate or contradict existing findings?
- Updates evidence tiers if new evidence changes confidence

## Backfill Strategy (Older Datasets)

Phase 1: Known major datasets (complete first)
- SFARI/SPARK (106K individuals, WGS available)
- MSSNG (>11,000 WGS, autism families)
- SSC (Simons Simplex Collection, 2,274 families WGS)
- ASC (Autism Sequencing Consortium, exome)
- Epi25 (epilepsy, cross-condition comparison)
- ENCODE + Roadmap Epigenomics (regulatory elements)
- GTEx (tissue-specific gene expression)
- BrainSpan (developmental brain transcriptome)
- PsychENCODE (brain gene regulation)
- Allen Brain Atlas

Phase 2: Published study datasets (mine supplementary tables)
- Paulsen 2023 CHOOSE (36 gene KOs, already analyzed)
- Pasca/Geschwind 2026 (9 mutations, already analyzed)
- Jin 2020 perturb-seq (35 genes, already analyzed)
- Lipton MEF2C organoids (already analyzed)
- Zhou 2019 (noncoding variant deep learning, autism WGS)
- An 2018 (WGS noncoding variants, 1,902 ASD families)
- Werling 2018 (WGS, SSC)
- Turner 2017 (promoter de novo mutations)
- Pugsley 2024 (noncoding SNPs, gene expression in brain tissue)
- Cell Genomics 2024 (TADs + promoter variants in ASD)
- Cell Genomics 2024 (rare noncoding variants, evolutionary signatures)

Phase 3: Systematic GEO/SRA sweep
- Query all autism/ASD entries in GEO from 2015-present
- Filter for: WGS, RNA-seq, scRNA-seq, ATAC-seq, ChIP-seq, MPRA
- Catalog metadata even if raw data is controlled-access
- Flag datasets that could be reanalyzed with new tools

Phase 4: Adjacent condition datasets
- Epilepsy (Epi25, EuroEPINOMICS)
- Intellectual disability
- Schizophrenia (PGC)
- Shared genetic architecture datasets

## Tools From Bookmarks to Integrate

Priority tools to evaluate and potentially incorporate into the atlas pipeline:

1. **varTFBridge** (bookmark #138) -- traces common AND rare noncoding variants to TFs and target genes. CRITICAL for the atlas annotation layer. Evaluate immediately.

2. **ANNEVO** (bookmark #12) -- MoE genome language model for gene annotation. Could automate gene-level annotation in the atlas.

3. **GET foundation model** (bookmark #55) -- cell-type-specific transcription prediction. Could provide cell-type annotations for regulatory variants.

4. **PARM** (bookmark #70) -- DL model for promoter activity prediction. Directly applicable to scoring promoter variants in the atlas.

5. **Genotype-Phenotype Map** (bookmark #128) -- gpmap.opengwas.io, fine-mapped GWAS for 16K traits. Major structured data source to ingest.

6. **Tabula Sapiens ncRNA** (bookmark #95) -- non-coding RNA landscape across 22 organs. Reference layer for the atlas.

7. **Claude Scientific Skills** (bookmark #175) -- database-lookup across 70+ databases. Could power the scanning agents.

8. **Moara** (bookmark #117) -- AI literature review. Could replace/augment the PubMed scanning agent.

9. **Claude Scholar** (bookmark #120) -- open-source research paper AI. Another scanning/evaluation option.

10. **BioML-bench** (bookmark #83) -- benchmark for evaluating bio AI tools. Use to evaluate tools before integrating.

## Knowledge Base Implementation (Karpathy Pattern)

Following the approach from bookmarks #225-226:

1. **Raw ingestion**: Papers, datasets, bookmarks -> raw/ directory as .md and .json files
2. **LLM compilation**: Agent reads raw/, writes/updates wiki/ .md files with summaries, cross-links, concept articles
3. **Index maintenance**: Agent auto-maintains index.md with brief summaries of all documents
4. **Q&A layer**: Once wiki is large enough, query agents can research answers across the whole knowledge base
5. **Output filing**: Query results and analysis outputs get filed back into wiki/ to enhance future queries
6. **Health checks**: Periodic LLM "linting" to find inconsistencies, missing data, broken cross-references, stale information

Key difference from Karpathy's general approach: our wiki has a STRUCTURED DATA layer (structured/) that's machine-readable, not just markdown. This is what makes it valuable to AI companies -- they can train on or query the structured layer directly.

## Scheduling

**Daily:**
- PubMed scanner (new papers in last 24h)
- bioRxiv/medRxiv scanner (new preprints)

**Weekly:**
- GEO/SRA dataset scanner
- GitHub repo scanner
- Bookmark ingester (from latest export)
- Cross-reference linting / health check

**Monthly:**
- Backfill progress check (next Phase items)
- Evidence tier review (have new papers changed confidence?)
- Wiki quality audit

## Implementation Priority

1. Set up directory structure and datasets_catalog.json schema
2. Build PubMed scanning agent (simplest, highest value)
3. Build relevance scorer (gates everything else)
4. Evaluate and integrate varTFBridge
5. Build paper integrator (extracts findings to wiki)
6. Migrate existing autism-data-atlas datasets.json into new schema
7. Build dataset integrator for GEO/SRA
8. Build cross-reference linker
9. Set up scheduling (Claude Code scheduled tasks or cron)
10. Begin Phase 1 backfill of major datasets

## What Makes This Valuable

For AI companies: A curated, structured, evidence-tiered dataset mapping noncoding regulatory variants to autism phenotypes by cell type. This is the training data / knowledge layer that general-purpose LLMs can't build from scratch.

For pharma: A queryable resource that answers "which regulatory elements in which cell types are disrupted in autism, and does the pattern predict epilepsy comorbidity?" -- with evidence tiers and source data.

For the autism community: An open, transparent, continuously updated knowledge base that synthesizes scattered research into an accessible whole. Built by a parent, not an institution.

---

Last updated: 2026-04-04
