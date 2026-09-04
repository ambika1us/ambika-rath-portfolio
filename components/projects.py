import streamlit as st

from components.media import render_svg
from config import ARCHITECTURE_SVG, FEATURED_PROJECT


def _tags(items: list[str], accent: bool = False) -> str:
    cls = "tag tag-accent" if accent else "tag"
    return "".join(f'<span class="{cls}">{item}</span>' for item in items)


def render_featured_project() -> None:
    st.markdown('<div id="featured-system"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">03 / Featured System</div>', unsafe_allow_html=True)
    st.markdown("## Multi-Agent Job Application System")
    st.markdown(
        '<div class="section-lead">A production-shaped agent system that reads a role, searches evidence, writes a tailored application, then critiques and ships it — with explicit ownership at every step.</div>',
        unsafe_allow_html=True,
    )

    meta1, meta2, meta3 = st.columns(3, gap="medium")
    with meta1:
        st.markdown(
            '<div class="product-meta"><b>Problem class</b><br>High-volume, high-variance job applications</div>',
            unsafe_allow_html=True,
        )
    with meta2:
        st.markdown(
            '<div class="product-meta"><b>System type</b><br>Planner · Workers · Critic · Executor</div>',
            unsafe_allow_html=True,
        )
    with meta3:
        st.markdown(
            '<div class="product-meta"><b>Success metric</b><br>Fit quality + reviewable artifacts</div>',
            unsafe_allow_html=True,
        )

    st.write("")
    overview, architecture, features = st.tabs(["Overview", "Architecture", "Features"])

    with overview:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown(
                """
                <div class="panel-card">
                    <div class="metric-label" style="margin-bottom:0.55rem;">Problem</div>
                    <p>Job search is a retrieval + generation + policy problem, not a prompt.
                    Candidates waste cycles rewriting similar narratives, while applications
                    fail because they are generic, incomplete, or unaligned with the JD.</p>
                    <p style="margin:0;">Manual workflows do not scale. A single LLM chat also does not:
                    it mixes research, writing, and judgment in one context window
                    with no audit trail.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")
            st.markdown(
                """
                <div class="panel-card">
                    <div class="metric-label" style="margin-bottom:0.55rem;">Solution</div>
                    <p>Decompose the loop into specialized agents with typed contracts:</p>
                    <ol style="margin:0; padding-left:1.15rem;">
                      <li><b>Ingest</b> the JD and candidate profile into structured state</li>
                      <li><b>Research</b> company, role, and evidence from resume + web</li>
                      <li><b>Draft</b> resume bullets and cover letter against a rubric</li>
                      <li><b>Critique</b> for hallucination, tone, and requirement coverage</li>
                      <li><b>Execute</b> packaging and optional submission with human gate</li>
                    </ol>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f"""
                <div class="panel-card">
                    <div class="metric-label" style="margin-bottom:0.55rem;">Tech stack</div>
                    {_tags(["Python", "LangGraph", "OpenAI / LLM APIs", "Pydantic", "FastAPI", "Streamlit", "Vector retrieval"])}
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")
            st.link_button("View on GitHub", FEATURED_PROJECT["github"], use_container_width=True)
            st.caption("Primary CTA — source, architecture notes, and run instructions.")

    with architecture:
        st.markdown("#### Control plane, not a chatbot")
        st.markdown(
            """
            Each node owns a contract. The graph is the source of truth for routing,
            retries, and human approval. Memory is explicit state, not leftover tokens.
            """
        )
        st.write("")

        try:
            render_svg(ARCHITECTURE_SVG)
        except Exception:
            st.markdown(
                """
                ```text
                JD + Profile
                    │
                    ▼
                Orchestrator (LangGraph)
                    ├─ Parser Agent      → structured role + constraints
                    ├─ Research Agent    → evidence pack (tools + RAG)
                    ├─ Writer Agent      → resume / cover letter drafts
                    ├─ Critic Agent      → coverage, factuality, tone
                    └─ Executor Agent    → package + human approval gate
                            │
                            ▼
                      Artifact Store + Eval scores
                ```
                """
            )

        st.write("")
        n1, n2, n3 = st.columns(3, gap="medium")
        notes = [
            ("Parser", "Normalizes JD into skills, must-haves, seniority, and blockers."),
            ("Research", "Only retrieves; never writes application copy."),
            ("Critic", "Can send work back. Writer cannot self-approve."),
        ]
        for col, (title, body) in zip([n1, n2, n3], notes):
            with col:
                st.markdown(
                    f'<div class="arch-note"><b>{title}</b><br>{body}</div>',
                    unsafe_allow_html=True,
                )

        st.write("")
        with st.expander("Design decisions"):
            st.markdown(
                """
                - **Separation of research and writing** reduces hallucinated claims.
                - **Critic as a separate node** encodes a real review policy.
                - **Human gate on executor** keeps outbound actions reversible.
                - **Typed state (Pydantic)** makes traces inspectable and testable.
                - **Eval hooks** score coverage and citation density per run.
                """
            )

    with features:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown(
                """
                <div class="panel-card">
                    <div class="metric-label" style="margin-bottom:0.55rem;">Key features</div>
                    <ul style="margin:0; padding-left:1.15rem;">
                      <li>Shared memory / state object instead of hidden chat history</li>
                      <li>Tool-bounded research (job board, company page, profile store)</li>
                      <li>Rubric-based critic with reject / revise / approve</li>
                      <li>Human-in-the-loop before any outbound action</li>
                      <li>Artifact log: JD parse, evidence, drafts, scores</li>
                      <li>Fallback path when retrieval confidence is low</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                """
                <div class="panel-card">
                    <div class="metric-label" style="margin-bottom:0.45rem;">System contract</div>
                    <p style="margin:0;">Research never writes copy. Writer never self-approves.
                    Executor never sends without a human gate. Every run leaves a scored artifact trail.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")
            st.link_button("View on GitHub", FEATURED_PROJECT["github"], use_container_width=True)

        st.write("")
        with st.expander("Interactive walkthrough (placeholder)"):
            st.caption("Simulated run — replace with live LangGraph trace when the service is wired.")
            jd = st.text_area(
                "Paste a job description",
                value="Senior Data Scientist, Agentic Systems — design multi-agent workflows, evaluate LLM tool use, and ship explainable models to production.",
                height=110,
            )
            if st.button("Run agent graph (simulated)"):
                with st.status("Executing graph...", expanded=True) as status:
                    st.write("1/5 Parser — extracted 8 must-have skills, seniority = senior")
                    st.write("2/5 Research — retrieved 12 evidence snippets from profile + public sources")
                    st.write("3/5 Writer — drafted resume bullets + cover letter against rubric")
                    st.write("4/5 Critic — coverage 0.86, factuality pass, 1 revision requested")
                    st.write("5/5 Executor — waiting on human approval")
                    status.update(label="Graph complete — pending human gate", state="complete")
                st.success("Artifacts ready for review. No outbound send without approval.")
                st.json(
                    {
                        "role": "Senior Data Scientist, Agentic Systems",
                        "coverage_score": 0.86,
                        "revision_cycles": 1,
                        "human_gate": "required",
                        "jd_chars": len(jd),
                    }
                )


def render_other_projects() -> None:
    st.markdown('<div class="section-kicker">04 / Selected Work</div>', unsafe_allow_html=True)
    st.markdown("## Other systems")
    st.markdown(
        '<div class="section-lead">Smaller surfaces, same bar: clear problem, measurable lift, inspectable output.</div>',
        unsafe_allow_html=True,
    )

    projects = [
        {
            "title": "Resume Matcher",
            "blurb": "Ranking system that scores resume–JD fit with interpretable skill overlap, gap analysis, and suggested evidence to add.",
            "tech": ["NLP", "Embeddings", "Ranking", "XAI"],
            "outcome": "Turns matching into a scored, explainable decision — not a keyword filter.",
        },
        {
            "title": "Gold Price Prediction",
            "blurb": "Forecasting pipeline for gold prices with feature lags, exogenous signals, and error-band reporting vs. naive baselines.",
            "tech": ["Time series", "XGBoost", "Backtesting", "Python"],
            "outcome": "25% forecasting improvement versus the production baseline.",
        },
        {
            "title": "Churn Intervention Engine",
            "blurb": "Propensity models plus a policy layer that ranks who to contact, why, and with which offer — with SHAP-backed explanations.",
            "tech": ["Classification", "SHAP", "Policy", "SQL"],
            "outcome": "18% churn reduction after intervention rollout.",
        },
    ]

    cols = st.columns(3, gap="medium")
    for col, project in zip(cols, projects):
        with col:
            st.markdown(
                f"""
                <div class="project-card">
                    <div class="metric-label" style="margin-bottom:0.5rem;">{project["title"]}</div>
                    <p style="margin:0 0 0.75rem 0; font-size:0.92rem;">{project["blurb"]}</p>
                    <p style="margin:0 0 0.75rem 0; font-size:0.82rem;"><b>Outcome.</b> {project["outcome"]}</p>
                    {_tags(project["tech"])}
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    for project in projects:
        with st.expander(f"Details — {project['title']}"):
            if project["title"] == "Resume Matcher":
                st.markdown(
                    """
                    **Approach.** Embed JD requirements and resume sections, then hybrid-rank with
                    lexical skill matching. Explanations surface matched evidence and missing must-haves.

                    **Why it matters.** Recruiters and candidates both need *why*, not only a score.
                    """
                )
            elif project["title"] == "Gold Price Prediction":
                st.markdown(
                    """
                    **Approach.** Feature set of lagged prices, FX, rates, and seasonality.
                    Walk-forward validation; report MAPE / RMSE against naive and ARIMA baselines.

                    **Why it matters.** Forecasting is only useful with error bands and a retraining cadence.
                    """
                )
            else:
                st.markdown(
                    """
                    **Approach.** Gradient-boosted propensity + uplift-aware targeting.
                    SHAP explanations attached to each intervention ticket for ops review.

                    **Why it matters.** A model that cannot be explained does not get used by retention teams.
                    """
                )
