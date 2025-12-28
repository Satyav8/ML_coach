import subprocess
import tempfile
import os
import pandas as pd


def infer_target_column(df: pd.DataFrame) -> str:
    keywords = ["target", "label", "class", "outcome", "prediction"]

    for col in df.columns:
        if any(k in col.lower() for k in keywords):
            return col

    # fallback → last column
    return df.columns[-1]


def run_ml_code(code: str, dataset_path: str):
    df = pd.read_csv(dataset_path)
    target_col = infer_target_column(df)

    with tempfile.TemporaryDirectory() as tmp:
        script = os.path.join(tmp, "train.py")

        with open(script, "w") as f:
            f.write(code)

        env = os.environ.copy()
        env["DATA_PATH"] = dataset_path
        env["TARGET_COLUMN"] = target_col

        result = subprocess.run(
            ["python", script],
            capture_output=True,
            text=True,
            env=env
        )

        return {
            "stdout": f"🎯 Target inferred: {target_col}\n" + result.stdout,
            "stderr": result.stderr
        }

