import argparse, joblib, pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="models/saved/best_model.pkl")
    parser.add_argument("--data", default="data/processed/features.csv")
    args = parser.parse_args()

    model = joblib.load(args.model)
    df = pd.read_csv(args.data)
    X = df.drop(columns=["has_learning_disability"])
    y = df["has_learning_disability"]

    preds = model.predict(X)
    proba = getattr(model, "predict_proba", None)
    auc = roc_auc_score(y, proba(X)[:,1]) if proba else "N/A"

    print("[INFO] Classification Report:\n", classification_report(y, preds))
    print("[INFO] Confusion Matrix:\n", confusion_matrix(y, preds))
    print("[INFO] ROC-AUC:", auc)
