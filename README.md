# AI Resume Fixer 

An **AI-powered resume analyzer** that helps job seekers tailor their resumes to specific job descriptions.  
Built with **Python, NLP, and LLaMA 3** for local AI suggestions.  

---

## Features  

- **Resume Parsing** → Upload PDF/DOCX, text is auto-extracted.  
- **Job Description Input** → Paste job postings.  
- **Match Score** → AI calculates similarity between resume & job description.  
- **Gap Analysis** → Highlights missing skills and keywords.  
- **AI Suggestions** → Uses **LLaMA 3 (via Ollama)** to recommend phrasing improvements. 
- **Export Options** (coming soon) → Save improved resume to DOCX/PDF.  

---

## Tech Stack  
  
- **Frontend:** Streamlit (simple UI)  
- **NLP:** scikit-learn
- **AI Suggestions:** LLaMA 3 via Ollama (local AI runtime)  
- **Resume Parsing:** pdfplumber, python-docx  

---

## Project Structure

```
│── backend/
│ ├── main.py
│ ├── resume_parser.py # PDF/DOCX parsing
│ ├── nlp.py # Keyword extraction & similarity
│ ├── ai_suggestions.py # AI (LLaMA 3 via Ollama)
│
│── frontend/
│ ├── app.py # Streamlit UI
│
│── data/
│ ├── sample_resume.pdf
│ └── job_description.txt
│
│── requirements.txt
│── README.md
```
---

## Setup Instructions

1. Clone the repo
```
git clone https://github.com/lucamuratori/resume-fixer-ai-project
```
2. Install Python dependencies
```
pip install -r requirements.txt
```
3. Install Ollama
- macOS/Linux (windows via WSL2)
```
bash
curl -fsSL https://ollama.com/install.sh | sh
```
4. Pull the Llama 3 model
```
bash
ollama pull llama3
```
5. Start ollama service (usually starts automatically in background)
```
bash
ollama serve
```
6. Run the app
```
streamlit run frontend/app.py
```
