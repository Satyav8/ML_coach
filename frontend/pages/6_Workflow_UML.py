import streamlit as st

st.title("🧭 Workflow / UML")

st.markdown(
    """
    ### ML Project Workflow

    This diagram explains **what you are building and why**, end-to-end.
    """
)

st.markdown("""
```text
[ Intent Definition ]
        ↓
[ Dataset Intelligence ]
        ↓
[ Model Decision Engine ]
        ↓
[ Pipeline Autopilot ]
        ↓
[ Production Ready ]
""")

st.info(
"""
This workflow represents the thinking path of the ML Co-Founder.

markdown
Copy code
Each step exists to answer:
- *Why this problem?*
- *Is the data good enough?*
- *Why this model?*
- *How will it be built?*
"""
)

st.markdown("### Stage Descriptions")

st.markdown("""

Intent Definition → Converts human goals into ML task types

Dataset Intelligence → Judges data quality & risks

Model Decision Engine → Recommends algorithms with reasoning

Pipeline Autopilot → Builds a concrete ML recipe

Production Ready → Indicates readiness for deployment
""")

