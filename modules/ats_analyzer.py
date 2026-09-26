import re


def analyze_ats(resume_text):

    text = resume_text.lower()

    sections = {
        "Contact Information": False,
        "Education": False,
        "Skills": False,
        "Projects": False,
        "Experience": False,
        "Certifications": False,
        "Summary / Objective": False
    }

    # Contact Information
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"\b\d{10}\b"

    has_email = re.search(email_pattern, resume_text)
    has_phone = re.search(phone_pattern, resume_text)

    if has_email or has_phone:
        sections["Contact Information"] = True

    # Education
    education_keywords = [
        "education",
        "b.e",
        "b.tech",
        "bachelor",
        "degree",
        "college",
        "university"
    ]

    if any(keyword in text for keyword in education_keywords):
        sections["Education"] = True

    # Skills
    skill_keywords = [
        "skills",
        "technical skills",
        "programming",
        "technologies",
        "technical knowledge"
    ]

    if any(keyword in text for keyword in skill_keywords):
        sections["Skills"] = True

    # Projects
    project_keywords = [
        "project",
        "projects",
        "academic project",
        "personal project"
    ]

    if any(keyword in text for keyword in project_keywords):
        sections["Projects"] = True

    # Experience
    experience_keywords = [
        "experience",
        "work experience",
        "internship",
        "intern",
        "worked as",
        "employment"
    ]

    if any(keyword in text for keyword in experience_keywords):
        sections["Experience"] = True

    # Certifications
    certification_keywords = [
        "certification",
        "certifications",
        "certificate",
        "certified"
    ]

    if any(keyword in text for keyword in certification_keywords):
        sections["Certifications"] = True

    # Summary / Objective
    summary_keywords = [
        "summary",
        "professional summary",
        "career objective",
        "objective",
        "profile"
    ]

    if any(keyword in text for keyword in summary_keywords):
        sections["Summary / Objective"] = True

    # Calculate ATS score
    total_sections = len(sections)

    completed_sections = sum(sections.values())

    ats_score = round(
        (completed_sections / total_sections) * 100,
        2
    )

    # Find missing sections
    missing_sections = [
        section
        for section, present in sections.items()
        if not present
    ]

    # Generate suggestions
    suggestions = []

    for section in missing_sections:
        suggestions.append(
            f"Consider adding a {section} section."
        )

    if not suggestions:
        suggestions.append(
            "Your resume contains all the major ATS sections."
        )

    return {
        "ats_score": ats_score,
        "sections": sections,
        "missing_sections": missing_sections,
        "suggestions": suggestions
    }