import pandas as pd

def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds interaction and binary engineered features:
    - FA_MMSE
    - ADL_MMSE
    - MMSE_bin
    """

    df = df.copy()

    if "FunctionalAssessment" in df and "MMSE" in df:
        df["FA_MMSE"] = df["FunctionalAssessment"] * df["MMSE"]

    if "ADL" in df and "MMSE" in df:
        df["ADL_MMSE"] = df["ADL"] * df["MMSE"]

    if "MMSE" in df:
        df["MMSE_bin"] = (df["MMSE"] < 22).astype(int)

    return df
