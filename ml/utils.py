import pandas as pd

def load_features(path, target_col):
    df = pd.read_csv(path)
    X = df.drop(columns=[target_col]) if target_col in df.columns else df
    y = df[target_col] if target_col in df.columns else None
    return X, y
