import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess(df: pd.DataFrame):
    """
    Basic preprocessing:
    - Separate features and target
    - Scale numerical features
    - Train/test split
    """
    y = df["Diagnosis"]
    X = df.drop(columns=["Diagnosis", "PatientID"], errors="ignore")

    numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns

    scaler = StandardScaler()
    X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train, y_test, scaler
