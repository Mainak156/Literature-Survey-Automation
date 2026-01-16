import fitz  # PyMuPDF
import re


def extract_text_from_pdf(pdf_path):
    """
    Extract full raw text from PDF
    """
    text = ""
    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text() + "\n"

    return text


def extract_sections_from_text(text):
    """
    Split paper text into logical research sections.
    Returns a dictionary of sections.
    """

    sections = {
        "introduction": "",
        "method": "",
        "dataset": "",
        "results": "",
        "limitations": ""
    }

    # Normalize text
    clean_text = re.sub(r"\s+", " ", text)

    patterns = {
        "introduction": r"(introduction|background)",
        "method": r"(methodology|methods|materials and methods)",
        "dataset": r"(dataset|data description|experimental setup)",
        "results": r"(results|experiments|evaluation)",
        "limitations": r"(limitations|discussion|threats to validity)"
    }

    for section, pattern in patterns.items():
        match = re.search(
            rf"{pattern}(.{{0,3000}})",
            clean_text,
            re.IGNORECASE
        )
        if match:
            sections[section] = match.group()

    return sections
