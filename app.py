import streamlit as st
from src.helper import extract_text_from_pdf, analyze_resume
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

st.set_page_config(page_title="JobGenie: AI Career Recommender", layout="wide")
st.title("🤖 JobGenie - AI-Powered Career Recommender")

uploaded_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Analyzing resume..."):
        summary, skills, roadmap = analyze_resume(resume_text)

    st.subheader("📋 Resume Summary")
    st.write(summary)

    st.subheader("🧠 Skill Gap Analysis")
    st.write(skills)

    st.subheader("🚀 Career Roadmap")
    st.write(roadmap)
    job_portal="LinkedIn"
    st.subheader("🔎 Job Recommendations")
    if job_portal == "LinkedIn":
        jobs = fetch_linkedin_jobs(summary)
    else:
        jobs = fetch_naukri_jobs(summary)
    for job in jobs:
        st.markdown(f"- **{job['title']}** at _{job['company']}_ – [{job['link']}]({job['link']})")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Analyzing resume..."):
        summary, skills, roadmap = analyze_resume(resume_text)

    st.subheader("📋 Resume Summary")
    st.write(summary)

    st.subheader("🧠 Skill Gap Analysis")
    st.write(skills)

    st.subheader("🚀 Career Roadmap")
    st.write(roadmap)

    # Job source selector
    st.subheader("🧭 Choose Job Portal")
    job_portal = st.radio("Select Source:", ["LinkedIn", "Naukri"])

    if job_portal == "LinkedIn":
        jobs = fetch_linkedin_jobs(summary)
    else:
        jobs = fetch_naukri_jobs(summary)

    st.subheader("🔎 Job Recommendations")
    for job in jobs:
        st.markdown(f"- **{job['title']}** at _{job['company']}_ – [Apply]({job['link']})")
