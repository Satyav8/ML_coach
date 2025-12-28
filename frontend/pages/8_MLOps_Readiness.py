import streamlit as st

st.title("🚦 MLOps Readiness")

readiness = {
    "Reproducibility": "✅",
    "Data Versioning": "⚠️",
    "Model Monitoring": "❌",
    "Scalability": "⚠️",
    "Deployment Ready": "❌"
}

for k, v in readiness.items():
    st.write(f"**{k}:** {v}")

st.info("""
This scorecard tells you what is missing 
before this project can go to production.
""")
