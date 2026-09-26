def calculate_resume_score(resume_text, detected_skills):
    text = resume_text.lower()

    score = 0

    # Skills - 30 marks
    if len(detected_skills) >= 8:
        skill_score = 30
    elif len(detected_skills) >= 5:
        skill_score = 25
    elif len(detected_skills) >= 3:
        skill_score = 20
    elif len(detected_skills) >= 1:
        skill_score = 10
    else:
        skill_score = 0

    score += skill_score

    # Education - 20 marks
    education_keywords = [
        "education",
        "b.e",
        "b.tech",
        "bachelor",
        "degree",
        "college",
        "university"
    ]

    education_score = 20 if any(
        keyword in text for keyword in education_keywords
    ) else 0

    score += education_score

    # Projects - 20 marks
    project_keywords = [
        "project",
        "projects"
    ]

    project_score = 20 if any(
        keyword in text for keyword in project_keywords
    ) else 0

    score += project_score

    # Experience - 15 marks
    experience_keywords = [
        "experience",
        "internship",
        "work experience",
        "worked as"
    ]

    experience_score = 15 if any(
        keyword in text for keyword in experience_keywords
    ) else 0

    score += experience_score

    # Certifications - 10 marks
    certification_keywords = [
        "certification",
        "certifications",
        "certificate",
        "certified"
    ]

    certification_score = 10 if any(
        keyword in text for keyword in certification_keywords
    ) else 0

    score += certification_score

    # Contact Information - 5 marks
    contact_keywords = [
        "@",
        "phone",
        "mobile",
        "email"
    ]

    contact_score = 5 if any(
        keyword in text for keyword in contact_keywords
    ) else 0

    score += contact_score

    return {
        "total_score": score,
        "skill_score": skill_score,
        "education_score": education_score,
        "project_score": project_score,
        "experience_score": experience_score,
        "certification_score": certification_score,
        "contact_score": contact_score
    }