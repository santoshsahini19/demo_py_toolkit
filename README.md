# 📚 demo_py_toolkit

**literature_demo** is a lightweight educational Python package that demonstrates how to structure, package, and publish a simple library for retrieving biomedical literature data from PubMed Central (PMC).

It provides two core modules:
- `ArticleSearcher` — Search PMC for article IDs by query or keyword  
- `ArticleDownloader` — Download full-text XMLs for those IDs  

## 🚀 Features

- Search PMC articles by term, field, and result count  
- Download article XMLs by PMC ID  
- Use programmatically or via command line (CLI)  
- Modular, easy-to-extend architecture  
- Ideal sandbox for packaging and distribution practice  

---

## 📦 Installation

```bash
pip install literature-demo

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

## 🧰 Dependencies

🧰 Dependencies
- requests
- tqdm
- python-dotenv

