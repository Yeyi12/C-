import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def result():
    st.title("🎗️💜 Model Performance Overview")

    # Load and display model metrics
    model_metrics = pd.read_csv("metrics.csv")
    st.dataframe(model_metrics)

    # Metric Bar Chart
    metric = st.selectbox("Select Comparison to Visualize", ["Accuracy", "Precision", "Recall", "F1-Score"])
    if metric == "Accuracy":
        st.image(Image.open("Accuracy.png"))
    elif metric == "Precision":
        st.image(Image.open("Precision.png"))
    elif metric == "Recall":
        st.image(Image.open("Recall.png"))
    elif metric == "F1-Score":
        st.image(Image.open("F1-Score.png"))

    st.markdown("---")
    st.subheader("📉 Detailed Model Visualizations")

    # Decision Tree Performance
    st.subheader("Decision Tree Performance")
    img_dt_classification = Image.open("classification_dt.png")
    img_dt_classification = img_dt_classification.resize((1000, 700))  
    st.image(img_dt_classification, caption="Decision Tree - Classification Report")

    img_dt_confusion = Image.open("confusion_dt.png")
    img_dt_confusion = img_dt_confusion.resize((1000, 700))  
    st.image(img_dt_confusion, caption="Decision Tree - Confusion Matrix")

    #SVC Performance
    st.subheader("SVC Performance")
    img_svc_classification = Image.open("classification_svc.png")
    img_svc_classification = img_svc_classification.resize((1000, 700))  
    st.image(img_svc_classification, caption="SVC - Classification Report")

    img_svc_confusion = Image.open("confusion_svc.png")
    img_svc_confusion = img_svc_confusion.resize((1000, 700))  
    st.image(img_svc_confusion, caption="SVC - Confusion Matrix")

    #Random Forest
    st.subheader("Random Forest Performance")
    img_rf_classification = Image.open("classification_rf.png")
    img_rf_classification = img_rf_classification.resize((1000, 700))  
    st.image(img_rf_classification, caption="Random Forest - Classification Report")

    img_rf_confusion = Image.open("confusion_rf.png")
    img_rf_confusion = img_rf_confusion.resize((1000, 700)) 
    st.image(img_rf_confusion, caption="Random Forest - Confusion Matrix")
