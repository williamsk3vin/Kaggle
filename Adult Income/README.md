
# 🧠 Alzheimer’s Risk Prediction (Machine Learning Project)

## 1. Project Overview
This project explores the Adult Census Income dataset to predict whether an individual earns more than $50K per year based on demographic, employment, and socioeconomic attributes.

The objective is to demonstrate a complete machine learning workflow including:
	•	data cleaning
	•	exploratory data analysis (EDA)
	•	preprocessing and feature engineering
	•	model comparison
	•	hyperparameter tuning
	•	model evaluation and interpretation

The analysis compares several classification approaches to determine which model best captures the relationships present in structured tabular census data.


---

## 2. Dataset

Source: UCI Adult Census dataset (commonly used benchmark dataset for income prediction).
Size: Train : (32561, 15)
      Test : (16281, 15)
| Feature   | Type    | Description                               | Relevance |
|-----------|---------|-------------------------------------------|-----------|
|     |   |              |     |


income_bracket
0 → ≤50K
1 → >50K
---

## 3. Data Cleaning & Preprocessing
The dataset contains placeholder missing values represented as "?".

Cleaning steps included:
	•	stripping whitespace from categorical columns
	•	converting "?" values to missing values
	•	removing rows containing missing entries
	•	correcting label formatting for the target variable

This ensured consistent categorical encoding and prevented artificial categories from appearing during model training.

---

## 4. Exploratory Data Analysis (EDA)

Visualizations included KDE plots, violin plots, and correlation analysis.

EDA revealed several meaningful socioeconomic patterns:
	•	The dataset is moderately imbalanced, with roughly 75% of individuals earning ≤$50K.
	•	Higher earners tend to be older and work slightly more hours per week.
	•	Education level shows a strong positive relationship with income.
	•	Capital gain is extremely sparse but highly predictive of higher income.

These observations helped guide feature preprocessing and model interpretation.

---

## 5. Feature Preprocessing

Because the dataset contains both numerical and categorical variables, preprocessing was handled using a ColumnTransformer pipeline.

Numerical features were standardized using:
StandardScaler()

Categorical variables were converted to numerical format using:
OneHotEncoder()

This approach ensures that preprocessing remains consistent between training and testing data while preventing data leakage.
---

## 6. Models Evaluated

Three classification models were trained and compared:

Logistic Regression

Used as an interpretable linear baseline.

Random Forest Classifier

A nonlinear ensemble model capable of capturing feature interactions.

Multilayer Perceptron (MLP) Neural Network

A feedforward neural network used to test whether deep learning improves performance on tabular data.


---

## 7. Hyperparameter Tuning

The Random Forest model was tuned using:
GridSearchCV()

Key parameters explored included:
	•	number of trees
	•	tree depth
	•	minimum samples per split
	•	minimum samples per leaf
	•	feature subsampling

The final tuned model used:

n_estimators = 300
max_depth = None
min_samples_split = 10
min_samples_leaf = 3
max_features = sqrt


---

## 8. Model Performance

| Model | Accuracy | ROC-AUC | 
| Logistic Regression | 0.8476 |0.9031 |
| MLP Neural Network | 0.8478 | 0.9055 |
| Random Forest (Tuned)| 0.8618 | 0.9154 |

The tuned Random Forest achieved the strongest performance on the test set.


---
## 9. Feature Importance Insights

Random Forest feature importance revealed that the most influential predictors of higher income include:
	•	capital gain
	•	education level
	•	marital status
	•	relationship role
	•	age
	•	hours worked per week

These findings align with expected socioeconomic patterns observed during EDA.


---

## 10. Key Findings

- Education and investment income are the strongest predictors of higher earnings.
- Age and weekly working hours show moderate correlation with income level.
- Logistic Regression performs surprisingly well, indicating relatively structured relationships in the dataset.
- Tree-based ensemble models capture nonlinear feature interactions and achieve the best predictive performance.
- Neural networks did not outperform Random Forest, reinforcing a common observation that tree ensembles often dominate tabular datasets of this size.

---
## 11. Conclusion

This project demonstrates a full machine learning workflow for a structured classification problem. Through model comparison and hyperparameter tuning, a Random Forest classifier achieved the best performance, highlighting the strength of ensemble tree methods for tabular socioeconomic data.

The analysis also emphasizes the importance of thoughtful preprocessing, exploratory analysis, and model interpretation when building practical machine learning solutions.

---

## 12. Tools & Libraries
	•	Python
	•	pandas
	•	numpy
	•	scikit-learn
	•	matplotlib
	•	seaborn
