import streamlit as st


def render_research() -> None:
    st.markdown('<div class="section-kicker">05 / Research</div>', unsafe_allow_html=True)
    st.markdown("## Trigger Precision")
    st.markdown(
        '<div class="section-lead">Peer-reviewed work on making intervention triggers tighter, more attributable, and safer to act on.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.7, 1], gap="large")
    with left:
        st.markdown(
            """
            <div class="research-highlight">
                <div class="badge">ICRET 2026 · Accepted</div>
                <div class="metric-label" style="font-size:1.2rem;margin-bottom:0.5rem;">
                    Trigger Precision
                </div>
                <p style="margin:0 0 0.85rem 0;">
                    A framework for scoring when an ML system should fire an action —
                    not only whether a prediction is accurate. The paper treats
                    precision of the <em>trigger</em> as a first-class metric:
                    false fires are operational cost, missed fires are lost value.
                </p>
                <p style="margin:0;">
                    <b>Key contribution.</b> Formalizes trigger precision against noisy labels,
                    couples it with explanation constraints so operators can audit
                    why a trigger fired, and reports lift on intervention quality
                    versus probability-threshold baselines.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="skill-card">
                <div class="metric-label" style="margin-bottom:0.85rem;">At a glance</div>
                <p style="margin:0 0 0.55rem 0;"><b>Conference</b><br>ICRET 2026</p>
                <p style="margin:0 0 0.55rem 0;"><b>Theme</b><br>Decision systems · XAI</p>
                <p style="margin:0 0 0.55rem 0;"><b>Role</b><br>Author — method + experiments</p>
                <p style="margin:0;"><b>Link to practice</b><br>Same discipline used in churn intervention and agent critic gates.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
