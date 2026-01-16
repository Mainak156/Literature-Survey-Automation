import requests
import re

def fetch_metadata(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)

    if response.status_code != 200:
        return "N/A", "N/A", "N/A"

    data = response.json()["message"]

    # Title
    title = data["title"][0] if data.get("title") else "N/A"

    # Authors
    authors = []
    for a in data.get("author", []):
        authors.append(f"{a.get('given','')} {a.get('family','')}")

    # Year
    year = data.get("issued", {}).get("date-parts", [[None]])[0][0]

    # Abstract (CrossRef returns HTML tags sometimes)
    abstract = data.get("abstract", "N/A")

    if abstract != "N/A":
        abstract = re.sub("<.*?>", "", abstract)  # remove HTML tags

    return title, f"{', '.join(authors)} ({year})", abstract
