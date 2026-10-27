
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

levels = [
    "Very Low",
    "Low",
    "Moderate",
    "High",
    "Very High"
]

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
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 📱 Digital Grip")
st.sidebar.markdown("Smartphone Dependence Analysis")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Predict Risk",
        "Analytics",
        "Model Information",
        "About"
    ]
)

# Home
if page == "Home":

    st.markdown(
        '<div class="main-title">Take Control of Your Digital Life</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Understand your smartphone habits and discover your digital dependence level.</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>📱 What is Digital Grip?</h3>
        <p>
        Digital Grip is a machine-learning based system that analyzes
        smartphone usage behaviors and estimates a user's smartphone
        dependence level.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🧠 Analyze</h3>
            <p>Analyze important smartphone-related behavioral patterns.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>📊 Predict</h3>
            <p>Use machine learning to estimate your dependence level.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>💡 Improve</h3>
            <p>Understand your habits and make healthier digital choices.</p>
        </div>
        """, unsafe_allow_html=True)

# Predict Risk
elif page == "Predict Risk":

    st.markdown(
        '<div class="section-title">📱 Predict Smartphone Dependence</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Answer the following questions based on your usual smartphone habits."
    )

    st.info("1 = Very Low    |    5 = Very High")

    phone_checking = st.slider(
        "1. How often do you check your phone without receiving a notification?",
        1, 5, 3
    )

    distraction = st.slider(
        "2. How often does smartphone use distract you while studying or working?",
        1, 5, 3
    )

    night_checking = st.slider(
        "3. How often do you wake up during the night and check your smartphone?",
        1, 5, 3
    )

    sleep_impact = st.slider(
        "4. How much does smartphone usage affect your sleep quality?",
        1, 5, 3
    )

    check_within_15 = st.slider(
        "5. How often do you check your smartphone within 15 minutes of waking up?",
        1, 5, 3
    )

    reduce_difficulty = st.slider(
        "6. How difficult is it for you to reduce your smartphone usage?",
        1, 5, 3
    )

    comfort_without_phone = st.slider(
        "7. How uncomfortable do you feel without your smartphone?",
        1, 5, 3
    )

    usage_interference = st.slider(
        "8. How often does smartphone use interfere with your responsibilities?",
        1, 5, 3
    )

    productivity_impact = st.slider(
        "9. How often does smartphone use reduce your productivity?",
        1, 5, 3
    )

    urge_to_check = st.slider(
        "10. How often do you feel the urge to check your smartphone?",
        1, 5, 3
    )

    if st.button("🔍 Predict Dependence", use_container_width=True):

        user_data = pd.DataFrame([{
            "Phone_Checking": phone_checking,
            "Distraction": distraction,
            "Night_Checking": night_checking,
            "Sleep_Impact": sleep_impact,
            "Check_Within_15_Min": check_within_15,
            "Reduce_Difficulty": reduce_difficulty,
            "Comfort_Without_Phone": comfort_without_phone,
            "Usage_Interference": usage_interference,
            "Productivity_Impact": productivity_impact,
            "Urge_To_Check": urge_to_check
        }])

        prediction = model.predict(user_data)[0]
        probabilities = model.predict_proba(user_data)[0]

        predicted_level = reverse_mapping[prediction]

        st.markdown("---")
        st.markdown("### 🎯 Your Result")

        if predicted_level == "Very Low":
            st.success("Your smartphone dependence level is Very Low.")
        elif predicted_level == "Low":
            st.success("Your smartphone dependence level is Low.")
        elif predicted_level == "Moderate":
            st.warning("Your smartphone dependence level is Moderate.")
        elif predicted_level == "High":
            st.warning("Your smartphone dependence level is High.")
        else:
            st.error("Your smartphone dependence level is Very High.")

        st.markdown("### 📊 Prediction Probability")

        probability_df = pd.DataFrame({
            "Dependence Level": levels,
            "Probability (%)": (probabilities * 100).round(2)
        })

        st.dataframe(
            probability_df,
            use_container_width=True,
            hide_index=True
        )

# Analytics
elif page == "Analytics":

    st.markdown(
        '<div class="section-title">📊 Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>Model Validation</h3>
        <p>
        The Random Forest model was evaluated using 5-fold stratified
        cross-validation on the real response dataset.
        </p>
        <h2>55.00% ± 2.85%</h2>
        <p>Mean cross-validation accuracy</p>
    </div>
    """, unsafe_allow_html=True)

# Model Information
elif page == "Model Information":

    st.markdown(
        '<div class="section-title">🤖 Model Information</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>Random Forest Classifier</h3>
        <p>
        Digital Grip uses a Random Forest classification model to estimate
        smartphone dependence from behavioral responses.
        </p>
    </div>

    <div class="card">
        <h3>Features Used</h3>
        <p>
        Phone checking, distraction, night checking, sleep impact,
        morning phone checking, difficulty reducing usage, discomfort
        without the phone, interference with responsibilities,
        productivity impact, and urge to check.
        </p>
    </div>

    <div class="card">
        <h3>Dependence Levels</h3>
        <p>
        Very Low → Low → Moderate → High → Very High
        </p>
    </div>
    """, unsafe_allow_html=True)

# About
elif page == "About":

    st.markdown(
        '<div class="section-title">ℹ️ About Digital Grip</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>About the Project</h3>
        <p>
        Digital Grip is a machine-learning project designed to understand
        smartphone usage behavior and estimate smartphone dependence.
        </p>

        <p>
        The system focuses on behavioral indicators such as distraction,
        phone checking, productivity impact, sleep impact, and the urge
        to check the smartphone.
        </p>
    </div>
    """, unsafe_allow_html=True)
