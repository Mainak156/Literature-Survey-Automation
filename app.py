import streamlit as st
from services.metadata_service import fetch_metadata
from services.pdf_service import download_pdf
from services.text_extractor import extract_text_from_pdf, extract_sections_from_text
from services.semantic_service import fetch_semantic_data
from services.llm_analyzer import analyze_paper
from utils.excel_writer import write_excel

OUTPUT_FILE = "output/literature_review.xlsx"

st.set_page_config(page_title="Literature Survey Automation", layout="wide")
st.title("📘 Literature Survey Automation")

st.subheader("Enter DOIs (one per line)")
doi_input = st.text_area("Example:\n10.1016/j.artmed.2020.101998", height=150)

if st.button("🚀 Generate Literature Survey"):

    if not doi_input.strip():
        st.warning("Please enter at least one DOI.")
    else:
        dois = [d.strip() for d in doi_input.splitlines() if d.strip()]
        rows = []
        progress = st.progress(0)

        for idx, doi in enumerate(dois, start=1):
            st.write(f"Processing DOI {idx}/{len(dois)}")

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

            progress.progress(idx / len(dois))

        write_excel(rows)
        st.success("✅ Literature survey generated")

        with open(OUTPUT_FILE, "rb") as f:
            st.download_button(
                "⬇️ Download Excel",
                f,
                file_name="literature_review.xlsx"
            )
