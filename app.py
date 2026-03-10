from flask import Flask, render_template, request
import os

from resume_analyzer import extract_text, analyze_resume
from interview_simulator import generate_interview_questions

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["resume"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(path)

    resume_text = extract_text(path)

    analysis = analyze_resume(resume_text)

    questions = generate_interview_questions(resume_text)

    return render_template(
        "index.html",
        analysis=analysis,
        questions=questions
    )


if __name__ == "__main__":
    app.run(debug=True)