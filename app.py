import streamlit as st
import os
from services.metadata_service import fetch_metadata
from services.pdf_service import download_pdf
from services.text_extractor import (
    extract_text_from_pdf,
    extract_sections_from_text
)
from services.llm_analyzer import analyze_paper
from services.semantic_service import fetch_semantic_data
from utils.excel_writer import write_excel

OUTPUT_FILE = "output/literature_review.xlsx"

st.set_page_config(
    page_title="Literature Survey Analyzer",
    layout="wide"
)

st.title("📚 Literature Survey Analyzer")
st.write(
    "Generate a structured literature review table from research paper DOIs "
    "using Semantic Scholar + Full-PDF AI analysis."
)

# ---------------- Input ----------------
st.subheader("🔹 Enter DOIs (one per line)")
doi_input = st.text_area(
    "Example:\n10.1016/j.artmed.2020.101998",
    height=150
)

# ---------------- Run Button ----------------
if st.button("🚀 Generate Literature Review"):

    if not doi_input.strip():
        st.warning("Please enter at least one DOI.")
    else:
        dois = [d.strip() for d in doi_input.splitlines() if d.strip()]
        rows = []

        progress = st.progress(0)
        status = st.empty()

        for idx, doi in enumerate(dois, start=1):
            status.write(f"🔍 Processing DOI {idx}/{len(dois)}: {doi}")

            # Metadata
            title, author_year, abstract = fetch_metadata(doi)

            # Semantic Scholar
            semantic = fetch_semantic_data(doi)

            # Default text
            intro = abstract
            method = abstract
            dataset = abstract
            results = abstract
            limitations = abstract

            if semantic:
                intro = semantic.get("abstract", abstract)
                method = semantic.get("methods", abstract)
                dataset = semantic.get("datasets", abstract)
                results = semantic.get("tldr", abstract)

            # PDF enhancement
            pdf_path = download_pdf(doi)
            if pdf_path:
                try:
                    full_text = extract_text_from_pdf(pdf_path)
                    sections = extract_sections_from_text(full_text)

                    intro = sections.get("introduction") or intro
                    method = sections.get("method") or method
                    dataset = sections.get("dataset") or dataset
                    results = sections.get("results") or results
                    limitations = sections.get("limitations") or limitations
                except Exception:
                    pass

            # AI extraction (section-wise)
            problem = analyze_paper(intro).get("problem", "N/A")
            method_used = analyze_paper(method).get("method", "N/A")
            dataset_used = analyze_paper(dataset).get("dataset", "N/A")
            findings = analyze_paper(results).get("findings", "N/A")
            limits = analyze_paper(limitations).get("limitations", "N/A")

            rows.append({
                "Serial No.": idx,
                "Title": title,
                "Author & Year": author_year,
                "DOI": doi,
                "Problem Addressed": problem,
                "Method Used": method_used,
                "Dataset": dataset_used,
                "Key Findings": findings,
                "Limitations": limits
            })

            progress.progress(idx / len(dois))

        write_excel(rows)
        st.success("✅ Literature review generated successfully!")

        # Download
        with open(OUTPUT_FILE, "rb") as f:
            st.download_button(
                label="⬇️ Download Excel File",
                data=f,
                file_name="literature_review.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        status.empty()
