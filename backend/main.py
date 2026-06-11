from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.extract_text import extract_resume_text
from services.resume_score import calculate_matching_score
from services.genai_suggestions import get_suggestions


class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str


app = FastAPI(
    title="AI Resume Analyzer Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return {
        "message": "AI Resume Analyzer API is running ..."
    }


@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    text = extract_resume_text(file)
    return {"resume_text": text}

@app.post("/analyze")
async def analyze(payload: AnalyzeRequest):

    resume_text = payload.resume_text
    job_description = payload.job_description

    # Score + ATS Boosters
    score = calculate_matching_score(
        resume_text,
        job_description
    )
    suggestions = get_suggestions(resume_text,job_description)
    if score >= 50 :
        assessment = "Interview Worthy!!"
    else:
        assessment = "Under Development"

    suggestions = suggestions.replace("\n", "<br>")
    return {
        "Matching Score": score,
        "Assessment": assessment,
        "Suggestions": suggestions
    }