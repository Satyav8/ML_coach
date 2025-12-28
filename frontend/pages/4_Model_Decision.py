import streamlit as st
import requests
from services.api import get_projects

BASE_URL = "http://127.0.0.1:8000"

# --------------------------------------------------
# AUTH GUARD (MANDATORY)
# --------------------------------------------------
if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first.")
    st.stop()

user = st.session_state.user

# --------------------------------------------------
# PAGE UI
# --------------------------------------------------
st.title("🤖 Model Decision Board")

projects = get_projects(user.id)  # ✅ FIXED

if not projects:
    st.warning("No projects found. Please create a project first.")
    st.stop()

project = st.selectbox(
    "Select Project",
    projects,
    format_func=lambda p: p.get("name", "Untitled Project")
)

if st.button("Get Model Recommendations"):
    res = requests.get(
        f"{BASE_URL}/decision",
        params={"project_id": project["id"]}
    )

    if res.status_code != 200:
        st.error("Model decision failed")
        st.code(res.text)
        st.stop()

    decisions = res.json()

    st.success("Model recommendations generated")

    for d in decisions:
        st.json(d)

