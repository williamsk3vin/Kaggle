🧠 Alzheimer’s Risk Prediction (Machine Learning Project)

1. Project Overview

This project uses clinical, cognitive, and behavioral data to predict the likelihood of Alzheimer’s Disease (AD).
The goal is to build a reliable classification model and understand which patient features contribute most to Alzheimer’s risk.
Model interpretability is performed using SHAP to visualize how different features influence predictions.

⸻

2. Dataset

Source: Provided Alzheimer’s clinical dataset
Size: ~430 rows, 30+ clinical and cognitive features
| Feature   | Type    | Description                               | Relevance |
|-----------|---------|-------------------------------------------|-----------|
| MMSE      | Float   | Richter scale magnitude                   | High      |
| ADL       | Float   | Earthquake depth in km                     | High      |
| FunctionalAssessment   | Binary  | Whether tsunami occurred                   | Target    |
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
