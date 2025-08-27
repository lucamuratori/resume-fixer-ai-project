from ollama import chat
from ollama import ChatResponse


def suggest_improvements(resume_text: str, job_description: str) -> str:
    prompt = f"""
    You are a career coach. Compare this resume

    Resume:
    {resume_text}

    Against this job description:
    Job Description:
    {job_description}

    1. Suggest missing keywords from the job description that should be included in the resume.
    2. Suggest improvements to make the resume more appealing for the job description.
    3.Suggest improvements in phrasing.
    """
    response: ChatResponse = chat(model="llama3", messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ])
    return response["message"]["content"]

