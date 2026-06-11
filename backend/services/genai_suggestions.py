from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    client = Groq(api_key=api_key)
else:
    client = None
    print("⚠️ WARNING: GROQ_API_KEY not set. Suggestions will be disabled.")

def get_suggestions(res, jd):
    if client is None:
        return "Groq API key not configured."

    prompt = f"""
    You are an expert ATS Resume Analyzer.

Compare the Resume and Job Description carefully.

TASK 1: Skill Boosters 🚀

Identify technical skills that appear in the Job Description but are not present in the Resume.

Include only:
- Programming Languages
- Frameworks
- Libraries
- Tools
- Databases
- Cloud Platforms
- Technologies
- Certifications
- Computer Science Concepts

Strictly exclude:
- Soft skills (communication, teamwork, leadership, etc.)
- Generic phrases
- Qualifications and degrees
- Job responsibilities
- Sentences and explanations

Start this section with:

🚀  Skill Boosters

and provide only the skill names as bullet points.

---------------------------------------------------

TASK 2: Resume Power-Ups 💡

Generate exactly 5 short and actionable suggestions to improve the resume.

Suggestions may involve:
- Missing technical skills up to 10
- Projects to build
- Certifications
- Resume presentation
- Achievement quantification
- Portfolio improvements
- Relevant soft skills if needed

Rules:
- Each suggestion must be one line only.
- Keep suggestions practical and specific.
- Do not repeat the ATS Boosters.
- Generate exactly 5 suggestions.

Start this section with:

💡 Resume Power-Ups

---------------------------------------------------

    Resume:
    {res}

    Job Description:
    {jd}

    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )
    content = response.choices[0].message.content
    return content