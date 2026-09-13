# AI Resume Analyzer 🤖

An AI-powered tool that compares a resume against a job description using Google's Gemini LLM API.

## 🚀 Features
- Uses Google Gemini API for natural language processing.
- Provides a match score (0-100%).
- Identifies missing keywords and skills.
- Offers actionable feedback to improve the resume.

## 🧠 Tech Stack
- Python
- Google GenAI SDK (`google-genai`)
- Prompt Engineering

## ⚙️ How to Use
1. Install dependency: `pip install google-genai`
2. Add your Gemini API key in the script (never share it publicly).
3. Run: `python resume_analyzer.py`
4. Paste the Job Description, type `END`.
5. Paste your Resume, type `END`.
6. Read the AI's feedback!

## ⚠️ Security Note
The API key is stored locally in the script. For production, use environment variables.
