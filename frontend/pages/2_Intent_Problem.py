import streamlit as st
import requests
from services.api import get_projects

BASE_URL = "http://127.0.0.1:8000"

# --------------------------------------------------
# AUTH GUARD (MANDATORY FOR ALL PAGES)
# --------------------------------------------------
if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first.")
    st.stop()

user = st.session_state.user

# --------------------------------------------------
# PAGE UI
# --------------------------------------------------
st.title("🎯 Intent & Problem Definition")

projects = get_projects(user.id)

if not projects:
    st.warning("No projects found. Please create a project first.")
    st.stop()

project = st.selectbox(
    "Select Project",
    projects,
    format_func=lambda p: p.get("name", "Untitled Project")
)

intent = st.text_area(
    "Describe what you want to build",
    placeholder="Example: Predict customer churn for a telecom dataset"
)

if st.button("Analyze Intent"):
    res = requests.post(
        f"{BASE_URL}/intent",
        json={
            "project_id": project["id"],
            "intent": intent
        }
    )

    if res.status_code != 200:
        st.error("Intent analysis failed")
        st.code(res.text)
        st.stop()

    data = res.json()

    st.success("Intent analyzed successfully")
    st.json(data)



