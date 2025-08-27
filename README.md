# Mini Minds Analytics Platform

A unified **data & ML platform** for Mini Minds LLC.  
It consolidates **behavioral + operational data** into analytics-ready formats with **SQL, Python, and dbt**, and applies **ML models on game results** to detect the likelihood of learning disabilities. Includes KPI reporting, validation, and SHAP-based interpretability.

## Features
- ETL pipelines (Python + SQL + dbt)
- Data quality validation & tests
- KPI reporting for product/business teams
- ML models (Random Forest, XGBoost)
- SHAP interpretability
- Dockerized for reproducibility

## Quickstart
```bash
# 1) Install
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2) Load raw -> SQLite + run dbt
python pipelines/run_etl.py --config config/config.yaml
bash pipelines/run_dbt.sh

# 3) Generate KPIs
python pipelines/kpi_summary.py --input data/warehouse --output reports/kpis.csv

# 4) ML workflow
python ml/preprocess.py --input data/raw/game_results.csv --output data/processed/features.csv
python ml/train_models.py --config config/config.yaml
python ml/evaluate.py --model models/saved/best_model.pkl --data data/processed/features.csv
python ml/interpret.py --model models/saved/best_model.pkl --data data/processed/features.csv

mini-minds-analytics/
├── README.md
├── LICENSE
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── config/
│   └── config.yaml
├── data/
│   ├── raw/
│   │   ├── behavioral.csv
│   │   ├── operational.csv
│   │   └── game_results.csv
│   ├── warehouse/        # (generated)
│   └── processed/        # (generated)
├── dbt_project/
│   ├── dbt_project.yml
│   ├── macros/
│   │   └── date_utils.sql
│   └── models/
│       ├── schema.yml
│       ├── staging/
│       │   ├── stg_behavioral.sql
│       │   ├── stg_operational.sql
│       │   └── stg_game_results.sql
│       └── marts/
│           ├── dim_users.sql
│           ├── fct_user_engagement.sql
│           └── kpi_summary.sql
├── pipelines/
│   ├── run_etl.py
│   ├── run_dbt.sh
│   ├── validate_data.py
│   └── kpi_summary.py
├── ml/
│   ├── preprocess.py
│   ├── train_models.py
│   ├── evaluate.py
│   ├── interpret.py
│   └── utils.py
└── tests/
    ├── test_data_quality.py
    └── test_ml_pipeline.py

