# AI Resume Analyzer

AI Resume Analyzer is a FastAPI and Streamlit-based application that evaluates the alignment between a resume and a job description using semantic similarity. The system leverages Sentence Transformers to generate embeddings and compute a Matching Score, along with AI-generated suggestions to improve resume relevance.

## Features

* Resume upload and text extraction
* Semantic similarity-based Matching Score
* AI-powered resume improvement suggestions
* FastAPI REST API backend
* Interactive Streamlit frontend

## Tech Stack

**Backend**

* FastAPI
* Python

**Frontend**

* Streamlit

**NLP & Machine Learning**

* Sentence Transformers
* Transformers
* Scikit-Learn
* NLTK

**Document Processing**

* PDFPlumber
* Python-Docx

**Generative AI**

* Groq API

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "AI Resume Analyzer API is running ..."
}
```

### Upload Resume

```http
POST /upload_resume
```

**Request**

* Multipart Form Data
* PDF Resume File

**Response**

```json
{
  "resume_text": "Extracted resume content..."
}
```

### Analyze Resume

```http
POST /analyze
```

**Request**

```json
{
  "resume_text": "Resume Content",
  "job_description": "Job Description"
}
```

**Response**

```json
{
  "Matching Score": 78.5,
  "Assessment": "Interview Worthy!!",
  "Suggestions": "Suggested improvements..."
}
```

---

## Installation

```bash
git clone <repository-url>
cd Resume_Analyzer

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the `backend` directory.

```env
GROQ_API_KEY=your_api_key
```

---

## Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Run Frontend

```bash
cd frontend
streamlit run frontend.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## License

This project is intended for educational, learning, and portfolio purposes.
