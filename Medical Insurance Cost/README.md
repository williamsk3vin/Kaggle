

# :chart_with_upwards_trend: Medical Insurance Cost (Machine Learning Project)

## 1. Project Overview

This project explores the UCI Heart Disease dataset to understand the factors that contribute to heart disease and to build predictive machine-learning models that can identify patients at higher risk.
The goal is to walk through a full end-to-end data science workflow — from exploration to modeling and interpretation — while keeping the analysis understandable and clinically meaningful.

This project highlights how data can support early detection of heart disease and provides a practical example of applying machine-learning techniques to a real medical dataset.

---

## 2. Dataset.  

Source: Public Domain:  https://www.kaggle.com/datasets/hetmengar/medical-insurance-cost-prediction <br>
Size: ~1338 rows, 7 features 
| Feature   | Type        | Description                                         | Relevance |
|-----------|-------------|-----------------------------------------------------|-----------|
| age       | Integer     | Age of Primary Beneficiary                          |           |
| sex       | Categorical | Gender of Insurance Contractor                      |           |
| bmi       | Integer     | Body Mass Index (kg/m^2                             |           |
| children  | Integer     | Number of children covered by health insurance      |           |
| smoker    | Categorical | Smoking Status (yes or no)                          |           |
| region    | Categorical | Beneficiarys residential area in the US             |           |
| charges   | Integer     | Individual medical costs billed by health insurance |   Target  |


Target:
 - target = $1121.87 - $63770.43 → Cost of Medical Insurance in USD


---

## 3. Exploratory Data Analysis
Exploratory Data Analysis (EDA)

EDA focused on understanding:
  - Relationships between features and the target
  - Relationships of Categorical features seperated by smoking vs non smoking
  - Correlation of all features to target

FEATURE ENGINEERING:
  - bmi x Smoker = BMI_Smoker
  - age x Smoker = Age_Smoker

Key Findings:
  - Smoking-related features, particularly interactions with BMI and age, show the strongest associations with insurance charges.
  - BMI and age have limited impact in isolation but substantially increase costs among smokers.
  - Region and children contribute marginally relative to smoking-related predictors.

---

## 4. Modeling Approach

Baseline Models:
 - Logistic Regression
 - Ridge
 - Random Forest
 - Histogram-based Gradient Boosting


Metrics Used:
 - R^2
 - Root Mean Squared Error (RMSE)

---

  ## 5. Model Interpretation

**Base Line Linear Regression** <br>
Linear Regression was used as a baseline model to establish a reference level of performance and interpretability. Initial exploratory analysis suggested largely linear relationships between predictors and insurance charges once key interaction effects were accounted for. This model provided a transparent benchmark against which more complex models were evaluated.

**Random Forest Regressor** <br>
A Random Forest Regressor was evaluated to capture potential nonlinear relationships without explicit feature engineering. While the model achieved very low training error, test performance was comparable to Ridge regression, indicating substantial overfitting without meaningful gains in generalization. This suggests that the dominant structure of the data was already well captured by the engineered linear model.

**Histogram Gradient Boosting Regression** <br>
Histogram Gradient Boosting was tested as an additional nonlinear ensemble method. Although effective at fitting training data, it underperformed relative to Ridge regression on held-out data. This further supports the conclusion that the dataset’s signal is primarily linear once interaction effects are modeled explicitly.

**Ridge Regressor (Final Model)** <br>
Ridge Regression was selected as the primary model to address multicollinearity introduced by interaction features while preserving all relevant predictors. Exploratory analysis revealed overlapping linear regimes driven by smoking status, motivating the inclusion of interaction terms between smoking and both BMI and age. Ridge regularization stabilized coefficient estimates and achieved strong generalization performance (R² ≈ 0.88, RMSE ≈ $4.6k), with minimal train–test error divergence.

---

  ## 6. Key Takeaways
- Smoking status is the dominant driver of insurance charges, with strong interaction effects observed between smoking and both BMI and age.
- Apparent non-linear patterns in the data were largely explained by overlapping linear relationships conditioned on smoking status.
- EDA-driven interaction feature engineering enabled a regularized linear model to achieve performance comparable to tree-based models.
- Ridge regression provided the best balance of predictive accuracy, stability, and interpretability, while tree-based models exhibited greater variance without improved generalization.

--- 

  ## 7. Tools and Libraries
  - Python
  - Pandas, NumPy
  - Matplotlib, Seaborn
  - Scikit-learn

