import streamlit as st


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

        :root {
            --ink: #0b1220;
            --muted: #5b6578;
            --line: #e6ebf2;
            --paper: #ffffff;
            --wash: #f5f7fb;
            --accent: #0f766e;
            --accent-2: #115e59;
            --accent-soft: #ccfbf1;
            --navy: #0b3b4a;
            --shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
            --shadow-hover: 0 18px 40px rgba(15, 23, 42, 0.10);
        }

        html, body, [class*="css"] {
            font-family: 'IBM Plex Sans', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(1200px 500px at 10% -10%, rgba(20, 184, 166, 0.10), transparent 50%),
                radial-gradient(900px 420px at 100% 0%, rgba(11, 59, 74, 0.08), transparent 45%),
                #fbfcfe;
        }

        .block-container {
            padding-top: 1.6rem;
            padding-bottom: 4.5rem;
            max-width: 1120px;
        }

        header[data-testid="stHeader"] {
            background: rgba(251, 252, 254, 0.72);
            backdrop-filter: blur(12px);
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stToolbar"] {right: 1rem;}

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f7fafb 0%, #eef4f5 100%);
            border-right: 1px solid var(--line);
            min-width: 260px;
        }

        [data-testid="stSidebar"] .block-container {
            padding-top: 1.6rem;
        }

        [data-testid="stSidebarCollapseButton"] {
            display: flex !important;
        }

        section[data-testid="stSidebar"] {
            transform: none !important;
            visibility: visible !important;
        }

        h1, h2, h3, h4 {
            font-family: 'IBM Plex Sans', sans-serif;
            color: var(--ink);
            letter-spacing: -0.03em;
        }

        p, li, span, label {
            color: var(--muted);
        }

        hr {
            margin: 2.4rem 0;
            border: none;
            border-top: 1px solid var(--line);
        }

        .hero-shell {
            background: rgba(255,255,255,0.72);
            border: 1px solid rgba(226,232,240,0.9);
            border-radius: 28px;
            padding: 1.85rem 1.8rem 1.5rem 1.8rem;
            box-shadow: var(--shadow);
            backdrop-filter: blur(10px);
            min-height: 260px;
        }

        .hero-kicker {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.74rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--accent);
            font-weight: 500;
            margin-bottom: 0.7rem;
        }

        .hero-name {
            font-size: 3.25rem;
            line-height: 1.04;
            font-weight: 700;
            margin: 0 0 0.55rem 0;
            background: linear-gradient(120deg, #0b1220 8%, #0f766e 58%, #14b8a6 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            -webkit-text-fill-color: transparent;
        }

        .hero-title {
            font-size: 1.12rem;
            color: var(--navy);
            font-weight: 600;
            margin-bottom: 0.8rem;
        }

        .hero-tagline {
            font-size: 1.04rem;
            color: var(--muted);
            max-width: 540px;
            line-height: 1.6;
            animation: fadeUp 0.7s ease 0.15s both;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 900px) {
            .hero-name { font-size: 2.2rem; }
        }

        [data-testid="stImage"] img, .hero-art svg {
            border-radius: 24px;
            box-shadow: var(--shadow-hover);
            width: 100%;
            height: auto;
            display: block;
        }

        .hero-fallback {
            background: linear-gradient(135deg, #0b3b4a 0%, #0f766e 100%);
            border-radius: 24px;
            padding: 2rem 1.6rem;
            min-height: 280px;
            color: #ecfeff;
            box-shadow: var(--shadow-hover);
        }

        .hero-fallback .hero-kicker { color: #99f6e4; }
        .hero-fallback .metric-label { color: #ffffff; }
        .hero-fallback .metric-hint { color: #ccfbf1; }

        .section-kicker {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--accent);
            margin-bottom: 0.4rem;
        }

        .section-title {
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--ink);
            margin: 0 0 0.45rem 0;
        }

        .section-lead {
            color: var(--muted);
            font-size: 1rem;
            max-width: 720px;
            margin-bottom: 1.35rem;
            line-height: 1.6;
        }

        .metric-card, .skill-card, .project-card, .research-card, .contact-card, .highlight-card, .panel-card {
            border: 1px solid var(--line);
            background: var(--paper);
            border-radius: 18px;
            padding: 1.25rem 1.3rem;
            box-shadow: var(--shadow);
            height: 100%;
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
        }

        .metric-card:hover, .skill-card:hover, .project-card:hover, .contact-card:hover, .research-card:hover, .panel-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-hover);
            border-color: #cde7e3;
        }

        .metric-card {
            background: linear-gradient(180deg, #ffffff 0%, #f4fffd 100%);
            text-align: center;
            padding: 1.4rem 1rem;
        }

        .metric-value {
            font-size: 2.05rem;
            font-weight: 700;
            color: var(--ink);
            line-height: 1;
            margin-bottom: 0.4rem;
        }

        .metric-label {
            font-size: 0.95rem;
            color: var(--ink);
            font-weight: 600;
        }

        .metric-hint {
            font-size: 0.82rem;
            color: var(--muted);
            margin-top: 0.28rem;
        }

        .tag {
            display: inline-block;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.72rem;
            padding: 0.28rem 0.65rem;
            margin: 0.18rem 0.22rem 0.18rem 0;
            border-radius: 999px;
            background: var(--wash);
            color: var(--navy);
            border: 1px solid var(--line);
            transition: background 0.15s ease, border-color 0.15s ease;
        }

        .tag:hover, .tag-accent {
            background: var(--accent-soft);
            border-color: #99f6e4;
            color: #115e59;
        }

        .tag-match {
            background: #ecfdf5;
            border-color: #a7f3d0;
            color: #047857;
        }

        .tag-miss {
            background: #fef2f2;
            border-color: #fecaca;
            color: #b91c1c;
        }

        .score-hero {
            text-align: center;
            background: linear-gradient(180deg, #ffffff 0%, #f0fdfa 100%);
            border: 1px solid var(--line);
            border-radius: 18px;
            padding: 1.2rem 1rem 1rem 1rem;
            box-shadow: var(--shadow);
            margin-bottom: 0.85rem;
        }

        .score-hero.score-green { border-color: #a7f3d0; background: linear-gradient(180deg, #ffffff 0%, #ecfdf5 100%); }
        .score-hero.score-orange { border-color: #fdba74; background: linear-gradient(180deg, #ffffff 0%, #fff7ed 100%); }
        .score-hero.score-red { border-color: #fecaca; background: linear-gradient(180deg, #ffffff 0%, #fef2f2 100%); }

        .score-value {
            font-size: 3rem;
            font-weight: 700;
            line-height: 1;
            margin: 0.25rem 0 0.35rem 0;
            color: #0f766e;
        }

        .score-value.score-green { color: #047857; }
        .score-value.score-orange { color: #c2410c; }
        .score-value.score-red { color: #b91c1c; }

        .explain-box {
            background: #f8fafc;
            border-left: 3px solid #0f766e;
            border-radius: 10px;
            padding: 0.85rem 1rem;
            color: var(--ink);
            font-size: 0.95rem;
            line-height: 1.55;
        }

        .explain-box.explain-green { border-left-color: #059669; }
        .explain-box.explain-orange { border-left-color: #ea580c; }
        .explain-box.explain-red { border-left-color: #dc2626; }

        .pipeline {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 0.45rem;
            background: #ffffff;
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 0.9rem 1rem;
            box-shadow: var(--shadow);
        }

        .pipe-node {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.78rem;
            background: #f0fdfa;
            color: #115e59;
            border: 1px solid #99f6e4;
            border-radius: 999px;
            padding: 0.35rem 0.75rem;
            font-weight: 500;
        }

        .pipe-arrow {
            color: #94a3b8;
            font-weight: 600;
        }

        .featured-wrap {
            border: 1px solid var(--line);
            border-radius: 24px;
            padding: 1.5rem 1.6rem 1.2rem 1.6rem;
            background: linear-gradient(180deg, #ffffff 0%, #f7fbfb 100%);
            box-shadow: var(--shadow);
        }

        .product-meta {
            background: #f8fafc;
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 0.9rem 1rem;
            height: 100%;
        }

        .product-meta b {
            color: var(--ink);
            font-size: 0.78rem;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .arch-note {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.78rem;
            color: var(--muted);
            background: var(--wash);
            border: 1px dashed var(--line);
            border-radius: 12px;
            padding: 0.9rem 1rem;
        }

        .research-highlight {
            background: linear-gradient(135deg, #f0fdfa 0%, #ffffff 55%, #f8fafc 100%);
            border: 1px solid #c7efe8;
            border-radius: 22px;
            padding: 1.6rem 1.7rem;
            box-shadow: var(--shadow);
        }

        .badge {
            display: inline-block;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #0f766e;
            background: #ccfbf1;
            border-radius: 999px;
            padding: 0.28rem 0.7rem;
            margin-bottom: 0.7rem;
        }

        .cta-band {
            text-align: center;
            background: linear-gradient(180deg, #ffffff 0%, #f4fbfa 100%);
            border: 1px solid var(--line);
            border-radius: 24px;
            padding: 2rem 1.5rem 1.6rem 1.5rem;
            box-shadow: var(--shadow);
        }

        .cta-band .section-title, .cta-band .section-lead {
            margin-left: auto;
            margin-right: auto;
        }

        .sidebar-avatar {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            background: linear-gradient(135deg, #0b3b4a, #14b8a6);
            color: #fff;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 0.75rem;
        }

        .sidebar-name {
            font-weight: 700;
            color: var(--ink);
            font-size: 1.05rem;
            margin-bottom: 0.15rem;
        }

        .sidebar-role {
            font-size: 0.82rem;
            color: var(--muted);
            margin-bottom: 0.8rem;
        }

        .footer-note {
            text-align: center;
            color: #94a3b8;
            font-size: 0.8rem;
            margin-top: 2.5rem;
        }

        div[data-testid="stExpander"] {
            border: 1px solid var(--line);
            border-radius: 14px;
            background: #fff;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.03);
        }

        .stButton > button, .stDownloadButton > button {
            border-radius: 12px;
            font-weight: 600;
            border: 1px solid #d7e3e1;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }
        .stButton > button[kind="primary"],
            [data-testid="stBaseButton-primary"],
            [data-testid="stBaseLinkButton-primary"],
            [data-testid="stBaseLinkButton-primary"] a {
            background: #0f766e !important;
            border: 1px solid #0f766e !important;
            color: #ffffff !important;
        }
        .stButton > button[kind="primary"] *,
            [data-testid="stBaseButton-primary"] *,
            [data-testid="stBaseLinkButton-primary"] *,
            [data-testid="stBaseLinkButton-primary"] a * {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        .stLinkButton > a {
            border-radius: 12px !important;
            font-weight: 600 !important;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }

        .stButton > button:hover, .stDownloadButton > button:hover, .stLinkButton > a:hover {
            transform: translateY(-1px);
            box-shadow: 0 8px 18px rgba(15, 118, 110, 0.12);
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.45rem;
            background: #f4f7f8;
            padding: 0.35rem;
            border-radius: 14px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 2.45rem;
            border-radius: 10px;
            padding: 0 1rem;
            font-weight: 600;
        }

        .stRadio > label { font-weight: 600; color: var(--ink); }
        </style>
        """,
        unsafe_allow_html=True,
    )
