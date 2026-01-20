# 📋 Changelog

All notable changes to this project are documented in this file.

This project loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and [Semantic Versioning](https://semver.org/spec/v2.0.0.html) principles.

---

## [v1.2.0] – 2026-01-20
### 🧠 Literature Survey Format Finalization
This release finalizes the project to strictly match college-level literature survey requirements and eliminates excessive `N/A` values.

#### ✨ Added
* Academic synthesis-based LLM analysis instead of rigid fact extraction.
* Narrative extraction of:
    * Methodology
    * Identification of gaps and limitations
    * Results / performance metrics (if reported)
* Explicit handling of missing information using: *"Not discussed in this paper"*
* Support for `Groq openai/gpt-oss-120b` model for deeper reasoning.
* Unified logic across:
    * Streamlit web app
    * CLI (`app_test.py`)

#### 🔧 Changed
* Reduced output columns to align with official literature survey format.
* **Removed:**
    * Dataset column
    * Problem Addressed column
* Updated LLM prompt from extraction to **analysis & summarization**.
* Improved prompt instructions to prevent hallucination.
* Excel output now focuses on academic readability instead of raw fields.

#### 🛠 Fixed
* Excessive `N/A` values in output Excel.
* Inconsistent outputs between PDF / abstract / Semantic Scholar paths.
* LLM over-fragmentation due to section-wise extraction.

---

## [v1.1.0] – 2026-01-20
### 🔄 Major Refactor – Academic Alignment
This version introduced structural changes to better align the system with academic evaluation standards.

#### ✨ Added
* Section-aware text aggregation (Abstract + Semantic Scholar + PDF).
* Improved fallback logic when PDFs are unavailable.
* Streamlit-based interactive UI with progress tracking.

#### 🔧 Changed
* Shift from dataset-centric extraction to literature survey narratives.
* Reduced number of LLM calls per paper.

#### 🛠 Fixed
* Broken environment variable loading across different execution contexts.
* Streamlit runtime crashes due to missing API keys.

---

## [v1.0.0] – 2026-01-20
### 🎉 Initial Stable Release
#### ✨ Added
* DOI-based literature survey automation.
* Metadata extraction using CrossRef.
* Semantic enrichment via Semantic Scholar.
* Full PDF download and parsing (open-access papers).
* AI-assisted information extraction using Groq LLMs.
* Automatic Excel literature review generation.
* Streamlit deployment on Community Cloud.

---

## 🔮 Planned Improvements
* Caching to reduce repeated LLM calls.
* Paper-type classification (Review vs Experimental).
* Confidence scoring for generated summaries.
* Citation / section-level traceability.
* PDF upload fallback for closed-access papers.
* Additional export formats (CSV, BibTeX).

## 📝 Notes
> **Academic Integrity:** The system does not hallucinate missing information. If content is not explicitly mentioned in a paper, it is marked as *"Not discussed in this paper"*. This behavior is intentional and aligns with academic integrity principles.