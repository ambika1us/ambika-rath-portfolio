from pathlib import Path

import streamlit as st


def render_svg(path: str, extra_class: str = "") -> None:
    svg_file = Path(path)
    if not svg_file.exists():
        st.info("Visual asset unavailable.")
        return
    svg = svg_file.read_text(encoding="utf-8").strip()
    if "<svg" in svg and "width=" not in svg.split(">", 1)[0]:
        svg = svg.replace("<svg", '<svg width="100%" height="auto"', 1)
    cls = extra_class or "svg-frame"
    st.html(f'<div class="{cls}">{svg}</div>')
