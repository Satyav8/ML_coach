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
st.title("📊 Dataset Intelligence")

projects = get_projects(user.id)  # ✅ FIXED

if not projects:
    st.warning("No projects found. Please create a project first.")
    st.stop()

project = st.selectbox(
    "Select Project",
    projects,
    format_func=lambda p: p.get("name", "Untitled Project")
)

file = st.file_uploader("Upload CSV Dataset", type=["csv"])

if file and st.button("Analyze Dataset"):
    res = requests.post(
        f"{BASE_URL}/dataset",
        params={"project_id": project["id"]},
        files={"file": file}
    )

    if res.status_code != 200:
        st.error("Dataset analysis failed")
        st.code(res.text)
        st.stop()

    data = res.json()

    st.success("Dataset analyzed successfully")
    st.json(data)

