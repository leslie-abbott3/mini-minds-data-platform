
# Mini Minds Analytics Platform

A unified **data & machine learning platform** for Mini Minds LLC.  
It consolidates **behavioral + operational data** into analytics-ready formats with **SQL, Python, and dbt pipelines**, and applies **ML models on game results** to detect the likelihood of learning disabilities.

---

## 🚀 Features
- 📦 ETL pipelines with Python + SQL + dbt  
- 🧪 Automated data quality validation  
- 📊 KPI reporting for product & business teams  
- 🧠 ML models (Random Forest, XGBoost) for learning disability detection  
- 🔎 Interpretability with SHAP  
- 🐳 Dockerized for reproducibility  

---

## 📂 Example Workflow

1. **Run ETL + dbt**
```bash
python pipelines/run_etl.py --config config/config.yaml
bash pipelines/run_dbt.sh


Generate KPI reports

python pipelines/kpi_summary.py --input data/warehouse --output reports/kpis.csv


Preprocess game results

python ml/preprocess.py --input data/raw/game_results.csv --output data/processed/features.csv


Train ML models

python ml/train_models.py --config config/config.yaml


Evaluate & interpret

python ml/evaluate.py --model models/saved/best_model.pkl --data data/processed/features.csv
python ml/interpret.py --model models/saved/best_model.pkl --data data/processed/features.csv

🛠️ Tech Stack

Python (pandas, scikit-learn, XGBoost, SHAP)

dbt (SQL transformations & tests)

SQL (SQLite/Postgres)

Docker (containerized pipelines)

📜 License

MIT License


---

## 🔹 `requirements.txt`
```txt
pandas
numpy
scikit-learn
xgboost
sqlalchemy
dbt-core
pyyaml
joblib
shap
matplotlib
seaborn
pytest

🔹 Project Structure
mini-minds-analytics/
│
├── config/
│   └── config.yaml                  # Unified config (ETL + ML models)
│
├── data/
│   ├── raw/                         # Raw input data (behavioral, operational, game results)
│   ├── warehouse/                   # Warehouse-ready dbt outputs
│   └── processed/                   # Features for ML models
│
├── dbt_project/                     # dbt SQL models & tests
│   ├── models/
│   │   ├── staging/                 # Clean staging models
│   │   ├── marts/                   # Business-facing marts (KPIs)
│   │   └── schema.yml               # dbt tests
│   └── macros/                      # Custom macros
│
├── pipelines/                       # ETL + reporting
│   ├── run_etl.py                   # Python ETL
│   ├── run_dbt.sh                   # Run dbt transformations
│   ├── validate_data.py             # Data quality checks
│   └── kpi_summary.py               # Generate KPI reports
│
├── ml/                              # ML workflow
│   ├── preprocess.py                # Feature extraction from game results
│   ├── train_models.py              # Train Random Forest, XGBoost
│   ├── evaluate.py                  # Evaluate model
│   ├── interpret.py                 # SHAP interpretability
│   └── utils.py                     # Shared helpers
│
├── notebooks/
│   ├── exploratory_analysis.ipynb   # KPI exploration
│   └── eda_game_metrics.ipynb       # Game data ML exploration
│
├── models/
│   └── saved/                       # Trained ML models
│
├── reports/
│   ├── kpis.csv                     # KPI summary
│   ├── model_performance.csv        # ML performance
│   └── feature_importance.png       # SHAP output
│
├── tests/
│   └── test_data_quality.py         # Unit tests
│
├── requirements.txt
├── README.md
├── Dockerfile
├── .dockerignore
└── LICENSE
