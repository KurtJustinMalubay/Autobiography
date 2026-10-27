"""CSIT 349 - Applied AI | Kurt Justin J. Malubay — Portfolio.

Genshin Impact–inspired dark UI. Pure Streamlit components.
Run: streamlit run app.py
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# Page config  (must be FIRST Streamlit call)
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Kurt Malubay · Portfolio",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="auto",
)

ROOT   = Path(__file__).parent
ASSETS = ROOT / "assets"

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────
NAME       = "Kurt"
FULL_NAME  = "Kurt Justin J. Malubay"
SECTION    = "F1"
PROGRAM    = "BSCS 3"
COURSE     = "CSIT 349 · Applied AI"
INSTRUCTOR = "Jun Albert S. Pardillo"
EMAIL      = "justinkurt837@gmail.com"
GITHUB     = "https://github.com/KurtJustinMalubay"
ITCH       = "https://sashimiproductions.itch.io/"
TAGLINE    = "Curiosity builds the engineer."

# ─────────────────────────────────────────────────────────────────────────────
# Colour palette  — dark only, tuned for comfortable viewing
# ─────────────────────────────────────────────────────────────────────────────
# Main surfaces
C_BG      = "#0c1018"   # true page background
C_PANEL   = "#111822"   # card / container fill
C_PANEL2  = "#18222f"   # slightly raised surface
C_BORDER  = "#243040"   # default border
C_DIVIDER = "#1c2838"

# Gold — primary brand accent (Genshin's signature)
C_GOLD    = "#c5a059"   # standard Genshin UI gold
C_GOLD_D  = "#8a6f3a"   # dim gold — less dominant

# Text — warm, comfortable, NOT glaring white
C_TEXT_H  = "#d8cfc4"   # headings: warm off-white
C_TEXT_B  = "#8a95a6"   # body: soft blue-grey (readable, not harsh)
C_TEXT_M  = "#4c5c72"   # muted captions

# Genshin element colours  (vivid but not neon)
EL_GEO     = "#d4bc5c"   # Geo    — golden earth
EL_PYRO    = "#d97a50"   # Pyro   — ember orange
EL_HYDRO   = "#4a9ed4"   # Hydro  — ocean blue
EL_ELECTRO = "#9c74cc"   # Electro— amethyst purple
EL_ANEMO   = "#4eb88a"   # Anemo  — jade green

# Map skill categories → elements
ELEM_MAP = {
    "Language":        {"color": EL_GEO,     "name": "Geo",     "icon": "⬡"},
    "Game Dev":        {"color": EL_PYRO,    "name": "Pyro",    "icon": "🔥"},
    "Web":             {"color": EL_HYDRO,   "name": "Hydro",   "icon": "💧"},
    "AI/Tooling":      {"color": EL_ELECTRO, "name": "Electro", "icon": "⚡"},
    "CS Fundamentals": {"color": EL_ANEMO,   "name": "Anemo",   "icon": "🌀"},
}

# ─────────────────────────────────────────────────────────────────────────────
# Data
# ─────────────────────────────────────────────────────────────────────────────
SKILLS = [
    ("Python",             85, "Language"),
    ("C",                  75, "Language"),
    ("C++",                80, "Language"),
    ("C#",                 88, "Language"),
    ("HTML / CSS",         70, "Web"),
    ("Prompt Engineering", 90, "AI/Tooling"),
    ("DSA / DAA",          82, "CS Fundamentals"),
    ("Game Systems",       85, "Game Dev"),
]

MILESTONES = [
    {"year": "Elementary",    "title": "San Juan, Southern Leyte",         "note": "Public school. First devices, first questions about how technology works."},
    {"year": "Jr & Sr High",  "title": "Self-study takes root",            "note": "No mentor, no syllabus. Researching and experimenting on the side."},
    {"year": "Entrance Exams","title": "Passed multiple state exams",       "note": "Nerves at interviews cost a few offers. CIT-U was always the target."},
    {"year": "CIT-U · Yr 1",  "title": "First prototype: TLGMS",          "note": "Enrolled in BS Computer Science. Built the first game solo."},
    {"year": "CIT-U · Yr 2–3","title": "Infinitus begins",                "note": "Joined Glenshayne Belarmino & Wilmark Racho. UI, code, design, PM."},
    {"year": "2026",           "title": "Target: Graduate",                "note": "BS Computer Science — first industry role.", "future": True},
]

NAV_LABELS = {
    "Home":          "◈  Home",
    "Autobiography": "◈  My Story",
    "Skills":        "◈  Skills",
    "Projects":      "◈  Projects",
    "Contact":       "◈  Contact",
}
PAGES = list(NAV_LABELS.keys())

# ─────────────────────────────────────────────────────────────────────────────
# Asset helpers
# ─────────────────────────────────────────────────────────────────────────────

def load_resume() -> tuple[bytes, str, str] | None:
    p = ASSETS / "cv.pdf"
    if not p.exists():
        return None
    data = p.read_bytes()
    if data.startswith(b"%PDF"):
        return data, "Kurt-Malubay-Resume.pdf", "application/pdf"
    return None


def show_image(fname: str, caption: str) -> None:
    p = ASSETS / fname
    if p.exists():
        cv = ASSETS / "cv.pdf"
        dupe = cv.exists() and p.stat().st_size == cv.stat().st_size and p.read_bytes() == cv.read_bytes()
        if not dupe:
            st.image(str(p), caption=caption, use_container_width=True)
            return
    # placeholder
    with st.container(border=True):
        st.caption(f"📂  {fname}")
        st.caption(f"Place in  assets/{fname}")
        st.caption(caption)

# ─────────────────────────────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    # Identity block
    st.markdown(
        f"""
        <div style="padding:1.2rem 0 0.8rem; text-align:center;">
            <div style="
                display:inline-flex; align-items:center; justify-content:center;
                width:56px; height:56px;
                border:2px solid {C_GOLD}; color:{C_GOLD};
                font-family:'Cinzel',serif; font-size:1rem; font-weight:700;
                background:{C_PANEL2}; margin-bottom:0.7rem;
                transform:rotate(45deg); letter-spacing:0.05em;
            ">
                <span style="transform:rotate(-45deg)">KM</span>
            </div>
            <div style="font-family:'Cinzel',serif; font-size:0.95rem;
                        color:{C_TEXT_H}; letter-spacing:0.12em; text-transform:uppercase;">
                {NAME}
            </div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:0.68rem;
                        color:{C_TEXT_M}; letter-spacing:0.06em; margin-top:0.25rem;">
                {PROGRAM} · {SECTION}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # Navigation — display names are different from page keys
    selected_display = st.radio(
        "nav",
        list(NAV_LABELS.values()),
        label_visibility="collapsed",
    )
    page = [k for k, v in NAV_LABELS.items() if v == selected_display][0]

    st.divider()

    # Quick stats — 2-column mini grid
    q1, q2 = st.columns(2)
    q1.metric("Year",     "3rd",  label_visibility="visible")
    q2.metric("Grad",     "2026", label_visibility="visible")

    st.divider()

    # Links
    st.link_button("⌥  GitHub",   GITHUB,             use_container_width=True)
    st.link_button("🎮  itch.io",  ITCH,               use_container_width=True)
    st.link_button("✉  Email",    f"mailto:{EMAIL}",  use_container_width=True)

    res = load_resume()
    if res:
        rb, rfn, rmt = res
        st.download_button("⬇  Résumé", rb, file_name=rfn, mime=rmt, use_container_width=True)
    else:
        st.caption("Résumé · add cv.pdf to assets/")

    st.divider()
    st.caption(f"{COURSE}")
    st.caption("Built with Streamlit")

# ─────────────────────────────────────────────────────────────────────────────
# Global CSS  — injected after sidebar so dark variable is available
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    f"""<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Cinzel+Decorative:wght@700&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

    /* ── Page ── */
    .stApp {{
        background:
            radial-gradient(ellipse 90% 50% at 5% -5%,  rgba(197,160,89,0.07) 0%, transparent 60%),
            radial-gradient(ellipse 60% 40% at 95% 100%, rgba(74,158,212,0.05) 0%, transparent 55%),
            {C_BG} !important;
        background-attachment: fixed !important;
    }}

    /* ── Typography base ── */
    html, body, [class*="css"], [class*="st-"] {{
        font-family: 'Inter', system-ui, sans-serif !important;
    }}
    [data-testid="stIconMaterial"],.material-symbols-rounded {{
        font-family:"Material Symbols Rounded" !important; line-height:1;
    }}
    .stApp p, .stApp li {{
        font-size: 0.93rem;
        line-height: 1.85;
        color: {C_TEXT_B} !important;
    }}
    .stMarkdown strong {{
        color: {C_TEXT_H} !important;
        font-weight: 600;
    }}

    /* ── Headings ── */
    h1 {{
        font-family: 'Cinzel Decorative','Cinzel',serif !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.04em !important;
        color: {C_GOLD} !important;
        text-shadow: 0 0 40px rgba(197,160,89,0.22) !important;
        line-height: 1.35 !important;
    }}
    h2 {{
        font-family: 'Cinzel',serif !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.10em !important;
        color: {C_TEXT_H} !important;
        text-transform: uppercase !important;
        padding-bottom: 0.3rem !important;
        border-bottom: 1px solid {C_DIVIDER} !important;
    }}
    h3 {{
        font-family: 'Cinzel',serif !important;
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.18em !important;
        text-transform: uppercase !important;
        color: {C_GOLD_D} !important;
        margin-bottom: 0.2rem !important;
    }}
    h4 {{
        font-family: 'Inter', sans-serif !important;
        font-size: 0.92rem !important;
        font-weight: 600 !important;
        color: {C_TEXT_H} !important;
    }}

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {{
        background: #0a0e18 !important;
        border-right: 1px solid {C_BORDER} !important;
    }}
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li {{
        color: {C_TEXT_B} !important;
        font-size: 0.84rem !important;
    }}
    [data-testid="stSidebar"] .stRadio label {{
        font-family: 'Cinzel',serif !important;
        font-size: 0.75rem !important;
        letter-spacing: 0.12em !important;
        color: {C_TEXT_B} !important;
    }}
    [data-testid="stHeader"] {{ background: transparent !important; }}

    /* ── Hide chrome ── */
    [data-testid="stDecoration"],
    [data-testid="stAppDeployButton"],
    [data-testid="stMainMenu"],
    [data-testid="stStatusWidget"] {{ display: none !important; }}

    /* ── Metrics ── */
    [data-testid="stMetric"] {{
        background: {C_PANEL} !important;
        border: 1px solid {C_BORDER} !important;
        border-top: 2px solid {C_GOLD_D} !important;
        padding: 0.9rem 1rem !important;
    }}
    [data-testid="stMetricValue"] {{
        font-family: 'Cinzel',serif !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        color: {C_GOLD} !important;
    }}
    [data-testid="stMetricLabel"] p {{
        font-family: 'JetBrains Mono',monospace !important;
        font-size: 0.62rem !important;
        letter-spacing: 0.18em !important;
        text-transform: uppercase !important;
        color: {C_TEXT_M} !important;
    }}
    [data-testid="stMetricDelta"] span {{
        color: {C_TEXT_M} !important;
        font-family: 'JetBrains Mono',monospace !important;
        font-size: 0.7rem !important;
    }}

    /* ── Bordered containers ── */
    [data-testid="stVerticalBlockBorderWrapper"] > div {{
        background: {C_PANEL} !important;
        border: 1px solid {C_BORDER} !important;
        border-top: 2px solid rgba(197,160,89,0.30) !important;
        padding: 1rem 1.1rem !important;
    }}

    /* ── Blockquote ── */
    blockquote {{
        background: rgba(197,160,89,0.05) !important;
        border-left: 3px solid {C_GOLD} !important;
        padding: 0.65rem 1rem !important;
        margin: 0.8rem 0 1.2rem 0 !important;
        border-radius: 0 3px 3px 0 !important;
    }}
    blockquote p {{
        font-family: 'Cormorant Garamond',Georgia,serif !important;
        font-size: 1.08rem !important;
        font-style: italic !important;
        color: #b8a880 !important;
        line-height: 1.6 !important;
    }}

    /* ── Captions ── */
    [data-testid="stCaptionContainer"] p {{
        font-family: 'JetBrains Mono',monospace !important;
        font-size: 0.70rem !important;
        letter-spacing: 0.05em !important;
        color: {C_TEXT_M} !important;
    }}

    /* ── Progress bars ── */
    .stProgress > div > div {{
        background: rgba(255,255,255,0.05) !important;
        border-radius: 2px !important;
    }}
    .stProgress > div > div > div > div {{
        background: linear-gradient(90deg, {C_GOLD_D}, {C_GOLD}) !important;
        border-radius: 2px !important;
    }}
    .stProgress p {{
        color: {C_TEXT_B} !important;
        font-size: 0.82rem !important;
    }}

    /* ── Dividers ── */
    hr {{
        border: none !important;
        border-top: 1px solid {C_DIVIDER} !important;
        margin: 1.4rem 0 !important;
    }}

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {{
        background: transparent !important;
        border-bottom: 1px solid {C_BORDER} !important;
        gap: 0 !important;
    }}
    .stTabs [data-baseweb="tab"] {{
        font-family: 'Cinzel',serif !important;
        font-size: 0.74rem !important;
        letter-spacing: 0.14em !important;
        text-transform: uppercase !important;
        color: {C_TEXT_M} !important;
        padding: 0.55rem 1.1rem !important;
        border-radius: 3px 3px 0 0 !important;
    }}
    .stTabs [aria-selected="true"] {{
        color: {C_GOLD} !important;
        background: {C_PANEL} !important;
        border-bottom: 2px solid {C_GOLD} !important;
    }}

    /* ── Form labels ── */
    .stSelectbox label, .stMultiSelect label, .stSlider label,
    .stTextInput label, .stTextArea label, .stCheckbox label,
    .stRadio label {{
        font-family: 'JetBrains Mono',monospace !important;
        font-size: 0.68rem !important;
        letter-spacing: 0.10em !important;
        text-transform: uppercase !important;
        color: {C_TEXT_M} !important;
    }}

    /* ── Buttons ── */
    .stButton button {{
        font-family: 'Cinzel',serif !important;
        font-size: 0.72rem !important;
        letter-spacing: 0.14em !important;
        text-transform: uppercase !important;
        border-color: {C_BORDER} !important;
    }}
    .stLinkButton a {{
        font-family: 'Cinzel',serif !important;
        font-size: 0.72rem !important;
        letter-spacing: 0.12em !important;
        text-transform: uppercase !important;
    }}

    /* ── Info / notification boxes ── */
    [data-testid="stNotification"] {{
        background: rgba(197,160,89,0.06) !important;
        border-left: 3px solid {C_GOLD_D} !important;
    }}
    [data-testid="stNotification"] p {{
        color: {C_TEXT_B} !important;
    }}

    /* ── Expanders ── */
    details summary, .streamlit-expanderHeader {{
        font-family: 'Cinzel',serif !important;
        font-size: 0.76rem !important;
        letter-spacing: 0.12em !important;
        text-transform: uppercase !important;
        color: {C_TEXT_B} !important;
    }}

    /* ── Code ── */
    .stCode code {{ font-family:'JetBrains Mono',monospace !important; font-size:0.80rem !important; }}

    /* ── Tables / dataframes ── */
    [data-testid="stDataFrame"] td,
    [data-testid="stDataFrame"] th {{
        color: {C_TEXT_B} !important;
        font-family: 'Inter',sans-serif !important;
        font-size: 0.82rem !important;
    }}
    [data-testid="stTable"] td,
    [data-testid="stTable"] th {{
        color: {C_TEXT_B} !important;
        font-size: 0.84rem !important;
    }}
    </style>""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
# Shared helpers
# ─────────────────────────────────────────────────────────────────────────────

def section_eyebrow(number: str) -> None:
    st.caption(f"✦  {number}  ·  {COURSE}  ·  {PROGRAM}")


def footer() -> None:
    st.divider()
    st.caption(
        f"✦  {FULL_NAME}  ·  {SECTION}  ·  {COURSE}  ·  {INSTRUCTOR}"
    )


def show_tags(items: list[str]) -> None:
    st.markdown("  ".join(f"`{t}`" for t in items))


def show_timeline(items: list[dict]) -> None:
    for item in items:
        future = item.get("future", False)
        left, right = st.columns([1, 3])
        with left:
            marker = "◈" if future else "◆"
            st.markdown(
                f"<span style='font-family:JetBrains Mono,monospace;"
                f"font-size:0.68rem;color:{C_GOLD_D if future else C_GOLD};"
                f"letter-spacing:0.06em;'>{marker}  {item['year']}</span>",
                unsafe_allow_html=True,
            )
        with right:
            style = f"opacity:0.6;" if future else ""
            st.markdown(f"**{item['title']}**")
            st.write(item["note"])
        st.write("")


def quest_bar(label: str, pct: float, color: str = C_GOLD) -> None:
    """A quest-progress row: label on top, coloured bar below."""
    pct_clamped = max(0.0, min(1.0, pct))
    filled = int(pct_clamped * 20)       # 20-segment bar
    empty  = 20 - filled
    bar_str = "█" * filled + "░" * empty
    col_l, col_r = st.columns([5, 1])
    col_l.markdown(f"**{label}**")
    col_r.markdown(
        f"<span style='font-family:JetBrains Mono,monospace;"
        f"font-size:0.68rem;color:{C_TEXT_M};'>{int(pct_clamped*100)}%</span>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='font-family:JetBrains Mono,monospace;font-size:0.68rem;"
        f"color:{color};letter-spacing:-0.5px;margin-bottom:1rem;'>{bar_str}</div>",
        unsafe_allow_html=True,
    )


def vision_panel(category: str, skills: list[tuple[str, int]]) -> None:
    """Vision-element skill panel — unique Genshin-style display."""
    el    = ELEM_MAP.get(category, {"color": C_GOLD, "name": category, "icon": "◆"})
    color = el["color"]
    icon  = el["icon"]
    ename = el["name"]

    with st.container(border=True):
        st.markdown(
            f"<div style='display:flex;align-items:center;gap:0.6rem;margin-bottom:0.4rem;'>"
            f"<span style='font-size:1.4rem;line-height:1;'>{icon}</span>"
            f"<div><div style='font-family:Cinzel,serif;font-size:0.72rem;"
            f"letter-spacing:0.18em;text-transform:uppercase;color:{color};'>{ename}</div>"
            f"<div style='font-family:JetBrains Mono,monospace;font-size:0.60rem;"
            f"color:{C_TEXT_M};letter-spacing:0.06em;'>{category}</div></div></div>",
            unsafe_allow_html=True,
        )
        st.divider()
        for sname, score in sorted(skills, key=lambda x: -x[1]):
            row_l, row_r = st.columns([4, 1])
            row_l.write(sname)
            row_r.markdown(
                f"<span style='font-family:JetBrains Mono,monospace;"
                f"font-size:0.78rem;color:{color};font-weight:600;'>{score}</span>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<div style='background:rgba(255,255,255,0.05);border-radius:2px;"
                f"height:4px;margin:-0.3rem 0 0.7rem;overflow:hidden;'>"
                f"<div style='background:{color};width:{score}%;height:4px;"
                f"border-radius:2px;opacity:0.75;'></div></div>",
                unsafe_allow_html=True,
            )

# ─────────────────────────────────────────────────────────────────────────────
# HOME
# ─────────────────────────────────────────────────────────────────────────────

def page_home() -> None:
    section_eyebrow("00")
    st.write("")

    # ── Hero ──────────────────────────────────────────────────────────────
    hero_l, hero_r = st.columns([1.6, 1], gap="large")
    with hero_l:
        st.title(NAME)
        st.caption(f"{FULL_NAME}  ·  {PROGRAM}  ·  Cebu City")
        st.write("")
        st.markdown(f"> *\"{TAGLINE}\"*")
        st.write("")
        st.write(
            "I write game systems, UI code, and the tooling that holds a project together. "
            "Mostly C#, C++, and Python — self-taught since a Blackberry phone sparked the "
            "question *\"how does this work?\"* Three years into a CS degree, still shipping "
            "on jam deadlines."
        )
        st.write(
            "The work I want is the part players feel but never see: "
            "UI flows, scene systems, the glue that saves the team an afternoon."
        )
        st.write("")
        b1, b2, b3 = st.columns(3)
        b1.link_button("🎮  Games",   ITCH,            use_container_width=True)
        b2.link_button("⌥  Code",     GITHUB,          use_container_width=True)
        b3.link_button("✉  Contact",  f"mailto:{EMAIL}", use_container_width=True)

    with hero_r:
        show_image("profile.jpg", "Kurt · BSCS 3 · CIT-U")

    st.divider()

    # ── Character Attributes ───────────────────────────────────────────────
    st.subheader("Character Attributes")
    st.write("")
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Projects",   "2+",   "shipped games")
    a2.metric("Languages",  "6+",   "C-family core")
    a3.metric("Year Level", "3rd",  "CIT-U BSCS")
    a4.metric("Graduating", "2026", "target")

    st.divider()

    # ── Specialisations ────────────────────────────────────────────────────
    st.subheader("Specialisations")
    st.write("")
    sp1, sp2, sp3 = st.columns(3, gap="medium")
    with sp1:
        with st.container(border=True):
            st.markdown(
                f"<span style='font-size:1.2rem;'>🔥</span>"
                f"<span style='font-family:Cinzel,serif;font-size:0.72rem;"
                f"letter-spacing:0.16em;text-transform:uppercase;"
                f"color:{EL_PYRO};margin-left:0.5rem;'>Game Systems</span>",
                unsafe_allow_html=True,
            )
            st.write("")
            st.write(
                "State machines, scene transitions, and the architecture keeping "
                "a Godot project stable under pressure. C# and GDScript."
            )
    with sp2:
        with st.container(border=True):
            st.markdown(
                f"<span style='font-size:1.2rem;'>💧</span>"
                f"<span style='font-family:Cinzel,serif;font-size:0.72rem;"
                f"letter-spacing:0.16em;text-transform:uppercase;"
                f"color:{EL_HYDRO};margin-left:0.5rem;'>UI / UX Dev</span>",
                unsafe_allow_html=True,
            )
            st.write("")
            st.write(
                "Menus, HUDs, and editor panels. Intentional, responsive, and "
                "clean — UI that makes a game feel polished without announcing itself."
            )
    with sp3:
        with st.container(border=True):
            st.markdown(
                f"<span style='font-size:1.2rem;'>🌀</span>"
                f"<span style='font-family:Cinzel,serif;font-size:0.72rem;"
                f"letter-spacing:0.16em;text-transform:uppercase;"
                f"color:{EL_ANEMO};margin-left:0.5rem;'>Project Lead</span>",
                unsafe_allow_html=True,
            )
            st.write("")
            st.write(
                "Repo ownership, task breakdowns, and the coordination that keeps "
                "a team honest under deadlines. The unglamorous work."
            )

    st.divider()

    # ── Active Quests ──────────────────────────────────────────────────────
    st.subheader("Active Quests")
    st.write("")

    quests = [
        ("Infinitus  ·  Multiplayer Battle Royale",  0.65, EL_PYRO),
        ("Portfolio  ·  Public presentation",         0.40, EL_HYDRO),
        ("CSIT 349   ·  Applied AI coursework",       0.25, EL_ANEMO),
    ]
    for label, pct, color in quests:
        quest_bar(label, pct, color)

    st.write("")
    st.info(
        "Available for internships, game jams, and teams that need someone "
        "who owns the full pipeline — design, code, and the merge at 2am.",
        icon="🌟",
    )
    footer()


# ─────────────────────────────────────────────────────────────────────────────
# AUTOBIOGRAPHY
# ─────────────────────────────────────────────────────────────────────────────

def page_autobiography() -> None:
    section_eyebrow("01")
    st.write("")
    st.title("My Story")
    st.write("*A Blackberry phone, a province childhood, and a question that never stopped pulling.*")
    st.write("")

    main_col, side_col = st.columns([1.55, 1], gap="large")

    with main_col:
        tab_bg, tab_edu, tab_now = st.tabs(
            ["  🌊  Origins  ", "  🎓  Education  ", "  ⚔️  Now  "]
        )

        with tab_bg:
            st.write("")
            st.subheader("The Province")
            st.write(
                "I grew up in San Juan, Southern Leyte — sea on one side, mountains on "
                "the other. Curious kids in the province run out of distractions fast, "
                "which was the best thing that could have happened to me. Time to think, "
                "take things apart, and ask questions nobody was rushing to answer."
            )

            st.subheader("The Blackberry Moment")
            st.write(
                "My mother brought home a Blackberry phone. I loaded Assassin's Creed on "
                "it and something shifted — not the game, but the question underneath it: "
                "*how does this exist?* How does something pocket-sized run a world that "
                "detailed?"
            )
            st.write(
                "That question pulled me through elementary and high school with no mentor "
                "and no roadmap — just a kid in the province who kept finding the next "
                "thing to learn."
            )

        with tab_edu:
            st.write("")
            st.subheader("Public School to CIT-U")
            st.write(
                "Public schools from elementary through senior high. When entrance exams "
                "came, I passed at several state universities. Most had interviews — I got "
                "shy and let some good offers go. CIT-U felt different: competitive in "
                "exactly the right way."
            )
            st.write(
                "Game development was already the direction. CIT-U felt like the place "
                "where that direction could become something real. Three years in, that "
                "instinct has held. The degree pushed my fundamentals harder than I "
                "expected — DSA, DAA, systems design — and I am glad it did."
            )

            st.write("")
            st.dataframe(
                pd.DataFrame({
                    "Stage":   ["Elementary", "Jr–Sr High", "Entrance Exams", "CIT-U"],
                    "Detail":  [
                        "San Juan, Southern Leyte · public school",
                        "Self-study habit solidifies",
                        "Passed multiple state exams · chose CIT-U",
                        "BS Computer Science · 3rd year",
                    ],
                }),
                hide_index=True,
                use_container_width=True,
            )

        with tab_now:
            st.write("")
            st.subheader("Current Chapter")
            st.write(
                "Game development is the through-line. It touches systems programming, "
                "UI, math, design, and the human work of making a team function. "
                "Every layer I learn opens two more underneath — that gap is not a "
                "problem, it is the whole point."
            )
            st.write(
                "Infinitus is the proving ground: a multiplayer battle royale built from "
                "scratch with two teammates. I own the UI, the code architecture, and the "
                "project management. Real constraints. Real stakes."
            )

            st.write("")
            with st.expander("Beyond code"):
                st.write(
                    "I play Genshin Impact, Assassin's Creed, and anything with systems "
                    "deep enough to pick apart. Gaming is how I study design — every UI "
                    "screen, every loading animation is a lesson in what to build next."
                )

    with side_col:
        st.subheader("Chronicle")
        show_timeline(MILESTONES)

        st.divider()
        st.subheader("Field Notes")
        st.dataframe(
            pd.DataFrame({
                "Field": ["Hometown", "Base", "Degree", "Grad target", "Spoken", "First game"],
                "Entry": [
                    "San Juan, Southern Leyte",
                    "Cebu City, Philippines",
                    "BS Computer Science, CIT-U",
                    "2026",
                    "English · Filipino · Bisaya",
                    "AC on a Blackberry",
                ],
            }),
            hide_index=True,
            use_container_width=True,
        )

        st.info(f"Section {SECTION}  ·  {INSTRUCTOR}", icon="📌")

    footer()


# ─────────────────────────────────────────────────────────────────────────────
# SKILLS  — Vision-panel layout, element affinity chart
# ─────────────────────────────────────────────────────────────────────────────

def page_skills() -> None:
    section_eyebrow("02")
    st.write("")
    st.title("Skills")
    st.write(
        "*Each skill is grouped under a Vision element — a domain metaphor. "
        "Scores are honest self-assessment: 90 = do it in the dark; 70 = ship with docs open.*"
    )
    st.write("")

    skill_df = pd.DataFrame(SKILLS, columns=["Skill", "Score", "Category"])
    cats = skill_df["Category"].unique().tolist()

    # Vision panels — 2 per row
    for i in range(0, len(cats), 2):
        pair = cats[i : i + 2]
        cols = st.columns(len(pair), gap="medium")
        for col, cat in zip(cols, pair):
            with col:
                rows = [
                    (r["Skill"], r["Score"])
                    for _, r in skill_df[skill_df["Category"] == cat].iterrows()
                ]
                vision_panel(cat, rows)
        st.write("")

    st.divider()

    # ── Element Affinity chart ─────────────────────────────────────────────
    st.subheader("Element Affinity")
    st.caption("Average mastery per Vision domain")
    st.write("")

    avg_df = (
        skill_df.groupby("Category", as_index=False)["Score"]
        .mean().round(1)
    )
    avg_df["Element"] = avg_df["Category"].map(
        lambda c: ELEM_MAP.get(c, {}).get("name", c)
    )
    avg_df["Color"] = avg_df["Category"].map(
        lambda c: ELEM_MAP.get(c, {}).get("color", C_GOLD)
    )
    sorted_avg = avg_df.sort_values("Score", ascending=False)

    chart = (
        alt.Chart(sorted_avg)
        .mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3, size=38)
        .encode(
            x=alt.X(
                "Element:N",
                sort=sorted_avg["Element"].tolist(),
                axis=alt.Axis(
                    labelFont="JetBrains Mono", labelColor=C_TEXT_M,
                    labelFontSize=11, labelAngle=0, title=None,
                    tickColor=C_DIVIDER, domainColor=C_DIVIDER,
                ),
            ),
            y=alt.Y(
                "Score:Q",
                scale=alt.Scale(domain=[0, 100]),
                axis=alt.Axis(
                    labelFont="JetBrains Mono", labelColor=C_TEXT_M,
                    labelFontSize=10, gridColor=C_DIVIDER,
                    domainColor=C_DIVIDER, title=None,
                ),
            ),
            color=alt.Color("Color:N", scale=None, legend=None),
            tooltip=[
                alt.Tooltip("Element:N",  title="Vision"),
                alt.Tooltip("Score:Q",    title="Avg", format=".1f"),
                alt.Tooltip("Category:N", title="Domain"),
            ],
        )
        .properties(height=240, background=C_PANEL)
        .configure_view(strokeWidth=0)
    )
    st.altair_chart(chart, use_container_width=True)

    st.divider()
    st.subheader("Approach")
    st.write("")

    ap1, ap2 = st.columns(2, gap="medium")
    with ap1:
        with st.container(border=True):
            st.markdown("#### Docs before forums")
            st.write(
                "Most of what I know came from source code and documentation, not tutorials. "
                "When something breaks I trace the stack first. "
                "DSA and DAA from the degree made that instinct systematic."
            )
    with ap2:
        with st.container(border=True):
            st.markdown("#### Own the full pipeline")
            st.write(
                "On Infinitus I write code, design UI, manage the repo, and coordinate "
                "the team. I don't wait for someone else to do the hard part — "
                "that's where the real learning is."
            )

    with st.expander("A loop I keep coming back to"):
        st.code(
            """\
# The heartbeat under every project I build
while running:
    dt = clock.tick(TARGET_FPS) / 1000.0

    process_input()          # read from controller / mouse / touch
    update_state(dt)         # physics, UI state, game logic
    render(state)            # draw this frame

    if debug_overlay:
        draw_fps_and_stats()
""",
            language="python",
        )
        st.caption("Illustrative — the pattern matters more than the file.")

    footer()


# ─────────────────────────────────────────────────────────────────────────────
# PROJECTS  — Quest Archive layout
# ─────────────────────────────────────────────────────────────────────────────

def page_projects() -> None:
    section_eyebrow("03")
    st.write("")
    st.title("Projects")
    st.write(
        "*Two games. The first proves I can build from nothing. "
        "The second proves I can lead a team.*"
    )
    st.write("")

    tab_inf, tab_tlgms, tab_open = st.tabs([
        "  ⚔️  Infinitus  ",
        "  🌀  TLGMS  ",
        "  ◈  Open Field  ",
    ])

    # ── Infinitus ──────────────────────────────────────────────────────────
    with tab_inf:
        st.write("")
        img_c, txt_c = st.columns([1.05, 1], gap="large")
        with img_c:
            show_image("infinitus.jpg", "Infinitus — battle royale")
        with txt_c:
            st.markdown(
                f"<span style='font-family:JetBrains Mono,monospace;font-size:0.65rem;"
                f"letter-spacing:0.14em;color:{EL_PYRO};text-transform:uppercase;'>"
                f"🔥  Active · Game Dev · Team</span>",
                unsafe_allow_html=True,
            )
            st.subheader("Infinitus")
            st.write(
                "A top-down multiplayer battle royale built from scratch with two teammates. "
                "I own the UI systems, core game logic, visual design, and day-to-day "
                "project direction — the full stack of what it takes to ship a game."
            )
            st.write("")
            st.markdown("**Role**")
            st.write("UI Developer · Programmer · Project Manager")
            st.markdown("**Stack**")
            show_tags(["Godot 4", "C#", "GDScript", "Git"])
            st.write("")
            st.link_button("⌥  View on GitHub", GITHUB, use_container_width=True)

        st.divider()
        d1, d2 = st.columns(2)
        with d1:
            st.markdown("**What I built**")
            st.markdown(
                "- All UI: menus, HUD, overlays, scene flow\n"
                "- Core game logic: input → state → render\n"
                "- Project management: tasks, milestones, alignment"
            )
        with d2:
            st.markdown("**How I led it**")
            st.markdown(
                "- Full repository ownership: merges, rebases, CI\n"
                "- Art direction and visual asset creation\n"
                "- Architecture decisions for long-term stability"
            )
        st.caption("Team: Glenshayne Belarmino · Wilmark Racho · Kurt Justin Malubay")

    # ── TLGMS ──────────────────────────────────────────────────────────────
    with tab_tlgms:
        st.write("")
        img_c, txt_c = st.columns([1.05, 1], gap="large")
        with img_c:
            show_image("tlgms.png", "TLGMS — first prototype")
        with txt_c:
            st.markdown(
                f"<span style='font-family:JetBrains Mono,monospace;font-size:0.65rem;"
                f"letter-spacing:0.14em;color:{EL_ANEMO};text-transform:uppercase;'>"
                f"🌀  Prototype · Solo · Year 1</span>",
                unsafe_allow_html=True,
            )
            st.subheader("TLGMS")
            st.write(
                "My first game prototype — built after Year 1 to prove I could take an idea "
                "from nothing to something playable. Not about polish; about proof of concept. "
                "The moment game dev stopped being a hobby and became a direction."
            )
            st.write("")
            st.markdown("**Role**")
            st.write("Solo Developer — design, code, art, audio")
            st.markdown("**Stack**")
            show_tags(["Godot", "GDScript"])
            st.write("")
            st.link_button("🎮  Play on itch.io", ITCH, use_container_width=True)

        st.divider()
        st.markdown("**What I built**")
        st.markdown(
            "- Everything solo: mechanics, UI, scene flow, assets\n"
            "- Learned Godot entirely from documentation\n"
            "- Shipped a playable build — first real proof of concept\n"
            "- The project that set the entire direction"
        )

    # ── Open Field ─────────────────────────────────────────────────────────
    with tab_open:
        st.write("")
        st.subheader("Looking Ahead")
        st.write("")

        col_a, col_b = st.columns(2, gap="medium")
        with col_a:
            with st.container(border=True):
                st.markdown("#### 🌟  Open for Internship")
                st.write(
                    "Actively seeking an internship with real problems and "
                    "experienced teammates. I learn fast when the work matters."
                )
                st.write("")
                st.link_button("✉  Get in touch", f"mailto:{EMAIL}", use_container_width=True)
        with col_b:
            with st.container(border=True):
                st.markdown("#### ⚔️  Game Jams")
                st.write(
                    "Always open to jam teams that actually ship. "
                    "I bring code architecture, UI, and the discipline "
                    "to scope a project that finishes."
                )
                st.write("")
                st.link_button("🎮  itch.io profile", ITCH, use_container_width=True)

        st.write("")
        with st.container(border=True):
            st.markdown("#### What I bring")
            c1, c2, c3 = st.columns(3)
            c1.metric("Ownership",  "100%", "of whatever I touch")
            c2.metric("Codebase",   "90%+", "authored on team projects")
            c3.metric("Shipped",    "2",    "playable games")

    footer()


# ─────────────────────────────────────────────────────────────────────────────
# CONTACT  — Dispatch Terminal (completely original layout)
# ─────────────────────────────────────────────────────────────────────────────

def page_contact() -> None:
    section_eyebrow("04")
    st.write("")
    st.title("Contact")
    st.write(
        "*Internship, collaboration, game jam invite, or just curiosity — "
        "all of those are worth a message.*"
    )
    st.write("")

    left_col, right_col = st.columns([1.45, 1], gap="large")

    # ── LEFT: message form ─────────────────────────────────────────────────
    with left_col:
        st.subheader("Send a Dispatch")
        st.write("")

        with st.container(border=True):
            with st.form("dispatch_form", clear_on_submit=True):
                # Sender
                st.markdown("**Identify yourself**")
                n_col, e_col = st.columns(2)
                sender_name  = n_col.text_input("Name",  placeholder="Your name")
                sender_email = e_col.text_input("Email", placeholder="your@email.com")

                st.write("")

                # Dispatch type — radio is visually distinct from the sample's selectbox
                st.markdown("**Type of dispatch**")
                dtype = st.radio(
                    "dispatch_type",
                    ["💼  Internship / Work",
                     "⚔️  Game Jam or Collab",
                     "🗺️  Project Feedback",
                     "👋  Just saying hi"],
                    label_visibility="collapsed",
                    horizontal=False,
                )

                st.write("")

                # Message
                st.markdown("**Message**")
                message = st.text_area(
                    "message_body",
                    placeholder="What are you building? What do you need? What caught your eye?",
                    height=120,
                    label_visibility="collapsed",
                )

                st.write("")
                can_reply = st.checkbox("Reply to my email address above")

                submitted = st.form_submit_button(
                    "✦  Transmit Message",
                    use_container_width=True,
                )

        # ── Form result handling ───────────────────────────────────────────
        if submitted:
            problems = []
            if not sender_name.strip():
                problems.append("Name is required.")
            if not message.strip():
                problems.append("Message cannot be empty.")
            if can_reply and ("@" not in sender_email or "." not in sender_email.split("@")[-1]):
                problems.append("Email address looks invalid.")

            for p in problems:
                st.warning(p, icon="⚠️")

            if not problems:
                st.session_state.setdefault("dispatches", []).append(
                    {
                        "sender":  sender_name.strip(),
                        "email":   sender_email.strip() or "—",
                        "type":    dtype,
                        "message": message.strip(),
                        "reply":   can_reply,
                        "at":      datetime.now().strftime("%H:%M"),
                    }
                )
                st.success(
                    f"Dispatch received, {sender_name.strip()}. "
                    "Note: this app has no mail backend — messages exist in this "
                    "session only. Use the email link on the right for a real reply.",
                    icon="📨",
                )

    # ── RIGHT: coordinates + info ──────────────────────────────────────────
    with right_col:
        st.subheader("Signal Coordinates")
        st.write("")

        with st.container(border=True):
            st.markdown(
                f"<div style='display:grid;gap:0.9rem;'>"
                f"<div>"
                f"  <div style='font-family:JetBrains Mono,monospace;font-size:0.60rem;"
                f"  letter-spacing:0.14em;text-transform:uppercase;color:{C_TEXT_M};'>"
                f"  Email</div>"
                f"  <div style='font-size:0.88rem;color:{C_TEXT_H};margin-top:0.15rem;'>"
                f"  {EMAIL}</div>"
                f"</div>"
                f"<div>"
                f"  <div style='font-family:JetBrains Mono,monospace;font-size:0.60rem;"
                f"  letter-spacing:0.14em;text-transform:uppercase;color:{C_TEXT_M};'>"
                f"  GitHub</div>"
                f"  <div style='font-size:0.88rem;color:{C_TEXT_H};margin-top:0.15rem;'>"
                f"  KurtJustinMalubay</div>"
                f"</div>"
                f"<div>"
                f"  <div style='font-family:JetBrains Mono,monospace;font-size:0.60rem;"
                f"  letter-spacing:0.14em;text-transform:uppercase;color:{C_TEXT_M};'>"
                f"  Games</div>"
                f"  <div style='font-size:0.88rem;color:{C_TEXT_H};margin-top:0.15rem;'>"
                f"  sashimiproductions.itch.io</div>"
                f"</div>"
                f"</div>",
                unsafe_allow_html=True,
            )
            st.write("")
            st.link_button("✉  Open email client",     f"mailto:{EMAIL}", use_container_width=True)
            st.link_button("⌥  Open GitHub",            GITHUB,            use_container_width=True)
            st.link_button("🎮  Open itch.io",           ITCH,              use_container_width=True)

        res = load_resume()
        if res:
            rb, rfn, rmt = res
            st.download_button("⬇  Download Résumé", rb, file_name=rfn, mime=rmt,
                               use_container_width=True)

        st.write("")
        with st.container(border=True):
            st.markdown("#### What I'm looking for")
            st.write(
                "An internship with real constraints and experienced teammates. "
                "A jam team that plans to finish. Any project where owning the "
                "whole pipeline — code, UI, coordination — is the job."
            )

        st.write("")
        st.caption("Response time · usually within 24 hours")
        st.caption("Fastest reply topic · anything about Genshin Impact")

    # ── Dispatch Log ───────────────────────────────────────────────────────
    log = st.session_state.get("dispatches", [])
    if log:
        st.divider()
        st.subheader("Dispatch Log")
        st.caption("Session-only · nothing is stored or sent")
        st.write("")
        for entry in reversed(log):
            with st.container(border=True):
                hdr_l, hdr_r = st.columns([4, 1])
                hdr_l.markdown(f"**{entry['sender']}**  ·  {entry['type'].split('  ')[1] if '  ' in entry['type'] else entry['type']}")
                hdr_r.caption(entry["at"])
                st.write(entry["message"])
                if entry["reply"]:
                    st.caption(f"Reply to: {entry['email']}")
        st.write("")
        if st.button("Clear log"):
            st.session_state["dispatches"] = []
            st.rerun()

    footer()


# ─────────────────────────────────────────────────────────────────────────────
# Router
# ─────────────────────────────────────────────────────────────────────────────
if   page == "Home":          page_home()
elif page == "Autobiography":  page_autobiography()
elif page == "Skills":         page_skills()
elif page == "Projects":       page_projects()
else:                          page_contact()
