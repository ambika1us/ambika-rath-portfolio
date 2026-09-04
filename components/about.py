import streamlit as st


def render_about() -> None:
    st.markdown('<div class="section-kicker">01 / About</div>', unsafe_allow_html=True)
    st.markdown("## Building systems that decide, explain, and act")
    st.write("")

    left, right = st.columns([1.35, 1], gap="large")

    with left:
        st.markdown(
            """
            <div class="panel-card">
            <p>I am a Data Scientist with 5+ years of experience taking models from notebooks
            into production systems. My work sits at the intersection of <b>machine learning</b>,
            <b>agentic AI</b>, and <b>explainable decisioning</b>.</p>
            <p>Recent focus: designing multi-agent pipelines where specialized agents retrieve,
            reason, critique, and execute — with explicit control planes for evaluation,
            fallback, and human review.</p>
            <p>I care less about demos and more about <b>system contracts</b>: what each agent
            owns, how tools are constrained, how failures propagate, and how a decision
            can be audited after the fact.</p>
            <p style="margin-bottom:0.4rem;"><b>Focus areas</b></p>
            <ul style="margin:0; padding-left:1.1rem;">
              <li>Multi-Agent Systems — role design, memory, routing, and evaluation loops</li>
              <li>LLM Orchestration — tool use, retrieval, structured outputs, fallbacks</li>
              <li>Explainable AI — feature attribution, policy-safe explanations, audit trails</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        cards = [
            ("18%", "Churn reduction", "Retention models + intervention policy that moved a live KPI."),
            ("25%", "Forecast improvement", "Demand / price models with tighter error bands vs. baseline."),
            ("5+", "Years experience", "Production ML, agent systems, and explainable decisioning."),
        ]
        for value, label, hint in cards:
            st.markdown(
                f"""
                <div class="metric-card" style="margin-bottom:0.85rem;">
                    <div class="metric-value">{value}</div>
                    <div class="metric-label">{label}</div>
                    <div class="metric-hint">{hint}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
