#!/usr/bin/env bash
set -euo pipefail
echo "[INFO] Running dbt models..."
dbt run --project-dir dbt_project
dbt test --project-dir dbt_project
