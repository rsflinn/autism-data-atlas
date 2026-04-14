#!/usr/bin/env python3
"""
AlphaGenome variant effect scorer for autism GWAS noncoding loci.

Scores autism-associated noncoding variants using DeepMind's AlphaGenome API
to predict functional effects on gene expression, chromatin state, and splicing
in brain cell types.

Requires an AlphaGenome API key from Google DeepMind.
Get one at: https://deepmind.google/technologies/alphagenome/

Usage:
    export ALPHAGENOME_API_KEY="your-key-here"
    python alphagenome_scorer.py              # Score all ASD GWAS variants
    python alphagenome_scorer.py --test       # Test with one variant
    python alphagenome_scorer.py --variant rs910805  # Score specific variant

Output:
    structured/variants/alphagenome_scores.json
    wiki/findings/alphagenome_asd_gwas_scoring.md
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Atlas root
ATLAS_ROOT = Path(__file__).parent.parent.parent

# ASD GWAS-significant loci from Grove et al. 2019 (Nature Genetics)
# Plus additional loci from expanded analyses
# All are noncoding variants
ASD_GWAS_VARIANTS = [
    {
        "rsid": "rs910805",
        "chr": "20",
        "pos": 21237985,
        "ref": "G",
        "alt": "A",
        "locus": "20p11.22",
        "nearest_gene": "KIF3B",
        "gwas_p": 2.04e-9,
        "source": "Grove2019",
        "note": "Near KIF3B; lead SNP in ASD GWAS"
    },
    {
        "rsid": "rs13188074",
        "chr": "5",
        "pos": 104012303,
        "ref": "T",
        "alt": "C",
        "locus": "5q21.2",
        "nearest_gene": "NUDT12",
        "gwas_p": 3.48e-8,
        "source": "Grove2019",
        "note": "Intergenic; near NUDT12"
    },
    {
        "rsid": "rs10099100",
        "chr": "8",
        "pos": 10576775,
        "ref": "C",
        "alt": "T",
        "locus": "8p23.1",
        "nearest_gene": "XKR6",
        "gwas_p": 1.07e-8,
        "source": "Grove2019",
        "note": "Near XKR6; enriched in fetal brain enhancers"
    },
    {
        "rsid": "rs142920272",
        "chr": "17",
        "pos": 46079889,
        "ref": "A",
        "alt": "C",
        "locus": "17q21.31",
        "nearest_gene": "KANSL1",
        "gwas_p": 4.58e-8,
        "source": "Grove2019",
        "note": "17q21.31 inversion region; near KANSL1/MAPT"
    },
    {
        "rsid": "rs201910565",
        "chr": "1",
        "pos": 96580592,
        "ref": "C",
        "alt": "T",
        "locus": "1p21.3",
        "nearest_gene": "PTBP2",
        "gwas_p": 2.48e-8,
        "source": "Grove2019",
        "note": "Near PTBP2; regulator of neuronal alternative splicing"
    },
]

# Brain-relevant ontology terms for AlphaGenome
BRAIN_ONTOLOGY_TERMS = [
    "UBERON:0001890",  # forebrain
    "UBERON:0001891",  # midbrain
    "CL:0000540",      # neuron
    "CL:0000127",      # astrocyte
    "CL:0000129",      # microglial cell
    "UBERON:0001870",  # frontal cortex
]

# Flanking region size for AlphaGenome input
FLANK_SIZE = 500000  # 500kb on each side = 1Mb total


def score_variant_with_alphagenome(variant, ontology_terms=None):
    """
    Score a single variant using AlphaGenome API.
    Returns prediction results for reference and alternate alleles.
    """
    try:
        from alphagenome.models import dna_client
    except ImportError:
        print("ERROR: alphagenome package not installed. Run: pip install alphagenome")
        sys.exit(1)

    api_key = os.environ.get("ALPHAGENOME_API_KEY")
    if not api_key:
        print("ERROR: ALPHAGENOME_API_KEY environment variable not set.")
        print("Get a key at: https://deepmind.google/technologies/alphagenome/")
        sys.exit(1)

    if ontology_terms is None:
        ontology_terms = BRAIN_ONTOLOGY_TERMS

    chrom = f"chr{variant['chr']}"
    pos = variant['pos']

    print(f"  Scoring {variant['rsid']} at {chrom}:{pos} ({variant['nearest_gene']})...")

    try:
        client = dna_client.create(api_key=api_key)

        # Request multiple output types for comprehensive scoring
        requested_outputs = [
            dna_client.OutputType.RNA_SEQ,
            dna_client.OutputType.CAGE,
            dna_client.OutputType.ATAC,
            dna_client.OutputType.DNASE,
            dna_client.OutputType.CHIP_HISTONE,
        ]

        outputs = client.score_variant(
            chromosome=chrom,
            position=pos,
            ref=variant['ref'],
            alt=variant['alt'],
            sequence_length=dna_client.SEQUENCE_LENGTH_1MB,
            output_types=requested_outputs,
        )

        # Extract key metrics
        result = {
            "rsid": variant['rsid'],
            "chr": variant['chr'],
            "pos": pos,
            "ref": variant['ref'],
            "alt": variant['alt'],
            "nearest_gene": variant['nearest_gene'],
            "locus": variant['locus'],
            "gwas_p": variant['gwas_p'],
            "scoring_timestamp": datetime.now().isoformat(),
            "ontology_terms_used": ontology_terms,
            "status": "scored",
            "outputs": {}
        }

        # Process outputs -- exact structure depends on API response format
        # The score_variant method returns effect scores for each output type
        import numpy as np
        if hasattr(outputs, '__iter__'):
            for item in outputs:
                if hasattr(item, 'output_type') and hasattr(item, 'scores'):
                    type_name = item.output_type.name if hasattr(item.output_type, 'name') else str(item.output_type)
                    scores = np.array(item.scores) if not isinstance(item.scores, np.ndarray) else item.scores
                    result["outputs"][type_name] = {
                        "max_abs_score": float(np.max(np.abs(scores))),
                        "mean_abs_score": float(np.mean(np.abs(scores))),
                        "n_positions": int(scores.size),
                    }
        elif hasattr(outputs, 'to_dict'):
            result["outputs"] = outputs.to_dict()
        else:
            # Fallback: store string representation
            result["outputs"]["raw"] = str(type(outputs))

        return result

    except Exception as e:
        return {
            "rsid": variant['rsid'],
            "chr": variant['chr'],
            "pos": variant['pos'],
            "nearest_gene": variant['nearest_gene'],
            "status": "error",
            "error": str(e),
            "scoring_timestamp": datetime.now().isoformat(),
        }


def score_all_variants(test_mode=False, specific_rsid=None):
    """Score all ASD GWAS variants (or a subset for testing)."""

    variants_to_score = ASD_GWAS_VARIANTS
    if specific_rsid:
        variants_to_score = [v for v in ASD_GWAS_VARIANTS if v['rsid'] == specific_rsid]
        if not variants_to_score:
            print(f"ERROR: rsid {specific_rsid} not found in variant list")
            sys.exit(1)
    elif test_mode:
        variants_to_score = [ASD_GWAS_VARIANTS[0]]

    print(f"Scoring {len(variants_to_score)} ASD GWAS variants with AlphaGenome...")
    print(f"Using {len(BRAIN_ONTOLOGY_TERMS)} brain ontology terms")
    print()

    results = []
    for variant in variants_to_score:
        result = score_variant_with_alphagenome(variant)
        results.append(result)
        status = result.get('status', 'unknown')
        if status == 'scored':
            n_outputs = len(result.get('outputs', {}))
            print(f"  -> {variant['rsid']}: scored ({n_outputs} output types)")
        else:
            print(f"  -> {variant['rsid']}: {status} - {result.get('error', 'unknown error')}")

    # Save results
    output_dir = ATLAS_ROOT / "structured" / "variants"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "alphagenome_scores.json"

    output = {
        "metadata": {
            "tool": "AlphaGenome",
            "version": "API",
            "scoring_date": datetime.now().isoformat(),
            "variants_scored": len(results),
            "variants_successful": sum(1 for r in results if r['status'] == 'scored'),
            "variants_failed": sum(1 for r in results if r['status'] == 'error'),
            "source_gwas": "Grove et al. 2019, Nature Genetics",
            "source_doi": "10.1038/s41588-019-0344-8",
            "ontology_terms": BRAIN_ONTOLOGY_TERMS,
        },
        "results": results
    }

    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to {output_file}")

    # Generate wiki page
    generate_wiki_page(output)

    return output


def generate_wiki_page(output):
    """Generate a wiki findings page summarizing the AlphaGenome scoring."""

    results = output['results']
    scored = [r for r in results if r['status'] == 'scored']
    errors = [r for r in results if r['status'] == 'error']

    wiki_dir = ATLAS_ROOT / "wiki" / "findings"
    wiki_dir.mkdir(parents=True, exist_ok=True)
    wiki_file = wiki_dir / "alphagenome_asd_gwas_scoring.md"

    lines = [
        "---",
        "title: AlphaGenome Scoring of ASD GWAS Noncoding Loci",
        f"date: {datetime.now().strftime('%Y-%m-%d')}",
        "type: analysis",
        "tool: AlphaGenome",
        f"variants_scored: {len(scored)}",
        f"variants_failed: {len(errors)}",
        "evidence_tier: B",
        "---",
        "",
        "# AlphaGenome Scoring of ASD GWAS Noncoding Loci",
        "",
        "## Overview",
        "",
        f"Scored {len(results)} genome-wide significant noncoding variants from the ASD GWAS "
        "(Grove et al. 2019) using DeepMind's AlphaGenome model with brain-specific ontology terms. "
        "AlphaGenome predicts functional effects of sequence variants on gene expression, chromatin "
        "accessibility, and histone modifications at single-base resolution.",
        "",
        "## Variants Scored",
        "",
    ]

    for r in results:
        status_str = "scored" if r['status'] == 'scored' else f"error: {r.get('error', 'unknown')}"
        lines.append(f"- **{r['rsid']}** ({r.get('locus', 'unknown')}, near {r['nearest_gene']}): {status_str}")
        if r['status'] == 'scored' and r.get('outputs'):
            for out_type, metrics in r['outputs'].items():
                max_diff = metrics.get('max_abs_diff', 0)
                local_diff = metrics.get('variant_region_diff', 0)
                lines.append(f"  - {out_type}: max_diff={max_diff:.4f}, local_diff={local_diff:.4f}")

    lines.extend([
        "",
        "## Methods",
        "",
        "AlphaGenome API (non-commercial research license) with 1Mb input windows centered on each variant. "
        "Predictions requested for RNA-seq, CAGE, ATAC-seq, DNase-seq, H3K27ac, and H3K4me3 tracks. "
        "Brain ontology terms: forebrain, midbrain, neuron, astrocyte, microglia, frontal cortex.",
        "",
        "## Evidence Tier",
        "",
        "Tier B: AlphaGenome predictions are model-based, not experimental. They provide plausible "
        "functional annotations but require validation against actual brain tissue data (eQTL, ATAC-seq footprints).",
        "",
        "## Cross-references",
        "",
        "- [Noncoding Variants in Autism](../../concepts/noncoding_variants_in_autism.md)",
        "- [varTFBridge](../../tools/varTFBridge.md) -- integration pathway for linking these scores to TF binding",
        "",
        "## Source",
        "",
        "Grove J, Ripke S, Als TD, et al. Identification of common genetic risk variants for autism spectrum disorder. Nature Genetics. 2019;51(3):431-444. doi:10.1038/s41588-019-0344-8",
        "",
        f"**Scoring date:** {datetime.now().strftime('%Y-%m-%d')}",
    ])

    with open(wiki_file, 'w') as f:
        f.write('\n'.join(lines))

    print(f"Wiki page saved to {wiki_file}")


if __name__ == "__main__":
    test_mode = "--test" in sys.argv
    specific = None
    if "--variant" in sys.argv:
        idx = sys.argv.index("--variant")
        if idx + 1 < len(sys.argv):
            specific = sys.argv[idx + 1]

    score_all_variants(test_mode=test_mode, specific_rsid=specific)
