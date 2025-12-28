from fastapi import APIRouter, UploadFile, File
from backend.core.dataset_engine import analyze_dataset
from backend.db.supabase import supabase

router = APIRouter()

@router.post("/")
async def upload_dataset(project_id: str, file: UploadFile = File(...)):
    analysis = analyze_dataset(file.file)

    supabase.table("projects").update({
        "stage": "decision"
    }).eq("id", project_id).execute()

    return analysis

