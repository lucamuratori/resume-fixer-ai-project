import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.resume_parser import extract_pdf, extract_docx
from backend.nlp import get_match_score
from backend.ai_suggestions import suggest_improvements


def create_button(resume_text, job_description):
    if st.button("Get suggestions"):
        score = get_match_score(resume_text, job_description)
        st.write(f"Match Score: {score}%")
        suggestions = suggest_improvements(resume_text, job_description)
        st.write(suggestions)


st.title("SmartHire Resume Matcher")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste the job description here")

if uploaded_file and job_description:
    if uploaded_file.type == "application/pdf":
        resume_text = extract_pdf(uploaded_file)
        create_button(resume_text, job_description)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_docx(uploaded_file)
        create_button(resume_text, job_description)
    else:
        st.error("Unsupported file type. Please upload a PDF or DOCX file.")

