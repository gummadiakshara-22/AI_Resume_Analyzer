import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "score" not in st.session_state:
    st.session_state.score = None

if "assessment" not in st.session_state:
    st.session_state.assessment = None

if "suggestions" not in st.session_state:
    st.session_state.suggestions = None

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.big-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #2563EB;
}

.subtitle {
    text-align: center;
    color: #64748B;
    font-size: 18px;
    margin-bottom: 25px;
}

.result-card {
    padding: 25px;
    border-radius: 16px;
    border: 1px solid rgba(128,128,128,0.25);
    margin-bottom: 20px;
    background-color: rgba(255,255,255,0.03);
}

.card-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 10px;
}

.score-number {
    font-size: 50px;
    font-weight: 800;
    text-align: center;
}

.assessment-text {
    font-size: 24px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    "<div class='big-title'>🚀 AI Resume Analyzer</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Upload Resume • Compare with Job Description • Get ATS Insights</div>",
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Job Description",
    height=250,
    placeholder="Paste the Job Description Here..."
)

# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------
if st.button(
    "🔍 Analyze Resume",
    use_container_width=True
):

    if uploaded_file is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter a job description.")
        st.stop()

    try:

        with st.spinner("Analyzing Resume..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }

            upload_response = requests.post(
                f"{API_URL}/upload_resume",
                files=files
            )

            if upload_response.status_code != 200:
                st.error("Failed to upload resume.")
                st.stop()

            resume_text = upload_response.json()["resume_text"]

            payload = {
                "resume_text": resume_text,
                "job_description": job_description
            }

            analyze_response = requests.post(
                f"{API_URL}/analyze",
                json=payload
            )

            if analyze_response.status_code != 200:
                st.error("Analysis failed.")
                st.stop()

            result = analyze_response.json()

            st.session_state.score = result["Matching Score"]
            st.session_state.assessment = result["Assessment"]
            st.session_state.suggestions = result["Suggestions"]

    except Exception as e:
        st.error(f"Error: {e}")

# --------------------------------------------------
# RESULTS SECTION
# --------------------------------------------------
if st.session_state.score is not None:

    score = st.session_state.score
    assessment = st.session_state.assessment
    suggestions = st.session_state.suggestions

    st.divider()

    st.markdown("""
    <h2 style='text-align:center; margin-bottom:25px;'>
    📊 Resume Analysis Report
    </h2>
    """, unsafe_allow_html=True)

    # Progress Bar
    st.progress(int(score))

    # SCORE CARD
    st.markdown(
        f"""
        <div class="result-card">
            <div class="card-title">🎯 Matching Score</div>
            <div class="score-number">{score}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ASSESSMENT
    if score >= 50:
        badge = "🟢 Interview Worthy"
    else:
        badge = "🔴 Under Development"

    st.markdown(
        f"""
        <div class="result-card">
            <div class="card-title">📋 Assessment</div>
            <div class="assessment-text">{badge}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # SUGGESTIONS
    st.markdown(
        f"""
        <div class="result-card">
            <div class="card-title">💡 Suggestions</div>
            {suggestions}
        </div>
        """,
        unsafe_allow_html=True
    )

