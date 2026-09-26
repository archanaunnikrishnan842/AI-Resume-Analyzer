from modules.skill_extractor import extract_skills


sample_resume = """
I am a Computer Science student with experience in Python,
SQL, AWS, Git and ServiceNow.
I have also worked with HTML and JavaScript.
"""


skills = extract_skills(sample_resume)

print("Detected Skills:")
print(skills)