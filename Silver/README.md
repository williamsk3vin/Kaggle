
🪙 Silver Cost Forecast
## 1. Project Overview

   
This project builds predictive models to forecast the daily cost of silver using historical COMEX silver futures data.

The goal is to:

	•	Analyze 10 years of historical price behavior
	•	Identify meaningful trends and patterns
	•	Engineer predictive features
	•	Train regression models
	•	Evaluate performance using RMSE and R²
	•	Interpret model behavior and feature importance

This project demonstrates:

	•	Time series feature engineering
	•	Regression modeling
	•	Financial data preprocessing
	•	Model evaluation and interpretation

---

## 2. Dataset.

Source: https://www.kaggle.com/datasets/muhammadaammartufail/silver-prices-10-year-data-and-2026-forecast?select=silver_prices_data.csv

    Provider: Yahoo Finance API (yfinance)
    Ticker Symbol: SI=F (COMEX Silver Futures)
    Collection Date: January 2026
    Update Frequency: Historical dataset (static)

Size: (2513, 8)
| Feature   | Type        | Description                                         | Relevance |
|-----------|-------------|-----------------------------------------------------|-----------|
| Date      | Date        | Trading date                                        |           |
| Close     | Float         | Closing price                                       |           |
| Price     | Float | Adjusted CLosing Price                              |   Target  |
| High      | Float     | Highest Price of the Day                            |           |
| Low       | Float     | Lowest Price of the Day                             |           |
| Open      | Float | Opening price in USD per troy ounce                 |           |
| Volume    | N/A | # of Contracts Traded                               |           |



🎯 Target Variable

Price — Daily cost of silver (USD per troy ounce)

---

## 3. Exploratory Data Analysis


📈 Exploratory Data Analysis (EDA)

The EDA phase focused on: <br>

1️⃣ Time Series Visualization:

	•	Long-term price trend
	•	Bull and bear cycles
	•	Volatility clusters

2️⃣ Distribution Analysis

	•	Price histogram
	•	Skewness
	•	Outliers

3️⃣ Correlation Analysis:

	•	Heatmap of feature correlations
	•	Multicollinearity detection
	•	Strong correlation between:
	•	Open, High, Low, Close, Price

4️⃣ Volatility Insights:

	•	Daily price ranges (High − Low)
	•	Rolling averages
	•	Trend smoothing

Key Observations:

	•	Silver prices show cyclical macro trends.
	•	Strong autocorrelation across consecutive days.
	•	Volume spikes during price breakouts.
	•	High multicollinearity between price-based features.


---

## 4. Modeling Approach

Because financial prices are highly autocorrelated and noisy, the following approach was used:

🔹 Feature Engineering:

	•	Lag features (Price(t−1), Price(t−2), etc.)
	•	Rolling averages
	•	Daily return calculation
	•	Volatility measures
	•	Price range (High − Low)

🔹 Train/Test Split:

	•	Time-aware split (no random shuffle)
	•	Prevented data leakage

🔹 Models Tested:

	•	Linear Regression
	•	Ridge Regression
	•	Random Forest Regressor
	•	Gradient Boosting (optional extension)

🔹 Evaluation Metrics:

	•	RMSE (Root Mean Squared Error)
	•	R² Score
	•	Cross-validation (where appropriate)

---

## 5. Model Interpretation
Linear Models:

	•	Capture general trend
	•	Sensitive to multicollinearity
	•	Good baseline model

Random Forest:

	•	Captures nonlinear patterns
	•	Handles volatility better
	•	Provides feature importance

Key Feature Drivers:

	•	Previous day price (strongest predictor)
	•	Rolling averages
	•	Intraday range
	•	Volume (secondary influence)

---

## 6. Key Takeaways
	•	Silver prices are highly autocorrelated.
	•	Simple lag-based models perform surprisingly well.
	•	Predicting raw price is difficult due to market efficiency.
	•	Predicting returns or direction may yield better results than predicting price directly.
	•	Ensemble models outperform linear regression on volatility-heavy periods.


## 7. Tools and Libraries
	•	Python
	•	Pandas
	•	NumPy
	•	Matplotlib
	•	Seaborn
	•	Scikit-learn (Sklearn)

---

