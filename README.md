# 📘 Literature Survey Automation

Live App: https://literature-survey-automation-lifemadeeasier-mainaksen.streamlit.app/

An AI-powered literature survey automation tool that accepts research paper DOIs and automatically generates a structured Excel literature review. The tool combines CrossRef, Semantic Scholar, full-paper PDF analysis (when open access), section-aware text extraction, and Groq LLMs (LLaMA 3.1) behind an interactive Streamlit web interface.

---

## 🚀 Key Features

- 📌 DOI-based paper input
- 📚 Metadata extraction via CrossRef
- 🧠 Abstract, methods, datasets, and TLDR via Semantic Scholar
- 📄 Full PDF download and analysis (if open access)
- ✂️ Section-aware text extraction (identifies Methods, Results, Datasets, etc.)
- 🤖 AI-powered analysis using Groq (LLaMA 3.1)
- 📊 Automatic Excel literature review generation
- 🌐 Interactive Streamlit UI with download-ready output

---

## 📊 Output Format

The generated Excel file contains the following columns:

- Serial No.
- Title
- Author & Year
- DOI
- Problem Addressed
- Method Used
- Dataset
- Key Findings
- Limitations

---

## 🔁 Processing Pipeline

DOI Input  
↓  
CrossRef (Metadata)  
↓  
Semantic Scholar (Abstract, Methods, Datasets, TLDR)  
↓  
PDF Download (if available)  
↓  
Section-aware Text Extraction  
↓  
Groq LLM (AI Analysis)  
↓  
Excel Output  
↓  
Streamlit UI

---

## 📁 Project Structure

Literature-Survey-Automation/
│
├── app.py                     # Streamlit application
├── requirements.txt
├── input/
│   └── dois.txt
├── output/
│   └── literature_review.xlsx
├── services/
│   ├── metadata_service.py
│   ├── semantic_service.py
│   ├── pdf_service.py
│   ├── text_extractor.py
│   └── llm_analyzer.py
├── utils/
│   └── excel_writer.py
├── .gitignore
└── README.md

---

## 🛠 Installation

1. Clone the repository
```bash
git clone https://github.com/Mainak156/Literature-Survey-Automation.git
cd Literature-Survey-Automation
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file (for local development) or add secrets in Streamlit Community Cloud.

Local (.env)
```env
GROQ_API_KEY="your_groq_api_key_here"
```

Streamlit Cloud (Secrets)
- Key: `GROQ_API_KEY`
- Value: `your_groq_api_key_here`

The application expects the Groq API key to call the LLM for analysis. Other service calls (CrossRef, Semantic Scholar, PDF sources) use public APIs or direct downloads.

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

The app will be available at: http://localhost:8501

---

## 🌐 Deployment (Streamlit Community Cloud)

1. Push the repository to GitHub
2. Visit https://share.streamlit.io
3. Click "New App"
4. Select:
   - Repository: `Literature-Survey-Automation`
   - Branch: `main`
   - Main file: `app.py`
5. Set Python version = 3.10
6. Add `GROQ_API_KEY` in Secrets
7. Click Deploy

---

## 🧪 Ethical Design Principles

- Avoid hallucination: do not invent missing details.
- Fields are filled only if explicitly available from sources.
- Missing or unavailable data is represented as `N/A`.
- Review and survey papers are treated appropriately (dataset/limitations might be N/A).
- Section-aware analysis improves transparency and traceability of extracted claims.

---

## ⚠️ Known Limitations

- Closed-access PDFs cannot be parsed or analyzed (only open-access PDFs are downloaded/analyzed).
- Some papers use non-standard section headings; section-aware extraction may miss content.
- Dataset and limitations fields may remain `N/A` for review/survey/editorial papers — this is expected and academically correct.
- Quality of LLM analysis depends on the Groq model and the quality/availability of extracted text.

---

## 🎓 Use Cases

- Systematic Literature Reviews (SLR)
- Academic projects (M.Tech / MS / PhD)
- Conference or viva demonstrations
- Research automation workflows
- Rapid survey creation for proposals and related-work sections

---

## 🔬 Example Workflow

1. Add DOIs (one per line) to `input/dois.txt` or paste into the Streamlit input.
2. Run the app and start processing.
3. Let the pipeline fetch metadata, pull abstracts and methods, download PDFs (if available), extract sectioned text, and run LLM analysis.
4. Download the generated `literature_review.xlsx` from the UI.

---

## 👤 Author

Mainak Sen  
GitHub: https://github.com/Mainak156

---

## 📄 License

This project is released under the MIT License. See the LICENSE file for details.

---

## ⭐ Contributing & Feedback

Contributions, issues, suggestions, and stars are welcome. If you find the project useful, please consider starring the repository.

If you want to contribute:
- Open an issue to discuss major changes
- Send a PR with a clear description and tests where appropriate

---

## 🙏 Acknowledgements

- CrossRef and Semantic Scholar for metadata and abstract/method retrieval
- Groq LLM (LLaMA 3.1) for AI-driven analysis
- Streamlit for powering the interactive UI
