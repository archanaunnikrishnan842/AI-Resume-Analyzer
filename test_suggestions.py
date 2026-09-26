from modules.resume_suggestions import generate_resume_suggestions


sample_resume = """
I am a Computer Science student.

I know Python and SQL.

I am studying B.E. Computer Science.
"""


detected_skills = [
    "Python",
    "SQL"
]


suggestions = generate_resume_suggestions(
    sample_resume,
    detected_skills
)


print("Resume Improvement Suggestions:")


for suggestion in suggestions:
    print("⚠️", suggestion)