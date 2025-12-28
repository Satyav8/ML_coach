from fastapi import APIRouter
from pydantic import BaseModel
from backend.core.intent_engine import infer_task_type
from backend.db.supabase import supabase

router = APIRouter()

class IntentRequest(BaseModel):
    project_id: str
    intent: str

@router.post("/")
def analyze_intent(data: IntentRequest):
    task_type = infer_task_type(data.intent)

    supabase.table("projects").update({
        "intent": data.intent,
        "task_type": task_type,
        "stage": "dataset"
    }).eq("id", data.project_id).execute()

    return {
        "task_type": task_type,
        "next_stage": "dataset"
    }

