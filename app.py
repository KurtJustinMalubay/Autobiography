"""
Kurt Justin J. Malubay | Autobiography & Portfolio
CSIT 349 - Applied AI | Streamlit app

Run with:  streamlit run app.py

Expected structure:
root/
  assets/  (profile.jpg, infinitus.jpg, tlgms.jpg, devvault.jpg)
  app.py
  requirements.txt
"""

from pathlib import Path
from urllib.parse import quote

import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# 1. PAGE CONFIG (must be the first Streamlit call)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Kurt Justin J. Malubay | Portfolio",
    page_icon="⚔️",
    layout="wide",
)

# Session state for routing
if "page" not in st.session_state:
    st.session_state.page = "Home"

ASSETS = Path(__file__).parent / "assets"

# ---------------------------------------------------------------------------
# 2. DATA
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Kurt Justin J. Malubay",
    "nickname": "Kurt",
    "initials": "KJ",
    "program": "BSCS 3 - F1",
    "grad": "2028",
    "status": "CHED Merit Scholar",
    "email": "justinkurt837@gmail.com",
    "phone": "09928330407",
    "github": "https://github.com/KurtJustinMalubay",
    "itch": "https://sashimiproductions.itch.io/",
}

SKILLS = pd.DataFrame(
    {
        "Skill": ["C#", "C++", "C", "Python", "HTML", "CSS", "React", "TypeScript", "Tailwind CSS"],
        "Proficiency": [78, 75, 70, 50, 70, 70, 60, 60, 60],
        "Category": [
            "Game Dev",
            "Systems / Algorithms",
            "Systems / Fundamentals",
            "Web / AI (newly started)",
            "Web Development",
            "Web Development",
            "Web Development",
            "Web Development",
            "Web Development",
        ],
    }
)

TOOLS = {
    "Engines": ["Godot 4", "Unity"],
    "Art & Design": ["Blender", "Figma", "Aseprite"],
    "Backend & Data": ["Django", "Supabase", "MySQL"],
}

PROJECTS = [
    {
        "name": "Infinitus",
        "tag": "INF",
        "image": "infinitus.jpg",
        "role": "Project Manager, Environment Artist, Model Designer, Skill Effects Designer, UI/UX Designer, Sound Designer",
        "collaborators": "Glenshayne Belarmino, Wilmark Racho",
        "description": "A multiplayer wizard battle game where players cast spells and navigate a meticulously crafted environment.",
        "stack": ["Godot 4", "C#", "Blender", "Figma"],
        "outcome": "Shipped prototype framework.",
    },
    {
        "name": "TLGMS (The Last Glensh Man Standing)",
        "tag": "TLG",
        "image": "tlgms.jpg",
        "role": "Sole Developer / Creator",
        "collaborators": "None (solo project)",
        "description": "A survival shooting game set on Earth 122 as the last surviving member of the Glensh species.",
        "stack": ["Unity", "C#", "Aseprite"],
        "outcome": "First completed solo game development project.",
    },
    {
        "name": "DevVault",
        "tag": "DVT",
        "image": "devvault.jpg",
        "role": "Lead Developer / Architect",
        "collaborators": "None listed",
        "description": (
            "A game development knowledge and asset management web application built for "
            "organizing technical documentation and reusable code snippets."
        ),
        "stack": ["Python Django", "Supabase", "MySQL"],
        "outcome": "Active internal tool for workflow efficiency.",
    },
]

CHAPTERS = [
    {
        "title": "Childhood & Background",
        "period": "Until 2018",
        "body": (
            "I grew up in <b>San Juan, Southern Leyte</b>, a town where the sea meets the mountains. "
            "The province was an important part of my childhood: the sea and mountains were part of everyday life, "
            "and I often found myself observing how things worked around me. I was curious about the patterns "
            "behind nature, daily routines, and the devices people used. One of my earliest technology memories "
            "is playing <b>Assassin's Creed</b> on my mother's <b>BlackBerry</b>. Even then, I wondered how a small "
            "phone could bring a game world to life. That childhood question stayed with me and grew into a deeper "
            "interest in technology. I attended <b>San Juan Central Elementary School</b> until 2018."
        ),
    },
    {
        "title": "The Spark of Curiosity",
        "period": "2018 - 2024",
        "body": (
            "As I grew older, the question that began in childhood—how technology and game worlds are made—" 
            "continued to follow me. I kept learning through curiosity, research, and experimenting with what "
            "I could access, gradually turning that early interest into a more focused passion for computers "
            "and game development. At <b>San Juan National High School</b>, where I studied until 2024, I pursued "
            "a background in <b>Media Arts and STEM</b>. That combination helped me appreciate both the creative "
            "side of making things and the logical thinking needed to understand how they work."
        ),
    },
    {
        "title": "Education & Transition to College",
        "period": "2024",
        "body": (
            "I went through public schools from elementary through senior high school, building my education "
            "step by step in the community where I grew up. After completing high school and passing multiple "
            "university entrance exams, I chose <b>Cebu Institute of Technology – University (CIT-U)</b>. Its "
            "challenging Computer Science program felt like the right place to turn my long-standing curiosity "
            "about technology into practical knowledge and stronger development skills. Moving from Southern "
            "Leyte to Cebu also marked an important transition as I began this next stage of my education."
        ),
    },
    {
        "title": "Current Life & Outlook",
        "period": "Present",
        "body": (
            "Today I am a <b>3rd-year Computer Science student</b> at CIT-U and a <b>CHED Merit Scholar</b>. "
            "Outside my studies, I work as an independent developer and collaborate with peers on game and "
            "software projects, taking part in both the technical and creative work. Each project gives me a "
            "chance to practice what I learn, explore unfamiliar tools, and improve how I approach problems. "
            "I want to keep growing as a developer and build things that are thoughtfully designed, efficient, "
            "and enjoyable to use."
        ),
    },
]

INTERNSHIP_TEXT = (
    "Actively seeking internship opportunities where I can apply my foundational computer science "
    "background, game development experience, and passion for optimised software engineering. "
    "Eager to learn from industry mentors, tackle complex engineering challenges, and contribute "
    "meaningfully to innovative tech and gaming teams."
)

# ---------------------------------------------------------------------------
# 3. STYLING
# ---------------------------------------------------------------------------
CSS = """
<style>
:root {
    --bg: #0d1117;
    --surface: #161b22;
    --surface-2: #12181f;
    --gold: #e8d5a3;
    --muted: #8b949e;
    --text: #c9d1d9;
    --border: #30363d;
    color-scheme: dark;
}

html, body, .stApp {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
/* Preserve Streamlit's ligature font so sidebar controls show icons, not names. */
.material-symbols-rounded,
.material-symbols-outlined,
span[data-testid="stIconMaterial"] {
    font-family: "Material Symbols Rounded" !important;
    font-weight: normal !important;
    font-style: normal !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
    -webkit-font-feature-settings: "liga";
    -webkit-font-smoothing: antialiased;
}
.stApp { background-color: var(--bg); }
[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 2.5rem; max-width: 1200px; }

.stApp p, .stApp li, .stApp label, .stApp [data-testid="stCaptionContainer"] { color: var(--text); }
.stApp [data-testid="stCaptionContainer"] { color: var(--muted); }
h1, h2, h3, h4 { color: var(--gold) !important; letter-spacing: 0.2px; font-weight: 700 !important; }
h1 { font-size: 2.6rem !important; }
a { color: var(--gold) !important; text-decoration: none; }
a:hover { text-decoration: underline; }
.muted { color: var(--muted) !important; }
hr { border-color: var(--border) !important; }

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: var(--surface-2);
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] .block-container, [data-testid="stSidebarContent"] { padding-top: 1.5rem; }
/* Keep Streamlit's sidebar toggle visible against the dark header/sidebar. */
[data-testid="stSidebarCollapseButton"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    color: var(--text) !important;
    opacity: 1 !important;
    visibility: visible !important;
}
[data-testid="stSidebarCollapseButton"] svg,
[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="collapsedControl"] svg {
    color: var(--text) !important;
    fill: var(--text) !important;
    opacity: 1 !important;
}
.brand { display: flex; align-items: center; gap: 0.9rem; margin-bottom: 0.4rem; }
.avatar {
    width: 52px; height: 52px; border-radius: 12px; flex: 0 0 52px;
    background: var(--gold); color: #0d1117;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 1.15rem; letter-spacing: 1px;
}
.brand .bn { color: var(--gold); font-weight: 700; line-height: 1.2; }
.brand .bs { color: var(--muted); font-size: 0.8rem; }
.nav-label { color: var(--muted); font-size: 0.72rem; letter-spacing: 2px; text-transform: uppercase; margin: 0.6rem 0 0.4rem 0; }
.side-links a { display: block; padding: 0.15rem 0; font-size: 0.88rem; }
.side-links span { color: var(--muted); font-size: 0.88rem; display: block; padding: 0.15rem 0; }

/* Typography helpers */
.eyebrow { color: var(--muted); text-transform: uppercase; letter-spacing: 3px; font-size: 0.78rem; margin-bottom: 0.2rem; }
.lead { color: var(--text); font-size: 1.1rem; margin: 0.2rem 0 0.8rem 0; }

/* Equal-height grids: every card in a row stretches to the tallest card */
.grid { display: grid; gap: 1rem; align-items: stretch; margin-bottom: 1rem; }
.grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
@media (max-width: 900px) {
    .grid-3, .grid-4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 600px) {
    .grid-2, .grid-3, .grid-4 { grid-template-columns: minmax(0, 1fr); }
}

/* Cards */
.card, .card-gold {
    background-color: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.3rem 1.5rem;
    box-sizing: border-box;
    height: 100%;
    transition: border-color 0.15s ease;
}
.card-gold { border-left: 4px solid var(--gold); }
.card:hover, .card-gold:hover { border-color: var(--gold); }
.card h4, .card-gold h4 { margin: 0 0 0.5rem 0; font-size: 1.05rem; }
.card p, .card-gold p { margin: 0; line-height: 1.6; }
.card .kicker { color: var(--muted); font-size: 0.72rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 0.4rem; }
.card .row { display: flex; justify-content: space-between; gap: 1rem; padding: 0.45rem 0; border-bottom: 1px solid var(--border); }
.card .row:last-child { border-bottom: none; }
.card .row .k { color: var(--muted); flex: 0 0 8.5rem; min-width: 8.5rem; }
.card .row .v { color: var(--text); flex: 1 1 0; min-width: 0; text-align: right; overflow-wrap: anywhere; }
.project-tags { margin-top: 0.6rem; padding-bottom: 1.5rem; }

.chip {
    display: inline-block; background: rgba(232,213,163,0.12); color: var(--gold);
    border: 1px solid rgba(232,213,163,0.35); border-radius: 6px;
    padding: 0.1rem 0.55rem; font-size: 0.75rem; letter-spacing: 1px; margin-bottom: 0.6rem;
}

/* Call-out */
.callout {
    background: linear-gradient(135deg, rgba(232,213,163,0.12), rgba(232,213,163,0.03));
    border: 1px solid var(--gold);
    border-radius: 12px;
    padding: 1.4rem 1.7rem;
    margin: 0.5rem 0 1.2rem 0;
}
.callout .label { color: var(--gold); font-weight: 700; letter-spacing: 2px; text-transform: uppercase; font-size: 0.78rem; }
.callout p { font-style: italic; margin: 0.5rem 0 0 0; font-size: 1.02rem; line-height: 1.6; }

/* Badges */
.badge {
    display: inline-block; background-color: var(--surface-2); color: var(--gold);
    border: 1px solid var(--border); border-radius: 999px;
    padding: 0.2rem 0.75rem; margin: 0.15rem 0.25rem 0.15rem 0; font-size: 0.82rem;
}

/* Image placeholder */
.placeholder {
    background-color: var(--surface-2); border: 2px dashed var(--border); border-radius: 12px;
    color: var(--muted); text-align: center; min-height: 260px;
    display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.3rem;
}
.placeholder .big { font-size: 3.2rem; font-weight: 800; color: var(--gold); letter-spacing: 3px; }
.placeholder .small { font-size: 0.75rem; }

/* Metrics */
[data-testid="stMetric"] {
    background-color: var(--surface); border: 1px solid var(--border);
    border-radius: 12px; padding: 1rem 1.2rem;
}
[data-testid="stMetricValue"] { color: var(--gold); }
[data-testid="stMetricLabel"] p { color: var(--muted) !important; }

/* Inputs */
input, textarea, [data-baseweb="select"] > div {
    background-color: var(--surface-2) !important; color: var(--text) !important;
}
.category-tags { display: flex; flex-flow: row wrap; align-items: center; gap: 0.45rem; margin: 0.6rem 0 1rem; }
.category-tag {
    display: inline-flex; align-items: center; gap: 0.35rem;
    width: max-content; max-width: 100%; padding: 0.35rem 0.7rem;
    color: var(--text); background: var(--surface-2);
    border: 1px solid var(--border); border-radius: 999px;
    line-height: 1.35; white-space: nowrap;
}
.category-tag a { color: var(--muted) !important; font-weight: 700; text-decoration: none; }
.category-tag a:hover { color: var(--gold) !important; }
[data-testid="stForm"] { background-color: var(--surface); border: 1px solid var(--border); border-radius: 12px; }

/* Buttons: same width, centred text */
.stButton, .stFormSubmitButton { width: 100%; }
.stButton > button, .stFormSubmitButton > button {
    width: 100%; border-radius: 10px; border: 1px solid var(--border);
    background-color: var(--surface); color: var(--text);
    padding: 0.55rem 0.9rem; justify-content: center; transition: all 0.15s ease;
}
.stButton > button p, .stFormSubmitButton > button p { color: var(--text); font-weight: 500; }
.stButton > button:hover, .stFormSubmitButton > button:hover { border-color: var(--gold); }
.stButton > button:hover p, .stFormSubmitButton > button:hover p { color: var(--gold); }

/* Give every navigation button the width of the longest label. */
section[data-testid="stSidebar"] div[class*="st-key-nav_"] {
    width: 240px !important; max-width: 100% !important;
}
section[data-testid="stSidebar"] div[class*="st-key-nav_"] button {
    display: flex; width: 240px !important; min-width: 240px !important;
    max-width: 100% !important;
    box-sizing: border-box; justify-content: flex-start; text-align: left;
}
section[data-testid="stSidebar"] div[class*="st-key-nav_"] button p {
    text-align: left; width: 100%;
}

/* Match the size and alignment of the two home-page calls to action. */
div[class*="st-key-hero_projects"] button,
div[class*="st-key-hero_contact"] button {
    width: 100%; min-height: 3.4rem; box-sizing: border-box;
    border-radius: 12px; padding: 0.8rem 1rem; justify-content: center;
}
div[class*="st-key-hero_projects"] { margin-top: 0.65rem; }
div[class*="st-key-hero_projects"] button {
    min-height: 3.25rem; padding: 0.7rem 1.25rem;
}

/* Explore cards are full-card buttons; pseudo-elements create a true card layout. */
div[class*="st-key-home_explore_"] { width: 100%; height: 100%; }
div[class*="st-key-home_explore_"] [data-testid="stButton"] { width: 100%; height: 100%; }
div[class*="st-key-home_explore_"] button {
    display: flex !important; flex-direction: column !important;
    align-items: flex-start !important; gap: 0;
    width: 100% !important; min-height: 13rem; height: 100%; box-sizing: border-box;
    padding: 1.3rem 1.5rem; border-radius: 12px;
    justify-content: flex-start !important; text-align: left !important;
}
div[class*="st-key-home_explore_"] button > div {
    display: block !important; align-self: stretch !important;
    width: 100% !important; text-align: left !important; white-space: normal;
}
div[class*="st-key-home_explore_"] button [data-testid="stMarkdownContainer"] {
    display: block !important; width: 100% !important;
    text-align: left !important; white-space: normal;
}
div[class*="st-key-home_explore_"] button p {
    display: block !important; width: 100% !important;
    text-align: left !important; white-space: normal; overflow-wrap: anywhere;
}
div[class*="st-key-home_explore_"] button p {
    align-self: stretch !important; text-align: left !important;
    color: var(--gold) !important; font-size: 1.35rem !important;
    font-weight: 700; margin: 0; white-space: normal;
}
div[class*="st-key-home_explore_"] button::after {
    align-self: stretch; text-align: left !important;
    color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin-top: 1rem;
}
div[class*="st-key-home_explore_Autobiography"] button::after { content: "My story, Southern Leyte to CIT-U."; }
div[class*="st-key-home_explore_Skills"] button::after { content: "Languages and tools."; }
div[class*="st-key-home_explore_Projects"] button::after { content: "Selected game and software work."; }
div[class*="st-key-home_explore_Contact"] button::after { content: "Get in touch."; }
/* Active / primary buttons: gold background with DARK text so it stays readable */
.stButton > button[kind="primary"],
.stButton > button[data-testid="stBaseButton-primary"],
.stFormSubmitButton > button[kind="primaryFormSubmit"],
.stFormSubmitButton > button[data-testid="stBaseButton-primaryFormSubmit"] {
    background-color: var(--gold); border-color: var(--gold);
}
.stButton > button[kind="primary"] p,
.stButton > button[data-testid="stBaseButton-primary"] p,
.stFormSubmitButton > button[kind="primaryFormSubmit"] p,
.stFormSubmitButton > button[data-testid="stBaseButton-primaryFormSubmit"] p,
.stButton > button[kind="primary"]:hover p,
.stButton > button[data-testid="stBaseButton-primary"]:hover p {
    color: #0d1117 !important; font-weight: 700;
}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="stBaseButton-primary"]:hover { filter: brightness(1.08); }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# 4. HELPERS
# ---------------------------------------------------------------------------
def set_page(name: str) -> None:
    """Callback used by every navigation button."""
    st.session_state.page = name


def add_skill_category() -> None:
    """Add the search selection to the removable category list."""
    category = st.session_state.get("skills_category_search")
    selected = st.session_state.get("skills_selected_categories", [])
    if category and category not in selected:
        st.session_state["skills_selected_categories"] = [*selected, category]
    st.session_state["skills_category_search"] = None


def show_image(filename: str, caption: str, label: str = "IMG") -> None:
    """Show an image from assets/, or a clean placeholder if it is missing."""
    path = ASSETS / filename
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.markdown(
            f'<div class="placeholder"><div class="big">{label}</div>'
            f"<div>{caption}</div>"
            f'<div class="small">Add assets/{filename}</div></div>',
            unsafe_allow_html=True,
        )


def badges(items) -> str:
    return "".join(f'<span class="badge">{item}</span>' for item in items)


def callout(text: str) -> None:
    st.markdown(
        f'<div class="callout"><div class="label">Looking for Internship</div><p>"{text}"</p></div>',
        unsafe_allow_html=True,
    )


def eyebrow(text: str) -> None:
    st.markdown(f'<div class="eyebrow">{text}</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# 5. SIDEBAR
# ---------------------------------------------------------------------------
NAV = ["Home", "Autobiography", "Skills", "Projects", "Contact"]

with st.sidebar:
    st.markdown(
        f"""
<div class="brand">
<div class="avatar">{PROFILE['initials']}</div>
<div><div class="bn">{PROFILE['name']}</div><div class="bs">{PROFILE['program']} · CIT-U</div></div>
</div>
""",
        unsafe_allow_html=True,
    )
    st.divider()

    st.markdown('<div class="nav-label">Navigate</div>', unsafe_allow_html=True)
    for label in NAV:
        st.button(
            label,
            key=f"nav_{label}",
            on_click=set_page,
            args=(label,),
            type="primary" if st.session_state.page == label else "secondary",
        )

    st.divider()
    st.markdown('<div class="nav-label">Contact</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
<div class="side-links">
<span>{PROFILE['email']}</span>
<span>{PROFILE['phone']}</span>
<a href="{PROFILE['github']}" target="_blank">GitHub</a>
<a href="{PROFILE['itch']}" target="_blank">Itch.io</a>
</div>
""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# 6. PAGES
# ---------------------------------------------------------------------------
def page_home() -> None:
    # Split hero: text on the left, profile image on the right
    text_col, img_col = st.columns([3, 2], vertical_alignment="center", gap="large")
    with text_col:
        eyebrow("Autobiography &amp; Portfolio")
        st.title(PROFILE["name"])
        st.markdown(
            '<div class="lead">Computer Science student, indie game developer and optimization enthusiast '
            "building games and software from Pardo, Cebu City.</div>"
            + badges([PROFILE["program"], "CIT-U", PROFILE["status"], f"Class of {PROFILE['grad']}"]),
            unsafe_allow_html=True,
        )
        st.button("View projects", key="hero_projects", on_click=set_page, args=("Projects",), type="primary")
    with img_col:
        with st.container(border=True):
            show_image("profile.jpg", PROFILE["name"], PROFILE["initials"])

    st.divider()

    # Metrics grid
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Year Level", "3rd Year")
    m2.metric("Shipped Projects", len(PROJECTS))
    m3.metric("Core Languages", len(SKILLS))
    m4.metric("Expected Graduation", PROFILE["grad"])

    st.header("Professional Summary")
    st.markdown(
        f"""
<div class="grid grid-2">
<div class="card-gold"><h4>About</h4><p>I am a <b>{PROFILE['program']}</b> student at <b>Cebu Institute of Technology – University</b> and a <b>CHED Merit Scholar</b>. By third year, I have built solid fundamentals in Data Structures &amp; Algorithms and Algorithm Design &amp; Analysis, which lets me write optimized code with strong engineering intuition. I build games and software with C#, C++, C and Python, and I enjoy wearing many hats, from programming to environment art, UI/UX and sound.</p></div>
<div class="card"><h4>At a glance</h4>
<div class="row"><span class="k">Program</span><span class="v">{PROFILE['program']}</span></div>
<div class="row"><span class="k">University</span><span class="v">CIT-U</span></div>
<div class="row"><span class="k">Status</span><span class="v">{PROFILE['status']}</span></div>
<div class="row"><span class="k">Graduation</span><span class="v">{PROFILE['grad']}</span></div>
<div class="row"><span class="k">Focus</span><span class="v">Games, Algorithms, Tools</span></div>
</div>
</div>
""",
        unsafe_allow_html=True,
    )

    callout(INTERNSHIP_TEXT)

    st.header("Explore")
    shortcuts = [
        ("Autobiography", "My story, from Southern Leyte to CIT-U."),
        ("Skills", "Languages, tools and proficiency."),
        ("Projects", "Infinitus, TLGMS and DevVault."),
        ("Contact", "Reach out or leave feedback."),
    ]
    cols = st.columns(4)
    card_titles = {"Autobiography": "Story", "Skills": "Skills", "Projects": "Work", "Contact": "Contact"}
    for col, (name, _) in zip(cols, shortcuts):
        with col:
            st.button(
                card_titles[name],
                key=f"home_explore_{name}",
                on_click=set_page,
                args=(name,),
            )


def page_autobiography() -> None:
    eyebrow("About me")
    st.title("Autobiography")
    st.caption("From the shores of Southern Leyte to the lecture halls of CIT-U.")
    st.divider()

    titles = [c["title"] for c in CHAPTERS]
    view = st.radio(
        "Choose a chapter",
        ["All chapters"] + titles,
        horizontal=True,
    )

    selected = CHAPTERS if view == "All chapters" else [c for c in CHAPTERS if c["title"] == view]

    for chapter in selected:
        st.markdown(
            f'<div class="card-gold" style="margin-bottom:1rem;">'
            f'<span class="chip">{chapter["period"]}</span>'
            f'<h4>{chapter["title"]}</h4><p>{chapter["body"]}</p></div>',
            unsafe_allow_html=True,
        )

    st.subheader("Quick Facts")
    c1, c2, c3 = st.columns(3)
    c1.metric("Hometown", "San Juan, Leyte")
    c2.metric("University", "CIT-U")
    c3.metric("Status", "CHED Merit")


def page_skills() -> None:
    if "remove_skill_category" in st.query_params:
        category_to_remove = st.query_params["remove_skill_category"]
        selected_categories = st.session_state.get("skills_selected_categories", [])
        st.session_state["skills_selected_categories"] = [
            category for category in selected_categories if category != category_to_remove
        ]
        del st.query_params["remove_skill_category"]

    eyebrow("Capabilities")
    st.title("Skills")
    st.header("Proficiency Overview")

    st.markdown(
        '<div class="card-gold"><p>By third year, I have built solid core fundamentals in '
        "<b>Data Structures &amp; Algorithms</b> and <b>Algorithm Design &amp; Analysis</b>. "
        "These fundamentals let me write optimized code and develop strong engineering intuition. "
        "The numbers below are my own honest self-assessment. Python is the newest addition to my "
        "toolkit, so it sits lower for now.</p></div>",
        unsafe_allow_html=True,
    )
    st.write("")

    # Filters live on the page itself
    with st.container(border=True):
        st.subheader("Filters")
        all_categories = SKILLS["Category"].drop_duplicates().tolist()
        if "skills_selected_categories" not in st.session_state:
            st.session_state.skills_selected_categories = all_categories.copy()

        categories = st.session_state.skills_selected_categories
        available_categories = [item for item in all_categories if item not in categories]
        st.selectbox(
            "Category",
            available_categories,
            index=None,
            placeholder="Search to add a category...",
            key="skills_category_search",
            on_change=add_skill_category,
        )
        if categories:
            tag_markup = "".join(
                f'<span class="category-tag">{category}<a href="?remove_skill_category={quote(category)}" aria-label="Remove {category}">×</a></span>'
                for category in categories
            )
            st.markdown(f'<div class="category-tags">{tag_markup}</div>', unsafe_allow_html=True)
        min_prof = st.slider(
            "Minimum proficiency (%)",
            min_value=0,
            max_value=100,
            value=0,
            step=5,
        )

    filtered = SKILLS[SKILLS["Proficiency"] >= min_prof]
    if categories:
        filtered = filtered[filtered["Category"].isin(categories)]
    else:
        filtered = filtered.iloc[0:0]
    filtered = filtered.reset_index(drop=True)

    tab_prof, tab_tools = st.tabs(["Proficiency", "Tools & Technologies"])

    with tab_prof:
        if filtered.empty:
            st.warning("No skills match the current filters. Lower the slider or pick another category.")
        else:
            left, right = st.columns([3, 2])
            with left:
                with st.container(border=True, height=380):
                    st.subheader("Skill Table")
                    st.dataframe(
                        filtered,
                        hide_index=True,
                        use_container_width=True,
                        height=270,
                        column_config={
                            "Proficiency": st.column_config.ProgressColumn(
                                "Proficiency",
                                min_value=0,
                                max_value=100,
                                format="%d%%",
                            )
                        },
                    )
            with right:
                with st.container(border=True, height=380):
                    st.subheader("Proficiency Chart")
                    st.bar_chart(
                        filtered.set_index("Skill")["Proficiency"],
                        color="#e8d5a3",
                        height=270,
                    )

            avg = float(np.mean(filtered["Proficiency"]))
            best = filtered.loc[filtered["Proficiency"].idxmax(), "Skill"]
            k1, k2, k3 = st.columns(3)
            k1.metric("Skills shown", len(filtered))
            k2.metric("Average proficiency", f"{avg:.1f}%")
            k3.metric("Strongest", best)

    with tab_tools:
        cards = "".join(
            f'<div class="card"><h4>{cat}</h4>{badges(items)}</div>' for cat, items in TOOLS.items()
        )
        st.markdown(f'<div class="grid grid-3">{cards}</div>', unsafe_allow_html=True)


def render_project(project: dict, index: int) -> None:
    with st.container(border=True):
        img_col, info_col = st.columns([2, 3], gap="large")
        with img_col:
            show_image(project["image"], project["name"], project["tag"])
        with info_col:
            st.markdown(
                f"""
<div class="kicker muted" style="letter-spacing:2px;font-size:0.75rem;">PROJECT 0{index + 1}</div>
<h3 style="margin:0.2rem 0 0.6rem 0;">{project['name']}</h3>
<p>{project['description']}</p>
<div class="card" style="margin:0.8rem 0;">
<div class="row"><span class="k">Role</span><span class="v">{project['role']}</span></div>
<div class="row"><span class="k">Collaborators</span><span class="v">{project['collaborators']}</span></div>
<div class="row"><span class="k">Outcome</span><span class="v">{project['outcome']}</span></div>
</div>
<div class="project-tags">{badges(project['stack'])}</div>
""",
                unsafe_allow_html=True,
            )


def page_projects() -> None:
    eyebrow("Selected work")
    st.title("Projects")
    st.caption("Three shipped projects across game development and web tooling.")
    st.divider()

    short_names = [p["name"].split(" (")[0] for p in PROJECTS]
    view = st.radio(
        "View",
        ["All projects"] + short_names + ["Comparison table"],
        horizontal=True,
    )

    if view == "Comparison table":
        overview = pd.DataFrame(
            {
                "Project": [p["name"] for p in PROJECTS],
                "Role": [p["role"].split(",")[0] for p in PROJECTS],
                "Stack": [", ".join(p["stack"]) for p in PROJECTS],
                "Outcome": [p["outcome"] for p in PROJECTS],
            }
        )
        st.table(overview)
        return

    for i, project in enumerate(PROJECTS):
        if view == "All projects" or view == short_names[i]:
            render_project(project, i)


def page_contact() -> None:
    eyebrow("Get in touch")
    st.title("Contact")
    st.caption("Questions, feedback or opportunities? I'd love to hear from you.")
    st.divider()

    callout(INTERNSHIP_TEXT)

    form_col, info_col = st.columns([3, 2], gap="large")

    with form_col:
        st.header("Feedback / Contact Form")
        with st.form("contact_form", clear_on_submit=True):
            n1, n2 = st.columns(2)
            with n1:
                name = st.text_input("Your name")
            with n2:
                email = st.text_input("Your email")
            topic = st.selectbox(
                "Topic",
                ["Internship opportunity", "Project collaboration", "Portfolio feedback", "Just saying hi"],
            )
            reply = st.radio("Preferred reply method", ["Email", "Phone"], horizontal=True)
            rating = st.slider("How would you rate this portfolio?", 1, 5, 5)
            message = st.text_area("Message", height=150)
            copy_me = st.checkbox("Send me a copy of this message")
            submitted = st.form_submit_button("Send Message", type="primary")

        if submitted:
            if not name.strip() or not email.strip() or not message.strip():
                st.error("Please fill in your name, email and message.")
            elif "@" not in email or "." not in email.split("@")[-1]:
                st.error("Please enter a valid email address.")
            else:
                st.success(
                    f"Thanks, {name.strip()}! Your message about “{topic}” was received "
                    f"(rating: {rating}/5). I'll reply by {reply.lower()}."
                    + (" A copy would be sent to your email." if copy_me else "")
                )

    with info_col:
        st.header("Direct Contact")
        st.markdown(
            f"""
<div class="grid" style="grid-template-columns: minmax(0, 1fr);">
<div class="card-gold"><div class="kicker">Email</div><p>{PROFILE['email']}</p></div>
<div class="card-gold"><div class="kicker">Phone</div><p>{PROFILE['phone']}</p></div>
<div class="card-gold"><div class="kicker">GitHub</div><p><a href="{PROFILE['github']}" target="_blank">KurtJustinMalubay</a></p></div>
<div class="card-gold"><div class="kicker">Itch.io</div><p><a href="{PROFILE['itch']}" target="_blank">sashimiproductions</a></p></div>
<div class="card"><div class="kicker">Location</div><p>Pardo, Cebu City, Philippines<br>Hometown: San Juan, Southern Leyte</p></div>
</div>
""",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# 7. ROUTER
# ---------------------------------------------------------------------------
ROUTES = {
    "Home": page_home,
    "Autobiography": page_autobiography,
    "Skills": page_skills,
    "Projects": page_projects,
    "Contact": page_contact,
}

ROUTES.get(st.session_state.page, page_home)()

st.divider()
st.caption("© 2026 Kurt Justin J. Malubay · CSIT 349 Applied AI · Built with Streamlit")