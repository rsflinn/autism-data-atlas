#!/usr/bin/env python3
"""
PubMed Scanner for Autism Genomics Atlas
Queries PubMed for papers matching autism + genomic variant queries
Saves results as JSON and logs scan information
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Set, Optional
from Bio import Entrez

# Configuration
ENTREZ_EMAIL = "ryan_flinn@outlook.com"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAPERS_DIR = os.path.join(BASE_DIR, "raw", "papers")
SCAN_LOGS_DIR = os.path.join(BASE_DIR, "raw", "scan_logs")

# Ensure Entrez email is set
Entrez.email = ENTREZ_EMAIL


class PubMedScanner:
    def __init__(self, days: int = 7, backfill: bool = False):
        """
        Initialize the PubMed scanner.

        Args:
            days: Number of days to search back (default 7)
            backfill: If True, search from 2015-present instead of recent days
        """
        self.days = days
        self.backfill = backfill
        self.papers_found: Dict[str, Dict] = {}
        self.scan_log: Dict = {
            "timestamp": datetime.now().isoformat(),
            "queries": [],
            "total_results": 0,
            "new_papers": 0,
            "existing_papers": 0,
            "pmids_found": []
        }

    def get_date_range(self) -> str:
        """Get the date range filter for PubMed query."""
        if self.backfill:
            return "2015-01-01[PDAT]:2099-12-31[PDAT]"
        else:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=self.days)
            start_str = start_date.strftime("%Y-%m-%d")
            end_str = end_date.strftime("%Y-%m-%d")
            return f"{start_str}[PDAT]:{end_str}[PDAT]"

    def build_queries(self) -> List[tuple]:
        """Build all query sets for searching."""
        date_range = self.get_date_range()

        queries = [
            (
                'autism AND (noncoding OR "non-coding" OR "regulatory variant" '
                'OR enhancer OR promoter OR "polygenic risk score")',
                "Autism + noncoding/regulatory variants"
            ),
            (
                'autism AND ("whole genome sequencing" OR GWAS OR "common variant")',
                "Autism + WGS/GWAS/common variants"
            ),
            (
                'epilepsy AND autism AND (GABA OR glutamate OR "ion channel") AND genetics',
                "Epilepsy + autism + ion channels/neurotransmitters"
            ),
        ]

        # Add gene-specific queries
        genes = ["MEF2C", "SCN2A", "FOXP1", "TCF4", "CDKL5", "DYRK1A"]
        for gene in genes:
            query = f'{gene} AND (autism OR neurodevelopmental)'
            queries.append((query, f"Gene-specific: {gene}"))

        return queries

    def fetch_paper_details(self, pmid: str) -> Optional[Dict]:
        """
        Fetch detailed information for a paper given its PMID.

        Args:
            pmid: PubMed ID

        Returns:
            Dictionary with paper details or None if fetch fails
        """
        try:
            handle = Entrez.efetch(db="pubmed", id=pmid, rettype="xml", retmode="xml")
            record = Entrez.read(handle)
            handle.close()

            if not record or "PubmedArticle" not in record:
                return None

            article = record["PubmedArticle"][0]["MedlineCitation"]["Article"]

            # Extract basic fields
            paper = {
                "pmid": pmid,
                "title": article.get("ArticleTitle", ""),
                "authors": [],
                "abstract": "",
                "journal": "",
                "date": "",
                "mesh_terms": [],
                "doi": ""
            }

            # Authors
            if "AuthorList" in article:
                for author in article["AuthorList"]:
                    if "LastName" in author and "ForeName" in author:
                        name = f"{author['LastName']}, {author['ForeName']}"
                    elif "LastName" in author:
                        name = author["LastName"]
                    else:
                        name = str(author)
                    paper["authors"].append(name)

            # Abstract
            if "Abstract" in article and "AbstractText" in article["Abstract"]:
                abstract_parts = article["Abstract"]["AbstractText"]
                if isinstance(abstract_parts, list):
                    paper["abstract"] = " ".join(str(part) for part in abstract_parts)
                else:
                    paper["abstract"] = str(abstract_parts)

            # Journal
            if "Journal" in article:
                paper["journal"] = article["Journal"].get("Title", "")

            # Publication date
            if "ArticleDate" in article:
                date_obj = article["ArticleDate"][0]
                year = date_obj.get("Year", "")
                month = date_obj.get("Month", "01").zfill(2)
                day = date_obj.get("Day", "01").zfill(2)
                paper["date"] = f"{year}-{month}-{day}"
            elif "PubDate" in article["Journal"]:
                pub_date = article["Journal"]["PubDate"]
                year = pub_date.get("Year", "")
                month = pub_date.get("Month", "01")
                month_map = {
                    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
                    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                    "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
                }
                month = month_map.get(month, "01")
                day = pub_date.get("Day", "01").zfill(2)
                paper["date"] = f"{year}-{month}-{day}"

            # MeSH terms
            if "MeshHeadingList" in record["PubmedArticle"][0]["MedlineCitation"]:
                mesh_list = record["PubmedArticle"][0]["MedlineCitation"]["MeshHeadingList"]
                for mesh in mesh_list:
                    if "DescriptorName" in mesh:
                        paper["mesh_terms"].append(mesh["DescriptorName"])

            # DOI
            if "ELocationID" in article:
                for eloc in article["ELocationID"]:
                    if eloc.get("EIdType") == "doi":
                        paper["doi"] = str(eloc)
                        break

            return paper

        except Exception as e:
            print(f"Error fetching details for PMID {pmid}: {e}", file=sys.stderr)
            return None

    def run_query(self, query: str, query_name: str, date_range: str) -> Set[str]:
        """
        Run a single PubMed query.

        Args:
            query: PubMed search query
            query_name: Human-readable name for the query
            date_range: Date range filter

        Returns:
            Set of PMIDs found
        """
        try:
            # Build the full query with date range
            full_query = f"{query} AND {date_range}"

            print(f"  Searching: {query_name}")
            print(f"    Query: {full_query}")

            # Search
            handle = Entrez.esearch(
                db="pubmed",
                term=full_query,
                retmax=10000,  # Max results
                rettype="json"
            )
            result = json.loads(handle.read().decode())
            handle.close()

            pmids = set(result.get("esearchresult", {}).get("idlist", []))
            print(f"    Found {len(pmids)} papers")

            query_info = {
                "query_name": query_name,
                "query_text": query,
                "date_range": date_range,
                "results": len(pmids),
                "pmids": list(pmids)
            }
            self.scan_log["queries"].append(query_info)
            self.scan_log["total_results"] += len(pmids)
            self.scan_log["pmids_found"].extend(list(pmids))

            return pmids

        except Exception as e:
            print(f"Error running query '{query_name}': {e}", file=sys.stderr)
            return set()

    def load_existing_pmids(self) -> Set[str]:
        """Load PMIDs of already-scanned papers."""
        existing = set()
        if not os.path.exists(PAPERS_DIR):
            os.makedirs(PAPERS_DIR, exist_ok=True)
            return existing

        for filename in os.listdir(PAPERS_DIR):
            if filename.endswith(".json"):
                pmid = filename.replace(".json", "")
                existing.add(pmid)

        return existing

    def save_paper(self, paper: Dict) -> bool:
        """Save a paper as JSON."""
        try:
            os.makedirs(PAPERS_DIR, exist_ok=True)
            filepath = os.path.join(PAPERS_DIR, f"{paper['pmid']}.json")
            with open(filepath, 'w') as f:
                json.dump(paper, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving paper {paper.get('pmid')}: {e}", file=sys.stderr)
            return False

    def save_scan_log(self):
        """Save the scan log as JSON."""
        try:
            os.makedirs(SCAN_LOGS_DIR, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(SCAN_LOGS_DIR, f"scan_{timestamp}.json")

            # Deduplicate PMIDs in log
            self.scan_log["pmids_found"] = list(set(self.scan_log["pmids_found"]))
            self.scan_log["total_unique_results"] = len(self.scan_log["pmids_found"])

            with open(filepath, 'w') as f:
                json.dump(self.scan_log, f, indent=2)

            print(f"\nScan log saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"Error saving scan log: {e}", file=sys.stderr)
            return None

    def scan(self):
        """Run the full scanning pipeline."""
        print(f"\n{'='*70}")
        print(f"PubMed Scanner - Autism Genomics Atlas")
        print(f"{'='*70}")
        print(f"Start time: {datetime.now().isoformat()}")
        print(f"Backfill mode: {self.backfill}")
        if not self.backfill:
            print(f"Search window: Last {self.days} days")
        else:
            print(f"Search window: 2015-present")
        print(f"{'='*70}\n")

        # Load existing papers
        existing_pmids = self.load_existing_pmids()
        print(f"Existing papers in database: {len(existing_pmids)}\n")

        # Build and run queries
        queries = self.build_queries()
        date_range = self.get_date_range()

        all_pmids = set()

        for query, query_name in queries:
            pmids = self.run_query(query, query_name, date_range)
            all_pmids.update(pmids)

        # Deduplicate
        all_pmids_list = list(all_pmids)
        print(f"\n{'='*70}")
        print(f"Total unique PMIDs found: {len(all_pmids_list)}")
        print(f"{'='*70}\n")

        # Fetch details and save new papers
        new_count = 0
        existing_count = 0

        for i, pmid in enumerate(all_pmids_list, 1):
            print(f"[{i}/{len(all_pmids_list)}] Processing PMID {pmid}...", end=" ")

            if pmid in existing_pmids:
                print("(already exists)")
                existing_count += 1
                continue

            paper = self.fetch_paper_details(pmid)
            if paper:
                self.save_paper(paper)
                self.papers_found[pmid] = paper
                new_count += 1
                print("(new - saved)")
            else:
                print("(fetch failed)")

        self.scan_log["new_papers"] = new_count
        self.scan_log["existing_papers"] = existing_count

        # Save scan log
        log_path = self.save_scan_log()

        # Print summary
        print(f"\n{'='*70}")
        print(f"SCAN SUMMARY")
        print(f"{'='*70}")
        print(f"Total papers found: {len(all_pmids_list)}")
        print(f"New papers saved: {new_count}")
        print(f"Already existing: {existing_count}")
        print(f"Total in database: {len(existing_pmids) + new_count}")
        print(f"{'='*70}")

        if log_path:
            print(f"\nScan log: {log_path}")

        return {
            "total_found": len(all_pmids_list),
            "new_papers": new_count,
            "existing_papers": existing_count,
            "papers": self.papers_found
        }


def main():
    parser = argparse.ArgumentParser(
        description="PubMed scanner for autism genomics research"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="Number of days to search back (default: 7)"
    )
    parser.add_argument(
        "--backfill",
        action="store_true",
        help="Search from 2015-present instead of recent days"
    )

    args = parser.parse_args()

    scanner = PubMedScanner(days=args.days, backfill=args.backfill)
    result = scanner.scan()

    return 0


if __name__ == "__main__":
    sys.exit(main())
