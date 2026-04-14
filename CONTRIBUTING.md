# Contributing to the Autism Data Atlas

This project maps publicly available datasets for autism genetics research. Contributions are welcome from researchers, citizen scientists, parents and anyone working with genetic data.

## How to add a dataset

1. Fork this repository
2. Add your dataset entry to `datasets.json`
3. Open a pull request

Each entry in `datasets.json` follows this schema:

```json
{
  "id": "short-unique-id",
  "name": "Full Dataset Name",
  "shortName": "Short Name",
  "description": "What this dataset contains and why it matters. Plain language, 2-3 sentences.",
  "whatYouCanDo": "Specific analyses possible with this data.",
  "whatYouCant": "Known limitations or what the data does NOT contain.",
  "citation": "Author et al., Journal Year",
  "doi": "10.xxxx/xxxxx",
  "dataType": ["scRNA-seq", "WES", "GWAS"],
  "organism": "Human",
  "sampleSize": "n=500 individuals",
  "accessLevel": "PUBLIC",
  "accessNotes": "How to actually get the data.",
  "primaryUrl": "https://...",
  "downloadUrls": [
    {
      "label": "Expression matrix",
      "url": "https://...",
      "format": "CSV",
      "sizeApprox": "32MB"
    }
  ],
  "fileFormats": ["h5ad", "csv", "fastq"],
  "genesRelevant": ["MECP2", "MEF2C"],
  "tags": ["organoid", "CRISPR", "autism"],
  "category": "perturbation",
  "publicationYear": 2024,
  "codeSnippet": "import scanpy as sc\nadata = sc.read_h5ad('file.h5ad')",
  "relatedDatasets": ["other-dataset-id"],
  "lastVerified": "2026-03-25"
}
```

### Required fields

Every entry needs at minimum: `id`, `name`, `description`, `accessLevel`, `primaryUrl`, `category`.

### Field details

**accessLevel** must be one of:
- `PUBLIC` -- anyone can download immediately
- `REGISTERED` -- requires free account signup (e.g., GEO, CellxGene)
- `CONTROLLED` -- requires institutional approval (e.g., dbGaP, SFARI Base)
- `GATED` -- requires contacting authors directly

**category** must be one of:
- `perturbation` -- CRISPR screens, knockouts, gene perturbation experiments
- `patient-organoid` -- patient-derived organoids, iPSC models
- `postmortem` -- postmortem brain tissue expression data
- `genetic-variation` -- WES, WGS, GWAS, variant databases
- `regulatory` -- gene regulatory networks, ChIP-seq, enhancer maps
- `developmental` -- developmental expression atlases, brain region maps
- `reference` -- gene constraint, phenotype ontologies, general databases
- `controlled-access` -- large cohort data requiring institutional access

### What makes a good entry

The catalog is designed for people who want to actually use these datasets, not just know they exist. Focus the description on what someone can DO with the data. Include a code snippet if you can -- even a simple one showing how to load the file.

Verify every URL before submitting. Include file sizes where possible. If access requires registration or approval, explain the process in `accessNotes`.

## How to connect your own genetic data

If you have personal genetic data (WGS, WES, clinical VCF) and want to contribute analysis:

1. **Do not upload raw genetic data to this repository.** Genetic data is identifying.
2. Open an issue describing what data you have and what you'd like to analyze.
3. We can help you set up a local analysis pipeline using the tools and datasets cataloged here.
4. Aggregate, de-identified findings can be contributed back as new catalog entries or analysis write-ups.

## Reporting errors

If a URL is broken, a DOI is wrong, an access level has changed, or a description is inaccurate, open an issue or submit a PR with the fix. Accuracy matters more than completeness.

## Code of conduct

Be respectful. Many contributors are parents of autistic children doing this work alongside day jobs. Corrections and disagreements are welcome; condescension is not.
