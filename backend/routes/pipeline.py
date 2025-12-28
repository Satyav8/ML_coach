from fastapi import APIRouter
from backend.core.pipeline_engine import build_pipeline
from backend.db.supabase import supabase

router = APIRouter()

@router.get("/")
def generate_pipeline(project_id: str, model: str):
    project = supabase.table("projects").select("*").eq("id", project_id).execute().data[0]

    pipeline = build_pipeline(project["task_type"], model)

    supabase.table("projects").update({
        "stage": "ready"
    }).eq("id", project_id).execute()

    return pipeline

