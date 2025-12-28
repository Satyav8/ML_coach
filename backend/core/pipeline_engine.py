def build_pipeline(task_type, model_name):
    pipeline = {
        "steps": [
            "Handle missing values",
            "Encode categorical features",
            "Scale numeric features",
            "Train/Test split",
            f"Train {model_name}",
            "Evaluate model"
        ],
        "metrics": [],
        "artifacts": ["model.pkl", "metrics.json"]
    }

    if task_type == "classification":
        pipeline["metrics"] = ["accuracy", "f1", "roc_auc"]

    if task_type == "regression":
        pipeline["metrics"] = ["rmse", "mae", "r2"]

    return pipeline
