from backend.core.model_registry import MODEL_REGISTRY

def select_models(task_type: str):
    """
    Returns all valid ML models for the inferred task type.
    """
    return MODEL_REGISTRY.get(task_type, [])

