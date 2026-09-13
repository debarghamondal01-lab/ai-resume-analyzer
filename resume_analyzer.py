from google import genai
from google.genai import types

# 1. SETUP YOUR API KEY
# Paste your actual API key inside the quotes below
API_KEY = "PASTE_YOUR_API_KEY_HERE"

# 2. CREATE A CLIENT
client = genai.Client(api_key=API_KEY)

def analyze_resume(resume_text, job_description):
    # 3. CREATE THE PROMPT
    prompt = f"""
    You are an expert HR Manager and Applicant Tracking System (ATS).
    Compare the following resume against the job description.
    
    JOB DESCRIPTION:
    {job_description}
    
    RESUME:
    {resume_text}
    
    Please provide:
    1. A match score out of 100%.
    2. The top 3 missing skills or keywords.
    3. 2 specific suggestions to improve the resume for this job.
    
    Keep your response short, professional, and easy to read.
    """
    
    # 4. SEND TO GOOGLE'S SERVERS
    print("\nAnalyzing... (This takes 3-5 seconds)")
    response = client.models.generate_content(
        model='gemini-3.6-flash', # Updated to the current model
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
        )
    )
    
    return response.text

def main():
    print("=" * 50)
    print("   AI RESUME ANALYZER (Powered by Gemini)")
    print("=" * 50)
    
    # Get the Job Description
    print("\nPaste the JOB DESCRIPTION below.")
    print("When finished, type 'END' on a new line and press Enter:")
    job_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        job_lines.append(line)
    job_description = " ".join(job_lines)
    
    # Get the Resume
    print("\nPaste your RESUME text below.")
    print("When finished, type 'END' on a new line and press Enter:")
    resume_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        resume_lines.append(line)
    resume_text = " ".join(resume_lines)
    
    if len(job_description) < 20 or len(resume_text) < 20:
        print("\nError: Please provide more text for both sections.")
        return

    # Run the analysis
    try:
        result = analyze_resume(resume_text, job_description)
        
        print("\n" + "=" * 50)
        print("   ANALYSIS RESULTS")
        print("=" * 50)
        print(result)
        print("=" * 50)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    main()
