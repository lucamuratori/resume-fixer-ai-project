import streamlit as st
from backend.resume_parser import extract_pdf, extract_docx
from backend.nlp import get_match_score
from backend.ai_suggestions import suggest_improvements


st.title("SmartHire Resume Matcher")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste the job description here")

if uploaded_file and job_description:
    if uploaded_file.type == "application/pdf":
        resume_text = extract_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_docx(uploaded_file)
    else:
        st.error("Unsupported file type. Please upload a PDF or DOCX file.")
