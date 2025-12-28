import requests

BASE_URL = "http://127.0.0.1:8000"

# -----------------------------
# CREATE PROJECT
# -----------------------------
def create_project(payload):
    """
    payload must include:
    - name
    - intent
    - persona
    - user_id
    """
    res = requests.post(f"{BASE_URL}/projects", json=payload)
    res.raise_for_status()
    return res.json()

# -----------------------------
# GET USER PROJECTS
# -----------------------------
def get_projects(user_id):
    res = requests.get(
        f"{BASE_URL}/projects",
        params={"user_id": user_id}
    )
    if res.status_code == 200:
        return res.json()
    return []

