import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_full_data():
    df = pd.read_csv("alzheimers_disease_data.csv")
    df.drop(['DoctorInCharge', 'PatientID'], axis=1, inplace=True)
    return df

def create_grouped_features(df):
    return {
        "Demographic": df[['Age','Gender','Ethnicity','EducationLevel']],
        "Lifestyle": df[['AlcoholConsumption','BMI','Smoking','PhysicalActivity', 'DietQuality', 'SleepQuality']],
        "Medical": df[['FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes', 'Depression','HeadInjury','Hypertension']],
        "Symptoms": df[['Confusion', 'Disorientation', 'PersonalityChanges', 'DifficultyCompletingTasks','Forgetfulness']],
        "Clinical": df[['SystolicBP', 'DiastolicBP', 'CholesterolTotal', 'CholesterolLDL','CholesterolHDL','CholesterolTriglycerides']],
        "Cognitive": df[['MMSE', 'FunctionalAssessment','MemoryComplaints', 'BehavioralProblems', 'ADL']]
    }

def plot_correlation_with_diagnosis(group_df, y, group_name):
    dfy = pd.concat([group_df, y], axis=1)
    correlation_matrix = dfy.corr()
    correlationy = correlation_matrix['Diagnosis'].drop('Diagnosis').sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=correlationy.index, y=correlationy.values, palette="coolwarm", ax=ax)
    ax.set_title(f"Correlation with Diagnosis - {group_name}")
    ax.set_ylabel("Correlation Coefficient")
    ax.set_xlabel("Features")
    plt.xticks(rotation=45)
    return fig

def plot_distribution(df):
    fig, ax = plt.subplots()
    sns.countplot(x="Diagnosis", data=df, ax=ax)
    ax.set_title("Distribution of Diagnosis")
    ax.set_xlabel("Diagnosis (0 = No, 1 = Yes)")
    ax.set_ylabel("Count")
    return fig

def plot_corr_matrix(df):
    
    df_numeric = df.select_dtypes(include=[np.number])

    correlation_matrix = df_numeric.corr()
    fig, ax = plt.subplots(figsize=(25, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
    ax.set_title("Correlation Matrix")
    return fig

