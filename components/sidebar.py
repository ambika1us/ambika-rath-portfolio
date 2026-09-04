from pathlib import Path

import streamlit as st

from config import PROFILE, RESUME_PATH

NAV_OPTIONS = [
    "Full Portfolio",
    "About",
    "Skills",
    "Featured System",
    "Live Demo",
    "Projects",
    "Research",
    "Contact",
]


def render_sidebar() -> str:
    if st.session_state.get("nav_choice") not in NAV_OPTIONS:
        st.session_state["nav_choice"] = "Full Portfolio"

    with st.sidebar:
        st.markdown(
            f"""
            <div class="sidebar-avatar">AP</div>
            <div class="sidebar-name">{PROFILE["name"]}</div>
            <div class="sidebar-role">Data Scientist · Agentic AI · XAI</div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("5+ years building production ML and multi-agent systems.")

        if st.button("Open Live Demo", type="primary", use_container_width=True):
            st.session_state["nav_choice"] = "Live Demo"
            st.rerun()

        section = st.selectbox(
            "Navigate",
            NAV_OPTIONS,
            key="nav_choice",
        )

        st.markdown("---")
        st.markdown("**Focus**")
        st.markdown(
            '<span class="tag tag-accent">Multi-Agent Systems</span>'
            '<span class="tag">LLM Orchestration</span>'
            '<span class="tag">Explainable AI</span>',
            unsafe_allow_html=True,
        )

        st.markdown("---")
        resume_file = Path(RESUME_PATH)
        if resume_file.exists():
            st.download_button(
                "Download Resume",
                data=resume_file.read_bytes(),
                file_name=resume_file.name,
                mime="application/pdf",
                use_container_width=True,
            )
        st.link_button("GitHub", PROFILE["github"], use_container_width=True)
        st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)

        st.markdown("---")
        st.caption("Currently exploring agent evaluation, tool-use reliability, and human-in-the-loop control.")

    return section
