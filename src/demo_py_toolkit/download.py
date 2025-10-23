import os
import requests
from tqdm import tqdm


class DownloadPMCArticle:
    """ download articles from PubMed Central using PMC IDs """

    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.session = requests.Session()


    def download(self, pmc_ids, output_directory):

        os.makedirs(output_directory, exist_ok=True)
        successes, failures = [], []

        for pmc_id in tqdm(pmc_ids, desc="Downloading articles..."):
            params = {
                'db': 'pmc',
                'id': pmc_id,
                'api_key': self.api_key,
                'retmode': 'xml'
            }

            try:
                response = self.session.get(self.fetch_url, params=params, timeout=10)
                response.raise_for_status()

                content = response.content
                # print()

                # validate content before saving
                # if len(content) < 1000 or b'<error>' in content:
                #     print(f"Invalid content for PMC ID {pmc_id}, skipping")
                #     continue

                with open(os.path.join(output_directory, f"{pmc_id}.xml"), "wb") as f:
                    f.write(content)

                successes.append(pmc_id)
            except Exception as e:
                failures.append((pmc_id, str(e)))
        
        print(f"Downloaded {len(successes)} articles successfully.")
        if failures:
            print(f"Failed to download {len(failures)} articles:")
            for pmc_id, error in failures:
                print(f"  PMC ID {pmc_id}: {error}")

        return successes, failures