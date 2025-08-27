import pandas as pd, yaml, argparse, os, joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

def train(cfg):
    df = pd.read_csv(cfg["data"]["input_path"])
    X = df.drop(columns=[cfg["ml"]["target_column"]])
    y = df[cfg["ml"]["target_column"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestClassifier(**cfg["ml"]["random_forest"])
    rf.fit(X_train, y_train)
    rf_score = f1_score(y_test, rf.predict(X_test))

    xgb = XGBClassifier(use_label_encoder=False, eval_metric="logloss", **cfg["ml"]["xgboost"])
    xgb.fit(X_train, y_train)
    xgb_score = f1_score(y_test, xgb.predict(X_test))

    best_model = rf if rf_score > xgb_score else xgb
    os.makedirs("models/saved", exist_ok=True)
    joblib.dump(best_model, "models/saved/best_model.pkl")
    print(f"[INFO] Best model saved with F1={max(rf_score,xgb_score):.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()
    with open(args.config) as f:
        cfg = yaml.safe_load(f)
    train(cfg)
