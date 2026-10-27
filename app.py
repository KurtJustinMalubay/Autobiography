"""
CSIT 349 – Applied AI  |  Kurt Justin J. Malubay
Genshin-inspired dark portfolio. Pure Streamlit.
Run: streamlit run app.py
"""
from __future__ import annotations
from datetime import datetime
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Kurt Malubay · Portfolio",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT   = Path(__file__).parent
ASSETS = ROOT / "assets"

# ── Personal info ─────────────────────────────────────────────────────────────
FULL_NAME  = "Kurt Justin J. Malubay"
PROGRAM    = "BSCS 3"
SECTION    = "F1"
COURSE     = "CSIT 349 · Applied AI"
INSTRUCTOR = "Jun Albert S. Pardillo"
EMAIL      = "justinkurt837@gmail.com"
GITHUB     = "https://github.com/KurtJustinMalubay"
ITCH       = "https://sashimiproductions.itch.io/"

# ── Design tokens ─────────────────────────────────────────────────────────────
BG      = "#090e16"
PANEL   = "#0f1720"
PANEL2  = "#15202e"
PANEL3  = "#1a2840"
BORDER  = "#1e2f42"
GOLD    = "#c9a84c"
GOLD_S  = "#e8c97a"       # softer highlight gold
GOLD_D  = "#6e5220"       # dim gold
TXT_H   = "#d6cfc4"       # warm off-white headings
TXT_B   = "#8a95a6"       # body text
TXT_M   = "#3d5268"       # muted / label
ACCENT  = "#2a3f55"       # subtle highlight band
SIDEBAR = "#07101a"

# ── Element vision palette ─────────────────────────────────────────────────────
EL = {
    "Language":        ("#c9a84c", "Geo",     "◇"),
    "Game Dev":        ("#c9623a", "Pyro",    "△"),
    "Web":             ("#3d8fc2", "Hydro",   "○"),
    "AI / Tooling":    ("#8f6fc0", "Electro", "✦"),
    "CS Fundamentals": ("#3dab78", "Anemo",   "☆"),
}

SKILLS = [
    ("Python",             85, "Language"),
    ("C",                  75, "Language"),
    ("C++",                80, "Language"),
    ("C#",                 88, "Language"),
    ("HTML / CSS",         70, "Web"),
    ("Prompt Engineering", 90, "AI / Tooling"),
    ("DSA / DAA",          82, "CS Fundamentals"),
    ("Game Systems",       85, "Game Dev"),
]

# ── Session state nav ─────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go(p: str) -> None:
    st.session_state.page = p
    st.rerun()

# ── Asset helpers ─────────────────────────────────────────────────────────────
def load_resume():
    p = ASSETS / "cv.pdf"
    if not p.exists():
        return None
    d = p.read_bytes()
    return (d, "Kurt-Malubay-Resume.pdf", "application/pdf") if d.startswith(b"%PDF") else None

def show_img(fname: str, caption: str = "", wide: bool = True) -> None:
    p = ASSETS / fname
    if p.exists():
        if wide:
            st.image(str(p), caption=caption, use_container_width=True)
        else:
            st.image(str(p), caption=caption)
    else:
        with st.container(border=True):
            st.caption(f"📂  Place image at  assets/{fname}")
            if caption:
                st.caption(caption)

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Cinzel+Decorative:wght@700&family=Cormorant+Garamond:ital,wght@1,400;1,600&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Base ── */
.stApp {{
  background:
    radial-gradient(ellipse 70% 40% at 15% 0%, rgba(201,168,76,.07) 0%, transparent 60%),
    radial-gradient(ellipse 50% 30% at 88% 95%, rgba(61,139,194,.05) 0%, transparent 55%),
    {BG} !important;
  background-attachment: fixed !important;
}}
html, body, [class*="css"], [class*="st-"] {{
  font-family: 'Inter', system-ui, sans-serif !important;
}}
[data-testid="stIconMaterial"], .material-symbols-rounded {{
  font-family: "Material Symbols Rounded" !important;
}}
.stApp p, .stApp li {{
  font-size: .91rem;
  line-height: 1.88;
  color: {TXT_B} !important;
}}
.stMarkdown strong {{ color: {TXT_H} !important; font-weight: 600; }}

/* ── Headings ── */
h1 {{
  font-family: 'Cinzel Decorative', 'Cinzel', serif !important;
  font-size: 1.95rem !important;
  font-weight: 700 !important;
  letter-spacing: .04em !important;
  color: {GOLD_S} !important;
  line-height: 1.28 !important;
  text-shadow: 0 0 48px rgba(201,168,76,.15) !important;
}}
h2 {{
  font-family: 'Cinzel', serif !important;
  font-size: .88rem !important;
  font-weight: 600 !important;
  letter-spacing: .22em !important;
  text-transform: uppercase !important;
  color: {TXT_H} !important;
}}
h3 {{
  font-family: 'Cinzel', serif !important;
  font-size: .70rem !important;
  font-weight: 600 !important;
  letter-spacing: .20em !important;
  text-transform: uppercase !important;
  color: {GOLD_D} !important;
}}
h4 {{
  font-family: 'Inter', sans-serif !important;
  font-size: .88rem !important;
  font-weight: 600 !important;
  color: {TXT_H} !important;
}}

/* ── Sidebar ── */
[data-testid="stSidebar"] {{
  background: {SIDEBAR} !important;
  border-right: 1px solid {BORDER} !important;
}}
[data-testid="stSidebar"] p {{
  color: {TXT_B} !important;
  font-size: .82rem !important;
}}
[data-testid="stHeader"] {{ background: transparent !important; }}

/* ── Hide chrome ── */
[data-testid="stDecoration"], [data-testid="stAppDeployButton"],
[data-testid="stMainMenu"], [data-testid="stStatusWidget"] {{
  display: none !important;
}}

/* ── Metrics ── */
[data-testid="stMetric"] {{
  background: {PANEL} !important;
  border: 1px solid {BORDER} !important;
  border-top: 2px solid {GOLD_D} !important;
  padding: .85rem 1rem !important;
  border-radius: 4px !important;
}}
[data-testid="stMetricValue"] {{
  font-family: 'Cinzel', serif !important;
  font-size: 1.45rem !important;
  font-weight: 700 !important;
  color: {GOLD} !important;
}}
[data-testid="stMetricLabel"] p {{
  font-family: 'JetBrains Mono', monospace !important;
  font-size: .58rem !important;
  letter-spacing: .18em !important;
  text-transform: uppercase !important;
  color: {TXT_M} !important;
}}
[data-testid="stMetricDelta"] span {{
  color: {TXT_M} !important;
  font-size: .66rem !important;
}}

/* ── Containers ── */
[data-testid="stVerticalBlockBorderWrapper"] > div {{
  background: {PANEL} !important;
  border: 1px solid {BORDER} !important;
  border-radius: 4px !important;
  padding: 1rem 1.1rem !important;
}}

/* ── Blockquote ── */
blockquote {{
  background: rgba(201,168,76,.04) !important;
  border-left: 3px solid {GOLD} !important;
  padding: .6rem 1rem !important;
  margin: .6rem 0 1rem !important;
  border-radius: 0 3px 3px 0 !important;
}}
blockquote p {{
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 1.05rem !important;
  font-style: italic !important;
  color: #b0a070 !important;
  line-height: 1.65 !important;
}}

/* ── Captions ── */
[data-testid="stCaptionContainer"] p {{
  font-family: 'JetBrains Mono', monospace !important;
  font-size: .65rem !important;
  letter-spacing: .06em !important;
  color: {TXT_M} !important;
}}

/* ── Dividers ── */
hr {{
  border: none !important;
  border-top: 1px solid {BORDER} !important;
  margin: 1.2rem 0 !important;
}}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {{
  background: transparent !important;
  border-bottom: 1px solid {BORDER} !important;
  gap: 0 !important;
}}
.stTabs [data-baseweb="tab"] {{
  font-family: 'Cinzel', serif !important;
  font-size: .68rem !important;
  letter-spacing: .16em !important;
  text-transform: uppercase !important;
  color: {TXT_M} !important;
  padding: .45rem 1rem !important;
}}
.stTabs [aria-selected="true"] {{
  color: {GOLD} !important;
  background: {PANEL} !important;
  border-bottom: 2px solid {GOLD} !important;
}}

/* ── Form labels ── */
.stSelectbox label, .stTextInput label, .stTextArea label,
.stRadio label, .stCheckbox label, .stSlider label {{
  font-family: 'JetBrains Mono', monospace !important;
  font-size: .63rem !important;
  letter-spacing: .10em !important;
  text-transform: uppercase !important;
  color: {TXT_M} !important;
}}

/* ── Buttons (global) ── */
.stButton button, .stLinkButton a {{
  font-family: 'Cinzel', serif !important;
  font-size: .67rem !important;
  letter-spacing: .12em !important;
  text-transform: uppercase !important;
}}

/* ── Sidebar nav buttons ── */
[data-testid="stSidebar"] .stButton button {{
  background: transparent !important;
  border: none !important;
  border-left: 2px solid transparent !important;
  border-radius: 0 3px 3px 0 !important;
  text-align: left !important;
  padding: .5rem .85rem !important;
  color: {TXT_B} !important;
  font-weight: 400 !important;
  box-shadow: none !important;
  width: 100% !important;
  margin-bottom: .15rem !important;
  transition: background .15s, color .15s !important;
}}
[data-testid="stSidebar"] .stButton button:hover {{
  background: rgba(201,168,76,.06) !important;
  color: {TXT_H} !important;
  border-left-color: {GOLD_D} !important;
}}
[data-testid="stSidebar"] .stButton button[kind="primary"] {{
  background: rgba(201,168,76,.10) !important;
  border-left: 2px solid {GOLD} !important;
  color: {GOLD_S} !important;
  font-weight: 600 !important;
}}

/* ── Expanders ── */
details summary, .streamlit-expanderHeader {{
  font-family: 'Cinzel', serif !important;
  font-size: .68rem !important;
  letter-spacing: .12em !important;
  text-transform: uppercase !important;
  color: {TXT_B} !important;
}}

/* ── Info/alerts ── */
[data-testid="stNotification"] {{
  background: rgba(201,168,76,.05) !important;
  border-left: 3px solid {GOLD_D} !important;
}}
[data-testid="stNotification"] p {{ color: {TXT_B} !important; }}

/* ── Progress bars ── */
.stProgress > div > div {{
  background: rgba(255,255,255,.04) !important;
  border-radius: 2px !important;
}}
.stProgress > div > div > div > div {{
  background: linear-gradient(90deg, {GOLD_D}, {GOLD}) !important;
  border-radius: 2px !important;
}}

/* ── Tables ── */
[data-testid="stDataFrame"] td, [data-testid="stDataFrame"] th,
[data-testid="stTable"] td, [data-testid="stTable"] th {{
  color: {TXT_B} !important;
  font-size: .80rem !important;
}}
</style>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
page = st.session_state.page

PAGES = [
    ("Home",    "Ⅰ",  "Base Camp"),
    ("Story",   "Ⅱ",  "Chronicle"),
    ("Skills",  "Ⅲ",  "Vision"),
    ("Works",   "Ⅳ",  "Codex"),
    ("Connect", "Ⅴ",  "Summon"),
]

with st.sidebar:
    # ── Top seal ──────────────────────────────────────────────────────────
    st.markdown(
        f"""
        <div style="padding: 1.6rem 0 1.2rem; text-align: center; border-bottom: 1px solid {BORDER};">
          <div style="
            display: inline-flex; align-items: center; justify-content: center;
            width: 52px; height: 52px;
            background: linear-gradient(135deg, {PANEL2}, {PANEL3});
            border: 1.5px solid {GOLD_D};
            clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
            font-family: 'Cinzel Decorative', Cinzel, serif;
            font-size: .80rem; font-weight: 700;
            color: {GOLD}; letter-spacing: .04em;
          ">KM</div>
          <div style="
            margin-top: .9rem;
            font-family: 'Cinzel Decorative', Cinzel, serif;
            font-size: .85rem; letter-spacing: .18em;
            color: {TXT_H};
          ">KURT</div>
          <div style="
            font-family: 'JetBrains Mono', monospace;
            font-size: .56rem; letter-spacing: .14em;
            color: {TXT_M}; margin-top: .3rem; text-transform: uppercase;
          ">UI · PM · BSCS · Class 2028</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # ── Nav ───────────────────────────────────────────────────────────────
    for key, numeral, subtitle in PAGES:
        active = page == key
        # Build label with numeral + page name + subtitle, all in one button
        btn_label = f"{numeral}  {key}  ·  {subtitle}"
        st.button(
            btn_label,
            key=f"nav_{key}",
            use_container_width=True,
            on_click=go, args=(key,),
            type="primary" if active else "secondary",
            help=subtitle,
        )

    st.write("")
    st.divider()

    # ── Bio strip ─────────────────────────────────────────────────────────
    st.markdown(
        f"""
        <div style="
          font-family: 'JetBrains Mono', monospace;
          font-size: .60rem; color: {TXT_M};
          letter-spacing: .08em; line-height: 2;
        ">
          📍&nbsp; Cebu City, PH<br>
          🎓&nbsp; CIT-U · {PROGRAM} · {SECTION}<br>
          ✦&nbsp;&nbsp; Graduating 2028<br>
          🌟&nbsp; Open for Internship
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.divider()

    # ── Links ─────────────────────────────────────────────────────────────
    lc1, lc2, lc3 = st.columns(3)
    lc1.link_button("GH", GITHUB,           use_container_width=True, help="GitHub")
    lc2.link_button("IT", ITCH,             use_container_width=True, help="itch.io")
    lc3.link_button("✉",  f"mailto:{EMAIL}", use_container_width=True, help="Email")

    res = load_resume()
    if res:
        rb, rfn, rmt = res
        st.download_button("⬇  Résumé", rb, file_name=rfn, mime=rmt, use_container_width=True)

    st.write("")
    st.caption(COURSE)
    st.caption(INSTRUCTOR)

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def eyebrow(label: str) -> None:
    st.markdown(
        f"<div style='font-family:JetBrains Mono,monospace;font-size:.60rem;"
        f"letter-spacing:.18em;text-transform:uppercase;color:{TXT_M};"
        f"margin-bottom:.4rem;'>✦ &nbsp;{label}&nbsp; · &nbsp;{COURSE}</div>",
        unsafe_allow_html=True,
    )

def footer() -> None:
    st.divider()
    st.caption(
        f"✦  {FULL_NAME}  ·  Section {SECTION}  ·  {COURSE}  ·  {INSTRUCTOR}"
    )

def rule(text: str, color: str = GOLD_D) -> None:
    """Thin labelled horizontal rule."""
    st.markdown(
        f"<div style='display:flex;align-items:center;gap:.9rem;margin:1.5rem 0 .8rem;'>"
        f"<span style='font-family:Cinzel,serif;font-size:.60rem;letter-spacing:.22em;"
        f"text-transform:uppercase;color:{color};white-space:nowrap;'>{text}</span>"
        f"<div style='flex:1;height:1px;background:{BORDER};'></div>"
        f"</div>",
        unsafe_allow_html=True,
    )

def mono_tag(text: str, color: str = TXT_M) -> None:
    st.markdown(
        f"<span style='font-family:JetBrains Mono,monospace;font-size:.63rem;"
        f"letter-spacing:.12em;text-transform:uppercase;color:{color};'>{text}</span>",
        unsafe_allow_html=True,
    )

def pill_row(items: list[tuple[str, str]]) -> None:
    """Render colored pill badges inline."""
    pills = "".join(
        f"<span style='display:inline-block;margin:0 .3rem .35rem 0;"
        f"padding:.15rem .55rem;border:1px solid {c};border-radius:3px;"
        f"font-family:JetBrains Mono,monospace;font-size:.58rem;"
        f"letter-spacing:.10em;text-transform:uppercase;color:{c};'>{t}</span>"
        for t, c in items
    )
    st.markdown(
        f"<div style='line-height:2.2;margin:.3rem 0 .6rem;'>{pills}</div>",
        unsafe_allow_html=True,
    )

def stat_card(label: str, value: str, sub: str = "", color: str = GOLD) -> None:
    st.markdown(
        f"<div style='background:{PANEL};border:1px solid {BORDER};"
        f"border-top:2px solid {color};border-radius:4px;"
        f"padding:.85rem 1rem;'>"
        f"<div style='font-family:JetBrains Mono,monospace;font-size:.55rem;"
        f"letter-spacing:.18em;text-transform:uppercase;color:{TXT_M};"
        f"margin-bottom:.35rem;'>{label}</div>"
        f"<div style='font-family:Cinzel,serif;font-size:1.35rem;"
        f"font-weight:700;color:{color};line-height:1.2;'>{value}</div>"
        f"{'<div style=\"font-family:JetBrains Mono,monospace;font-size:.60rem;color:' + TXT_M + ';margin-top:.25rem;letter-spacing:.06em;\">' + sub + '</div>' if sub else ''}"
        f"</div>",
        unsafe_allow_html=True,
    )

def vision_panel(category: str, skills: list[tuple[str, int]]) -> None:
    color, ename, icon = EL.get(category, (GOLD, category, "◆"))
    with st.container(border=True):
        # Header
        st.markdown(
            f"<div style='display:flex;align-items:flex-start;gap:.65rem;margin-bottom:.7rem;'>"
            f"<div style='font-size:1.45rem;line-height:1;margin-top:.1rem;'>{icon}</div>"
            f"<div>"
            f"<div style='font-family:Cinzel,serif;font-size:.65rem;letter-spacing:.22em;"
            f"text-transform:uppercase;color:{color};'>{ename}</div>"
            f"<div style='font-family:JetBrains Mono,monospace;font-size:.57rem;"
            f"color:{TXT_M};letter-spacing:.08em;margin-top:.1rem;'>{category}</div>"
            f"</div></div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='height:1px;background:linear-gradient(90deg,{color}44,transparent);"
            f"margin-bottom:.75rem;'></div>",
            unsafe_allow_html=True,
        )
        # Skills
        for name, score in sorted(skills, key=lambda x: -x[1]):
            filled = int(score / 10)
            empty  = 10 - filled
            dots   = (
                f"<span style='color:{color};opacity:.85;'>{'◆' * filled}</span>"
                f"<span style='color:{TXT_M};opacity:.35;'>{'◇' * empty}</span>"
            )
            st.markdown(
                f"<div style='display:flex;align-items:center;justify-content:space-between;"
                f"margin-bottom:.55rem;'>"
                f"<div style='font-size:.82rem;color:{TXT_B};'>{name}</div>"
                f"<div style='display:flex;align-items:center;gap:.5rem;'>"
                f"<div style='font-family:JetBrains Mono,monospace;font-size:.60rem;"
                f"letter-spacing:.04em;'>{dots}</div>"
                f"<span style='font-family:JetBrains Mono,monospace;font-size:.68rem;"
                f"color:{color};font-weight:600;min-width:24px;text-align:right;'>{score}</span>"
                f"</div></div>",
                unsafe_allow_html=True,
            )

# ─────────────────────────────────────────────────────────────────────────────
# PAGE — HOME
# ─────────────────────────────────────────────────────────────────────────────

def page_home() -> None:
    eyebrow("Portfolio · Base Camp")
    st.write("")

    # ── Hero ─────────────────────────────────────────────────────────────
    hero_l, hero_r = st.columns([5, 3], gap="large")

    with hero_l:
        st.markdown(
            f"<div style='font-family:JetBrains Mono,monospace;font-size:.58rem;"
            f"letter-spacing:.24em;text-transform:uppercase;color:{TXT_M};"
            f"margin-bottom:.55rem;'>CIT-U  ·  Cebu City  ·  Class of 2028</div>",
            unsafe_allow_html=True,
        )
        st.title("Kurt Justin J. Malubay")
        st.markdown(
            f"<div style='font-family:Cinzel,serif;font-size:.78rem;letter-spacing:.16em;"
            f"text-transform:uppercase;color:{GOLD_D};margin:.15rem 0 1.2rem;'>"
            f"UI / UX &nbsp;·&nbsp; Project Management &nbsp;·&nbsp; Game Dev</div>",
            unsafe_allow_html=True,
        )
        st.markdown("> *\"Curiosity builds the engineer.\"*")
        st.write("")
        st.write(
            "Third-year BS Computer Science student at CIT-U. "
            "I came into computer science through a question a Blackberry phone once raised. "
            "That question turned into game development, interface design, and the "
            "coordination work that holds projects together."
        )
        st.write(
            "Right now I'm leading the UI/UX and project management side of **Infinitus** "
            "alongside two teammates, while finishing the degree and staying "
            "open to what comes after 2028."
        )
        st.write("")

        ba, bb, bc = st.columns(3)
        ba.button("⚔  Works",       key="hero_works",   on_click=go, args=("Works",),   use_container_width=True)
        bb.link_button("⌥  GitHub", GITHUB,             use_container_width=True)
        bc.link_button("✉  Contact", f"mailto:{EMAIL}", use_container_width=True)

    with hero_r:
        show_img("profile.jpg", f"{FULL_NAME} · BSCS 3 · CIT-U")

    # ── Stats strip ──────────────────────────────────────────────────────
    st.divider()
    s1, s2, s3, s4 = st.columns(4)
    with s1: stat_card("Degree",      "BSCS",  "Computer Science")
    with s2: stat_card("University",  "CIT-U", "Cebu Institute of Tech", GOLD)
    with s3: stat_card("Year",        "3rd",   "Section F1", EL["Web"][0])
    with s4: stat_card("Graduating",  "2028",  "BS Comp. Science", EL["Anemo"][0])

    # ── Roles ─────────────────────────────────────────────────────────────
    rule("What I Bring")
    r1, r2, r3 = st.columns(3, gap="medium")

    with r1:
        with st.container(border=True):
            st.markdown(
                f"<div style='font-family:JetBrains Mono,monospace;font-size:.58rem;"
                f"letter-spacing:.16em;text-transform:uppercase;color:{EL['Web'][0]};"
                f"margin-bottom:.5rem;'>🎨 &nbsp;UI / UX Design</div>",
                unsafe_allow_html=True,
            )
            st.markdown("#### Interface Architecture")
            st.write(
                "Menus, HUDs, and interaction flows built to feel intentional. "
                "I design for the layer players actually see, not just the layer "
                "developers build."
            )

    with r2:
        with st.container(border=True):
            st.markdown(
                f"<div style='font-family:JetBrains Mono,monospace;font-size:.58rem;"
                f"letter-spacing:.16em;text-transform:uppercase;color:{EL['Anemo'][0]};"
                f"margin-bottom:.5rem;'>🌀 &nbsp;Project Management</div>",
                unsafe_allow_html=True,
            )
            st.markdown("#### Coordination & Structure")
            st.write(
                "Milestone breakdowns, sprint planning, and surfacing blockers "
                "before they compound. The invisible structure that lets "
                "creative work happen on time."
            )

    with r3:
        with st.container(border=True):
            st.markdown(
                f"<div style='font-family:JetBrains Mono,monospace;font-size:.58rem;"
                f"letter-spacing:.16em;text-transform:uppercase;color:{EL['AI / Tooling'][0]};"
                f"margin-bottom:.5rem;'>⚡ &nbsp;AI Tooling</div>",
                unsafe_allow_html=True,
            )
            st.markdown("#### Prompt Engineering")
            st.write(
                "Applying AI deliberately — knowing what questions to ask, "
                "when to let it generate, and when to just write the thing yourself."
            )

    # ── Project snapshot ──────────────────────────────────────────────────
    rule("Project Snapshot")
    p1, p2 = st.columns(2, gap="medium")

    with p1:
        with st.container(border=True):
            show_img("infinitus.jpg", "")
            st.write("")
            mono_tag("Active  ·  Team Project", EL["Game Dev"][0])
            st.markdown("#### Infinitus")
            st.write(
                "Multiplayer battle royale in active development. "
                "My role covers all UI/UX design and project management "
                "for the three-person team."
            )
            st.button("Explore →", key="snap_inf", on_click=go, args=("Works",), use_container_width=True)

    with p2:
        with st.container(border=True):
            show_img("tlgms.png", "")
            st.write("")
            mono_tag("Complete  ·  Solo  ·  Unity", EL["Language"][0])
            st.markdown("#### TLGMS")
            st.write(
                "First solo game, built entirely in Unity. "
                "100% self-directed from concept to shipped build — "
                "the project that confirmed the direction."
            )
            st.button("Explore →", key="snap_tlg", on_click=go, args=("Works",), use_container_width=True)

    st.write("")
    st.info(
        "Open for internship — UI/UX design, project coordination, or applied AI roles. "
        "Graduating 2028.",
        icon="🌟",
    )
    footer()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE — STORY
# ─────────────────────────────────────────────────────────────────────────────

def page_story() -> None:
    eyebrow("Chronicle · My Story")
    st.write("")
    st.title("The Story So Far")
    st.write(
        "*From Southern Leyte to CIT-U — no roadmap, no mentor. "
        "Just the next question and the patience to follow it.*"
    )
    st.divider()

    narrative, timeline = st.columns([3, 2], gap="large")

    # ── Left narrative ────────────────────────────────────────────────────
    with narrative:
        rule("Roots")
        st.write(
            "I grew up in San Juan, Southern Leyte — a province town where sea "
            "and mountain were the closest things to the internet. "
            "Curious kids with no mentor and no YouTube channel for everything "
            "learn one skill fast: how to find the next question. "
            "That habit became the engine."
        )

        rule("The Pivot")
        st.write(
            "My mother brought home a Blackberry phone. I loaded Assassin's Creed "
            "on it. The game was good — but the thought sitting underneath it was louder: "
            "*how does this exist?*"
        )
        st.write(
            "That question carried me through elementary, junior high, and senior high "
            "with no formal guidance. No CS club, no programming teacher, no roadmap. "
            "Just the question and whatever I could find on a slow connection."
        )

        rule("University")
        st.write(
            "University entrance exams came, and I passed at several state schools. "
            "Most had interviews — shyness cost me a few of those. "
            "CIT-U was always the target anyway. "
            "The computer science program ran competitive in exactly the right direction, "
            "and game development was already where I was headed."
        )
        st.write(
            "Three years in, the fundamentals hit harder than I expected — "
            "DSA, DAA, systems thinking, algorithm analysis. I'm glad they did. "
            "Knowing what's expensive to compute makes you ask better questions "
            "about what's worth building at all."
        )

        rule("Now")
        st.write(
            "Most hours go to **Infinitus** — a multiplayer battle royale with "
            "two teammates. My side of the table: all UI/UX design and project management. "
            "Every interface the player touches, and every sprint that keeps us on track."
        )
        st.write(
            "Outside the team project, I study interfaces seriously. "
            "Games like Genshin Impact are research as much as entertainment — "
            "every transition, every feedback loop, every HUD decision is a design "
            "problem somebody already solved."
        )

        with st.expander("What I actually do outside of code"):
            st.write(
                "Genshin Impact, Assassin's Creed, anything with a UI worth dissecting. "
                "At some point gaming became a form of field research. "
                "Every game screen is a design decision I can learn from — "
                "and occasionally steal from."
            )

    # ── Right timeline ────────────────────────────────────────────────────
    with timeline:
        rule("Chronicle")

        milestones = [
            ("Elementary",    "San Juan, Southern Leyte",
             "Province life. First questions about how devices work."),
            ("Jr / Sr High",  "Self-study solidifies",
             "No syllabus. Research, experiments, the next question."),
            ("Entrance Exams","Multiple state exams passed",
             "Shyness cost a few interviews. CIT-U was always the plan."),
            ("Year 1 — CIT-U","TLGMS",
             "First solo game shipped in Unity. Proved I could finish something."),
            ("Year 2 — CIT-U","Interface focus",
             "Started studying UI/UX design seriously alongside the degree."),
            ("Year 3 — CIT-U","Infinitus · UI/UX Lead & PM",
             "Joined the team. Owns all design and coordination."),
            ("2028",          "Target: Graduate",
             "BS Computer Science — then the first professional role.", True),
        ]

        for entry in milestones:
            year, title, note = entry[0], entry[1], entry[2]
            future     = len(entry) > 3 and entry[3]
            dot_color  = TXT_M if future else GOLD
            bar_color  = BORDER if future else GOLD_D
            txt_opacity = "opacity:.45;" if future else ""

            st.markdown(
                f"<div style='display:flex;gap:.9rem;margin-bottom:1rem;'>"
                f"<div style='display:flex;flex-direction:column;align-items:center;"
                f"padding-top:.28rem;'>"
                f"<div style='width:7px;height:7px;background:{dot_color};"
                f"clip-path:polygon(50% 0%,100% 50%,50% 100%,0% 50%);"
                f"flex-shrink:0;{txt_opacity}'></div>"
                f"<div style='flex:1;width:1px;background:{bar_color};"
                f"margin-top:.3rem;min-height:28px;opacity:.4;'></div>"
                f"</div>"
                f"<div style='{txt_opacity}'>"
                f"<div style='font-family:JetBrains Mono,monospace;font-size:.57rem;"
                f"letter-spacing:.14em;text-transform:uppercase;color:{dot_color};"
                f"margin-bottom:.1rem;'>{year}</div>"
                f"<div style='font-size:.85rem;font-weight:600;color:{TXT_H};"
                f"margin-bottom:.15rem;'>{title}</div>"
                f"<div style='font-size:.80rem;color:{TXT_B};line-height:1.62;'>{note}</div>"
                f"</div></div>",
                unsafe_allow_html=True,
            )

        st.write("")
        rule("At a Glance")
        glance = {
            "Hometown":   "San Juan, Southern Leyte",
            "Based":      "Cebu City",
            "Program":    "BS Computer Science",
            "University": "CIT-U",
            "Graduating": "2028",
            "Languages":  "English · Filipino · Bisaya",
        }
        for k, v in glance.items():
            st.markdown(
                f"<div style='display:flex;gap:.6rem;justify-content:space-between;"
                f"margin-bottom:.4rem;padding-bottom:.4rem;"
                f"border-bottom:1px solid {BORDER};'>"
                f"<span style='font-family:JetBrains Mono,monospace;font-size:.60rem;"
                f"letter-spacing:.10em;text-transform:uppercase;color:{TXT_M};'>{k}</span>"
                f"<span style='font-size:.82rem;color:{TXT_H};text-align:right;'>{v}</span>"
                f"</div>",
                unsafe_allow_html=True,
            )

        st.write("")
        st.info(f"Section {SECTION}  ·  {INSTRUCTOR}", icon="📌")

    footer()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE — SKILLS
# ─────────────────────────────────────────────────────────────────────────────

def page_skills() -> None:
    eyebrow("Vision · Skills")
    st.write("")
    st.title("Skills")
    st.markdown(
        "> *Each category maps to a Genshin Vision element — its domain. "
        "Scores are self-assessed and honest: 90 means I reach for it without thinking; "
        "70 means the documentation is open in another tab.*"
    )
    st.divider()

    # ── Vision panels ─────────────────────────────────────────────────────
    skill_df  = pd.DataFrame(SKILLS, columns=["Skill", "Score", "Category"])
    cats      = list(dict.fromkeys(r["Category"] for _, r in skill_df.iterrows()))

    for i in range(0, len(cats), 2):
        pair = cats[i: i + 2]
        cols = st.columns(len(pair), gap="medium")
        for col, cat in zip(cols, pair):
            with col:
                rows = [
                    (r["Skill"], r["Score"])
                    for _, r in skill_df[skill_df["Category"] == cat].iterrows()
                ]
                vision_panel(cat, rows)
        st.write("")

    # ── Affinity chart ────────────────────────────────────────────────────
    rule("Element Affinity Chart")
    st.caption("Average proficiency per Vision domain")
    st.write("")

    avg = (
        skill_df
        .groupby("Category", as_index=False)["Score"]
        .mean()
        .round(1)
    )
    avg["Element"] = avg["Category"].map(lambda c: EL.get(c, (GOLD, c, ""))[1])
    avg["Icon"]    = avg["Category"].map(lambda c: EL.get(c, (GOLD, c, ""))[2])
    avg["Color"]   = avg["Category"].map(lambda c: EL.get(c, (GOLD, c, ""))[0])
    avg["Label"]   = avg["Element"] + " " + avg["Icon"]
    avg = avg.sort_values("Score", ascending=False)

    chart = (
        alt.Chart(avg)
        .mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3, size=44)
        .encode(
            x=alt.X(
                "Label:N",
                sort=avg["Label"].tolist(),
                axis=alt.Axis(
                    labelFont="JetBrains Mono", labelColor=TXT_B,
                    labelFontSize=11, labelAngle=0, title=None,
                    tickColor=BORDER, domainColor=BORDER,
                ),
            ),
            y=alt.Y(
                "Score:Q",
                scale=alt.Scale(domain=[0, 100]),
                axis=alt.Axis(
                    labelFont="JetBrains Mono", labelColor=TXT_M,
                    labelFontSize=10, gridColor=BORDER,
                    domainColor=BORDER, title=None,
                ),
            ),
            color=alt.Color("Color:N", scale=None, legend=None),
            tooltip=[
                alt.Tooltip("Element:N",  title="Vision"),
                alt.Tooltip("Category:N", title="Domain"),
                alt.Tooltip("Score:Q",    title="Avg", format=".1f"),
            ],
        )
        .properties(height=240, background=PANEL)
        .configure_view(strokeWidth=0)
    )
    st.altair_chart(chart, use_container_width=True)

    # ── Philosophy ────────────────────────────────────────────────────────
    rule("Approach")
    st.write("")
    a1, a2 = st.columns(2, gap="medium")

    with a1:
        with st.container(border=True):
            mono_tag("Study the interface, not just the code", EL["Web"][0])
            st.write("")
            st.markdown("#### Design instinct over syntax recall")
            st.write(
                "My strongest pull is toward the user-facing layer — why a design "
                "decision was made, not only what it looks like. "
                "Game UIs are the best teacher for this: every pixel is deliberate."
            )

    with a2:
        with st.container(border=True):
            mono_tag("Keep the team in motion", EL["Anemo"][0])
            st.write("")
            st.markdown("#### Coordination as a skill")
            st.write(
                "On Infinitus I hold the structure together — tasks broken down, "
                "priorities visible, blockers surfaced early. "
                "Good coordination is what makes the design work possible."
            )

    footer()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE — WORKS
# ─────────────────────────────────────────────────────────────────────────────

def page_works() -> None:
    eyebrow("Codex · Works")
    st.write("")
    st.title("Works")
    st.write(
        "*Two projects. One is an active team effort I help lead. "
        "The other I built alone, start to finish.*"
    )
    st.divider()

    # ── Tab navigation ────────────────────────────────────────────────────
    tab_inf, tab_tlg = st.tabs(["  Infinitus  ", "  TLGMS  "])

    # ── INFINITUS tab ─────────────────────────────────────────────────────
    with tab_inf:
        st.write("")
        img_col, desc_col = st.columns([1, 1], gap="large")

        with img_col:
            show_img("infinitus.jpg", "Infinitus — battle royale")
            st.write("")
            pill_row([
                ("Active",       EL["Game Dev"][0]),
                ("Team · 3 pax", EL["Web"][0]),
                ("UI/UX · PM",   EL["Anemo"][0]),
            ])
            st.write("")
            mono_tag("Tech stack", TXT_M)
            pill_row([
                ("C#",    TXT_B),
                ("Figma", TXT_B),
                ("Git",   TXT_B),
            ])

        with desc_col:
            st.markdown("## Infinitus")
            st.write(
                "A top-down multiplayer battle royale in active development. "
                "The game is programmed by Glenshayne Belarmino and Wilmark Racho — "
                "I joined the team to own the UI/UX and project management layer: "
                "everything the player sees and everything that keeps the team on schedule."
            )

            rule("My Responsibilities")

            resp_a, resp_b = st.columns(2, gap="medium")
            with resp_a:
                with st.container(border=True):
                    mono_tag("🎨  UI / UX Design", EL["Web"][0])
                    st.write("")
                    st.write(
                        "Full in-game interface design: main menus, HUD layout, "
                        "overlay systems, feedback animations. "
                        "The visual language of the game from the player's side."
                    )
            with resp_b:
                with st.container(border=True):
                    mono_tag("🌀  Project Management", EL["Anemo"][0])
                    st.write("")
                    st.write(
                        "Sprint planning, task breakdown, milestone tracking. "
                        "Keeping three people aligned and surfacing blockers "
                        "before they become delays."
                    )

            rule("Team")
            t1, t2, t3 = st.columns(3)
            t1.metric("Kurt M.",        "UI/UX · PM",   "Design + Coordination")
            t2.metric("Glenshayne B.",  "Programmer",   "Core systems")
            t3.metric("Wilmark R.",     "Programmer",   "Game logic")

            st.write("")
            st.link_button("⌥  View on GitHub", GITHUB, use_container_width=True)

    # ── TLGMS tab ─────────────────────────────────────────────────────────
    with tab_tlg:
        st.write("")
        desc_col, img_col = st.columns([1, 1], gap="large")

        with desc_col:
            st.markdown("## TLGMS")
            st.write(
                "My first game — built entirely alone. TLGMS was never about shipping "
                "a polished commercial product. It was about proving that I could take "
                "something from concept all the way to a playable build by myself. "
                "Every decision, every line of code, every asset: mine."
            )

            rule("Role & Contribution")
            with st.container(border=True):
                mono_tag("◇  Solo Developer  ·  100% Contribution", EL["Language"][0])
                st.write("")
                kv_pairs = [
                    ("Engine",   "Unity"),
                    ("Language", "C#"),
                    ("Design",   "Concept, mechanics, UX flow — self-directed"),
                    ("Art",      "All game assets created from scratch"),
                    ("Outcome",  "Shipped a playable build"),
                ]
                for k, v in kv_pairs:
                    st.markdown(
                        f"<div style='display:flex;gap:.8rem;margin-bottom:.4rem;"
                        f"padding-bottom:.4rem;border-bottom:1px solid {BORDER};'>"
                        f"<span style='font-family:JetBrains Mono,monospace;font-size:.60rem;"
                        f"letter-spacing:.10em;text-transform:uppercase;color:{TXT_M};"
                        f"min-width:64px;'>{k}</span>"
                        f"<span style='font-size:.82rem;color:{TXT_H};'>{v}</span>"
                        f"</div>",
                        unsafe_allow_html=True,
                    )

            rule("What It Proved")
            st.write(
                "You can ship a game alone. You can learn an engine from documentation. "
                "Curiosity is enough to start — discipline is what finishes it. "
                "TLGMS turned game development from an interest into a commitment."
            )

            st.write("")
            st.link_button("🎮  Play on itch.io", ITCH, use_container_width=True)

        with img_col:
            show_img("tlgms.png", "TLGMS — solo Unity project")
            st.write("")
            pill_row([
                ("Complete",    EL["Language"][0]),
                ("Solo",        EL["Language"][0]),
                ("Unity",       EL["Game Dev"][0]),
                ("100%",        GOLD),
            ])

    # ── Availability ──────────────────────────────────────────────────────
    st.divider()
    rule("Open Field")
    av1, av2 = st.columns(2, gap="medium")

    with av1:
        with st.container(border=True):
            mono_tag("🌟  Open for Internship", GOLD)
            st.write("")
            st.markdown("#### Seeking a real problem to work on")
            st.write(
                "UI/UX design, product work, or any role where coordination "
                "and design overlap. I learn fast when the stakes are real."
            )
            st.link_button("✉  Reach out", f"mailto:{EMAIL}", use_container_width=True)

    with av2:
        with st.container(border=True):
            mono_tag("⚔  Game Jams", EL["Game Dev"][0])
            st.write("")
            st.markdown("#### Teams that plan to finish")
            st.write(
                "Open to jam teams that commit to shipping. "
                "I bring design thinking, project structure, and the "
                "drive to get something playable before the deadline."
            )
            st.link_button("🎮  itch.io", ITCH, use_container_width=True)

    footer()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE — CONNECT
# ─────────────────────────────────────────────────────────────────────────────

def page_connect() -> None:
    eyebrow("Summon · Connect")
    st.write("")
    st.title("Connect")
    st.write(
        "*Internship, collab, jam, or just a message — all worth reaching out about.*"
    )
    st.divider()

    left_col, right_col = st.columns([1, 1.6], gap="large")

    # ── Left: channels ────────────────────────────────────────────────────
    with left_col:
        rule("Direct Channels")
        st.write("")

        channels = [
            ("✉  Email",     EMAIL,              f"mailto:{EMAIL}",  "Primary · fastest reply",    GOLD),
            ("◇  GitHub",    "KurtJustinMalubay", GITHUB,            "Source code & projects",      EL["Language"][0]),
            ("🎮  itch.io",  "sashimiproductions", ITCH,             "Published games",             EL["Game Dev"][0]),
        ]
        for label, handle, url, note, color in channels:
            st.markdown(
                f"<div style='background:{PANEL};border:1px solid {BORDER};"
                f"border-left:3px solid {color};border-radius:4px;"
                f"padding:.85rem 1rem;margin-bottom:.7rem;'>"
                f"<div style='font-family:Cinzel,serif;font-size:.68rem;"
                f"letter-spacing:.16em;text-transform:uppercase;color:{color};"
                f"margin-bottom:.25rem;'>{label}</div>"
                f"<div style='font-family:JetBrains Mono,monospace;font-size:.72rem;"
                f"color:{TXT_H};margin-bottom:.2rem;'>{handle}</div>"
                f"<div style='font-family:JetBrains Mono,monospace;font-size:.58rem;"
                f"color:{TXT_M};letter-spacing:.06em;'>{note}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )
            st.link_button(f"Open {label.split()[1]} →", url, use_container_width=True)
            st.write("")

        res = load_resume()
        if res:
            rb, rfn, rmt = res
            st.download_button(
                "⬇  Download Résumé", rb,
                file_name=rfn, mime=rmt,
                use_container_width=True,
            )

        st.divider()
        rule("What I'm Looking For")
        with st.container(border=True):
            st.write(
                "An internship where UI/UX design, project coordination, or applied "
                "AI work is the actual role — not a footnote. "
                "Real problems, experienced teammates. "
                "Graduating 2028; available now for part-time or remote work."
            )
        st.write("")
        st.caption("Response time  ·  within 24 hours")
        st.caption("Best topic opener  ·  Genshin Impact or game design")

    # ── Right: form ───────────────────────────────────────────────────────
    with right_col:
        rule("Send a Message")
        st.write("")

        with st.container(border=True):
            with st.form("contact_form", clear_on_submit=True):
                name_field = st.text_input(
                    "Your name",
                    placeholder="Who's reaching out?",
                )
                reason_field = st.selectbox(
                    "Purpose",
                    options=[
                        "💼  Internship / work opportunity",
                        "⚔  Game jam or collaboration",
                        "🎨  Design or UI feedback",
                        "💬  General question",
                        "👋  Just saying hello",
                    ],
                )
                msg_field = st.text_area(
                    "Message",
                    placeholder=(
                        "What are you building? What do you need? "
                        "What caught your eye?"
                    ),
                    height=150,
                )
                email_field = st.text_input(
                    "Your email  (optional — only if you want a reply)",
                    placeholder="you@example.com",
                )
                submitted = st.form_submit_button(
                    "Send  ✦", use_container_width=True, type="primary"
                )

        if submitted:
            errors = []
            if not name_field.strip():
                errors.append("A name would help me address my reply.")
            if not msg_field.strip():
                errors.append("The message is empty.")
            for err in errors:
                st.warning(err, icon="⚠️")
            if not errors:
                st.session_state.setdefault("msgs", []).append({
                    "name":    name_field.strip(),
                    "reason":  reason_field,
                    "message": msg_field.strip(),
                    "email":   email_field.strip() or "—",
                    "at":      datetime.now().strftime("%H:%M · %d %b"),
                })
                st.success(
                    f"Received, {name_field.strip()}. "
                    "Messages are stored in this session only — "
                    "use a direct channel on the left for a guaranteed reply.",
                    icon="📨",
                )

        # ── Session log ───────────────────────────────────────────────
        log = st.session_state.get("msgs", [])
        if log:
            rule("Message Log  ·  Session Only")
            for entry in reversed(log):
                with st.container(border=True):
                    top, ts = st.columns([5, 2])
                    top.markdown(f"**{entry['name']}**")
                    ts.caption(entry["at"])
                    st.caption(entry["reason"])
                    st.write(entry["message"])
                    if entry["email"] != "—":
                        st.caption(f"Reply to: {entry['email']}")
            st.write("")
            if st.button("Clear log", key="clear_log"):
                st.session_state["msgs"] = []
                st.rerun()

    footer()

# ─────────────────────────────────────────────────────────────────────────────
# ROUTER
# ─────────────────────────────────────────────────────────────────────────────
if   page == "Home":    page_home()
elif page == "Story":   page_story()
elif page == "Skills":  page_skills()
elif page == "Works":   page_works()
else:                   page_connect()
