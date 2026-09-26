from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

from modules.resume_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.resume_scorer import calculate_resume_score
from modules.ats_analyzer import analyze_ats
from modules.job_matcher import (
    calculate_job_match,
    compare_skills,
    calculate_skill_match_percentage
)
from modules.resume_suggestions import generate_resume_suggestions


app = Flask(__name__)

os.makedirs("uploads", exist_ok=True)
@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    resume_file = request.files.get(
        "resume"
    )

    job_description = request.form.get(
        "job_description",
        ""
    )

    if not resume_file:

        return "Please upload a resume."

    resume_text = extract_text_from_pdf(
        resume_file
    )

    detected_skills = extract_skills(
        resume_text
    )

    resume_result = calculate_resume_score(
        resume_text,
        detected_skills
    )

    ats_result = analyze_ats(
        resume_text
    )

    resume_suggestions = (
        generate_resume_suggestions(
            resume_text,
            detected_skills
        )
    )

    job_match_score = 0

    skill_match_percentage = 0

    matching_skills = []

    missing_skills = []

    job_skills = []

    if job_description.strip():

        job_match_score = calculate_job_match(
            resume_text,
            job_description
        )

        job_skills = extract_skills(
            job_description
        )

        (
            matching_skills,
            missing_skills
        ) = compare_skills(
            detected_skills,
            job_skills
        )

        skill_match_percentage = (
            calculate_skill_match_percentage(
                detected_skills,
                job_skills
            )
        )

    return render_template(
        "results.html",
        resume_result=resume_result,
        detected_skills=detected_skills,
        resume_text=resume_text,
        job_description=job_description,
        ats_result=ats_result,
        resume_suggestions=resume_suggestions,
        job_match_score=job_match_score,
        skill_match_percentage=skill_match_percentage,
        matching_skills=matching_skills,
        missing_skills=missing_skills,
        job_skills=job_skills
    )


@app.route(
    "/download-report",
    methods=["POST"]
)
def download_report():

    resume_score = request.form.get(
        "resume_score",
        "0"
    )

    ats_score = request.form.get(
        "ats_score",
        "0"
    )

    job_match_score = request.form.get(
        "job_match_score",
        "0"
    )

    skill_match_percentage = request.form.get(
        "skill_match_percentage",
        "0"
    )

    matching_skills = request.form.get(
        "matching_skills",
        ""
    )

    missing_skills = request.form.get(
        "missing_skills",
        ""
    )

    suggestions = request.form.get(
        "suggestions",
        ""
    )

    file_path = os.path.join(
        "uploads",
        "resume_analysis_report.pdf"
    )

    pdf = canvas.Canvas(
        file_path,
        pagesize=A4
    )

    width, height = A4

    y = height - 50

    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawString(
        50,
        y,
        "AI Resume Analyzer Report"
    )

    y -= 40

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        50,
        y,
        f"Resume Score: {resume_score}/100"
    )

    y -= 25

    pdf.drawString(
        50,
        y,
        f"ATS Score: {ats_score}%"
    )

    y -= 25

    pdf.drawString(
        50,
        y,
        f"Job Match Score: {job_match_score}%"
    )

    y -= 25

    pdf.drawString(
        50,
        y,
        f"Skill Match: {skill_match_percentage}%"
    )

    y -= 40

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        y,
        "Matching Skills"
    )

    y -= 25

    pdf.setFont(
        "Helvetica",
        11
    )

    for skill in matching_skills.split(","):

        if skill.strip():

            pdf.drawString(
                60,
                y,
                "• " + skill.strip()
            )

            y -= 18

    y -= 15

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        y,
        "Missing Skills"
    )

    y -= 25

    pdf.setFont(
        "Helvetica",
        11
    )

    for skill in missing_skills.split(","):

        if skill.strip():

            pdf.drawString(
                60,
                y,
                "• " + skill.strip()
            )

            y -= 18

    y -= 15

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        y,
        "Resume Suggestions"
    )

    y -= 25

    pdf.setFont(
        "Helvetica",
        11
    )

    for suggestion in suggestions.split("|"):

        if suggestion.strip():

            pdf.drawString(
                60,
                y,
                "• " + suggestion.strip()
            )

            y -= 18

            if y < 50:

                pdf.showPage()

                y = height - 50

                pdf.setFont(
                    "Helvetica",
                    11
                )

    pdf.save()

    return send_file(
        file_path,
        as_attachment=True,
        download_name="resume_analysis_report.pdf"
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )