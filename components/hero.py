from pathlib import Path

import streamlit as st

from components.media import render_svg
from config import PROFILE

HERO_ART = "assets/images/hero_panel.svg"


def render_hero() -> None:
    left, right = st.columns([1.25, 1], gap="large")

    with left:
        st.markdown(
            f"""
            <div class="hero-shell">
                <div class="hero-kicker">Portfolio / 2026</div>
                <div class="hero-name">{PROFILE["name"]}</div>
                <div class="hero-title">{PROFILE["title"]}</div>
                <div class="hero-tagline">{PROFILE["tagline"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.link_button("View Projects", PROFILE["github"] + "?tab=repositories",type="primary", use_container_width=True)
        with c2:
            st.link_button("GitHub", PROFILE["github"], type="primary",use_container_width=True)
        with c3:
            st.link_button("LinkedIn", PROFILE["linkedin"], type="primary",use_container_width=True)

    with right:
        if Path(HERO_ART).exists():
            render_svg(HERO_ART, extra_class="hero-art")
        else:
            st.markdown(
                """
                <div class="hero-fallback">
                    <div class="hero-kicker">Agent graph</div>
                    <div class="metric-label">Planner · Workers · Critic · Executor</div>
                    <p class="metric-hint">Typed state, tool-bounded research, human gate before send.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")

    m1, m2, m3, m4 = st.columns(4, gap="medium")
    stats = [
        ("5+", "Years in applied ML"),
        ("18%", "Churn reduction shipped"),
        ("25%", "Forecasting lift"),
        ("ICRET 2026", "Research publication"),
    ]
    for col, (value, label) in zip([m1, m2, m3, m4], stats):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{value}</div>
                    <div class="metric-hint">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
