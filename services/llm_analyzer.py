from groq import Groq
import os
import json
import re
api_key = None

try:
    import streamlit as st
    api_key = st.secrets.get("GROQ_API_KEY")
except Exception:
    pass

if not api_key:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found")

client = Groq(api_key=api_key)

PROMPT = """
You are helping write an academic literature survey. Read & analyze the entire paper like a student doing survey and use intelligence to extract the following details from the paper. Look for keywords and important facts.

From the given research paper text, generate the following in clear academic language:

1. Methodology: Describe the techniques, models, or approaches used.
2. Identification of gaps and limitations: Identify limitations or research gaps mentioned or implied.
3. Results: Mention performance metrics or outcomes.

Rules:
- Do NOT invent facts.
- Do NOT say N/A.
- If information is missing, say "Not discussed in this paper".
- Return ONLY valid JSON.
- No markdown, no explanations.

JSON format:

{
  "methodology": "",
  "gaps": "",
  "results": ""
}

Text:
"""

def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return None


def analyze_paper(text):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": PROMPT + str(text)[:8000]}],
            temperature=0.2
        )

        raw = response.choices[0].message.content
        parsed = extract_json(raw)

        if parsed:
            return parsed
        else:
            return fallback()

    except Exception as e:
        print("❌ Groq error:", e)
        return fallback()


def fallback():
    return {
        "methodology": "Not explicitly discussed",
        "gaps": "Not explicitly discussed",
        "results": "Not explicitly discussed"
    }
