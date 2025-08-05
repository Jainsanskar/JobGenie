import io
from pdfminer.high_level import extract_text
import openai
import os
from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
def extract_text_from_pdf(pdf_file):
    return extract_text(pdf_file)

def analyze_resume(resume_text):
    prompt = f"""
You are a career advisor AI. Given the resume text below:

\"\"\"{resume_text}\"\"\"

1. Summarize the candidate's profile in 100 words.
2. Identify missing but relevant skills for their domain.
3. Suggest a 3-step roadmap to enhance their career based on their resume.

Return in 3 sections:
SUMMARY:
...
SKILLS TO IMPROVE:
...
CAREER ROADMAP:
...
"""
      # uses OPENAI_API_KEY from env or .streamlit/secrets.toml

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    output = response.choices[0].message.content
    
    # Split output into parts
    summary = extract_between(output, "SUMMARY:", "SKILLS TO IMPROVE:")
    skills = extract_between(output, "SKILLS TO IMPROVE:", "CAREER ROADMAP:")
    roadmap = output.split("CAREER ROADMAP:")[-1]

    return summary.strip(), skills.strip(), roadmap.strip()


# def analyze_resume(resume_text):
#     # TEMPORARY MOCK RESPONSE
#     return (
#         "Sample summary: Experienced Data Scientist with 3+ years in ML & NLP.",
#         ["Python", "TensorFlow", "SQL", "Pandas"],
#         "Learn cloud deployment, contribute to open-source projects, prepare for interviews."
#     )



def extract_between(text, start, end):
    return text.split(start)[-1].split(end)[0]
