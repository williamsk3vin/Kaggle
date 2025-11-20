📘 Predicting Alzheimer’s Risk with Machine Learning

This project explores how machine learning can help predict the likelihood of Alzheimer’s Disease (AD) using a combination of clinical, cognitive, and behavioral features.
I used XGBoost for classification and SHAP for interpretability to understand which features contribute most to Alzheimer’s risk and how they influence predictions.

This project was a way for me to practice:
	•	Exploratory data analysis (EDA)
	•	Feature engineering
	•	Model building + tuning
	•	Model interpretability (SHAP)
	•	Evaluating classification performance
	•	Structuring an ML project for a portfolio

⸻

📂 Project Overview

The goal of this project is to classify whether a patient is diagnosed with Alzheimer’s (Diagnosis = 1) or not (Diagnosis = 0) based on a dataset of health, cognitive, and behavioral attributes.

The project focuses on:
	•	Understanding which features are most predictive
	•	Building a reliable ML classifier
	•	Interpreting model behavior using SHAP
	•	Comparing engineered features vs. raw features

⸻

📊 Dataset Description

The dataset contains 430 patients, each with clinical and lifestyle attributes:

Core cognitive + functional features
	•	MMSE (Mini-Mental State Exam)
	•	ADL (Activities of Daily Living)
	•	FunctionalAssessment
	•	MemoryComplaints
	•	BehavioralProblems

Clinical metrics
	•	Cholesterol (LDL, HDL, Triglycerides, Total)
	•	SystolicBP, DiastolicBP
	•	BMI
	•	SleepQuality
	•	PhysicalActivity
	•	AlcoholConsumption
	•	EducationLevel
	•	FamilyHistoryAlzheimers

Target:
	•	Diagnosis (0 = No AD, 1 = AD)
