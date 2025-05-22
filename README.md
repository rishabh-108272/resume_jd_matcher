# Resume and Job Description matcher
Simple NLP project to predict the score of match between resume and job description.

# Resume and Job Description Analysis Pipeline

## Overview

This project implements an NLP-powered pipeline to extract **skills** and **experience-related phrases** from:

- Candidate **resumes**
- Employer **job descriptions**

It leverages **SpaCy** and **NLTK** to tokenize, process, and analyze natural language text. The results are saved into human-readable `.txt` corpora for downstream applications like matching, clustering, or visualization.

---

##  Dataset Structure

###  Resumes

- **File**: `UpdatedResumeDataSet.csv`
- **Columns**:
  - `Category`: Role or field (e.g., Data Science)
  - `Resume`: Raw resume text

###  Job Descriptions

- **File**: `job_descriptions.csv`
- **Columns**:
  - `Job Description`: Raw text of job postings

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/rishabh-108272/resume_jd_matcher.git
cd resume_jd_matcher
