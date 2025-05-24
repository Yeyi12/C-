dashboard/:

Contains all the Streamlit app components (app.py, overview.py, filtered.py, model_result.py, prediction.py) for building the interactive dashboard.

alzheimers_disease_data.csv:

The primary dataset used for analysis and training.

Correlation-Accuracy_Results:

Folder with the results from the GA,the best correlation and accuracy from each run

GA2.ipynb:

Genetic Algorithm used to select features.

models.ipynb:

Trains and evaluates ML models using selected features from GA.

models2.ipynb:

Trains and evaluates models using all features for comparison.

metrics.csv:

Contains saved metrics like accuracy from different models using the selected features

preprocessing.ipynb:

Handles missing values, scaling, and other preprocessing steps.

requirements.txt:

List of libraries needed to run the code.

results.txt:

Contains the accuracy, correlation and features selected from each run

Selected_features.csv:

The final selected features after applying genetic algorithm optimization.

Tradeoff_plot.png:

Visual representation of the trade-off between accuracy and correlation results from GA.