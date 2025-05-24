
import streamlit as st
import pandas as pd
from visuals import load_full_data, create_grouped_features, plot_correlation_with_diagnosis, plot_distribution, plot_corr_matrix

df_filtered = pd.read_csv("filtered_selected_features.csv")
df_full = pd.read_csv("alzheimers_disease_data.csv")  
feature_cols = df_filtered.columns[:-1]

def data_overview():
    st.title("🎗️💜 Dataset Description & Insights")
    st.subheader("Dataset View")
    dataset_choice = st.radio("Select Dataset", ["Selected Features", "Full Dataset"])

    st.write("Diagnosis Information: ")
    st.write("Diagnosis status for Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.")

    if dataset_choice == "Selected Features":
        st.subheader("Selected Features Dataset")
        st.dataframe(df_filtered)

        #option to download the datase
        csv = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Selected Features CSV",
            data=csv,
            file_name='selected_features.csv',
            mime='text/csv')
    else:
        st.subheader("Full Dataset")
        st.dataframe(df_full)
    
        csv = df_full.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Full Dataset CSV",
            data=csv,
            file_name='full_dataset.csv',
            mime='text/csv')


    st.subheader("Diagnosis Distribution")
    fig = plot_distribution(df_full)
    fig.set_size_inches(10, 4)
    st.pyplot(fig)

    st.subheader("Feature distribution")
    st.image(image= "categorical.png")
    st.image(image= "numerical.png")

    # Load full dataset and grouped features
    df_full_cleaned = load_full_data()
    groups = create_grouped_features(df_full_cleaned)
    y = df_full_cleaned['Diagnosis']

    for group_name, group_df in groups.items():
        st.markdown(f"## 📌 {group_name} Features")

        col1, col2 = st.columns([1, 2])  

        with col1:
            st.markdown(f"""
                    **Description:**
                    - These features belong to the **{group_name.lower()}** category.
                    - Correlations are calculated against the `Diagnosis` variable.
                    - Higher bars = stronger relationship with Alzheimer's diagnosis.
                    """)
            if group_name == "Demographic":
                st.write("""
            **Age:** The age of the patients ranges from 60 to 90 years.

            **Gender:** Gender of the patients, where 0 represents Male and 1 represents Female.

            **Ethnicity:** The ethnicity of the patients, coded as:
            - 0: Caucasian
            - 1: African American
            - 2: Asian
            - 3: Other

            **EducationLevel:** Education level coded as:
            - 0: None
            - 1: High School
            - 2: Bachelor's
            - 3: Higher
            """)
                
            elif group_name == "Cognitive":
                st.write(""" Cognitive and Functional Assessments

        MMSE: Mini-Mental State Examination score, ranging from 0 to 30. Lower scores indicate cognitive impairment.

        FunctionalAssessment: Functional assessment score, ranging from 0 to 10. Lower scores indicate greater impairment.

        MemoryComplaints: Presence of memory complaints, where 0 indicates No and 1 indicates Yes.

        BehavioralProblems: Presence of behavioral problems, where 0 indicates No and 1 indicates Yes.

        ADL: Activities of Daily Living score, ranging from 0 to 10. Lower scores indicate greater impairment.""")


            elif group_name == "Lifestyle":
                st.write("""Lifestyle Factors

        BMI: Body Mass Index of the patients, ranging from 15 to 40.

        Smoking: Smoking status, where 0 indicates No and 1 indicates Yes.

        AlcoholConsumption: Weekly alcohol consumption in units, ranging from 0 to 20.

        PhysicalActivity: Weekly physical activity in hours, ranging from 0 to 10.

        DietQuality: Diet quality score, ranging from 0 to 10.

        SleepQuality: Sleep quality score, ranging from 4 to 10.""")
                    
            elif group_name == "Clinical":
                st.write("""Clinical Measurements

        SystolicBP: Systolic blood pressure, ranging from 90 to 180 mmHg.

        DiastolicBP: Diastolic blood pressure, ranging from 60 to 120 mmHg.

        CholesterolTotal: Total cholesterol levels, ranging from 150 to 300 mg/dL.

        CholesterolLDL: Low-density lipoprotein cholesterol levels, ranging from 50 to 200 mg/dL.

        CholesterolHDL: High-density lipoprotein cholesterol levels, ranging from 20 to 100 mg/dL.

        CholesterolTriglycerides: Triglycerides levels, ranging from 50 to 400 mg/dL.""")

            elif group_name == "Medical":
                st.write("""Medical History

        FamilyHistoryAlzheimers: Family history of Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.

        CardiovascularDisease: Presence of cardiovascular disease, where 0 indicates No and 1 indicates Yes.

        Diabetes: Presence of diabetes, where 0 indicates No and 1 indicates Yes.

        Depression: Presence of depression, where 0 indicates No and 1 indicates Yes.

        HeadInjury: History of head injury, where 0 indicates No and 1 indicates Yes.

        Hypertension: Presence of hypertension, where 0 indicates No and 1 indicates Yes.""")

            elif group_name == "Symptoms":
                st.write("""Symptoms

        Confusion: Presence of confusion, where 0 indicates No and 1 indicates Yes.

        Disorientation: Presence of disorientation, where 0 indicates No and 1 indicates Yes.

        PersonalityChanges: Presence of personality changes, where 0 indicates No and 1 indicates Yes.

        DifficultyCompletingTasks: Presence of difficulty completing tasks, where 0 indicates No and 1 indicates Yes.

        Forgetfulness: Presence of forgetfulness, where 0 indicates No and 1 indicates Yes.""")


                    
        with col2:
            fig = plot_correlation_with_diagnosis(group_df, y, group_name)
            st.pyplot(fig)

    with st.expander("Show Full Correlation Matrix"):
        fig = plot_corr_matrix(df_full)
        st.pyplot(fig)