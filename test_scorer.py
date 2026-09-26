from modules.resume_scorer import calculate_resume_score


sample_resume = """
Archana P
Email: archana@example.com
Phone: 9876543210

Education
B.E Computer Science and Engineering

Projects
AI Resume Analyzer

Experience
Internship in Software Development

Certifications
ServiceNow Certified Application Developer

Skills
Python, SQL, Git, AWS, ServiceNow
"""


detected_skills = [
    "Python",
    "SQL",
    "Git",
    "AWS",
    "ServiceNow"
]


result = calculate_resume_score(
    sample_resume,
    detected_skills
)


print("Resume Score")
print("----------------")

print("Total Score:", result["total_score"])
print("Skill Score:", result["skill_score"])
print("Education Score:", result["education_score"])
print("Project Score:", result["project_score"])
print("Experience Score:", result["experience_score"])
print("Certification Score:", result["certification_score"])
print("Contact Score:", result["contact_score"])