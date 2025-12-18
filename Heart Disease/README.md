
# 🫀 Heart Disease Prediction (Machine Learning Project)

## 1. Project Overview

This project explores the UCI Heart Disease dataset to understand the factors that contribute to heart disease and to build predictive machine-learning models that can identify patients at higher risk.
The goal is to walk through a full end-to-end data science workflow — from exploration to modeling and interpretation — while keeping the analysis understandable and clinically meaningful.

This project highlights how data can support early detection of heart disease and provides a practical example of applying machine-learning techniques to a real medical dataset.

---

## 2. Dataset.  

Source: University of California, Irvine, Heart Disease Dataset
Size: ~303 rows, 14 features 
| Feature   | Type        | Description                                         | Relevance |
|-----------|-------------|-----------------------------------------------------|-----------|
| age       | Integer     | Age of Patient                                      |           |
| sex       | Categorical | Gender of Patient                                   |           |
| cp        | Integer     | General functioning score                           |           |
| tresetbps | Integer     | resting blood pressure on hospital admission        |           |
| chol      | Integer     | serum cholestoral (mg/dl)                           |           |
| fbs       | Categorical | fasting blood sugar > 120 mg/dl                     |           |
| restecg   | Categorical | Resting Electrocardiogram Results                   |           |
| thalach   | Integer     | maximum heart rate achieved                         |           |
| exang     | Categorical | exercuse induced angina                             |           |
| oldpeak   | Integer     | ST depression induced by exercise relative to rest  |           |
| slope     | Categorical | slope of Peak Exercise ST segment                   |           |
| ca        | Integer     | number of major vassels (0-3) colored by flourosopy |           |
| thal      | Categorical | Thalassemia Test Result                             |           |
| target    | Binary      | diagnosis of heart disease                          | Target    |

Target:
 - target = 1 → presence of heart disease
 - target = 0 → no heart disease

---

## 3. Exploratory Data Analysis
Exploratory Data Analysis (EDA)

EDA focused on understanding:
	- Feature distributions and ranges
	- Skewness and outliers (notably in oldpeak and chol)
	- Class balance of the target variable
	- Relationships between features and the target

Key findings:
	- Strong associations observed for cp, thalach, exang, oldpeak, ca, and slope
	- Several features are categorical but numerically encoded, requiring careful interpretation
	- Correlation analysis complemented by countplots to capture non-linear and categorical patterns

---

## 4. Modeling Approach

Baseline Models:
 - Logistic Regression
 - Random Forest
 - XGBoost (baseline


Metrics Used:
 - Accuracy
 - Precision / Recall/ F1-score
 - Confusion Matrix
 - ROC AUC (threshold free)

---

## 5. Model Tuning

- Random Forest tuned using GridSearchCV
- XGBoost tuned using cross-validated grid search
- F1-score used as the primary optimization metric due to class balance considerations

---

## 6. Threshold Selection
In a medical screening context, false negatives are more costly than false positives.
Threshold tuning was performed by evaluating performance across probability cutoffs from 0.05 to 0.95.

Chosen threshold: 0.35<br>

This threshold:
 - Achieves 97% recall for heart disease
 - Minimizes false negatives
 - Accepts additional false positives as a clinical trade-off


Final evaluation (threshold = 0.35):
 - Recall (heart disease): 0.97
 - ROC AUC (threshold-free): 0.889
 - Confusion matrix shows strong sensitivity with acceptable specificity

---

  ## 7. Model Interpretation
  Feature Importance<br>

  Tree-based feature importance highlights:
	- Chest pain type (cp)
	- Thalassemia (thal)
	- ST depression (oldpeak)
	- Maximum heart rate (thalach)
	- Number of major vessels (ca)

  SHAP Analysis<br>

  SHAP was used to:
	- Explain individual predictions
	- Understand how feature values push predictions toward or away from heart disease
	- Validate alignment between clinical intuition and model behavior

---

  ## 8. Calibration
  - Probability calibration curves evaluated model confidence
  - Isotonic calibration applied to improve probability reliability
  - Ensures predicted risk aligns more closely with observed outcomes

  ## 9. Key Takeaways
  - Exercise-related and cardiac stress indicators are strong predictors of heart disease
  - Threshold selection is as important as model choice in medical applications
  - Tree-based models capture non-linear clinical relationships effectively
  - Interpretability tools (feature importance, SHAP) are essential for trust and insight

--- 

  ## 10. Tools and Libraries
  - Python
  - Pandas, NumPy
  - Matplotlib, Seaborn
  - Scikit-learn
  - XGBoost
  - SHAP
