import pdfplumber
import docx
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def analyze_resume(text):

    prompt = f"""
    Analyze the following resume and give:

    1. Improved bullet points using strong action verbs
    2. Missing skills suggestions
    3. Recommended projects
    4. Grammar and clarity improvements
    5. LinkedIn summary

    Resume:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def extract_text(file_path):

    if file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text

    elif file_path.endswith(".txt"):
        with open(file_path, "r") as f:
            return f.read()

    return ""