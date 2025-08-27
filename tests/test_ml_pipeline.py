import os

def test_model_artifact_after_training():
    # Run training before this in CI or locally
    assert os.path.exists("models/saved/best_model.pkl"), "Train the model before running this test."
