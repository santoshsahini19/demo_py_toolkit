# cli script for searching and downloading PMC articles

import argparse
from demo_py_toolkit import SearchPMCArticle
from demo_py_toolkit import DownloadPMCArticle


def main():
    parser = argparse.ArgumentParser(description="Basic PMC Article Downloader")

    parser.add_argument("--query", type=str, required=True, help="Search query")
    parser.add_argument("--field", type=str, default="Abstract",
                        choices=["Title", "Abstract", "Text Word"])
    parser.add_argument("--max_results", type=int, default=5, help="Maximum search results")
    parser.add_argument("--output_directory", type=str, default="downloads")
    parser.add_argument("--api_key", type=str, default="")

    args = parser.parse_args()

    searcher = SearchPMCArticle(api_key=args.api_key)
    downloader = DownloadPMCArticle(api_key=args.api_key)

    pmc_ids = searcher.search(args.query, args.field, args.max_results)
    print(f"Found {len(pmc_ids)} articles for '{args.query}'")

    downloader.download(pmc_ids, args.output_directory)
    print("Download complete")