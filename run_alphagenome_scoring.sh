#!/bin/bash
# AlphaGenome ASD GWAS Variant Scorer
# Run this on your Mac from the autism-data-atlas folder
#
# Prerequisites:
#   brew install python3    (if you don't have a proper Python)
#   pip3 install alphagenome
#
# Usage:
#   chmod +x run_alphagenome_scoring.sh
#   ./run_alphagenome_scoring.sh YOUR_API_KEY

if [ -z "$1" ]; then
    echo "Usage: ./run_alphagenome_scoring.sh YOUR_ALPHAGENOME_API_KEY"
    exit 1
fi

export ALPHAGENOME_API_KEY="$1"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 not found. Install with: brew install python3"
    exit 1
fi

# Check alphagenome package
python3 -c "from alphagenome.models import dna_client" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing alphagenome package..."
    pip3 install alphagenome
fi

echo "=== AlphaGenome ASD GWAS Variant Scorer ==="
echo ""
echo "Scoring 5 GWAS-significant autism noncoding variants"
echo "from Grove et al. 2019 (Nature Genetics)"
echo ""

python3 agents/scorers/alphagenome_scorer.py "$@"
