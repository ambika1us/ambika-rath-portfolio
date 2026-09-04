from pathlib import Path

OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "Ambika_Prasad_Rath_Resume.pdf"

CONTENT = [
    ("T", "AMBIKA PRASAD RATH"),
    ("S", "Data Scientist  |  Agentic AI Systems  |  Explainable AI"),
    ("S", "ambika.prasad.rath@outlook.com  ·  github.com/ambikaprasadrath"),
    ("H", "PROFILE"),
    (
        "B",
        "Data Scientist with 5+ years building production ML and multi-agent systems.",
    ),
    (
        "B",
        "Focus on LLM orchestration, evaluation, and decision systems that can be audited.",
    ),
    ("H", "SELECTED IMPACT"),
    ("B", "18% churn reduction via propensity models and an explainable intervention policy."),
    ("B", "25% forecasting improvement versus production baseline on gold / demand series."),
    ("B", "ICRET 2026 publication: Trigger Precision."),
    ("H", "FEATURED SYSTEM"),
    ("B", "Multi-Agent Job Application System - planner, research, writer, critic, executor."),
    ("B", "Typed shared state, tool-bounded retrieval, critic policy, human approval gate."),
    ("H", "SKILLS"),
    ("B", "ML: ranking, forecasting, evaluation, SHAP / XAI, experiment design."),
    ("B", "Agents: LangGraph, tool use, memory, guardrails, agent eval harnesses."),
    ("B", "Stack: Python, SQL, PyTorch, XGBoost, FastAPI, Streamlit, Docker, AWS."),
]


def escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def main() -> None:
    ops = []
    y = 760
    for kind, text in CONTENT:
        if kind == "T":
            ops.append(f"BT /F2 18 56 {y} Td ({escape(text)}) Tj ET")
            y -= 22
        elif kind == "S":
            ops.append(f"BT /F1 10 56 {y} Td ({escape(text)}) Tj ET")
            y -= 16
        elif kind == "H":
            y -= 12
            ops.append(f"BT /F2 11 56 {y} Td ({escape(text)}) Tj ET")
            y -= 18
        else:
            ops.append(f"BT /F1 10 56 {y} Td ({escape(text)}) Tj ET")
            y -= 16

    stream = ("\n".join(ops) + "\n").encode("latin-1")

    def obj(n: int, body: bytes) -> bytes:
        return f"{n} 0 obj\n".encode() + body + b"\nendobj\n"

    objs = [
        obj(1, b"<< /Type /Catalog /Pages 2 0 R >>"),
        obj(2, b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>"),
        obj(
            3,
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>",
        ),
        obj(4, b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"endstream"),
        obj(5, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"),
        obj(6, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>"),
    ]

    header = b"%PDF-1.4\n"
    body = b"".join(objs)
    offsets = []
    running = len(header)
    for item in objs:
        offsets.append(running)
        running += len(item)

    xref = [b"xref\n0 7\n0000000000 65535 f \n"]
    for off in offsets:
        xref.append(f"{off:010d} 00000 n \n".encode())
    trailer = (
        b"trailer\n<< /Size 7 /Root 1 0 R >>\nstartxref\n"
        + str(len(header) + len(body)).encode()
        + b"\n%%EOF\n"
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(header + body + b"".join(xref) + trailer)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
