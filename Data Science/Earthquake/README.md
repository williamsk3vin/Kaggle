Earthquake Tsunami Risk Analysis



1. Project Overview

This project analyzes global earthquake data to predict the potential for tsunamis. 
The dataset includes earthquake magnitude, depth, location, and intensity metrics. 
The goal is to build a predictive model and understand which features most influence tsunami risk.


2. Dataset

Source: (Kaggle, NOAA, etc.)

Key features: list important columns and what they represent

782 earthquake records with magnitude ≥6.5

13 standardized numeric features including magnitude, depth, coordinates

Binary tsunami classification (38.9% tsunami events, 61.1% non-tsunami)

Complete dataset with zero missing values

Global geographic coverage (-61.85° to 71.63° latitude)

22-year temporal span capturing major seismic events

Size: number of rows/columns
(782, 13)

Target variable : Tsunami 


3. Data Cleaning & Preprocessing

Feature transformations (scaling, encoding, binning)


4. Exploratory Data Analysis (EDA)

Visualizations: histograms, scatter plots, correlation heatmaps

Key insights from the data


Relationships between features and target



5. Feature Engineering

New features created

Feature selection or reduction

Interaction terms, derived metrics, or aggregations


6. Modeling

Models tried (RandomForest, Logistic Regression, XGBoost, etc.)

Hyperparameter tuning methods

Training and validation approach (cross-validation, train/test split)

Performance metrics (RMSE, F1, Precision, Recall, ROC-AUC)


7. Evaluation

Compare model performances

Confusion matrices, ROC/PR curves

Any limitations or assumptions


8. Visualization

Include 2–3 key visualizations that tell your story

Examples:

Feature importance bar chart

Geographic map of epicenters

Predicted vs actual plots


9. Key Takeaways & Insights

What did you learn from the project?

Which features were most important?

Any recommendations or next steps?


10. Tools & Libraries

Python: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

Plotly, Folium for geospatial visualizations
