from groq import Groq
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)

PROMPT = """
You are an academic research assistant.

Your task is to extract structured information from a research paper.

IMPORTANT RULES:
- Respond ONLY with valid JSON
- Do NOT add explanations
- Do NOT use markdown
- Do NOT add extra text

JSON schema (must match exactly):

{
  "problem": "string",
  "method": "string",
  "dataset": "string or N/A",
  "findings": "string",
  "limitations": "string or N/A"
}

Text:
"""

def extract_json(text):
    """
    Safely extract JSON object from model output
    """
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
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": PROMPT + str(text)[:8000]}
            ],
            temperature=0
        )

        raw_output = response.choices[0].message.content
        parsed = extract_json(raw_output)

        if parsed:
            return parsed
        else:
            print("⚠️ JSON not found in model output")
            return fallback()

    except Exception as e:
        print("❌ Groq error:", str(e))
        return fallback()


def fallback():
    return {
        "problem": "N/A",
        "method": "N/A",
        "dataset": "N/A",
        "findings": "N/A",
        "limitations": "N/A"
    }
