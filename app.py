import streamlit as st
import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Skill list
skills = [
    "python",
    "sql",
    "machine learning",
    "java",
    "data analysis",
    "tensorflow",
    "deep learning"
]

# Create matcher
matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp(skill) for skill in skills]
matcher.add("SKILLS", patterns)

# Extract skills
def extract_skills(text):
    doc = nlp(str(text).lower())
    matches = matcher(doc)

    found_skills = []
    for match_id, start, end in matches:
        found_skills.append(doc[start:end].text)

    return list(set(found_skills))

# Similarity calculation
def skill_match(user_skills, job_skills):
    user_set = set(user_skills)
    job_set = set(job_skills)

    if len(job_set) == 0:
        return 0

    return len(user_set.intersection(job_set)) / len(job_set)

# Streamlit UI
st.title("Job Recommendation System")

uploaded_file = st.file_uploader(
    "Upload Job Dataset CSV",
    type=["csv"]
)

user_input = st.text_area(
    "Enter Your Skills",
    placeholder="Python, SQL, Machine Learning"
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    if st.button("Recommend Jobs"):

        user_skills = extract_skills(user_input)

        df["Extracted_User_Skills"] = [user_skills] * len(df)

        df["Extracted_Job_Skills"] = df["Job_Requirements"].apply(
            extract_skills
        )

        df["Similarity"] = df.apply(
            lambda x: skill_match(
                x["Extracted_User_Skills"],
                x["Extracted_Job_Skills"]
            ),
            axis=1
        )

        recommendations = df.sort_values(
            by="Similarity",
            ascending=False
        )

        st.subheader("Top Job Recommendations")

        st.dataframe(
            recommendations[
                ["Job_ID", "Job_Requirements", "Similarity"]
            ].head(10)
        )