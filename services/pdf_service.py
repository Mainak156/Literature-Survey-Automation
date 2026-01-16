import requests
import os

def download_pdf(doi, save_dir="temp_pdfs", email="test@example.com"):
    os.makedirs(save_dir, exist_ok=True)

    api_url = f"https://api.unpaywall.org/v2/{doi}?email={email}"
    r = requests.get(api_url)

    if r.status_code != 200:
        return None

    data = r.json()
    location = data.get("best_oa_location")

    if not location or not location.get("url_for_pdf"):
        return None

    pdf_url = location["url_for_pdf"]
    pdf_path = os.path.join(save_dir, doi.replace("/", "_") + ".pdf")

    pdf_data = requests.get(pdf_url)
    if pdf_data.status_code == 200:
        with open(pdf_path, "wb") as f:
            f.write(pdf_data.content)
        return pdf_path

    return None
