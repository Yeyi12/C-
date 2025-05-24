import streamlit as st
import pandas as pd
from overview import data_overview
from filtered import selected_data
from model_result import result
from prediction import predict
st.set_page_config(page_title="Alzheimer's Dashboard", layout="wide")

# Load Data
df_full = pd.read_csv("alzheimers_disease_data.csv")  

# Set default page
if "page" not in st.session_state:
    st.session_state.page = "Dataset Overview"

st.sidebar.markdown("## Tabs")
if st.sidebar.button("Dataset Overview"):
    st.session_state.page = "Dataset Overview"
if st.sidebar.button("Selected Features"):
    st.session_state.page = "Selected Features"
if st.sidebar.button("Model Results"):
    st.session_state.page = "Model Results"
if st.sidebar.button("Make a Prediction"):
    st.session_state.page = "Make a Prediction"


st.title(f"💜🧠{st.session_state.page}")

if st.session_state.page == "Dataset Overview":
    data_overview()

elif st.session_state.page == "Selected Features":
    selected_data()

elif st.session_state.page == "Model Results":
    result()

elif st.session_state.page == "Make a Prediction":
    predict()

