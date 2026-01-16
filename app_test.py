from services.metadata_service import fetch_metadata
from services.pdf_service import download_pdf
from services.text_extractor import (
    extract_text_from_pdf,
    extract_sections_from_text
)
from services.llm_analyzer import analyze_paper
from services.semantic_service import fetch_semantic_data
from utils.excel_writer import write_excel
from tqdm import tqdm


def read_dois(file_path="input/dois.txt"):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def main():
    dois = read_dois()
    rows = []

    for idx, doi in enumerate(tqdm(dois), start=1):

        # 1️⃣ Metadata (CrossRef)
        title, author_year, abstract = fetch_metadata(doi)

        # 2️⃣ Semantic Scholar (structure-rich hints)
        semantic = fetch_semantic_data(doi)

        # 3️⃣ Default texts (fallbacks)
        intro_text = abstract
        method_text = abstract
        dataset_text = abstract
        results_text = abstract
        limitations_text = abstract

        # 4️⃣ Use Semantic Scholar if available
        if semantic:
            intro_text = semantic.get("abstract", abstract)
            method_text = semantic.get("methods", abstract)
            dataset_text = semantic.get("datasets", abstract)
            results_text = semantic.get("tldr", abstract)

        # 5️⃣ PDF-based full-paper enhancement (BEST)
        pdf_path = download_pdf(doi)
        if pdf_path:
            try:
                full_text = extract_text_from_pdf(pdf_path)
                sections = extract_sections_from_text(full_text)

                intro_text = sections.get("introduction") or intro_text
                method_text = sections.get("method") or method_text
                dataset_text = sections.get("dataset") or dataset_text
                results_text = sections.get("results") or results_text
                limitations_text = sections.get("limitations") or limitations_text

            except Exception:
                pass  # graceful fallback

        # 6️⃣ Section-wise AI analysis (NO hallucination)
        problem = analyze_paper(intro_text).get("problem", "N/A")
        method = analyze_paper(method_text).get("method", "N/A")
        dataset = analyze_paper(dataset_text).get("dataset", "N/A")
        findings = analyze_paper(results_text).get("findings", "N/A")
        limitations = analyze_paper(limitations_text).get("limitations", "N/A")

        rows.append({
            "Serial No.": idx,
            "Title": title,
            "Author & Year": author_year,
            "DOI": doi,
            "Problem Addressed": problem,
            "Method Used": method,
            "Dataset": dataset,
            "Key Findings": findings,
            "Limitations": limitations
        })

    write_excel(rows)
    print("✅ literature_review.xlsx generated successfully")


if __name__ == "__main__":
    main()
