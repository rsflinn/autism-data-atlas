# Autism Data Atlas

A public resource combining an interactive gene network visualization with a searchable dataset catalog for autism genetics research.

## What's Included

- **Explore**: Interactive network visualization of autism-associated genes and their regulatory relationships
- **Datasets**: Searchable catalog of 10+ major research datasets (CHOOSE, MSSNG, Epi25, post-mortem brain, patient organoids, etc.)
- **Getting Started**: Plain-language guide to file formats, tools, and how to work with genomic data
- **About**: Project context and contact information

## Design

- **Dark background** (Synaptic Cartography theme): #0a0a0f background, #e2e8f0 text
- **Category-specific colors** for data type badges (perturbation, organoid, post-mortem, genetic, regulatory, developmental)
- **No external dependencies**: Single HTML file, CSS Grid/Flexbox layout, vanilla JavaScript
- **GitHub Pages compatible**: Static, no backend required

## Features

### Datasets Section
- **Search**: By name, description, genes, keywords
- **Filters**: Category (7 types), access level (public/registered/controlled/gated), organism (human/mouse)
- **Card view**: Name, description, sample count, publication year, badges
- **Expanded view**: Full description, what you can do, limitations, citation with DOI, download links, code snippet, related datasets
- **Copy button**: One-click copy of code snippets to clipboard

### Navigation
Tab-based navigation between 4 main sections. Active section highlighted with blue accent.

### Responsive
- Desktop-first design with mobile-friendly breakpoints
- Stacked layout on phones/tablets
- Readable at all sizes

## File Structure

```
autism-data-atlas/
├── index.html          # Complete self-contained website
└── README.md           # This file
```

## Datasets Included

1. **CHOOSE**: CRISPR screen in human organoids (Paulsen 2023)
2. **Lipton 2024**: MEF2C patient organoids with scRNA-seq
3. **Jin 2020**: In vivo perturb-seq in mouse brain
4. **Pasca 2026**: Patient-derived organoids with temporal RNA-seq
5. **Gandal 2024**: Post-mortem brain single-cell data
6. **Epi25**: Epilepsy exome sequencing burden test (54K samples)
7. **SFARI Gene**: Autism risk gene database (reference)
8. **ChromBPNet**: Regulatory variant predictions in brain
9. **MSSNG**: Whole genome sequencing (10K+ autism families)
10. **Rett iPSC**: MECP2 patient neurons RNA-seq
11. **GENCODE**: Gene annotation reference
12. **ClinVar**: Clinical variant interpretation

Each entry includes:
- Full description
- What you can do with it
- Limitations
- Citation with DOI link
- Download/access links
- Example code (Python)
- Related datasets

## Getting Started Guide

The "Getting Started" section covers:
- What autism genetics data looks like (expression, variants, GWAS, regulatory networks)
- Common file formats (VCF, H5AD, FASTQ, GZ, TSV, BED, XLSX)
- Environment setup (Python packages)
- Your first analysis (GSE28521 worked example)
- Access levels explained (public → controlled → gated)
- Learning resources

All written for someone with no bioinformatics background.

## Usage

1. Open `index.html` in a web browser
2. Navigate tabs: Explore → Datasets → Getting Started → About
3. Search or filter datasets
4. Click a dataset card to expand and see full details
5. Use "Open Full Screen" to view gene network in full viewport

## Technology Stack

- **HTML5**: Semantic structure
- **CSS3**: Grid/Flexbox, CSS variables for theming
- **Vanilla JavaScript**: No frameworks, search/filter logic, dynamic rendering
- **Google Fonts**: Inter (UI), JetBrains Mono (code)
- **Embedded data**: 10+ datasets defined as JavaScript objects

## Browser Compatibility

Works on all modern browsers (Chrome, Safari, Firefox, Edge) with ES6 support.
Mobile-friendly on iOS Safari and Android Chrome.

## Data Sources

All datasets sourced from public repositories:
- GEO (Gene Expression Omnibus)
- Synapse
- dbGaP
- Zenodo
- Journal supplements

## Contact

Ryan Flinn | ryan_flinn@outlook.com

---

Last updated: March 2026
