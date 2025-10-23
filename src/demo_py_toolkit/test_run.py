# running modules locally for testing

from search import SearchPMCArticle
from download import DownloadPMCArticle
from dotenv import load_dotenv
import os

def test_example_run():

    # ncbi api key
    load_dotenv()  # load environment variables from .env
    api_key = os.getenv("NCBI_API_KEY")

    searcher = SearchPMCArticle(api_key=api_key)
    downloader = DownloadPMCArticle(api_key=api_key)

    ids = searcher.search(query="cancer immunotherapy", field="Abstract", retmax=5)
    print(f"Found PMC IDs: {ids}")

    success, failure = downloader.download(pmc_ids=ids, output_directory="./downloaded_articles")
    # example - 12528155
    print(f"Successfully downloaded: {success}")
    print(f"Failed to download: {failure}")

if __name__ == "__main__":
    test_example_run()
