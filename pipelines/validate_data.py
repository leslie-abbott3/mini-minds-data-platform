import pandas as pd, os, argparse, glob

def validate(dir_path):
  csvs = glob.glob(os.path.join(dir_path, "*.csv"))
  if not csvs:
    print("[WARN] No CSVs found in warehouse dir.")
  for f in csvs:
    df = pd.read_csv(f)
    if df.empty:
      print(f"[FAIL] {os.path.basename(f)} is empty")
    elif df.isnull().any().any():
      print(f"[WARN] Missing values in {os.path.basename(f)}")
    else:
      print(f"[PASS] {os.path.basename(f)}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--data", default="data/warehouse")
  args = parser.parse_args()
  validate(args.data)
