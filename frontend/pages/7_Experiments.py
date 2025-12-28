import streamlit as st

st.title("🧪 Experiments")

st.markdown("Track experiments and reasoning (execution comes later).")

experiments = [
    {
        "model": "Random Forest",
        "metrics": {"accuracy": 0.87, "f1": 0.84},
        "notes": "Handled non-linearity well"
    },
    {
        "model": "Logistic Regression",
        "metrics": {"accuracy": 0.81, "f1": 0.78},
        "notes": "Strong baseline, interpretable"
    }
]

for exp in experiments:
    st.subheader(exp["model"])
    st.json(exp)