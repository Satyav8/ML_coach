import streamlit as st
from services.api import create_project, get_projects

st.title("🧠 Project Overview")

user = st.session_state.user  # 🔐 logged-in user

# ---------------- CREATE PROJECT ----------------
with st.form("new_project"):
    name = st.text_input("Project Name")
    intent = st.text_area("What are you building & why?")
    persona = st.selectbox("Persona", ["student", "startup", "research", "interview"])

    submitted = st.form_submit_button("Create Project")

    if submitted:
        project = create_project({
            "name": name,
            "intent": intent,
            "persona": persona,
            "user_id": user.id      # ✅ REQUIRED
        })
        st.success("Project created")
        st.json(project)

st.divider()

# ---------------- LIST PROJECTS ----------------
st.subheader("📂 Your Projects")

projects = get_projects(user.id)  # ✅ FIXED

if not projects:
    st.info("No projects yet.")
else:
    for p in projects:
        st.markdown(
            f"- **{p.get('name', 'Untitled')}** — stage: `{p.get('stage', 'unknown')}`"
        )
