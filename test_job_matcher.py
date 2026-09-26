from modules.job_matcher import (
    calculate_job_match,
    compare_skills
)


resume = """
I am a Computer Science student with experience in
Python, SQL, AWS, Git and ServiceNow.
I have knowledge of cloud computing and Linux.
"""


job_description = """
We are looking for a Cloud Engineer with experience in
Python, AWS, Linux, Docker and Terraform.
The candidate should have knowledge of cloud computing.
"""


match_score = calculate_job_match(
    resume,
    job_description
)


resume_skills = [
    "Python",
    "SQL",
    "AWS",
    "Git",
    "ServiceNow",
    "Linux"
]


job_skills = [
    "Python",
    "AWS",
    "Linux",
    "Docker",
    "Terraform"
]


matching_skills, missing_skills = compare_skills(
    resume_skills,
    job_skills
)


print("Job Match Score:", match_score, "%")


print("\nMatching Skills:")

for skill in matching_skills:
    print("✅", skill)


print("\nMissing Skills:")

for skill in missing_skills:
    print("❌", skill)