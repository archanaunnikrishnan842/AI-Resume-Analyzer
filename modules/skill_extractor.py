import os
import re


def load_skills():

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    skills_file = os.path.join(
        base_dir,
        "data",
        "skills.txt"
    )

    with open(
        skills_file,
        "r",
        encoding="utf-8"
    ) as file:

        skills = [
            line.strip()
            for line in file
            if line.strip()
        ]

    return skills


def extract_skills(resume_text):

    skills = load_skills()

    detected_skills = []

    for skill in skills:

        # Escape special characters
        # so skills like C++, C#, etc. work correctly.
        escaped_skill = re.escape(skill)

        # Match complete words instead of
        # matching letters inside other words.
        pattern = r"(?<!\w)" + escaped_skill + r"(?!\w)"

        if re.search(
            pattern,
            resume_text,
            re.IGNORECASE
        ):

            detected_skills.append(skill)

    return detected_skills