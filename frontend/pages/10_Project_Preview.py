import streamlit as st
import requests
from services.api import get_projects

BASE_URL = "http://127.0.0.1:8000"

# -----------------------------------
# AUTH GUARD
# -----------------------------------
if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first.")
    st.stop()

user = st.session_state.user

# -----------------------------------
# PAGE UI
# -----------------------------------
st.title("🚀 ML Project Preview")

projects = get_projects(user.id)

if not projects:
    st.warning("No projects found. Please create a project first.")
    st.stop()

project = st.selectbox(
    "Select Project",
    projects,
    format_func=lambda p: p.get("name", "Untitled Project")
)

problem_statement = st.text_area(
    "Describe your ML problem",
    placeholder="Example: Predict whether a patient has diabetes based on health indicators"
)

file = st.file_uploader("Upload Dataset (CSV)", type=["csv"])

# -----------------------------------
# EXECUTION
# -----------------------------------
if file and problem_statement and st.button("Run ML Project"):
    with st.spinner("Thinking, building, and running models..."):
        res = requests.post(
            f"{BASE_URL}/execute",
            data={
                "problem_statement": problem_statement
            },
            files={
                "file": file
            }
        )

    if res.status_code != 200:
        st.error("Execution failed")
        st.code(res.text)
        st.stop()

    data = res.json()

    st.success(f"Task inferred: **{data['task_type']}**")

    # -----------------------------------
    # RESULTS
    # -----------------------------------
    for r in data["results"]:
        st.subheader(f"🧠 Model: {r['model']}")

        if r.get("errors"):
            st.error("Execution error")
            st.code(r["errors"])
        else:
            st.subheader("📊 Output")
            st.code(r.get("preview", ""))

        st.subheader("📦 Generated Code")
        st.code(r.get("code", ""), language="python")


        st.download_button(
            f"⬇️ Download {r['model']} Code",
            r["code"],
            file_name=f"{r['model'].replace(' ', '_').lower()}.py"
        )



