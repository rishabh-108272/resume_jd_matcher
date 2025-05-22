import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer (ensure you saved them during training)
model = joblib.load("resume_job_matching_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Resume-JD Match Predictor")

# Inputs
resume_text = st.text_area("Paste Resume Content")
jd_text = st.text_area("Paste Job Description")

if st.button("Predict Match"):
    if resume_text.strip() and jd_text.strip():
        combined_text = resume_text + " " + jd_text
        input_vector = vectorizer.transform([combined_text])  # Always use list
        prediction = model.predict(input_vector)[0]
        probability = model.predict_proba(input_vector)[0][1]  # Optional: match confidence

        st.success(f"✅ Match!" if prediction == 1 else "❌ No Match")
        st.write(f"Confidence Score: {probability:.2f}")
    else:
        st.warning("Please provide both resume and job description.")
