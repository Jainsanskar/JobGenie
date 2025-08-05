
# JobGenie: AI-Powered Career Recommender

JobGenie is an AI-powered Streamlit web application that analyzes uploaded resumes and recommends suitable job opportunities from LinkedIn and Naukri, generates skill roadmaps, and offers personalized career insights using OpenAI's GPT API.

---

## 🔍 Features

- 📄 **Resume Parsing**: Upload your resume (PDF) and extract key information.
- 💬 **OpenAI-Powered Suggestions**: Generate a professional summary, skill list, and learning roadmap.
- 🔗 **Job Scraping**: Real-time job scraping from **LinkedIn** and **Naukri** based on your resume.
- 📊 **Skill Analysis**: Breaks down hard and soft skills from resume content.
- 🛠️ **Modular Codebase**: Easy to extend and adapt to different use cases.

---

## ⚙️ Installation

```bash
git clone https://github.com/Jainsanskar/jobgenie.git
cd jobgenie
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔑 Setup

1. Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```
2. Ensure you have a valid OpenAI account with sufficient quota.

---

## 🚀 Usage

```bash
streamlit run app.py
```

Then open the app in your browser and upload your resume to get started.

---

## 🗂️ Project Structure

```
├── app.py                # Streamlit frontend
├── src/
│   ├── helper.py         # Resume parsing and OpenAI analysis
│   ├── job_api.py        # Job scraping logic
│   └── utils.py          # Utility functions
├── requirements.txt
└── README.md
```

---

## 📌 Future Enhancements

- 🌐 Support more job portals (Indeed, Monster)
- 🔎 Semantic job matching with embeddings
- 📉 Dashboard for visual analytics
- 📱 Mobile-responsive design

---

## 🙏 Acknowledgements

- [OpenAI](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

