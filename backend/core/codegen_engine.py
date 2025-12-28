def generate_training_code(task_type: str, model_def: dict):
    model_import = model_def["import"]
    model_constructor = model_def["constructor"]
    model_name = model_def["name"]

    return f'''
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

{model_import}

DATA_PATH = os.environ["DATA_PATH"]

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv(DATA_PATH)

# -----------------------------
# Auto target inference
# -----------------------------
target_col = df.columns[-1]

X = df.drop(target_col, axis=1)
y = df[target_col]

# -----------------------------
# Auto feature typing
# -----------------------------
categorical_cols = X.select_dtypes(include=["object", "category"]).columns
numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns

# -----------------------------
# Preprocessing
# -----------------------------
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ]
)

# -----------------------------
# Model
# -----------------------------
model = {model_constructor}

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model),
    ]
)

# -----------------------------
# Train / Test
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline.fit(X_train, y_train)

preds = pipeline.predict(X_test)

print("Model:", "{model_name}")
print("Target:", target_col)
print("Accuracy:", accuracy_score(y_test, preds))
'''






