from services.metadata_service import fetch_metadata
from services.pdf_service import download_pdf
from services.text_extractor import extract_text_from_pdf, extract_sections_from_text
from services.semantic_service import fetch_semantic_data
from services.llm_analyzer import analyze_paper
from utils.excel_writer import write_excel
from tqdm import tqdm

def read_dois(file_path="input/dois.txt"):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    dois = read_dois()
    rows = []

    for idx, doi in enumerate(tqdm(dois), start=1):

        title, author_year, abstract = fetch_metadata(doi)
        semantic = fetch_semantic_data(doi)

        text = abstract
        if semantic:
            text = semantic.get("abstract", "") + "\n" + semantic.get("tldr", "")

        pdf_path = download_pdf(doi)
        if pdf_path:
            try:
                full_text = extract_text_from_pdf(pdf_path)
                sections = extract_sections_from_text(full_text)
                text += "\n".join(sections.values())
            except Exception:
                pass

        analysis = analyze_paper(text)

        rows.append({
            "S. No": idx,
            "Title (Author, Year)": f"{title} ({author_year})",
            "Methodology": analysis["methodology"],
            "Identification of gaps and limitations": analysis["gaps"],
            "Results": analysis["results"]
        })

    write_excel(rows)
    print("✅ literature_review.xlsx generated")

if __name__ == "__main__":
    main()
