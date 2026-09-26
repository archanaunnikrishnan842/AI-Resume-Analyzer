import math
import re
from collections import Counter


# ==================================================
# STOP WORDS
# ==================================================

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be",
    "by", "for", "from", "has", "have", "in",
    "is", "it", "of", "on", "or", "that",
    "the", "this", "to", "with", "we", "you",
    "your", "our", "will", "should", "looking",
    "candidate", "experience", "knowledge"
}


# ==================================================
# TOKENIZE TEXT
# ==================================================

def _tokenize(text):

    words = re.findall(
        r"[a-zA-Z0-9+#.]+",
        text.lower()
    )

    return [
        word
        for word in words
        if word not in STOP_WORDS
    ]


# ==================================================
# TERM FREQUENCY
# ==================================================

def _calculate_tf(tokens):

    if not tokens:
        return {}

    word_counts = Counter(tokens)

    total_words = len(tokens)

    return {
        word: count / total_words
        for word, count in word_counts.items()
    }


# ==================================================
# JOB MATCHING
# TF-IDF + COSINE SIMILARITY
# ==================================================

def calculate_job_match(
    resume_text,
    job_description
):

    resume_tokens = _tokenize(resume_text)

    job_tokens = _tokenize(job_description)

    documents = [
        resume_tokens,
        job_tokens
    ]

    document_count = len(documents)

    vocabulary = set(
        resume_tokens + job_tokens
    )

    if not vocabulary:
        return 0.0


    # ----------------------------------------------
    # DOCUMENT FREQUENCY
    # ----------------------------------------------

    document_frequency = {}

    for word in vocabulary:

        document_frequency[word] = sum(
            1
            for document in documents
            if word in document
        )


    # ----------------------------------------------
    # IDF
    # ----------------------------------------------

    idf = {}

    for word in vocabulary:

        idf[word] = (
            math.log(
                (1 + document_count)
                /
                (1 + document_frequency[word])
            )
            + 1
        )


    # ----------------------------------------------
    # TF-IDF
    # ----------------------------------------------

    vectors = []

    for tokens in documents:

        tf = _calculate_tf(tokens)

        vector = {}

        for word in vocabulary:

            vector[word] = (
                tf.get(word, 0.0)
                * idf[word]
            )

        vectors.append(vector)


    resume_vector = vectors[0]

    job_vector = vectors[1]


    # ----------------------------------------------
    # DOT PRODUCT
    # ----------------------------------------------

    dot_product = sum(
        resume_vector[word]
        * job_vector[word]
        for word in vocabulary
    )


    # ----------------------------------------------
    # MAGNITUDES
    # ----------------------------------------------

    resume_magnitude = math.sqrt(
        sum(
            value ** 2
            for value in resume_vector.values()
        )
    )

    job_magnitude = math.sqrt(
        sum(
            value ** 2
            for value in job_vector.values()
        )
    )


    if (
        resume_magnitude == 0
        or job_magnitude == 0
    ):

        return 0.0


    # ----------------------------------------------
    # COSINE SIMILARITY
    # ----------------------------------------------

    similarity = (
        dot_product
        /
        (
            resume_magnitude
            * job_magnitude
        )
    )


    return round(
        similarity * 100,
        2
    )


# ==================================================
# COMPARE SKILLS
# ==================================================

def compare_skills(
    resume_skills,
    job_skills
):

    resume_skills_lower = {
        skill.lower(): skill
        for skill in resume_skills
    }

    job_skills_lower = {
        skill.lower(): skill
        for skill in job_skills
    }

    matching_skills = []

    missing_skills = []


    for (
        skill_lower,
        original_skill
    ) in job_skills_lower.items():

        if skill_lower in resume_skills_lower:

            matching_skills.append(
                original_skill
            )

        else:

            missing_skills.append(
                original_skill
            )


    return (
        matching_skills,
        missing_skills
    )


# ==================================================
# SKILL MATCH PERCENTAGE
# ==================================================

def calculate_skill_match_percentage(
    resume_skills,
    job_skills
):

    if not job_skills:
        return 0.0


    matching_skills, missing_skills = (
        compare_skills(
            resume_skills,
            job_skills
        )
    )


    percentage = (
        len(matching_skills)
        /
        len(job_skills)
    ) * 100


    return round(
        percentage,
        2
    )