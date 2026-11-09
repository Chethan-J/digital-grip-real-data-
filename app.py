
        elif predicted_level == "High":

            st.warning(
                "⚠️ Your smartphone usage shows a high level of dependence."
            )

        else:

            st.error(
                "🚨 Your smartphone usage shows a very high level of dependence."
            )

        st.html(f"""
        <div class="suggestion-card">
            <h3>💡 Suggestion for You</h3>

            <p>
                {suggestions[predicted_level]}
            </p>
        </div>
        """)


# Analytics
elif page == "Analytics":

    st.markdown(
        '<div class="section-title">📊 Analytics</div>',
        unsafe_allow_html=True
    )

    st.html("""
    <div class="card">
        <h3>Model Validation</h3>

        <p>
        The Random Forest model was evaluated using 5-fold stratified
        cross-validation on the real response dataset.
        </p>

        <h2>55.00% ± 2.85%</h2>

        <p>
        Mean cross-validation accuracy
        </p>
    </div>
    """)

    st.markdown("### Test Dataset Performance")
    st.write(
        "The following metrics show the model's performance on the "
        "held-out test dataset. Precision, recall, and F1-score are "
        "weighted averages."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Accuracy", "55.71%")

    with col2:
        st.metric("Precision", "49%")

    with col3:
        st.metric("Recall", "56%")

    with col4:
        st.metric("F1-Score", "51%")


# Model Information
elif page == "Model Information":

    st.markdown(
        '<div class="section-title">🤖 Model Information</div>',
        unsafe_allow_html=True
    )

    st.html("""
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
    """)


# About
elif page == "About":

    st.markdown(
        '<div class="section-title">ℹ️ About Digital Grip</div>',
        unsafe_allow_html=True
    )

    st.html("""
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
    """)
