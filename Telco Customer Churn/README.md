# Telco Customer Churn Prediction & Retention Prioritization

## Overview

Customer churn prediction is most useful when it supports a business decision rather than simply producing a classification.

This project analyzes the IBM Telco Customer Churn dataset to answer three questions:

1. Which customers are at elevated risk of churn?
2. What customer characteristics are associated with higher churn?
3. How could a retention team prioritize customers when outreach capacity is limited?

The project combines exploratory data analysis, machine learning, cross-validated hyperparameter tuning, and customer risk ranking to build an interpretable churn-prioritization workflow.

Rather than ending with model accuracy, predicted churn probabilities are used to rank customers and evaluate retention strategies using **Precision@K, Recall@K, and Lift@K**.

---

## Dataset

The analysis uses the **Telco Customer Churn** dataset containing:

- **7,043 customers**
- **21 original variables**
- Customer demographics
- Account information
- Internet and phone services
- Contract information
- Billing and payment methods
- Monthly and total charges
- Customer churn status

The target variable is:

`Churn`

which indicates whether a customer left the company.

Overall churn prevalence in the dataset is approximately:

- **No Churn:** 73.5%
- **Churn:** 26.5%

Because the classes are imbalanced, model evaluation extends beyond accuracy to include ROC-AUC, PR-AUC, precision, recall, and ranking-based metrics.

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Jupyter Notebook

---

## Data Cleaning

Several preprocessing steps were performed before modeling.

### TotalCharges

`TotalCharges` was originally stored as an object/string column.

Eleven customers contained blank values. All eleven had:

`tenure = 0`

indicating newly created accounts.

`TotalCharges` was converted to numeric and these values were assigned:

`TotalCharges = 0`

### Customer ID

`customerID` was excluded from model training because it is an identifier rather than a predictive customer characteristic.

### Exploratory Features

Temporary binned features were created during exploratory analysis for:

- Tenure
- Monthly charges

These features were excluded from modeling because the original continuous variables were retained.

---

## Exploratory Data Analysis

Several customer characteristics showed strong associations with churn.

### Contract Type

Customers with month-to-month contracts had substantially higher churn rates.

| Contract | Churn Rate |
|---|---:|
| Month-to-month | 42.7% |
| One year | 11.3% |
| Two year | 2.8% |

---

### Customer Tenure

Churn decreased substantially as customer tenure increased.

| Tenure | Churn Rate |
|---|---:|
| 0–6 months | 52.9% |
| 7–12 months | 35.9% |
| 13–24 months | 28.7% |
| 25–48 months | 20.4% |
| 49–72 months | 9.5% |

Customers who churned had a median tenure of approximately **10 months**, compared with **38 months** among customers who remained.

---

### Internet Service

| Internet Service | Churn Rate |
|---|---:|
| DSL | 19.0% |
| Fiber optic | 41.9% |
| No internet | 7.4% |

Fiber-optic customers showed substantially higher churn within the dataset.

This relationship persisted after examining contract type. For example, among month-to-month customers:

- DSL churn: **32.2%**
- Fiber-optic churn: **54.6%**
- No internet churn: **18.9%**

---

### Technical Support

Customers without technical support showed higher churn.

| Tech Support | Churn Rate |
|---|---:|
| No | 41.6% |
| Yes | 15.2% |
| No internet service | 7.4% |

---

### Online Security

| Online Security | Churn Rate |
|---|---:|
| No | 41.8% |
| Yes | 14.6% |
| No internet service | 7.4% |

Technical support and online security were associated but were not redundant features.

---

### Payment Method

Electronic check customers showed the highest churn rate.

| Payment Method | Churn Rate |
|---|---:|
| Bank transfer (automatic) | 16.7% |
| Credit card (automatic) | 15.2% |
| Electronic check | 45.3% |
| Mailed check | 19.1% |

---

### Paperless Billing

Customers using paperless billing also showed higher churn:

- Paperless billing: **33.6%**
- Non-paperless billing: **16.3%**

The association remained when examining customers within individual payment methods.

These relationships represent **associations within the dataset and should not be interpreted as causal effects**.

---

## Machine Learning Pipeline

The dataset was divided into training and held-out test sets using a stratified split to preserve churn prevalence.

Numeric features were processed using standard scaling for Logistic Regression.

Categorical features were transformed using one-hot encoding.

Tree-based models used the original numeric feature values while categorical variables were one-hot encoded.

Three models were evaluated:

1. Logistic Regression
2. Random Forest
3. XGBoost

---

## Baseline Models

Initial untuned models produced the following results:

| Model | ROC-AUC | PR-AUC |
|---|---:|---:|
| Logistic Regression | 0.842 | 0.634 |
| Random Forest | 0.819 | 0.611 |
| XGBoost | 0.815 | 0.603 |

The initial baseline therefore favored Logistic Regression.

However, model selection was not stopped at baseline performance.

---

## Cross-Validation & Hyperparameter Tuning

Five-fold stratified cross-validation was used to evaluate model configurations using **ROC-AUC** as the primary tuning metric.

### Logistic Regression

Regularization strength (`C`) was evaluated using GridSearchCV.

Best configuration:

`C = 10`

Cross-validation ROC-AUC:

**0.8464**

Performance was nearly identical across several values of `C`, suggesting that Logistic Regression was relatively insensitive to regularization strength over the tested range.

---

### Random Forest

Random Forest tuning evaluated:

- Number of trees
- Maximum tree depth
- Minimum samples per leaf

Best configuration:

- `n_estimators = 300`
- `max_depth = 10`
- `min_samples_leaf = 10`

Cross-validation ROC-AUC:

**0.8479**

The repeated appearance of larger minimum leaf sizes among the strongest configurations suggested that additional tree regularization improved generalization.

---

### XGBoost

XGBoost was tuned using RandomizedSearchCV.

The search evaluated combinations of:

- Number of boosting trees
- Learning rate
- Maximum tree depth
- Row subsampling
- Feature subsampling

Best sampled configuration:

- `n_estimators = 500`
- `learning_rate = 0.01`
- `max_depth = 3`
- `subsample = 0.8`
- `colsample_bytree = 0.7`

Cross-validation ROC-AUC:

**0.8506**

The strongest configurations generally favored relatively shallow trees and low learning rates.

---

## Cross-Validation Comparison

| Model | CV ROC-AUC |
|---|---:|
| Logistic Regression | 0.8464 |
| Random Forest | 0.8479 |
| XGBoost | **0.8506** |

The differences were relatively small, but tuned XGBoost achieved the strongest mean cross-validation ROC-AUC among the tested configurations.

---

## Final Held-Out Test Results

After model selection and tuning, the models were evaluated on the held-out test set.

| Model | ROC-AUC | PR-AUC |
|---|---:|---:|
| Logistic Regression | 0.8412 | 0.6281 |
| Random Forest | 0.8436 | 0.6545 |
| XGBoost | **0.8480** | **0.6654** |

The ordering observed during cross-validation was maintained on the held-out test set.

XGBoost was selected as the final model for customer risk ranking.

---

## From Prediction to Customer Prioritization

A fixed classification threshold does not necessarily match a real retention team's operating constraints.

For example, a company may only have enough resources to contact:

- 50 customers
- 100 customers
- 200 customers
- 300 customers
- 500 customers

Instead of relying on an arbitrary probability threshold, XGBoost's predicted probabilities were used to **rank customers from highest to lowest churn risk**.

The ranked customers were then evaluated using:

### Precision@K

Among the top K customers contacted, what proportion actually churned?

### Recall@K

What proportion of all actual churners were captured within the top K customers?

### Lift@K

How concentrated are churners within the selected group compared with the overall churn prevalence?

Lift is calculated as:

`Lift@K = Precision@K / Overall Churn Rate`

---

## Retention Prioritization Results

| Customers Contacted (K) | Precision@K | Recall@K | Lift@K |
|---:|---:|---:|---:|
| 50 | 84.0% | 11.2% | 3.16x |
| 100 | 78.0% | 20.9% | 2.94x |
| 200 | 73.0% | 39.0% | 2.75x |
| 300 | 67.3% | 54.0% | 2.54x |
| 500 | 56.2% | 75.1% | 2.12x |

These results demonstrate the tradeoff between precision and coverage.

For example, targeting the **top 200 highest-risk customers** resulted in:

- **73.0% Precision@200**
- **39.0% Recall@200**
- **2.75x Lift@200**

The top 200 customers were therefore approximately **2.75 times as concentrated with actual churners as the overall test population**.

If retention capacity increased to **500 customers**, the model captured:

**75.1% of all actual churners**

while maintaining:

- **56.2% precision**
- **2.12x lift**

As outreach expands, recall increases while precision and lift generally decrease because progressively lower-risk customers are included.

---

## Business Interpretation

The model can support different retention strategies depending on available resources.

A small retention team could focus on the highest-risk customers, producing high precision and high lift.

A larger retention operation could contact more customers, sacrificing some precision while capturing a substantially larger proportion of total churners.

Importantly, this analysis does **not** claim that a specific value of K is economically optimal.

Determining an optimal outreach strategy would require additional information such as:

- Customer lifetime value
- Cost per retention contact
- Cost of discounts or incentives
- Expected value of retaining a customer
- Probability that an intervention successfully prevents churn

Without these values, Precision@K, Recall@K, and Lift@K demonstrate how model performance changes under different hypothetical retention capacities.

---

## Conclusion

This project demonstrates how a customer churn model can be extended beyond binary classification into a practical customer-prioritization workflow.

Exploratory analysis identified several characteristics associated with higher churn, including shorter tenure, month-to-month contracts, fiber-optic internet service, lack of technical support or online security, electronic check payments, and paperless billing.

After comparing Logistic Regression, Random Forest, and XGBoost using cross-validation and held-out testing, tuned XGBoost achieved the strongest ranking performance:

- **ROC-AUC: 0.848**
- **PR-AUC: 0.665**

More importantly, predicted probabilities were converted into an actionable customer ranking.

The top 200 customers achieved **73.0% precision and 2.75x lift**, while expanding outreach to the top 500 captured **75.1% of all churners**.

This illustrates how machine-learning predictions can be translated into a decision-support system that allows a retention team to balance outreach capacity against churn coverage.

---

## Limitations

The dataset represents a historical customer snapshot rather than a longitudinal history of customer behavior.

As a result, the analysis identifies associations with churn but does not establish why customers churn.

The dataset also does not contain information about retention interventions. Therefore, high predicted churn risk should not be interpreted as evidence that a customer would respond positively to a retention offer.

A churn model answers:

> **Who is likely to churn?**

It does not necessarily answer:

> **Whose behavior can be changed by contacting them?**

A more mature retention system could extend this work through randomized retention experiments, customer lifetime value modeling, and uplift modeling to estimate which customers are most likely to change their behavior because of an intervention.

---

## Future Work

Potential extensions include:

- Model explainability and feature importance analysis
- SHAP-based global and customer-level explanations
- Customer lifetime value integration
- Cost-sensitive threshold optimization
- Retention campaign simulation
- Uplift modeling using randomized intervention data
- Monitoring model performance and churn behavior over time

---

## Author

**Kevin Williams**

M.S. Computer Science  
Data Scientist | Python | SQL | Machine Learning

GitHub: [williamsk3vin](https://github.com/williamsk3vin)
