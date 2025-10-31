# 📚 demo_py_toolkit

**demo_py_toolkit** is a lightweight educational Python package that demonstrates how to structure, package, and publish a simple library for retrieving biomedical literature data from PubMed Central (PMC).

It provides two core modules:
- `ArticleSearcher` - Search PMC for article IDs by query or keyword  
- `ArticleDownloader` - Download full-text XMLs for those IDs  

## 🚀 Features

- Search PMC articles by term, field, and result count  
- Download article XMLs by PMC ID  
- Use programmatically or via command line (CLI)  
- Modular, easy-to-extend architecture  
- Ideal sandbox for packaging and distribution practice  

---

## 📦 Installation

```bash
pip install demo_py_toolkit
```

## 🧰 Dependencies

```bash
- requests
- tqdm
- python-dotenv
```

---

## 🗂️ Package Structure
```bash
literature_demo/
│
└── src/
    └── literature_demo/
        ├── __init__.py          # Package initialization
        ├── search.py            # Search module (ArticleSearcher)
        ├── download.py          # Download module (ArticleDownloader)
        ├── cli.py               # CLI entry point
└── examples/
    └── example.py
├── pyproject.toml
├── README.md
└── .gitignore
└── LICENSE
```

---

## 🧩 Example: Search and Download

```python
from demo_py_toolkit import SearchPMCArticle, DownloadPMCArticle

# Initialize
searcher = SearchPMCArticle(api_key="YOUR_NCBI_API_KEY")  # optional
downloader = DownloadPMCArticle(api_key="YOUR_NCBI_API_KEY")

# Search for articles
query = "lung cancer"
pmc_ids = searcher.search(query, field="Abstract", retmax=5)
print(f"Found {len(pmc_ids)} articles: {pmc_ids}")

# Download them
downloader.download(pmc_ids, output_directory="downloaded_articles")
print("✅ Download complete.")
```

## 💻 Command Line Usage
Once installed, the package provides a command-line interface (CLI):
```bash
demo_py_toolkit --query "breast cancer" --field Abstract --max_results 5 --output_directory results

```
Available arguments:

| Argument             | Description                                              | Default   |
| -------------------- | -------------------------------------------------------- | --------- |
| `--query`            | Search term (required)                                   | —         |
| `--field`            | Field to search in (`Title`, `Abstract`, or `Text Word`) | Abstract  |
| `--max_results`      | Maximum number of search results                         | 5         |
| `--output_directory` | Directory to store downloaded XML files                  | downloads |
| `--api_key`          | Optional NCBI API key for higher rate limits             | ""        |


## 📄 License

MIT License
Copyright © 2025

