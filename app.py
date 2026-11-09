import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Digital Grip",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load model
model = joblib.load("digital_grip_real_model.pkl")

reverse_mapping = {
    0: "Very Low",
    1: "Low",
    2: "Moderate",
    3: "High",
    4: "Very High"
}

# Suggestions for each dependence level
suggestions = {
    "Very Low": "Your smartphone habits appear well controlled. Continue maintaining healthy screen-time habits and regular phone-free periods.",

    "Low": "Your smartphone dependence is relatively low. Try keeping unnecessary notifications off and maintain regular phone-free periods during study, work, and sleep.",

    "Moderate": "Try setting specific phone-free periods during study or work. Reduce unnecessary phone checking and avoid using your smartphone immediately before sleep.",

    "High": "Consider setting daily screen-time limits, reducing unnecessary notifications, and creating dedicated phone-free periods during study, work, and sleep.",

    "Very High": "Your smartphone usage may be strongly affecting your daily habits. Consider strict screen-time limits, reducing notifications, creating phone-free periods, and gradually reducing unnecessary phone checking."
}

# Custom theme
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0b1020, #111936, #17133a);
    color: white;
}

[data-testid="stSidebar"] {
    background: #0b1020;
}

[data-testid="stSidebar"] * {
    color: white;
}

.main-title {
    font-size: 52px;
    font-weight: 800;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 20px;
    color: #b8bfd6;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
}

.card h3 {
    color: white;
}

.card p {
    color: #b8bfd6;
    line-height: 1.6;
}

.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 20px;
}

.result-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 30px;
    margin-top: 20px;
    margin-bottom: 20px;
}
