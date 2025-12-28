from fastapi import FastAPI
from backend.routes import (
    intent, dataset, decision, pipeline, project, execute
)

app = FastAPI(title="ML Project Co-Founder")

app.include_router(project.router, prefix="/projects")
app.include_router(intent.router, prefix="/intent")
app.include_router(dataset.router, prefix="/dataset")
app.include_router(decision.router, prefix="/decision")
app.include_router(pipeline.router, prefix="/pipeline")
app.include_router(execute.router, prefix="/execute")  # ✅ REQUIRED

@app.get("/")
def root():
    return {"status": "ML Co-Founder backend alive"}


