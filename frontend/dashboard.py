import streamlit as st
import numpy as np
from ml_models.predict_model import load_model, predict_fatigue
from fuzzy_engine.fuzzy_model import calculate_fatigue_score
from nlp_module.sentiment_analysis import analyze_sentiment

# Load trained model
model = load_model()

st.title("Mental Fatigue Detection System")
st.subheader("Engineering Students AI Analysis")

st.write("Enter student details to predict mental fatigue level.")

# User inputs
sleep_hours = st.slider("Sleep Hours", 0, 10, 6)
study_hours = st.slider("Study Hours", 0, 12, 6)
screen_time = st.slider("Screen Time", 0, 12, 6)
stress_level = st.slider("Stress Level", 1, 10, 5)
workload = st.slider("Workload", 1, 10, 5)
exercise_hours = st.slider("Exercise Hours", 0, 5, 1)
caffeine_intake = st.slider("Caffeine Intake", 0, 5, 1)
break_frequency = st.slider("Break Frequency", 0, 5, 2)
assignment_pressure = st.slider("Assignment Pressure", 1, 10, 5)

feedback = st.text_area("Student Feedback")

# Predict button
if st.button("Predict Fatigue"):

    student_data = [
        sleep_hours,
        study_hours,
        screen_time,
        stress_level,
        workload,
        exercise_hours,
        caffeine_intake,
        break_frequency,
        assignment_pressure
    ]

    # ML prediction
    prediction = predict_fatigue(model, student_data)

    # Fuzzy logic
    score, level = calculate_fatigue_score(
        sleep_hours,
        stress_level,
        study_hours
    )

    # NLP sentiment
    sentiment = analyze_sentiment(feedback)

    st.subheader("Results")

    st.write("ML Predicted Fatigue Level:", prediction)
    st.write("Fuzzy Fatigue Level:", level)
    st.write("Fuzzy Fatigue Score:", score)
    st.write("Feedback Sentiment:", sentiment)