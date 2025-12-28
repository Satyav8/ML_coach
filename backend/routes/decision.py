from fastapi import APIRouter
from backend.core.decision_engine import recommend_models
from backend.db.supabase import supabase

router = APIRouter()

@router.get("/")
def decide(project_id: str):
    project = supabase.table("projects").select("*").eq("id", project_id).execute().data[0]

    # temporary placeholder until dataset summary persistence
    dataset_summary = {
        "rows": 1000,
        "numeric_cols": ["a", "b"],
        "categorical_cols": ["c"],
        "warnings": []
    }

    decisions = recommend_models(project["task_type"], dataset_summary)

    supabase.table("projects").update({
        "stage": "pipeline"
    }).eq("id", project_id).execute()

    return decisions

