# search literature 

import time
import xml.etree.ElementTree as ET
import requests

class SearchPMCArticle:
    """search articles from PubMed using Entrez E-utilities API""" 

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()

    
    def search(self, query, field='Abstract', retmax=20):
        search_term = f"{query}[{field}]"
        params = {
            'db': 'pubmed',
            'term': search_term,
            'retmax': retmax,
            'api_key': self.api_key
        }

        response = self.session.get(self.base_url, params=params, timeout=10)
        response.raise_for_status()

        root = ET.fromstring(response.text)
        id_list = [i.text for i in root.findall('.//Id')]

        time.sleep(0.34)  # to respect NCBI rate limits

        return id_list
