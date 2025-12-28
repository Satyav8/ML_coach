def recommend_models(task_type, dataset_summary):
    rows = dataset_summary["rows"]
    numeric = len(dataset_summary["numeric_cols"])
    categorical = len(dataset_summary["categorical_cols"])
    warnings = dataset_summary.get("warnings", [])

    recommendations = []

    if task_type == "classification":
        recommendations.append({
            "model": "Logistic Regression",
            "why": "Strong baseline, interpretable",
            "when_not": "Non-linear decision boundaries"
        })

        recommendations.append({
            "model": "Random Forest",
            "why": "Handles non-linearity & mixed features",
            "when_not": "Very large datasets, latency sensitive"
        })

        if rows > 10000:
            recommendations.append({
                "model": "XGBoost / LightGBM",
                "why": "High performance on structured data",
                "when_not": "Low interpretability"
            })

    if task_type == "regression":
        recommendations.append({
            "model": "Linear Regression",
            "why": "Fast, interpretable",
            "when_not": "Complex non-linear patterns"
        })

        recommendations.append({
            "model": "Random Forest Regressor",
            "why": "Robust to noise",
            "when_not": "Hard to explain"
        })

    if rows < 500:
        recommendations.append({
            "warning": "Dataset too small for deep learning"
        })

    return recommendations
