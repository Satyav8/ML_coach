import pandas as pd

def analyze_dataset(file) -> dict:
    df = pd.read_csv(file)

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numeric_cols": df.select_dtypes(include="number").columns.tolist(),
        "categorical_cols": df.select_dtypes(exclude="number").columns.tolist(),
        "missing": df.isnull().mean().to_dict()
    }

    warnings = []
    if summary["rows"] < 100:
        warnings.append("Very small dataset")

    if any(v > 0.4 for v in summary["missing"].values()):
        warnings.append("High missing value columns detected")

    summary["warnings"] = warnings
    summary["health_score"] = max(0, 100 - len(warnings) * 20)

    return summary
