# 📘 Literature Survey Automation

🔗 **Live App:**  
https://literature-survey-automation-lifemadeeasier-mainaksen.streamlit.app/

An **AI-powered literature survey automation tool** that takes research paper **DOIs** as input and automatically generates a **structured Excel literature review** using **CrossRef, Semantic Scholar, full-paper PDF analysis, and Groq LLMs**, all through a **Streamlit web interface**.

---

## 🚀 Key Features

- 📌 DOI-based paper input
- 📚 Metadata extraction via **CrossRef**
- 🧠 Abstract, methods, datasets, and TLDR via **Semantic Scholar**
- 📄 Full PDF download and analysis (if open access)
- ✂️ Section-aware text extraction
- 🤖 AI-powered analysis using **Groq (LLaMA 3.1)**
- 📊 Automatic Excel literature review generation
- 🌐 Interactive **Streamlit UI**
- ⬇️ Download-ready output

---

## 📊 Output Format

The generated Excel file contains the following columns:

| Serial No. | Title | Author & Year | DOI | Problem Addressed | Method Used | Dataset | Key Findings | Limitations |
|-----------|-------|---------------|-----|-------------------|-------------|---------|--------------|-------------|

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
├── app.py # Streamlit application
├── requirements.txt
├── input/
│ └── dois.txt
├── output/
│ └── literature_review.xlsx
├── services/
│ ├── metadata_service.py
│ ├── semantic_service.py
│ ├── pdf_service.py
│ ├── text_extractor.py
│ └── llm_analyzer.py
├── utils/
│ └── excel_writer.py
├── .gitignore
└── README.md


---

## 🛠 Installation

### Clone the repository
git clone https://github.com/Mainak156/Literature-Survey-Automation.git
cd Literature-Survey-Automation

Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate  # Linux / macOS

Install dependencies
pip install -r requirements.txt

🔐 Environment Configuration
Local (.env)
GROQ_API_KEY="your_groq_api_key_here"

Streamlit Cloud (Secrets)
GROQ_API_KEY = "your_groq_api_key_here"

▶️ Run Locally
streamlit run app.py


The app will be available at:

http://localhost:8501

🌐 Deployment

This project is deployed using Streamlit Community Cloud.

Steps:

Push the repository to GitHub

Go to https://share.streamlit.io

Click New App

Select:

Repository: Literature-Survey-Automation

Branch: main

Main file: app.py

Set Python version = 3.10

Add GROQ_API_KEY in Secrets

Click Deploy

🧪 Ethical Design Principles

No hallucination of missing information

Fields are filled only if explicitly stated

Missing data is represented as N/A

Review and survey papers are handled correctly

Section-aware analysis improves transparency

⚠️ Known Limitations

Closed-access PDFs cannot be parsed

Some papers use non-standard section headings

Dataset and limitations may remain N/A for:

Review papers

Survey papers

Conceptual/editorial articles

These are academically correct outcomes.

🎓 Use Cases

Systematic Literature Reviews (SLR)

Minor / Major academic projects

M.Tech / MS / PhD research

Conference and viva demonstrations

Research automation workflows

👤 Author

Mainak Sen
GitHub: https://github.com/Mainak156

📄 License
MIT License

⭐ If you find this project useful, please consider starring the repository.
