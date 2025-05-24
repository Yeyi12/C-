import pytest
import pandas as pd
from visuals import load_full_data, create_grouped_features, plot_distribution, plot_correlation_with_diagnosis

# Test Data Loading
def test_load_full_data():
    df = load_full_data()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "Diagnosis" in df.columns

# Test Feature Grouping 
def test_create_grouped_features():
    df = load_full_data()
    grouped = create_grouped_features(df)
    assert isinstance(grouped, dict)
    assert "Cognitive" in grouped 
    assert isinstance(grouped["Cognitive"], pd.DataFrame)

# Test Distribution Plotting 
def test_plot_distribution_returns_figure():
    df = load_full_data()
    fig = plot_distribution(df)
    assert fig is not None
    assert hasattr(fig, "savefig")

# Test Correlation Plotting
def test_plot_correlation_with_diagnosis():
    df = load_full_data()
    groups = create_grouped_features(df)
    y = df["Diagnosis"]
    group_df = groups["Clinical"]
    fig = plot_correlation_with_diagnosis(group_df, y, "Clinical")
    assert fig is not None
    assert hasattr(fig, "savefig")
