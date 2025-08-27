import shap, joblib, pandas as pd, argparse, matplotlib.pyplot as plt, os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="models/saved/best_model.pkl")
    parser.add_argument("--data", default="data/processed/features.csv")
    args = parser.parse_args()

    model = joblib.load(args.model)
    df = pd.read_csv(args.data)
    X = df.drop(columns=["has_learning_disability"]) if "has_learning_disability" in df.columns else df

    os.makedirs("reports", exist_ok=True)
    explainer = shap.Explainer(model, X)
    shap_values = explainer(X, check_additivity=False)
    shap.summary_plot(shap_values, X, plot_type="bar", show=False)
    plt.tight_layout()
    plt.savefig("reports/feature_importance.png", dpi=200)
    print("[INFO] SHAP feature importance -> reports/feature_importance.png")
