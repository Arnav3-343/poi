import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_features(data):
    """Preprocesses and ensures features are consistent with training data."""
    for column in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column].astype(str))

    X = data.drop(columns=["Diagnosis (ALS)"])
    y = data["Diagnosis (ALS)"]

    try:
        y = y.astype(int)
    except ValueError as e:
        st.error(f"Error: Non-numeric values found in target variable: {e}")
        return None, None

    return X, y

def preprocess_audio(audio_file):
    """Extracts features from the uploaded audio file."""
    return np.zeros((134,))  # Example placeholder; replace with actual feature extraction

def predict_als_risk_prob(features, model):
    """Predict ALS risk probability based on extracted features."""
    probabilities = model.predict_proba(features.reshape(1, -1))
    return probabilities[0]

def main():
    st.title("ALS Vowel Analysis App")

    st.write("""
    ### Instructions for Use:
    1. **Prepare Your Dataset**:
       - Ensure your dataset, `Minsk2020_ALS_dataset.csv`, includes pre-extracted features and the `Diagnosis (ALS)` column.
    2. **Test Your Model**:
       - Upload a WAV audio file (e.g., of a person pronouncing vowels "a" or "i").
    3. **Run the Script**:
       - Save the script as `als_vowel_analysis.py` and run with:
         ```bash
         streamlit run als_vowel_analysis.py
         ```
       - Follow the web interface instructions.
    """)

    data = pd.read_csv("Minsk2020_ALS_dataset.csv")
    X, y = preprocess_features(data)
    if X is None or y is None:
        return

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    uploaded_file = st.file_uploader("Choose an audio file")
    if uploaded_file is not None:
        features = preprocess_audio(uploaded_file)
        if features is not None:
            probabilities = predict_als_risk_prob(features, model)
            prob_als = probabilities[1] * 100
            prob_healthy = probabilities[0] * 100

            st.write(f"Probability of ALS: {prob_als:.2f}%")
            st.write(f"Probability of Healthy: {prob_healthy:.2f}%")

            if prob_als > 50:
                st.write("High risk of ALS")
            else:
                st.write("Low risk of ALS")

if __name__ == "__main__":
    main()
