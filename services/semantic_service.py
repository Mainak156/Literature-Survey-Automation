import requests

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/DOI:"

FIELDS = (
    "title,"
    "abstract,"
    "tldr,"
    "methods,"
    "dataSources,"
    "openAccessPdf"
)

def fetch_semantic_data(doi):
    url = f"{BASE_URL}{doi}?fields={FIELDS}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "abstract": data.get("abstract", ""),
        "tldr": data.get("tldr", {}).get("text", ""),
        "methods": ", ".join(data.get("methods", [])) if data.get("methods") else "",
        "datasets": ", ".join(data.get("dataSources", [])) if data.get("dataSources") else "",
        "pdf_url": data.get("openAccessPdf", {}).get("url")
    }
