#!/usr/bin/env python3
"""
Paper Integration Agent for Autism Genomics Atlas

Reads evaluation decisions from logs/evaluation_decisions.jsonl and generates
wiki pages for papers marked with status "INTEGRATE". Extracts structured data
including genes, datasets, and concept relevance.
"""

import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple


# Autism/NDD genes to match against
AUTISM_GENES = {
    "MEF2C", "SCN2A", "FOXP1", "TCF4", "CDKL5", "MECP2", "MYT1L", "EP300",
    "BCL11A", "DYRK1A", "SYNGAP1", "SHANK3", "GRIN2B", "RBFOX1", "CACNA1A",
    "KCNB1", "SLC6A1", "GABRB3", "GABRG2", "GABRA1", "GABRB2", "GRIK1",
    "GRIK2", "GRIA4", "GRID2", "PCDH19", "GRIN2A", "CHD8", "ARID1B", "ADNP",
    "KMT2A", "POGZ", "ASH1L", "SETD5", "TBR1", "RBBP5", "HDAC4", "FOXP2",
    "CREBBP", "HIVEP2", "MBD5", "KCNA1", "KCNA2", "CACNA1G", "CACNA1E",
    "GRIN1", "DLX1", "DLX2", "DLX5"
}

# Dataset accessions to match
DATASET_PATTERNS = {
    "GEO": r"GSE\d+",
    "dbGaP": r"phs\d+",
    "SFARI": r"SFARI",
}

# Concept mapping for wiki linkages
CONCEPT_KEYWORDS = {
    "receptor_type_separation.md": ["GABA", "glutamate"],
    "convergence_phenomenon.md": ["convergence", "convergent"],
    "noncoding_variants_in_autism.md": ["noncoding", "regulatory", "enhancer", "GWAS", "polygenic"],
}

# Default values
DEFAULT_EVIDENCE_TIER = "C"
ATLAS_BASE_PATH = Path(__file__).parent.parent.parent


class PaperIntegrator:
    def __init__(self, base_path: Path = ATLAS_BASE_PATH):
        self.base_path = base_path
        self.logs_path = base_path / "logs"
        self.raw_path = base_path / "raw" / "papers"
        self.wiki_path = base_path / "wiki"
        self.findings_path = self.wiki_path / "findings"
        self.genes_path = self.wiki_path / "genes"
        self.concepts_path = self.wiki_path / "concepts"
        self.index_path = self.wiki_path / "index.md"
        self.integration_log_path = self.logs_path / "integration_log.jsonl"

        # Ensure directories exist
        self.findings_path.mkdir(parents=True, exist_ok=True)

    def read_evaluation_decisions(self, input_file: Path) -> List[Dict]:
        """Read evaluation decisions from JSONL file."""
        decisions = []
        if not input_file.exists():
            print(f"Warning: Evaluation file not found: {input_file}")
            return decisions

        try:
            with open(input_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            decisions.append(json.loads(line))
                        except json.JSONDecodeError as e:
                            print(f"Warning: Failed to parse JSON line: {e}")
                            continue
        except Exception as e:
            print(f"Error reading evaluation file: {e}")

        return decisions

    def load_paper(self, pmid: str) -> Optional[Dict]:
        """Load raw paper JSON from raw/papers/{pmid}.json."""
        # Try exact PMID first
        paper_path = self.raw_path / f"{pmid}.json"
        if paper_path.exists():
            try:
                with open(paper_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Failed to load paper {pmid}: {e}")
                return None

        return None

    def extract_genes(self, text: str) -> Set[str]:
        """Extract known autism genes from text."""
        found_genes = set()
        text_lower = text.lower()

        for gene in AUTISM_GENES:
            # Word boundary matching to avoid partial matches
            pattern = r'\b' + re.escape(gene.lower()) + r'\b'
            if re.search(pattern, text_lower):
                found_genes.add(gene)

        return found_genes

    def extract_datasets(self, text: str) -> Dict[str, Set[str]]:
        """Extract dataset accessions from text."""
        datasets = {}

        for dataset_type, pattern in DATASET_PATTERNS.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                datasets[dataset_type] = set(matches)

        return datasets

    def extract_concepts(self, text: str) -> Set[str]:
        """Extract relevant atlas concepts from text."""
        concepts = set()
        text_lower = text.lower()

        for concept_file, keywords in CONCEPT_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    concepts.add(concept_file)
                    break

        return concepts

    def get_gene_crosslinks(self, genes: Set[str]) -> List[Tuple[str, str]]:
        """Get crosslinks to existing gene wiki pages."""
        crosslinks = []

        for gene in sorted(genes):
            gene_wiki = self.genes_path / f"{gene}.md"
            if gene_wiki.exists():
                crosslinks.append((gene, f"./../../genes/{gene}.md"))

        return crosslinks

    def get_concept_links(self, concepts: Set[str]) -> List[Tuple[str, str]]:
        """Get links to concept pages."""
        links = []

        for concept in sorted(concepts):
            concept_path = self.concepts_path / concept
            if concept_path.exists():
                # Convert filename to display name
                display_name = concept.replace(".md", "").replace("_", " ").title()
                links.append((display_name, f"./../../concepts/{concept}"))

        return links

    def generate_wiki_page(self, paper: Dict, evaluation: Dict) -> str:
        """Generate markdown wiki page for a paper."""
        pmid = paper.get("pmid", evaluation.get("pmid", "unknown"))
        title = paper.get("title", "Unknown Title")
        authors = paper.get("authors", [])
        abstract = paper.get("abstract", "")

        # Extract structured data
        genes = self.extract_genes(abstract + " " + title)
        datasets = self.extract_datasets(abstract)
        concepts = self.extract_concepts(abstract)
        gene_links = self.get_gene_crosslinks(genes)
        concept_links = self.get_concept_links(concepts)

        # Get DOI if available (fallback to empty)
        doi = paper.get("doi", "")

        # Get publication date (fallback to today)
        pub_date = paper.get("publication_date", datetime.now().strftime("%Y-%m-%d"))

        # Get journal if available
        journal = paper.get("journal", "Unknown Journal")

        # Calculate relevance score from evaluation
        relevance_score = evaluation.get("score", 0)

        # Extract abstract summary (first 2-3 sentences or full abstract if short)
        abstract_summary = abstract[:500] + "..." if len(abstract) > 500 else abstract

        # Build YAML front matter
        yaml_lines = [
            "---",
            f"title: {title}",
            f"pmid: {pmid}",
        ]

        if doi:
            yaml_lines.append(f"doi: {doi}")

        yaml_lines.extend([
            f"date: {pub_date}",
            f"journal: {journal}",
            f"evidence_tier: {DEFAULT_EVIDENCE_TIER}",
            f"relevance_score: {relevance_score}",
            f"last_updated: {datetime.now().strftime('%Y-%m-%d')}",
            "---"
        ])

        # Build content
        content_lines = yaml_lines + ["", f"# {title}"]

        # Authors section
        if authors:
            authors_str = ", ".join(authors[:5])
            if len(authors) > 5:
                authors_str += f", et al."
            content_lines.extend(["", "## Authors", "", authors_str])

        # Abstract
        content_lines.extend(["", "## Abstract", "", abstract_summary])

        # Key Genes
        if genes:
            content_lines.extend(["", "## Key Genes", ""])
            for gene in sorted(genes):
                content_lines.append(f"- {gene}")

        # Datasets Referenced
        if datasets:
            content_lines.extend(["", "## Datasets Referenced", ""])
            for dataset_type, accessions in sorted(datasets.items()):
                for accession in sorted(accessions):
                    content_lines.append(f"- {dataset_type}: {accession}")

        # Relevance to Atlas
        if concept_links:
            content_lines.extend(["", "## Relevance to Atlas", ""])
            for concept_name, concept_path in concept_links:
                content_lines.append(f"- [{concept_name}]({concept_path})")

        # Cross-links
        if gene_links:
            content_lines.extend(["", "## Related Genes", ""])
            for gene_name, gene_path in gene_links:
                content_lines.append(f"- [{gene_name}]({gene_path})")

        # Metadata section
        content_lines.extend([
            "",
            "---",
            "",
            f"**PMID:** {pmid}",
            f"**Relevance Score:** {relevance_score}",
            f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}",
        ])

        return "\n".join(content_lines)

    def save_wiki_page(self, pmid: str, content: str) -> bool:
        """Save generated wiki page to findings directory."""
        page_path = self.findings_path / f"{pmid}.md"

        try:
            with open(page_path, 'w') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error saving wiki page for {pmid}: {e}")
            return False

    def update_index(self, pmid: str, title: str) -> bool:
        """Update wiki/index.md to include new finding."""
        if not self.index_path.exists():
            print(f"Warning: Index file not found: {self.index_path}")
            return False

        try:
            with open(self.index_path, 'r') as f:
                content = f.read()

            # Check if PMID already in index
            if f"pmid: {pmid}" in content or f"/{pmid}.md" in content:
                return True  # Already listed

            # Find the Findings section
            findings_marker = "## Findings"
            if findings_marker not in content:
                print(f"Warning: Findings section not found in index")
                return False

            # Find where to insert (after Findings section header, before next section or EOF)
            lines = content.split("\n")
            findings_idx = None
            next_section_idx = None

            for i, line in enumerate(lines):
                if line.strip() == findings_marker:
                    findings_idx = i
                elif findings_idx is not None and line.startswith("##") and line != findings_marker:
                    next_section_idx = i
                    break

            if findings_idx is None:
                print("Warning: Could not find Findings section")
                return False

            # Determine insertion point (after any placeholder text)
            insert_idx = findings_idx + 1
            while insert_idx < len(lines) and (
                not lines[insert_idx].strip() or
                "(Placeholder" in lines[insert_idx]
            ):
                insert_idx += 1

            # Remove placeholder if present
            if insert_idx < len(lines) and "(Placeholder" in lines[insert_idx]:
                lines.pop(insert_idx)

            # Insert new finding entry
            new_entry = f"- [{title}](./findings/{pmid}.md) -- PMID: {pmid}"
            lines.insert(insert_idx, new_entry)

            updated_content = "\n".join(lines)

            with open(self.index_path, 'w') as f:
                f.write(updated_content)

            return True

        except Exception as e:
            print(f"Error updating index: {e}")
            return False

    def log_integration(self, pmid: str, title: str, status: str = "success",
                       details: Optional[Dict] = None) -> bool:
        """Log integration to integration_log.jsonl."""
        log_entry = {
            "pmid": pmid,
            "title": title,
            "status": status,
            "timestamp": datetime.now().isoformat(),
            "details": details or {}
        }

        try:
            with open(self.integration_log_path, 'a') as f:
                f.write(json.dumps(log_entry) + "\n")
            return True
        except Exception as e:
            print(f"Error logging integration: {e}")
            return False

    def integrate_papers(self, decisions: List[Dict], dry_run: bool = False) -> Dict:
        """Integrate papers marked with status INTEGRATE."""
        results = {
            "total_decisions": len(decisions),
            "integrate_count": 0,
            "success_count": 0,
            "skip_count": 0,
            "errors": []
        }

        for decision in decisions:
            status = decision.get("status", "")
            pmid = decision.get("pmid", "")
            title = decision.get("title", "Unknown")

            if status != "INTEGRATE":
                results["skip_count"] += 1
                continue

            results["integrate_count"] += 1

            # Load paper
            paper = self.load_paper(pmid)
            if not paper:
                error_msg = f"Could not load paper {pmid}"
                print(f"Error: {error_msg}")
                results["errors"].append(error_msg)
                if not dry_run:
                    self.log_integration(pmid, title, "error", {"reason": error_msg})
                continue

            # Generate wiki page
            try:
                wiki_content = self.generate_wiki_page(paper, decision)
            except Exception as e:
                error_msg = f"Failed to generate wiki page for {pmid}: {e}"
                print(f"Error: {error_msg}")
                results["errors"].append(error_msg)
                if not dry_run:
                    self.log_integration(pmid, title, "error", {"reason": str(e)})
                continue

            # Save wiki page
            if not dry_run:
                if not self.save_wiki_page(pmid, wiki_content):
                    error_msg = f"Failed to save wiki page for {pmid}"
                    print(f"Error: {error_msg}")
                    results["errors"].append(error_msg)
                    self.log_integration(pmid, title, "error", {"reason": error_msg})
                    continue

                # Update index
                if not self.update_index(pmid, paper.get("title", title)):
                    print(f"Warning: Failed to update index for {pmid}")

                # Log integration
                self.log_integration(pmid, title, "success")
                results["success_count"] += 1
            else:
                results["success_count"] += 1
                print(f"[DRY-RUN] Would integrate: {pmid} - {title}")

        return results


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Paper Integration Agent for Autism Genomics Atlas"
    )
    parser.add_argument(
        "--input-file",
        type=Path,
        default=ATLAS_BASE_PATH / "logs" / "evaluation_decisions.jsonl",
        help="Path to evaluation decisions JSONL file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run without making changes (preview mode)"
    )
    parser.add_argument(
        "--base-path",
        type=Path,
        default=ATLAS_BASE_PATH,
        help="Base path for atlas project"
    )

    args = parser.parse_args()

    # Initialize integrator
    integrator = PaperIntegrator(base_path=args.base_path)

    # Read evaluation decisions
    print(f"Reading evaluation decisions from {args.input_file}")
    decisions = integrator.read_evaluation_decisions(args.input_file)
    print(f"Loaded {len(decisions)} decisions")

    # Integrate papers
    mode = "DRY-RUN" if args.dry_run else "EXECUTE"
    print(f"\n[{mode}] Starting paper integration...")
    results = integrator.integrate_papers(decisions, dry_run=args.dry_run)

    # Print summary
    print(f"\n=== Integration Summary ===")
    print(f"Total decisions processed: {results['total_decisions']}")
    print(f"Papers to integrate: {results['integrate_count']}")
    print(f"Successfully integrated: {results['success_count']}")
    print(f"Skipped (not INTEGRATE status): {results['skip_count']}")

    if results['errors']:
        print(f"\nErrors ({len(results['errors'])}):")
        for error in results['errors']:
            print(f"  - {error}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
