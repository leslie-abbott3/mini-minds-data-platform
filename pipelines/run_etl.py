import pandas as pd, os, argparse, yaml
from sqlalchemy import create_engine

def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)

def run_etl(cfg):
    engine = create_engine(f"sqlite:///{cfg['database']['path']}")
    os.makedirs(cfg["warehouse"]["output"], exist_ok=True)

    for src in cfg["etl"]["sources"]:
        df = pd.read_csv(src)
        table = os.path.splitext(os.path.basename(src))[0]
        df.to_sql(table, engine, if_exists="replace", index=False)
        print(f"[INFO] Loaded {src} into table {table}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()
    cfg = load_config(args.config)
    run_etl(cfg)
