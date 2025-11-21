import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Loads the Alzheimer dataset from a CSV file.
    """
    try:
        alzheimers = pd.read_csv(path)
        print(f"Data loaded successfully: {alzheimers.shape[0]} rows, {alzheimers.shape[1]} columns")
        return alzheimers
    except Exception as e:
        print("Error loading data:", e)
        raise
