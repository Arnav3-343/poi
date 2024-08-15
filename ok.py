import streamlit as st
import pandas as pd

# Function to calculate risk level based on time
def calculate_risk_level(time):
    if time < 10:
        return "High Risk"
    elif time < 30:
        return "Moderate Risk"
    else:
        return "Low Risk"

# Streamlit app
st.title("Timed Standing on One Foot Test")

# Instructions
st.write("This app allows you to enter the results for the timed standing on one foot test.")
st.write("You will input the time (in seconds) for each leg across three trials.")

# Input for the test results
st.subheader("Enter Times for Left Leg")
left_leg_times = [st.number_input(f"Left Leg - Trial {i+1} (seconds)", min_value=0.0, format="%.1f", key=f"left_trial_{i}") for i in range(3)]

st.subheader("Enter Times for Right Leg")
right_leg_times = [st.number_input(f"Right Leg - Trial {i+1} (seconds)", min_value=0.0, format="%.1f", key=f"right_trial_{i}") for i in range(3)]

# Create a DataFrame to display the results
data = {
    "Trial": [1, 2, 3],
    "Left Leg Time (seconds)": left_leg_times,
    "Right Leg Time (seconds)": right_leg_times,
}

df = pd.DataFrame(data)

# Display the table
st.subheader("Test Results")
st.write(df)

# Calculate and display risk levels
left_leg_risks = [calculate_risk_level(time) for time in left_leg_times]
right_leg_risks = [calculate_risk_level(time) for time in right_leg_times]

risk_data = {
    "Trial": [1, 2, 3],
    "Left Leg Risk Level": left_leg_risks,
    "Right Leg Risk Level": right_leg_risks,
}

risk_df = pd.DataFrame(risk_data)

st.subheader("Risk Levels")
st.write(risk_df)

# Optional: Calculate and display average times and risk levels
average_left_leg_time = sum(left_leg_times) / len(left_leg_times) if left_leg_times else 0
average_right_leg_time = sum(right_leg_times) / len(right_leg_times) if right_leg_times else 0

st.subheader("Average Times and Risk Levels")
st.write(f"Average Left Leg Time: {average_left_leg_time:.1f} seconds - Risk Level: {calculate_risk_level(average_left_leg_time)}")
st.write(f"Average Right Leg Time: {average_right_leg_time:.1f} seconds - Risk Level: {calculate_risk_level(average_right_leg_time)}")

# Navigation button to ALS vowel analysis app
if st.button("Next: Go to ALS Vowel Analysis App"):
    st.session_state["next_app"] = "als_vowel_analysis"

# Redirect to ALS Vowel Analysis App
if "next_app" in st.session_state and st.session_state["next_app"] == "als_vowel_analysis":
    st.write("[Click here to go to ALS Vowel Analysis App](http://localhost:8502/als_vowel_analysis)")
