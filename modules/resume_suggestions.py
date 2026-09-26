def generate_resume_suggestions(resume_text, detected_skills):

    suggestions = []

    text = resume_text.lower()

    # Check technical skills
    if len(detected_skills) < 5:
        suggestions.append(
            "Add more relevant technical skills to your resume."
        )

    # Check education
    education_keywords = [
        "education",
        "b.e",
        "b.tech",
        "bachelor",
        "degree",
        "college",
        "university"
    ]

    if not any(keyword in text for keyword in education_keywords):
        suggestions.append(
            "Add your educational qualifications."
        )

    # Check projects
    project_keywords = [
        "project",
        "projects"
    ]

    if not any(keyword in text for keyword in project_keywords):
        suggestions.append(
            "Add academic or personal projects to demonstrate practical skills."
        )

    # Check experience
    experience_keywords = [
        "experience",
        "internship",
        "work experience",
        "worked as"
    ]

    if not any(keyword in text for keyword in experience_keywords):
        suggestions.append(
            "Add internship, work experience, or relevant practical experience."
        )

    # Check certifications
    certification_keywords = [
        "certification",
        "certifications",
        "certificate",
        "certified"
    ]

    if not any(keyword in text for keyword in certification_keywords):
        suggestions.append(
            "Add relevant certifications to strengthen your resume."
        )

    # Check contact information
    contact_keywords = [
        "@",
        "phone",
        "mobile",
        "email"
    ]

    if not any(keyword in text for keyword in contact_keywords):
        suggestions.append(
            "Add your contact information such as email and phone number."
        )

    # If no problems are found
    if not suggestions:
        suggestions.append(
            "Your resume contains the major sections. "
            "Consider improving formatting and tailoring it to the target job."
        )

    return suggestions