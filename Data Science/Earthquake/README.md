# Earthquake Tsunami Risk Analysis

## 1. Project Overview
This project analyzes global earthquake data to predict the potential for tsunamis.  
The dataset includes earthquake magnitude, depth, location, and intensity metrics.  
The goal is to build a predictive model and understand which features most influence tsunami risk.

---

## 2. Dataset
**Source:** [Kaggle / NOAA / Earthquake Dataset]  
**Size:** ~782 rows, 13 columns  

| Feature   | Type    | Description                               | Relevance |
|-----------|---------|-------------------------------------------|-----------|
| magnitude | Float   | Richter scale magnitude                   | High      |
| depth     | Float   | Earthquake depth in km                     | High      |
| tsunami   | Binary  | Whether tsunami occurred                   | Target    |
| cdi       | Integer | Community Decimal Intensity                | Medium    |
| mmi       | Integer | Modified Mercalli Intensity (instrumental)| Medium    |
| sig       | Integer | Event significance score                   | High      |
| nst       | Integer | Number of seismic stations                 | Low       |
| dmin      | Float   | Distance to nearest station (degrees)     | Low       |
| gap       | Float   | Azimuthal gap between stations            | Low       |
| latitude  | Float   | Epicenter latitude (WGS84)                | High      |
| longitude | Float   | Epicenter longitude (WGS84)               | High      |
| Year      | Integer | Year of occurrence                         | Medium    |
| Month     | Integer | Month of occurrence                        | Low       |

---

## 3. Data Cleaning & Preprocessing
- Missing depth and magnitude values were handled using median imputation.  
- Categorical features were one-hot encoded where needed.  
- Numeric features were scaled using MinMaxScaler.  
- Outliers were inspected and handled to improve model stability.

---

## 4. Exploratory Data Analysis (EDA)
- Visualizations: histograms, scatter plots, and correlation heatmaps, interactive maps  
- Key insights:  
  - Magnitude and shallow depth are the most important predictors of tsunamis.  
  - Earthquakes near coastlines have higher tsunami risk.  

---

## 5. Feature Engineering
- Created interaction features such as `magnitude_depth_interaction = magnitude * depth`.  
- Binned magnitude into categories for interpretability.  
- Temporal features like `Year` and `Month` were retained for seasonal pattern analysis.

---

## 6. Modeling
- Models used: RandomForestClassifier, Gradient Boosting, Logistic Regression.  
- Hyperparameter tuning performed using cross-validation.  
- Performance metrics: Accuracy, F1-score, Precision, Recall.

**Best Model:** RandomForestClassifier  
- F1-score: 0.91  
- Accuracy: 0.92  
- Key features: magnitude, depth, latitude, longitude

---

## 7. Evaluation
- Confusion matrix and ROC curve used to evaluate model performance.  
- Class imbalance handled via `class_weight='balanced'`.  
- Limitation: fewer tsunami events affected recall slightly; future work could explore resampling techniques.

---

## 8. Visualization
### Interactive Map of Earthquake Epicenters
An interactive map plotting the global distribution of earthquakes:  
- Markers are color-coded by magnitude and sized by event significance.  
- Zoom and hover to see details like magnitude, depth, and tsunami potential.  
- Helps identify high-risk regions and patterns in earthquake occurrence.
###Earthquake and Tsunami Frequency by Month
A bar chart showing the distribution of earthquakes and tsunamis across the months of the year:
- X-axis: Month of occurrence (January to December)
- Y-axis: Number of events (or percentage of total events)
- Bars can differentiate all earthquakes versus tsunami events for comparison.
- Highlights seasonal patterns in earthquake and tsunami activity, helping identify months with higher risk.

---

## 9. Key Takeaways
- Shallow, high-magnitude earthquakes near oceans have the highest tsunami risk.  
- Magnitude and depth are the most predictive features.  
- Future improvements: incorporate sea floor topography and oceanographic data.

---

## 10. Tools & Libraries
- Python: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Cartopy   

---

## 11. Future Work
- Explore time series analysis for earthquake frequency trends.  
- Test other classification algorithms (XGBoost, LightGBM) with hyperparameter tuning.  
- Add geospatial clustering to identify high-risk regions.
