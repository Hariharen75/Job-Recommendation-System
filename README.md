# Job Recommendation System using spaCy PhraseMatcher

## Overview
This project recommends jobs to users based on their skills. It uses Natural Language Processing (NLP) with spaCy PhraseMatcher to extract skills from user profiles and job requirements. The extracted skills are compared to calculate a similarity score and recommend the most suitable jobs.

## Problem Statement
Job seekers often struggle to find positions that match their skills. This project automates the process by analyzing user skills and matching them with job requirements.

## Features
- Skill Extraction using spaCy PhraseMatcher
- Job Requirement Analysis
- Similarity Score Calculation
- Job Recommendation
- NLP-based Matching

## Technologies Used
- Python
- Pandas
- spaCy
- PhraseMatcher
- Jupyter Notebook

## Workflow

Dataset
→ EDA
→ Data Preprocessing
→ Skill Extraction using PhraseMatcher
→ Skill Matching
→ Similarity Score Calculation
→ Job Recommendation

## Dataset Columns

- User_ID
- Job_ID
- User_Skills
- Job_Requirements
- Match_Score
- Recommended

## Installation

```bash
pip install pandas spacy
```

## Run

```bash
python job_recommendation.py
```

