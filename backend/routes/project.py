from fastapi import APIRouter, Query
from pydantic import BaseModel
from backend.db.supabase import supabase

router = APIRouter()

# -----------------------------
# SCHEMAS
# -----------------------------
class ProjectCreate(BaseModel):
    name: str
    intent: str
    persona: str
    user_id: str   # 🔐 REQUIRED

# -----------------------------
# CREATE PROJECT
# -----------------------------
@router.post("")
def create_project(data: ProjectCreate):
    result = (
        supabase
        .table("projects")
        .insert({
            "name": data.name,
            "intent": data.intent,
            "persona": data.persona,
            "user_id": data.user_id,
            "stage": "intent"
        })
        .execute()
    )

    return result.data[0]

# -----------------------------
# LIST PROJECTS (USER-SCOPED)
# -----------------------------
@router.get("")
def list_projects(user_id: str = Query(...)):
    result = (
        supabase
        .table("projects")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )

    return result.data


