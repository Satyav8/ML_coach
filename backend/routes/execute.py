from fastapi import APIRouter, UploadFile, File, Form
from backend.core.problem_inference import infer_task_type
from backend.core.model_selector import select_models
from backend.core.codegen_engine import generate_training_code
from backend.core.execution_engine import run_ml_code
import tempfile
import os
import pandas as pd

router = APIRouter()


@router.post("/")
async def execute_pipeline(
    problem_statement: str = Form(...),
    file: UploadFile = File(...)
):
    """
    End-to-end ML pipeline execution:
    - Infer task type from problem statement
    - Select suitable ML models
    - Generate training code dynamically
    - Execute code safely
    - Return live preview + generated code
    """

    # ------------------------------------------------
    # Save uploaded dataset
    # ------------------------------------------------
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(await file.read())
        dataset_path = tmp.name

    # ------------------------------------------------
    # Validate dataset
    # ------------------------------------------------
    try:
        df = pd.read_csv(dataset_path)
        if df.shape[1] < 2:
            raise ValueError("Dataset must have at least 2 columns")
    except Exception as e:
        os.remove(dataset_path)
        return {
            "status": "error",
            "message": f"Invalid dataset: {str(e)}"
        }

    # ------------------------------------------------
    # Infer task type from problem statement
    # ------------------------------------------------
    task_type = infer_task_type(problem_statement)

    # ------------------------------------------------
    # Select models suitable for task
    # ------------------------------------------------
    model_defs = select_models(task_type)

    results = []

    # ------------------------------------------------
    # Run pipeline for each model
    # ------------------------------------------------
    for model_def in model_defs:
        model_name = model_def.get("name", "Unknown Model")

        try:
            code = generate_training_code(task_type, model_def)

            exec_result = run_ml_code(
                code=code,
                dataset_path=dataset_path
            )

            results.append({
                "model": model_name,
                "success": exec_result["stderr"] == "",
                "preview": exec_result["stdout"],
                "errors": exec_result["stderr"],
                "code": code
            })

        except Exception as e:
            results.append({
                "model": model_name,
                "success": False,
                "preview": "",
                "errors": str(e),
                "code": ""
            })

    # ------------------------------------------------
    # Cleanup
    # ------------------------------------------------
    try:
        os.remove(dataset_path)
    except:
        pass

    # ------------------------------------------------
    # Final Response
    # ------------------------------------------------
    return {
        "status": "ok",
        "task_type": task_type,
        "models_tried": len(results),
        "results": results
    }



