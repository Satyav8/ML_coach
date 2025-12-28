import streamlit as st

st.title("📦 Exports")

st.markdown("Generate assets from your ML project.")

if st.button("Generate README"):
    st.code("""
# ML Project Co-Founder Output

## Problem
Intent-driven ML system that converts goals into pipelines.

## Approach
- Intent inference
- Dataset intelligence
- Model decision engine
- Pipeline autopilot

## Outcome
Explainable, production-ready ML blueprint.
""", language="markdown")

if st.button("Generate Resume Bullets"):
    st.success("Resume bullets generated")
    st.write("""
- Built an intent-driven ML decision system using FastAPI & Streamlit  
- Designed dataset intelligence & explainable model selection engine  
- Automated ML pipeline generation with lifecycle tracking  
""")
