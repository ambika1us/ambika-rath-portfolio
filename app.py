

import streamlit as st
from config import PROFILE

st.set_page_config(
    page_title=f"{PROFILE['name']} · Data Scientist",
    page_icon="A",
    layout="wide",
    initial_sidebar_state="expanded",
)

from components.about import render_about
from components.contact import render_contact
from components.demo import render_demo
from components.hero import render_hero
from components.projects import render_featured_project, render_other_projects
from components.research import render_research
from components.sidebar import render_sidebar
from components.skills import render_skills
from components.styles import inject_styles


st.markdown("""
<style>

/* ===== Layout ===== */
.main > div {
    padding-top: 2rem;
}

/* ===== Card System ===== */
.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    transition: all 0.2s ease-in-out;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 28px rgba(0,0,0,0.08);
}

/* ===== Section Titles ===== */
.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* ===== Tag Pills ===== */
.tag {
    display: inline-block;
    background: #E6FFFA;
    color: #00A88F;
    padding: 6px 12px;
    border-radius: 20px;
    margin: 4px;
    font-size: 13px;
}

/* ===== Highlight Box ===== */
.highlight {
    background: linear-gradient(135deg, #E0F7FA, #EEF2FF);
    padding: 20px;
    border-radius: 16px;
}

/* ===== Divider ===== */
.divider {
    border-top: 1px solid #E5E7EB;
    margin: 30px 0;
}

</style>
""", unsafe_allow_html=True)



inject_styles()
section = render_sidebar()

FULL_PAGES = {"Full Portfolio", "Home"}

if section in FULL_PAGES:
    render_hero()
    st.write("")
    st.markdown("---")
    render_about()
    st.write("")
    st.markdown("---")
    render_skills()
    st.write("")
    st.markdown("---")
    render_featured_project()
    st.write("")
    st.markdown("---")
    render_demo()
    st.write("")
    st.markdown("---")
    render_other_projects()
    st.write("")
    st.markdown("---")
    render_research()
    st.write("")
    st.markdown("---")
    render_contact()
elif section == "About":
    render_hero()
    st.write("")
    st.markdown("---")
    render_about()
elif section == "Skills":
    render_skills()
elif section in {"Featured System", "Featured Project"}:
    render_featured_project()
elif section == "Live Demo":
    render_demo()
elif section == "Projects":
    render_featured_project()
    st.write("")
    st.markdown("---")
    render_demo()
    st.write("")
    st.markdown("---")
    render_other_projects()
elif section == "Research":
    render_research()
elif section == "Contact":
    render_contact()
else:
    render_hero()
    st.write("")
    st.markdown("---")
    render_about()
    st.write("")
    st.markdown("---")
    render_skills()
    st.write("")
    st.markdown("---")
    render_featured_project()
    st.write("")
    st.markdown("---")
    render_demo()
    st.write("")
    st.markdown("---")
    render_other_projects()
    st.write("")
    st.markdown("---")
    render_research()
    st.write("")
    st.markdown("---")
    render_contact()
