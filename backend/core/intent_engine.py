def infer_task_type(intent: str) -> str:
    intent = intent.lower()

    if any(word in intent for word in ["classify", "predict whether", "yes or no", "churn", "fraud", "classification"]):
        return "classification"

    if any(word in intent for word in ["predict value", "price", "sales", "revenue", "forecast"]):
        return "regression"

    if any(word in intent for word in ["group", "cluster", "segment"]):
        return "clustering"

    return "unknown"
