import pandas as pd, yaml, argparse, os, joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, roc_auc_score

def train(cfg):
    df = pd.read_csv(cfg["ml"]["features_path"])
    X = df.drop(columns=[cfg["ml"]["target_column"]])
    y = df[cfg["ml"]["target_column"]]

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    rf = RandomForestClassifier(**cfg["ml"]["random_forest"])
    rf.fit(Xtr, ytr)
    rf_f1 = f1_score(yte, rf.predict(Xte))
    rf_auc = roc_auc_score(yte, rf.predict_proba(Xte)[:,1])
    print(f"[RF] F1={rf_f1:.4f} AUC={rf_auc:.4f}")

    xgb = XGBClassifier(use_label_encoder=False, eval_metric="logloss", **cfg["ml"]["xgboost"])
    xgb.fit(Xtr, ytr)
    xgb_f1 = f1_score(yte, xgb.predict(Xte))
    xgb_auc = roc_auc_score(yte, xgb.predict_proba(Xte)[:,1])
    print(f"[XGB] F1={xgb_f1:.4f} AUC={xgb_auc:.4f}")

    best = ("rf", rf, rf_f1) if rf_f1 >= xgb_f1 else ("xgb", xgb, xgb_f1)
    os.makedirs("models/saved", exist_ok=True)
    joblib.dump(best[1], "models/saved/best_model.pkl")
    pd.DataFrame([{"model": best[0], "f1": best[2], "rf_auc": rf_auc, "xgb_auc": xgb_auc}]).to_csv(
        "reports/model_performance.csv", index=False
    )
    print("[INFO] Saved best model -> models/saved/best_model.pkl")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()
    with open(args.config) as f:
        cfg = yaml.safe_load(f)
    train(cfg)
