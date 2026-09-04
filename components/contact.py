import streamlit as st

from config import PROFILE


def render_contact() -> None:
    st.markdown(
        """
        <div class="cta-band">
            <div class="section-kicker">06 / Contact</div>
            <div class="section-title">Let's collaborate</div>
            <div class="section-lead">Open to roles and collaborations in agentic systems, applied ML, and explainable decisioning.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    c1, c2, c3 = st.columns(3, gap="medium")
    cards = [
        ("LinkedIn", PROFILE["linkedin_label"], PROFILE["linkedin"], "Professional network"),
        ("GitHub", PROFILE["github_label"], PROFILE["github"], "Code and system write-ups"),
        ("Email", PROFILE["email"], f"mailto:{PROFILE['email']}", "Direct reach"),
    ]
    for col, (title, label, url, hint) in zip([c1, c2, c3], cards):
        with col:
            st.markdown(
                f"""
                <div class="contact-card">
                    <div class="metric-label">{title}</div>
                    <div class="metric-hint" style="margin:0.35rem 0 0;">{hint}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")
            st.link_button(label, url, use_container_width=True)

    st.markdown(
        '<div class="footer-note">Ambika Prasad Rath · Data Scientist · Agentic AI Systems · Explainable AI</div>',
        unsafe_allow_html=True,
    )
