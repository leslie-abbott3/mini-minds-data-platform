import pandas as pd, argparse, os

def generate(input_dir, output_file):
    # Expect dbt to materialize kpi_summary as a table exported to CSV by your choice
    kpi_path = os.path.join(input_dir, "kpi_summary.csv")
    if not os.path.exists(kpi_path):
        # Fallback: compute KPIs from marts CSVs if exported
        raise FileNotFoundError("Expected kpi_summary.csv in warehouse. Export from dbt or adapt script.")
    df = pd.read_csv(kpi_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"[INFO] KPIs written -> {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/warehouse")
    parser.add_argument("--output", default="reports/kpis.csv")
    args = parser.parse_args()
    generate(args.input, args.output)
