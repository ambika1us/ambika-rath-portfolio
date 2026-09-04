import streamlit as st


SKILL_GROUPS = [
    {
        "title": "Machine Learning",
        "kicker": "ML",
        "items": [
            "Python",
            "SQL",
            "Supervised learning",
            "Ranking",
            "Time-series forecasting",
            "Feature stores",
            "Model evaluation",
            "SHAP / XAI",
            "Experiment design",
        ],
    },
    {
        "title": "Agentic AI / LLM",
        "kicker": "Agents",
        "items": [
            "LLMs",
            "Multi-Agent Systems",
            "LLM orchestration",
            "Tool-calling",
            "Retrieval + memory",
            "Planner / critic / executor",
            "Guardrails",
            "Agent evaluation",
        ],
    },
    {
        "title": "Tools & Tech",
        "kicker": "Tools",
        "items": [
            "pandas",
            "scikit-learn",
            "PyTorch",
            "XGBoost",
            "LangChain",
            "LangGraph",
            "FastAPI",
            "Streamlit",
            "Docker",
            "Git",
            "AWS",
        ],
    },
]


def render_skills() -> None:
    st.markdown('<div class="section-kicker">02 / Skills</div>', unsafe_allow_html=True)
    st.markdown("## A stack built for systems, not slides")
    st.markdown(
        '<div class="section-lead">Grouped by how work actually ships: models, agents, and the tooling that holds them together.</div>',
        unsafe_allow_html=True,
    )

    cols = st.columns(3, gap="medium")
    for col, group in zip(cols, SKILL_GROUPS):
        with col:
            tags = "".join(f'<span class="tag">{item}</span>' for item in group["items"])
            st.markdown(
                f"""
                <div class="skill-card">
                    <div class="badge">{group["kicker"]}</div>
                    <div class="metric-label" style="margin-bottom:0.85rem;">{group["title"]}</div>
                    {tags}
                </div>
                """,
                unsafe_allow_html=True,
            )
