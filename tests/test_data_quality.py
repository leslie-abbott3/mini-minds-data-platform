import os, pandas as pd

def test_behavioral_exists():
    assert os.path.exists("data/raw/behavioral.csv")

def test_operational_exists():
    assert os.path.exists("data/raw/operational.csv")

def test_game_results_exists():
    assert os.path.exists("data/raw/game_results.csv")

def test_game_results_headers():
    df = pd.read_csv("data/raw/game_results.csv")
    needed = {"user_id","reaction_time","accuracy","levels_completed","hints_used"}
    assert needed.issubset(df.columns)
