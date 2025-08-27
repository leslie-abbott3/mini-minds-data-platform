import pandas as pd, argparse, os

def preprocess(input_file, output_file):
    df = pd.read_csv(input_file)

    features = df.groupby("user_id").agg({
        "reaction_time": ["mean","std"],
        "accuracy": "mean",
        "levels_completed": "sum",
        "hints_used": "sum"
    })
    features.columns = ["_".join(col) for col in features.columns]

    if "has_learning_disability" in df.columns:
        labels = df.groupby("user_id")["has_learning_disability"].first()
        features["has_learning_disability"] = labels

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    features.to_csv(output_file)
    print(f"[INFO] Features saved -> {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw/game_results.csv")
    parser.add_argument("--output", default="data/processed/features.csv")
    args = parser.parse_args()
    preprocess(args.input, args.output)
