from modules.ats_analyzer import analyze_ats


sample_resume = """
Archana P

Email: archana@example.com
Phone: 9876543210

Professional Summary

Computer Science Engineering student interested in Cloud Computing.

Education

B.E. Computer Science and Engineering

Technical Skills

Python, SQL, AWS, Git, Linux

Projects

AI Resume Analyzer

Experience

Internship experience

Certifications

ServiceNow CSA
ServiceNow CAD
"""


result = analyze_ats(sample_resume)


print("ATS Score:", result["ats_score"], "%")


print("\nSections:")

for section, present in result["sections"].items():

    if present:
        print("✅", section)

    else:
        print("❌", section)


print("\nMissing Sections:")

for section in result["missing_sections"]:

    print("-", section)


print("\nSuggestions:")

for suggestion in result["suggestions"]:

    print("-", suggestion)