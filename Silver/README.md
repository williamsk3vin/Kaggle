
🪙 Silver Cost Forecast
1. Project Overview

   
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

2. Dataset.

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



Target: Price - Daily Cost of Silver 



3. Exploratory Data Analysis

Exploratory Data Analysis (EDA)


4. Modeling Approach



5. Model Interpretation


6. Key Takeaways



7. Tools and Libraries
Python
Matplotlib
Seaborn
Sklearn

