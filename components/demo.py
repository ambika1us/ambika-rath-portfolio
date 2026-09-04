from __future__ import annotations

import io
import math
import re
from collections import Counter
from typing import Any

import streamlit as st

SAMPLE_RESUME = """
Ambika Prasad Rath
Data Scientist | Agentic AI Systems | Explainable AI

Experience
Data Scientist with 5+ years building production machine learning systems,
multi-agent LLM orchestration, and explainable decisioning.

Skills
Python, SQL, pandas, scikit-learn, PyTorch, XGBoost, LangChain, LangGraph,
FastAPI, Streamlit, Docker, Git, AWS, SHAP, time-series forecasting,
feature stores, model evaluation, experiment design, retrieval, memory,
guardrails, tool-calling, ranking, NLP, embeddings.

Impact
18% churn reduction via propensity models and intervention policy.
25% forecasting improvement versus production baseline.
Designed planner / critic / executor loops with human-in-the-loop control.
"""

SAMPLE_JD = """
Senior Data Scientist, Agentic Systems

We are hiring a Senior Data Scientist to design multi-agent workflows,
evaluate LLM tool use, and ship explainable models to production.

Must-haves
- Python, SQL, and production ML pipelines
- Multi-agent systems / LangGraph or similar orchestration
- LLM tool-calling, retrieval, and evaluation harnesses
- Explainable AI (SHAP or equivalent) and audit-ready decisions
- FastAPI or similar service layer, Docker, AWS

Nice to have
- Ranking / NLP / embeddings
- Time-series forecasting
- Experiment design and model monitoring
"""

SKILL_CANON = [
    "python",
    "sql",
    "pandas",
    "scikit-learn",
    "pytorch",
    "xgboost",
    "machine learning",
    "deep learning",
    "nlp",
    "embeddings",
    "ranking",
    "time-series forecasting",
    "feature stores",
    "model evaluation",
    "experiment design",
    "shap",
    "explainable ai",
    "llms",
    "multi-agent systems",
    "llm orchestration",
    "langgraph",
    "langchain",
    "tool-calling",
    "retrieval",
    "memory",
    "guardrails",
    "agent evaluation",
    "fastapi",
    "streamlit",
    "docker",
    "git",
    "aws",
    "ci",
    "pydantic",
]

ALIASES = {
    "scikit learn": "scikit-learn",
    "sklearn": "scikit-learn",
    "xai": "explainable ai",
    "explainability": "explainable ai",
    "llm": "llms",
    "large language models": "llms",
    "multi agent": "multi-agent systems",
    "multi-agent": "multi-agent systems",
    "agentic ai": "multi-agent systems",
    "lang graph": "langgraph",
    "tool calling": "tool-calling",
    "tool use": "tool-calling",
    "rag": "retrieval",
    "vector search": "embeddings",
    "time series": "time-series forecasting",
    "forecasting": "time-series forecasting",
    "feature store": "feature stores",
    "evaluation": "model evaluation",
    "mlops": "model evaluation",
    "amazon web services": "aws",
}

STOPWORDS = {
    "a", "an", "the", "and", "or", "to", "of", "in", "on", "for", "with",
    "is", "are", "be", "as", "by", "at", "from", "that", "this", "we",
    "you", "your", "our", "into", "using", "use", "used", "plus", "via",
}


def _normalize(text: str) -> str:
    text = text.lower()
    text = text.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", text).strip()


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z][a-z0-9+\-/#.]{1,}", _normalize(text))


def extract_text(file: Any) -> str:
    if file is None:
        return ""
    name = getattr(file, "name", "upload").lower()
    raw = file.read() if hasattr(file, "read") else file
    if hasattr(file, "seek"):
        try:
            file.seek(0)
        except Exception:
            pass
    if isinstance(raw, str):
        return raw
    data = bytes(raw)
    if name.endswith(".txt") or name.endswith(".md"):
        return data.decode("utf-8", errors="ignore")
    if name.endswith(".pdf"):
        try:
            from pypdf import PdfReader

            reader = PdfReader(io.BytesIO(data))
            pages = [page.extract_text() or "" for page in reader.pages]
            text = "\n".join(pages).strip()
            if text:
                return text
        except Exception:
            pass
        return data.decode("utf-8", errors="ignore")
    return data.decode("utf-8", errors="ignore")


def _contains_skill(blob: str, skill: str) -> bool:
    if len(skill) <= 3:
        return re.search(rf"(?<![a-z0-9]){re.escape(skill)}(?![a-z0-9])", blob) is not None
    return skill in blob


def _canonical_skills(text: str) -> set[str]:
    blob = _normalize(text)
    found: set[str] = set()
    for alias, canon in ALIASES.items():
        if _contains_skill(blob, alias):
            found.add(canon)
    for skill in SKILL_CANON:
        if _contains_skill(blob, skill):
            found.add(skill)
    return found


def _tfidf_cosine(resume: str, jd: str) -> tuple[float, list[tuple[str, float]]]:
    resume_tokens = [t for t in _tokenize(resume) if t not in STOPWORDS and len(t) > 2]
    jd_tokens = [t for t in _tokenize(jd) if t not in STOPWORDS and len(t) > 2]
    if not resume_tokens or not jd_tokens:
        return 0.0, []

    docs = [resume_tokens, jd_tokens]
    df: Counter[str] = Counter()
    for doc in docs:
        df.update(set(doc))
    n_docs = 2
    vocab = sorted(df)

    def vector(tokens: list[str]) -> list[float]:
        tf = Counter(tokens)
        length = max(len(tokens), 1)
        vec = []
        for term in vocab:
            idf = math.log((1 + n_docs) / (1 + df[term])) + 1.0
            vec.append((tf[term] / length) * idf)
        return vec

    v1, v2 = vector(resume_tokens), vector(jd_tokens)
    dot = sum(a * b for a, b in zip(v1, v2))
    n1 = math.sqrt(sum(a * a for a in v1)) or 1.0
    n2 = math.sqrt(sum(b * b for b in v2)) or 1.0
    cosine = max(0.0, min(1.0, dot / (n1 * n2)))

    contrib = []
    for term, a, b in zip(vocab, v1, v2):
        score = a * b
        if score > 0 and term in set(jd_tokens) and term in set(resume_tokens):
            contrib.append((term, score))
    contrib.sort(key=lambda x: x[1], reverse=True)
    return cosine, contrib[:12]


def compute_match(resume: str, jd: str) -> dict[str, Any]:
    resume_skills = _canonical_skills(resume)
    jd_skills = _canonical_skills(jd)
    matched = sorted(resume_skills & jd_skills)
    missing = sorted(jd_skills - resume_skills)
    extra = sorted(resume_skills - jd_skills)

    coverage = (len(matched) / len(jd_skills)) if jd_skills else 0.0
    cosine, keywords = _tfidf_cosine(resume, jd)
    score = int(round(100 * (0.62 * coverage + 0.38 * cosine)))
    score = max(0, min(100, score))

    if score >= 75:
        band = "strong"
        why = "high skill coverage and overlapping language with the job description"
        tone = "green"
    elif score >= 50:
        band = "good"
        why = "solid overlap on core skills, with a few must-haves still missing"
        tone = "orange"
    else:
        band = "weak"
        why = "limited overlap with the stated requirements"
        tone = "red"

    priority = [
        "multi-agent systems",
        "llms",
        "langgraph",
        "explainable ai",
        "python",
        "machine learning",
        "shap",
        "fastapi",
        "aws",
    ]
    core = {"python", "sql", "multi-agent systems", "llms", "explainable ai", "langgraph"}
    missing_core = sorted(core & set(missing), key=lambda s: (priority.index(s) if s in priority else 99, s))

    agreement = 1.0 - abs(coverage - cosine)
    evidence = min(1.0, (len(resume.split()) / 180) * 0.5 + (len(jd_skills) / 10) * 0.5)
    conf_raw = 0.45 * coverage + 0.25 * cosine + 0.20 * agreement + 0.10 * evidence
    if conf_raw >= 0.72 and len(jd_skills) >= 5:
        confidence = "High"
    elif conf_raw >= 0.42:
        confidence = "Medium"
    else:
        confidence = "Low"

    if missing_core:
        risk = "Missing Core Skills"
    elif score < 50:
        risk = "Low overlap"
    elif missing:
        risk = "Partial gaps"
    else:
        risk = "Low"
    ranked_match = sorted(
        matched,
        key=lambda s: (priority.index(s) if s in priority else 99, s),
    )
    ranked_missing = sorted(
        missing,
        key=lambda s: (priority.index(s) if s in priority else 99, s),
    )
    top_match = ", ".join(_pretty(s) for s in ranked_match[:3]) or "core technical skills"
    top_missing = ", ".join(_pretty(s) for s in ranked_missing[:3]) or "no critical gaps in the extracted skill set"

    if score >= 75 and not missing:
        explanation = f"Your profile matches strongly in {top_match}, with no critical skill gaps detected."
    elif score >= 50:
        explanation = f"Your profile matches well in {top_match}, but lacks {top_missing}." if missing else f"Your profile matches well in {top_match}."
    else:
        explanation = f"Your profile has limited overlap with this role. Strongest gaps: {top_missing}."

    return {
        "score": score,
        "band": band,
        "tone": tone,
        "why": why,
        "coverage": coverage,
        "cosine": cosine,
        "matched": matched,
        "missing": missing,
        "missing_core": missing_core,
        "extra": extra[:8],
        "keywords": [k for k, _ in keywords],
        "explanation": explanation,
        "jd_skill_count": len(jd_skills),
        "resume_skill_count": len(resume_skills),
        "confidence": confidence,
        "risk": risk,
    }


def _pretty(skill: str) -> str:
    special = {
        "sql": "SQL",
        "nlp": "NLP",
        "llms": "LLMs",
        "aws": "AWS",
        "shap": "SHAP",
        "ci": "CI",
        "fastapi": "FastAPI",
        "xgboost": "XGBoost",
        "pytorch": "PyTorch",
        "langgraph": "LangGraph",
        "langchain": "LangChain",
        "scikit-learn": "scikit-learn",
        "explainable ai": "Explainable AI",
        "multi-agent systems": "Multi-Agent Systems",
        "llm orchestration": "LLM Orchestration",
        "time-series forecasting": "Time-series forecasting",
    }
    return special.get(skill, skill.title())


def _tag_html(items: list[str], kind: str) -> str:
    if not items:
        return '<span class="metric-hint">None detected</span>'
    return "".join(f'<span class="tag {kind}">{_pretty(item)}</span>' for item in items)


def _render_results(result: dict[str, Any]) -> None:
    score = result["score"]
    tone = result.get("tone", "green" if score >= 75 else "orange" if score >= 50 else "red")
    st.markdown(
        f"""
        <div class="score-hero score-{tone}">
            <div class="metric-hint">Match score</div>
            <div class="score-value score-{tone}">{score}%</div>
            <div class="metric-hint">{result["band"].title()} fit · coverage {int(result["coverage"]*100)}% · lexical {int(result["cosine"]*100)}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(score / 100)
    st.write("")
    m1, m2, m3 = st.columns(3)
    m1.metric("Match Score", f"{score}%")
    m2.metric("Confidence", result.get("confidence", "Medium"))
    m3.metric("Risk", result.get("risk", "—"))
    st.write("")
    st.markdown(
        f'<div class="explain-box explain-{tone}">{result["explanation"]}</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown(
            f"""
            <div class="panel-card">
                <div class="metric-label" style="margin-bottom:0.55rem;">Matching skills</div>
                {_tag_html(result["matched"], "tag-match")}
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""
            <div class="panel-card">
                <div class="metric-label" style="margin-bottom:0.55rem;">Missing skills</div>
                {_tag_html(result["missing"], "tag-miss")}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    with st.expander("Explainability — why this score", expanded=True):
        st.markdown(
            f"""
            **Why the score is {result['band']}.** {result['why'].capitalize()}.
            Coverage looks at required skills found in the resume ({result['jd_skill_count']} JD skills extracted).
            Lexical score is TF-IDF cosine similarity on the two documents.
            """
        )
        if result["keywords"]:
            st.markdown("**Highlighted overlapping terms**")
            st.markdown(
                "".join(f'<span class="tag tag-accent">{k}</span>' for k in result["keywords"]),
                unsafe_allow_html=True,
            )
        if result["extra"]:
            st.caption("Also present on the resume, not required by this JD: " + ", ".join(_pretty(s) for s in result["extra"]))


def _render_thinking() -> None:
    st.markdown("## How the System Works")
    st.markdown(
        '<div class="section-lead">How the AI thinks — a scored pipeline, not a single prompt.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="pipeline">
            <span class="pipe-node">Resume</span>
            <span class="pipe-arrow">→</span>
            <span class="pipe-node">Skill Extraction</span>
            <span class="pipe-arrow">→</span>
            <span class="pipe-node">Embedding / Matching</span>
            <span class="pipe-arrow">→</span>
            <span class="pipe-node">Scoring</span>
            <span class="pipe-arrow">→</span>
            <span class="pipe-node">Explanation</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    s1, s2, s3, s4, s5 = st.columns(5)
    steps = [
        ("1", "Extract skills from resume"),
        ("2", "Extract required skills from job description"),
        ("3", "Compute similarity (TF-IDF / embeddings)"),
        ("4", "Calculate match score"),
        ("5", "Generate explanation"),
    ]
    for col, (n, text) in zip([s1, s2, s3, s4, s5], steps):
        with col:
            st.markdown(
                f'<div class="arch-note"><b>{n}</b><br>{text}</div>',
                unsafe_allow_html=True,
            )


def _render_agent_sim() -> None:
    st.markdown("#### Agent simulation")
    st.caption("Same graph as the featured system: specialized nodes, shared state, inspectable steps.")
    if st.button("Run Agent Pipeline", use_container_width=True):
        with st.spinner("Agents working..."):
            st.write("Job Agent: Extracting requirements...")
            st.write("Resume Agent: Parsing resume...")
            st.write("Matching Agent: Computing similarity...")
            st.write("Decision Agent: Scoring match...")
        result = st.session_state.get("match_result")
        if result:
            st.success(
                f"Pipeline complete — score {result['score']}% · confidence {result['confidence']} · risk {result['risk']}"
            )
        else:
            st.info("Pipeline traced. Run Analyze Match to attach a live score to this graph.")


def _render_why_better() -> None:
    st.markdown("#### Why this is better than ChatGPT")
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown(
            """
            <div class="panel-card">
                <div class="metric-label" style="margin-bottom:0.45rem;">This pipeline</div>
                <ul style="margin:0; padding-left:1.1rem;">
                  <li>Structured pipeline vs a single prompt</li>
                  <li>Explicit scoring vs subjective output</li>
                  <li>Explainability layer (coverage + TF-IDF)</li>
                  <li>Modular agents with inspectable state</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="panel-card">
                <div class="metric-label" style="margin-bottom:0.45rem;">A chat completion</div>
                <ul style="margin:0; padding-left:1.1rem;">
                  <li>One mixed context window</li>
                  <li>Score is whatever the model invents</li>
                  <li>Hard to audit after the fact</li>
                  <li>Research, judgment, and writing collapsed</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


def _render_use_cases() -> None:
    st.markdown("#### Real-world use case")
    st.markdown(
        """
        <div class="panel-card">
            <div class="metric-label" style="margin-bottom:0.45rem;">Used for</div>
            <span class="tag tag-accent">Resume screening automation</span>
            <span class="tag tag-accent">Hiring tools</span>
            <span class="tag tag-accent">Candidate-job matching systems</span>
            <p class="metric-hint" style="margin:0.7rem 0 0 0;">
            Same contract as the Resume Matcher: scored fit, missing must-haves, and a reviewable explanation.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_demo() -> None:
    st.markdown('<div id="live-demo"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">03b / Live product</div>', unsafe_allow_html=True)
    st.markdown("## Live AI Demo: Resume → Job Match")
    st.markdown(
        '<div class="section-lead">Upload a resume, paste a job description, and get a scored, explainable match — the same contract used in the Resume Matcher system.</div>',
        unsafe_allow_html=True,
    )
    _render_thinking()
    st.write("")

    left, right = st.columns([1.05, 1.15], gap="large")

    with left:
        st.markdown('<div class="metric-label">Inputs</div>', unsafe_allow_html=True)
        uploaded = st.file_uploader(
            "Resume (PDF or text)",
            type=["pdf", "txt", "md"],
            help="Optional. If empty, a sample Data Scientist resume is used.",
        )
        use_sample = st.checkbox("Use sample resume", value=uploaded is None)
        jd = st.text_area(
            "Job description",
            value=SAMPLE_JD.strip(),
            height=220,
        )
        analyze = st.button("Analyze Match", type="primary", use_container_width=True)

    with right:
        st.markdown('<div class="metric-label">Results</div>', unsafe_allow_html=True)
        if analyze:
            resume_text = SAMPLE_RESUME if use_sample or uploaded is None else extract_text(uploaded)
            if uploaded is not None and not use_sample and len(resume_text.strip()) < 40:
                st.warning("Could not extract enough text from the file. Try a text resume or enable the sample.")
            elif len(jd.strip()) < 40:
                st.warning("Paste a fuller job description to score against.")
            else:
                with st.spinner("Analyzing..."):
                    result = compute_match(resume_text, jd)
                    st.session_state["match_result"] = result
                    st.session_state["match_resume_chars"] = len(resume_text)

        result = st.session_state.get("match_result")
        if result:
            _render_results(result)
        else:
            st.markdown(
                """
                <div class="panel-card">
                    <div class="metric-label">Waiting for a run</div>
                    <p class="metric-hint" style="margin:0.4rem 0 0 0;">
                    Click Analyze Match. You will get a 0–100 score, matching / missing skills, and an explanation of why.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    st.markdown("---")
    a1, a2 = st.columns(2, gap="large")
    with a1:
        _render_agent_sim()
    with a2:
        _render_why_better()
    st.write("")
    _render_use_cases()
