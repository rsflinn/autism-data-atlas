#!/usr/bin/env python3
"""
Relevance scoring agent for the autism genomics atlas.

Scores papers based on keyword/concept matching without LLM.
Categorizes papers into integration queues based on relevance score.

Scoring criteria (0-50 total):
- Direct autism relevance (0-10)
- Noncoding/regulatory variant relevance (0-10)
- Dataset availability (0-10)
- Novelty signals (0-10)
- Cell-type/phenotype specificity (0-10)
"""

import json
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, Any, Tuple


# Key genes for autism atlas
KEY_GENES = {
    "MEF2C", "SCN2A", "FOXP1", "TCF4", "CDKL5", "GRIN2B", "SHANK3",
    "SYNGAP1", "RBFOX1", "CACNA1A", "KCNB1", "SLC6A1", "DYRK1A",
    "MECP2", "MYT1L", "EP300", "BCL11A"
}


def normalize_text(text: str) -> str:
    """Normalize text for matching (lowercase, strip whitespace)."""
    if not text:
        return ""
    return text.lower().strip()


def check_keywords(text: str, keywords: list) -> int:
    """
    Check if any keywords are in the text.
    Returns 1 if found, 0 otherwise.
    """
    if not text:
        return 0
    normalized = normalize_text(text)
    for keyword in keywords:
        if normalize_text(keyword) in normalized:
            return 1
    return 0


def check_keywords_multiple(text: str, keywords: list, points_per: int = 1, max_points: int = None) -> int:
    """
    Check multiple keywords and sum points.

    Args:
        text: Text to search
        keywords: List of keywords to check
        points_per: Points awarded per keyword found
        max_points: Maximum total points to return

    Returns:
        Total points, capped at max_points if provided
    """
    if not text:
        return 0

    normalized = normalize_text(text)
    points = 0

    for keyword in keywords:
        if normalize_text(keyword) in normalized:
            points += points_per

    if max_points is not None:
        points = min(points, max_points)

    return points


def score_direct_autism_relevance(paper: Dict[str, Any]) -> Tuple[int, Dict[str, int]]:
    """
    Score direct autism relevance (0-10).

    - "autism" or "ASD" in title: +5
    - "autism" or "ASD" in abstract: +3
    - "neurodevelopmental" in title/abstract: +2
    """
    breakdown = {}
    score = 0

    title = paper.get("title", "")
    abstract = paper.get("abstract", "")

    # Title autism relevance
    if check_keywords(title, ["autism", "ASD"]):
        breakdown["autism_in_title"] = 5
        score += 5

    # Abstract autism relevance
    if check_keywords(abstract, ["autism", "ASD"]):
        breakdown["autism_in_abstract"] = 3
        score += 3

    # Neurodevelopmental relevance
    if check_keywords(title, ["neurodevelopmental"]) or check_keywords(abstract, ["neurodevelopmental"]):
        breakdown["neurodevelopmental"] = 2
        score += 2

    return min(score, 10), breakdown


def score_noncoding_regulatory(paper: Dict[str, Any]) -> Tuple[int, Dict[str, int]]:
    """
    Score noncoding/regulatory variant relevance (0-10).

    Any of: "noncoding", "non-coding", "regulatory variant", "enhancer",
    "promoter", "GWAS", "polygenic", "common variant", "SNP" in abstract: +3 each, max 10
    """
    breakdown = {}
    abstract = paper.get("abstract", "")

    keywords = [
        "noncoding", "non-coding", "regulatory variant", "enhancer",
        "promoter", "GWAS", "polygenic", "common variant", "SNP"
    ]

    points = check_keywords_multiple(abstract, keywords, points_per=3, max_points=10)

    if points > 0:
        breakdown["noncoding_regulatory"] = points

    return points, breakdown


def score_dataset_availability(paper: Dict[str, Any]) -> Tuple[int, Dict[str, int]]:
    """
    Score dataset availability (0-10).

    - "GEO" or "GSE" or "dbGaP" or "SFARI" or "SPARK" in abstract: +5
    - "supplementary" or "data availability" in abstract: +3
    - "open access" in abstract: +2
    """
    breakdown = {}
    score = 0
    abstract = paper.get("abstract", "")

    # Public database availability
    if check_keywords(abstract, ["GEO", "GSE", "dbGaP", "SFARI", "SPARK"]):
        breakdown["public_databases"] = 5
        score += 5

    # Supplementary data
    if check_keywords(abstract, ["supplementary", "data availability"]):
        breakdown["supplementary_data"] = 3
        score += 3

    # Open access
    if check_keywords(abstract, ["open access"]):
        breakdown["open_access"] = 2
        score += 2

    return min(score, 10), breakdown


def score_novelty_signals(paper: Dict[str, Any]) -> Tuple[int, Dict[str, int]]:
    """
    Score novelty signals (0-10).

    - "whole genome" or "WGS" in abstract: +3
    - "single-cell" or "scRNA" in abstract: +3
    - "organoid" in abstract: +2
    - "CRISPR" or "perturbation" in abstract: +2
    """
    breakdown = {}
    score = 0
    abstract = paper.get("abstract", "")

    # Whole genome sequencing
    if check_keywords(abstract, ["whole genome", "WGS"]):
        breakdown["whole_genome"] = 3
        score += 3

    # Single-cell methods
    if check_keywords(abstract, ["single-cell", "single cell", "scRNA", "sc-RNA"]):
        breakdown["single_cell"] = 3
        score += 3

    # Organoid work
    if check_keywords(abstract, ["organoid"]):
        breakdown["organoid"] = 2
        score += 2

    # CRISPR/perturbation
    if check_keywords(abstract, ["CRISPR", "perturbation"]):
        breakdown["crispr_perturbation"] = 2
        score += 2

    return min(score, 10), breakdown


def score_cell_type_phenotype(paper: Dict[str, Any]) -> Tuple[int, Dict[str, int]]:
    """
    Score cell-type/phenotype specificity (0-10).

    - "cell type" or "cell-type" or "neuron" or "excitatory" or "inhibitory" in abstract: +3
    - "epilepsy" or "seizure" in abstract: +2
    - "severity" or "phenotype" in abstract: +2
    - Key genes in title/abstract: +3
    """
    breakdown = {}
    score = 0

    title = paper.get("title", "")
    abstract = paper.get("abstract", "")

    # Cell type specificity
    if check_keywords(abstract, ["cell type", "cell-type", "neuron", "excitatory", "inhibitory"]):
        breakdown["cell_type_specificity"] = 3
        score += 3

    # Phenotype keywords
    if check_keywords(abstract, ["epilepsy", "seizure"]):
        breakdown["epilepsy_seizure"] = 2
        score += 2

    # Severity/phenotype
    if check_keywords(abstract, ["severity", "phenotype"]):
        breakdown["severity_phenotype"] = 2
        score += 2

    # Key genes
    combined_text = f"{title} {abstract}".lower()
    for gene in KEY_GENES:
        if gene.lower() in combined_text:
            breakdown["key_genes"] = 3
            score += 3
            break  # Only award once

    return min(score, 10), breakdown


def score_paper(paper: Dict[str, Any]) -> Tuple[int, Dict[str, int]]:
    """
    Score a paper on relevance to autism atlas.

    Returns:
        Tuple of (total_score, detailed_breakdown)
    """
    breakdown = {}
    total_score = 0

    # Score each category
    autism_score, autism_breakdown = score_direct_autism_relevance(paper)
    total_score += autism_score
    breakdown.update(autism_breakdown)

    noncoding_score, noncoding_breakdown = score_noncoding_regulatory(paper)
    total_score += noncoding_score
    breakdown.update(noncoding_breakdown)

    dataset_score, dataset_breakdown = score_dataset_availability(paper)
    total_score += dataset_score
    breakdown.update(dataset_breakdown)

    novelty_score, novelty_breakdown = score_novelty_signals(paper)
    total_score += novelty_score
    breakdown.update(novelty_breakdown)

    celltype_score, celltype_breakdown = score_cell_type_phenotype(paper)
    total_score += celltype_score
    breakdown.update(celltype_breakdown)

    return min(total_score, 50), breakdown


def load_existing_pmids(output_file: Path) -> set:
    """Load PMIDs that have already been scored."""
    if not output_file.exists():
        return set()

    pmids = set()
    try:
        with open(output_file, 'r') as f:
            for line in f:
                if line.strip():
                    entry = json.loads(line)
                    pmids.add(entry.get("pmid"))
    except Exception as e:
        print(f"Warning: Could not load existing PMIDs: {e}")

    return pmids


def categorize_status(score: int) -> str:
    """Categorize paper based on score."""
    if score >= 15:
        return "INTEGRATE"
    elif score >= 10:
        return "REVIEW"
    else:
        return "SKIP"


def main():
    parser = argparse.ArgumentParser(
        description="Score papers for relevance to autism atlas"
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("/sessions/friendly-serene-ride/mnt/autism-data-atlas/raw/papers"),
        help="Directory containing paper JSON files"
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=Path("/sessions/friendly-serene-ride/mnt/autism-data-atlas/logs/evaluation_decisions.jsonl"),
        help="Output JSONL file for scored results"
    )

    args = parser.parse_args()

    # Create output directory if needed
    args.output_file.parent.mkdir(parents=True, exist_ok=True)

    # Load existing scores
    existing_pmids = load_existing_pmids(args.output_file)
    print(f"Found {len(existing_pmids)} previously scored papers")

    # Find all JSON files in input directory
    if not args.input_dir.exists():
        print(f"Input directory does not exist: {args.input_dir}")
        print("No papers to score.")
        return

    paper_files = list(args.input_dir.glob("*.json"))
    print(f"Found {len(paper_files)} paper JSON files")

    if not paper_files:
        print("No paper files found. Exiting.")
        return

    # Track results
    results_by_status = defaultdict(list)
    scored_count = 0
    skipped_count = 0

    # Score each paper
    for paper_file in paper_files:
        try:
            with open(paper_file, 'r') as f:
                paper = json.load(f)
        except Exception as e:
            print(f"Error reading {paper_file}: {e}")
            continue

        pmid = paper.get("pmid")

        # Skip if already scored
        if pmid and pmid in existing_pmids:
            skipped_count += 1
            continue

        # Score the paper
        score, breakdown = score_paper(paper)
        status = categorize_status(score)

        # Create output entry
        entry = {
            "pmid": pmid,
            "title": paper.get("title", ""),
            "score": score,
            "score_breakdown": breakdown,
            "status": status,
            "timestamp": datetime.utcnow().isoformat()
        }

        # Append to output file
        with open(args.output_file, 'a') as f:
            f.write(json.dumps(entry) + "\n")

        results_by_status[status].append(entry)
        scored_count += 1

    # Print summary
    print("\n" + "=" * 60)
    print("SCORING SUMMARY")
    print("=" * 60)
    print(f"Papers scored: {scored_count}")
    print(f"Papers skipped (already scored): {skipped_count}")
    print(f"\nResults by status:")
    print(f"  INTEGRATE (score >= 25): {len(results_by_status['INTEGRATE'])}")
    print(f"  REVIEW    (15-24):       {len(results_by_status['REVIEW'])}")
    print(f"  SKIP      (< 15):        {len(results_by_status['SKIP'])}")
    print(f"\nOutput file: {args.output_file}")


if __name__ == "__main__":
    main()
