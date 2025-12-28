import streamlit as st
import requests
from services.api import get_projects

BASE_URL = "http://127.0.0.1:8000"

# --------------------------------------------------
# AUTH GUARD
# --------------------------------------------------
if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first.")
    st.stop()

user = st.session_state.user

# --------------------------------------------------
# PAGE UI
# --------------------------------------------------
st.title("🧩 Pipeline Autopilot")

projects = get_projects(user.id)  # ✅ FIXED

if not projects:
    st.warning("No projects found. Please create a project first.")
    st.stop()

project = st.selectbox(
    "Select Project",
    projects,
    format_func=lambda p: p.get("name", "Untitled Project")
)

model = st.text_input("Chosen Model (e.g. RandomForestClassifier)")

if st.button("Generate Pipeline"):
    res = requests.get(
        f"{BASE_URL}/pipeline",
        params={
            "project_id": project["id"],
            "model": model
        }
    )

    if res.status_code != 200:
        st.error("Pipeline generation failed")
        st.code(res.text)
        st.stop()

    data = res.json()

    st.success("Pipeline generated successfully")

    st.subheader("Pipeline Steps")
    for step in data.get("steps", []):
        st.write("•", step)

    st.subheader("Metrics")
    st.write(data.get("metrics", []))

    st.subheader("Artifacts")
    st.write(data.get("artifacts", []))
