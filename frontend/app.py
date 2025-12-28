import streamlit as st
import os
import requests
from supabase import create_client
from dotenv import load_dotenv

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(page_title="ML Co-Founder", layout="wide")

# --------------------------------------------------
# ENV SETUP
# --------------------------------------------------
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BACKEND_URL = "http://127.0.0.1:8000"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "user" not in st.session_state:
    st.session_state.user = None

# --------------------------------------------------
# AUTH GATE (LOGIN + SIGNUP)
# --------------------------------------------------
if not st.session_state.user:
    st.title("🔐 ML Co-Founder")

    mode = st.radio("Choose Action", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if mode == "Sign Up":
        confirm = st.text_input("Confirm Password", type="password")

        if st.button("Create Account"):
            if password != confirm:
                st.error("Passwords do not match")
                st.stop()

            try:
                supabase.auth.sign_up({
                    "email": email,
                    "password": password
                })
                st.success("Account created. Please login.")
            except Exception as e:
                st.error(str(e))
        st.stop()

    if st.button("Login"):
        try:
            res = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            st.session_state.user = res.user
            st.rerun()
        except Exception:
            st.error("Invalid credentials")

    st.stop()

# --------------------------------------------------
# USER IS LOGGED IN
# --------------------------------------------------
user = st.session_state.user

# Sidebar
st.sidebar.success(f"Logged in as\n{user.email}")

if st.sidebar.button("Logout"):
    st.session_state.user = None
    st.rerun()

# --------------------------------------------------
# HELPERS
# --------------------------------------------------
def get_user_projects(user_id):
    try:
        res = requests.get(
            f"{BACKEND_URL}/projects",
            params={"user_id": user_id}
        )
        if res.status_code == 200:
            return res.json()
    except Exception:
        pass
    return []

projects = get_user_projects(user.id)

# --------------------------------------------------
# COMMAND CENTER
# --------------------------------------------------
st.title("🧠 ML Co-Founder — Command Center")

# ---------------- WORKFLOW ----------------
st.markdown("### 🔁 How This System Works")

st.code(
"""Intent Definition
        ↓
Dataset Intelligence
        ↓
Model Decision
        ↓
Pipeline Autopilot
        ↓
Live Preview & Code Export""",
language="text"
)

st.caption(
    "Describe a problem → Upload data → Get model reasoning → See it run → Take the code."
)

st.divider()

# ---------------- ANALYTICS ----------------
st.markdown("### 📊 Your ML Activity")

if not projects:
    st.info("You haven’t created any ML projects yet.")
else:
    total = len(projects)
    stage_counts = {}

    for p in projects:
        stage = p.get("stage", "unknown")
        stage_counts[stage] = stage_counts.get(stage, 0) + 1

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Projects", total)
    col2.metric(
        "In Progress",
        stage_counts.get("dataset", 0) + stage_counts.get("decision", 0)
    )
    col3.metric("Ready", stage_counts.get("ready", 0))

st.divider()

# ---------------- RECENT PROJECTS ----------------
st.markdown("### 🗂️ Recent Projects")

if not projects:
    st.write("No projects yet.")
else:
    for p in projects[:5]:
        st.markdown(
            f"- **{p.get('name', 'Untitled')}** — stage: `{p.get('stage', 'unknown')}`"
        )

st.divider()

# ---------------- NEXT STEP ----------------
st.markdown("### 🚀 Recommended Next Step")

if not projects:
    st.success("Start by defining a new ML problem in Intent Problem.")
else:
    unfinished = [p for p in projects if p.get("stage") != "ready"]

    if unfinished:
        p = unfinished[0]
        st.warning(
            f"Continue **{p.get('name', 'Untitled')}** → next step: `{p.get('stage')}`"
        )
    else:
        st.success("All projects completed 🎉 Create a new one!")

st.divider()

# ---------------- CTA ----------------
st.markdown("### ✨ What would you like to do?")
st.markdown(
    "- Start a new ML intent\n"
    "- Resume an existing project\n"
    "- Explore model decisions and pipelines\n"
)
