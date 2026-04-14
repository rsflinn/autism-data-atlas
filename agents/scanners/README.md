# PubMed Scanner for Autism Genomics Atlas

This directory contains the PubMed scanner that queries NCBI's PubMed database for papers relevant to autism genomics research.

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt --break-system-packages
```

## Usage

### Basic scan (last 7 days)
```bash
python3 pubmed_scanner.py
```

### Scan last N days
```bash
python3 pubmed_scanner.py --days 30
```

### Backfill scan (2015-present)
```bash
python3 pubmed_scanner.py --backfill
```

## Query Sets

The scanner runs 9 different query sets:

1. **Autism + noncoding/regulatory variants** - Searches for papers on autism-related noncoding variants, enhancers, promoters, and polygenic risk scores
2. **Autism + WGS/GWAS/common variants** - Whole genome sequencing and GWAS studies in autism
3. **Epilepsy + autism + ion channels/neurotransmitters** - Papers on shared genetic mechanisms between autism and epilepsy
4-9. **Gene-specific queries** - For MEF2C, SCN2A, FOXP1, TCF4, CDKL5, DYRK1A

## Output

### Papers
Each paper found is saved as a JSON file in `raw/papers/{pmid}.json`:

```json
{
  "pmid": "12345678",
  "title": "Paper title",
  "authors": ["Author, First", "Author, Second"],
  "abstract": "Abstract text...",
  "journal": "Journal Name",
  "date": "2024-01-15",
  "mesh_terms": ["Term1", "Term2"],
  "doi": "10.1234/doi"
}
```

### Scan Logs
Each scan creates a log file in `raw/scan_logs/scan_{timestamp}.json`:

```json
{
  "timestamp": "2026-04-04T12:00:00.000000",
  "queries": [...],
  "total_results": 125,
  "new_papers": 5,
  "existing_papers": 120,
  "pmids_found": [...],
  "total_unique_results": 125
}
```

## Features

- **Deduplication**: Automatically checks for existing PMIDs before fetching
- **Rich metadata**: Extracts titles, authors, abstracts, journals, dates, MeSH terms, and DOIs
- **Flexible date ranges**: Search recent papers or backfill from 2015
- **Comprehensive logging**: All scan details stored for audit trail
- **Resume-friendly**: Can be run multiple times without re-downloading existing papers

## Configuration

Entrez email is configured in the script as: `ryan_flinn@outlook.com`

To change this, edit the `ENTREZ_EMAIL` variable in `pubmed_scanner.py`.
