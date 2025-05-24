import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load models & scaler
with open("rf_model.pkl", "rb") as f:
    rf_model = pickle.load(f)
with open("svc_model.pkl", "rb") as f:
    svc_model = pickle.load(f)
with open("dt_model.pkl", "rb") as f:
    dt_model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

models = {
    "Random Forest": rf_model,
    "Support Vector Classifier": svc_model,
    "Decision Tree": dt_model
}

df_filtered = pd.read_csv("filtered_selected_features.csv")
feature_cols = df_filtered.columns[:-1]

# Defining the features and their ranges
feature_info = {
    'BehavioralProblems': {
        'Range': '0 to 1',
        'Description': 'Indicates whether the patient has behavioural problems. 0 = No, 1 = Yes'
    },
    'Gender': {
        'Range': '0 to 1',
        'Description': 'Gender of the patient. 0 = Male, 1 = Female'
    },
    'MemoryComplaints': {
        'Range': '0 to 1',
        'Description': 'Indicates whether the patient has memory complaints. 0 = No, 1 = Yes'
    },
    'FunctionalAssessment': {
        'Range': '0 to 10',
        'Description': 'Functional assessment score, ranging from 0 to 10. Lower scores indicate greater impairment.'
    },
    'ADL': {
        'Range': '0 to 10',
        'Description': 'Activities of Daily Living (ADL) score, ranging from 0 to 10. Lower scores indicate greater impairment.'
    },
    'MMSE': {
        'Range': '0 to 30',
        'Description': 'Mini-Mental State Examination (MMSE) score, ranging from 0 to 30. Lower scores indicate cognitive impairment.'
    }
}

# Clean up feature names to match the keys in feature_info
def feature_name(feature):
    feature_clean = feature.strip().replace(" ", "")
    return feature_clean

# Convert the feature into a table
feature_table = pd.DataFrame.from_dict(feature_info, orient='index')

def validate_input(feature, value):
    """Validate that input value is within the valid range."""
    feature_match = feature_name(feature) 
    
    if feature_match not in feature_info:
        return f"Error: The feature '{feature}' is not recognized."

    range_str = feature_info[feature_match]['Range']
    min_val, max_val = map(float, range_str.split(' to '))
    
    if not (min_val <= value <= max_val):
        return f"Error: {feature} must be between {min_val} and {max_val}."
    return None

def predict():
    st.title("🎗️💜Predict Alzheimer's Diagnosis")

    model_name = st.selectbox("Choose a Model", list(models.keys()))
    selected_model = models[model_name]
    #display feature information
    st.subheader("Helpful tip to input data ;)")
    st.table(feature_table)

    user_input = []
    error_messages = []

    for col in feature_cols:
        val = st.number_input(f"{col}", step=0.1)
        user_input.append(val)
        
        # Validate input value for each feature
        error_message = validate_input(col, val)
        if error_message:
            error_messages.append(error_message)
    
    if st.button("Predict"):
        # Show error messages if any invalid input
        if error_messages:
            for msg in error_messages:
                st.error(msg)
        else:
            # If inputs are valid, proceed with prediction
            input_array = np.array(user_input).reshape(1, -1)
            scaled_input = scaler.transform(input_array)
            
            prob = selected_model.predict_proba(scaled_input)
            # Probability for class 1 (Alzheimer's present)
            alz_prob = prob[0][1] * 100  
            no_alz_prob = prob[0][0] * 100  
            
            # Display probabilities
            st.write(f"Prediction with {model_name}:")
            #st.write(f"🟢 {alz_prob:.2f}% chance of Alzheimer's")
            #st.write(f"🔴 {no_alz_prob:.2f}% chance of No Alzheimer's")
            
            if alz_prob > no_alz_prob:
                st.success(f"🟢 Positive Alzheimer's diagnosis ({alz_prob:.2f}% chance of Alzheimer's)")
            else:
                st.success(f"🔴 Negative Alzheimer's diagnosis ({no_alz_prob:.2f}% chance of no Alzheimer's)")
