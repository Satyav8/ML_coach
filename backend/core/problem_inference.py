def infer_task_type(problem_statement: str) -> str:
    """
    Infers ML task type from a natural language problem description.

    Design goals:
    - Deterministic (no randomness, no LLMs)
    - Transparent (rule-based, easy to debug)
    - Safe default behavior

    Returns:
        One of: "classification", "regression", "clustering"
    """

    if not problem_statement:
        return "classification"  # safe default

    text = problem_statement.lower()

    classification_keywords = [
        "classify",
        "classification",
        "predict whether",
        "yes or no",
        "true or false",
        "binary",
        "label",
        "category",
        "spam",
        "fraud",
        "disease",
        "churn"
    ]

    regression_keywords = [
        "predict value",
        "estimate",
        "forecast",
        "regression",
        "price",
        "amount",
        "score",
        "sales",
        "revenue",
        "temperature",
        "demand"
    ]

    clustering_keywords = [
        "cluster",
        "group",
        "segment",
        "unsupervised",
        "customer segments",
        "cohorts"
    ]

    if any(keyword in text for keyword in clustering_keywords):
        return "clustering"

    if any(keyword in text for keyword in regression_keywords):
        return "regression"

    if any(keyword in text for keyword in classification_keywords):
        return "classification"

    # Final fallback (explicit by design)
    return "classification"


