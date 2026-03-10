from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_interview_questions(resume_text):

    prompt = f"""
    Based on this resume generate 10 interview questions.

    Include:
    - technical questions
    - project based questions
    - behavioral questions

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content