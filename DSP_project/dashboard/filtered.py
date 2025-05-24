import streamlit as st
import pandas as pd
from visuals import plot_corr_matrix

df_filtered = pd.read_csv("filtered_selected_features.csv")
df_full = pd.read_csv("alzheimers_disease_data.csv")
feature_cols = df_filtered.columns[:-1]

def selected_data():
    st.title("🎗️💜Selected Features Insight")
    st.subheader("Dataset View")
    dataset_choice = st.radio("Select Dataset", ["Selected Features", "Full Dataset"])

    st.write("Diagnosis Information: ")
    st.write("Diagnosis status for Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.")

    if dataset_choice == "Selected Features":
        st.subheader("Selected Features Dataset")
        st.dataframe(df_filtered)
    else:
        st.subheader("Full Dataset")
        st.dataframe(df_full)

    with st.expander("Show Full Correlation Matrix"):
        fig = plot_corr_matrix(df_filtered)
        st.pyplot(fig)

    st.subheader(" Feature Distributions by Diagnosis (Filtered Dataset)")
    st.image(image= "categorical_f.png")
    st.image(image="numerical_f.png")