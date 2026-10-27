import streamlit as st
import pandas as pd
import numpy as np
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Kurt Justin J. Malubay | Portfolio",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Genshin-inspired dark theme CSS ──────────────────────────────────────────
st.markdown("""
<style>
/* Import fonts */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Lato:wght@300;400;700&display=swap');

/* Root variables – Genshin palette */
:root {
    --bg-deep:       #0d0f14;
    --bg-mid:        #161a24;
    --bg-card:       #1c2130;
    --bg-card-hover: #222840;
    --accent-gold:   #c8a96e;
    --accent-light:  #e8d5a3;
    --accent-blue:   #4a90c4;
    --accent-glow:   #6ab0e0;
    --text-primary:  #e8e0d0;
    --text-secondary:#a09880;
    --text-muted:    #6a6458;
    --border-soft:   rgba(200,169,110,0.18);
    --border-bright: rgba(200,169,110,0.50);
    --shadow-gold:   0 0 18px rgba(200,169,110,0.15);
}

/* Global reset */
html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
    background-color: var(--bg-deep) !important;
    color: var(--text-primary) !important;
}

/* Main area */
.main .block-container {
    padding: 2rem 3rem;
    max-width: 1200px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1219 0%, #161a24 60%, #0d0f14 100%) !important;
    border-right: 1px solid var(--border-soft) !important;
}
[data-testid="stSidebar"] * { color: var(--text-primary) !important; }

/* Hero banner */
.hero-banner {
    background: linear-gradient(135deg, #0f1219 0%, #1a2035 40%, #0f1a2a 100%);
    border: 1px solid var(--border-soft);
    border-radius: 12px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-gold);
}
.hero-banner::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at top right, rgba(74,144,196,0.08) 0%, transparent 60%),
                radial-gradient(ellipse at bottom left, rgba(200,169,110,0.06) 0%, transparent 60%);
    pointer-events: none;
}
.hero-name {
    font-family: 'Cinzel', serif;
    font-size: 2.6rem;
    font-weight: 700;
    color: var(--accent-gold);
    letter-spacing: 0.04em;
    margin: 0;
    line-height: 1.1;
    text-shadow: 0 0 30px rgba(200,169,110,0.35);
}
.hero-subtitle {
    font-family: 'Lato', sans-serif;
    font-size: 1rem;
    color: var(--text-secondary);
    margin-top: 0.4rem;
    font-weight: 300;
    letter-spacing: 0.12em;
}
.hero-tagline {
    font-size: 0.95rem;
    color: var(--accent-glow);
    margin-top: 0.8rem;
    font-style: italic;
    opacity: 0.85;
}

/* Section divider */
.section-divider {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 2rem 0 1.2rem;
}
.divider-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--accent-gold) 0%, transparent 100%);
    opacity: 0.35;
}
.divider-title {
    font-family: 'Cinzel', serif;
    font-size: 1rem;
    color: var(--accent-gold);
    letter-spacing: 0.18em;
    white-space: nowrap;
}

/* Cards */
.card {
    background: var(--bg-card);
    border: 1px solid var(--border-soft);
    border-radius: 10px;
    padding: 1.4rem 1.6rem;
    transition: border-color 0.25s, background 0.25s;
}
.card:hover { border-color: var(--border-bright); background: var(--bg-card-hover); }

/* Skill tag */
.skill-tag {
    display: inline-block;
    background: rgba(200,169,110,0.10);
    border: 1px solid rgba(200,169,110,0.30);
    color: var(--accent-light);
    border-radius: 4px;
    padding: 0.25rem 0.75rem;
    font-size: 0.82rem;
    margin: 0.2rem 0.15rem;
    letter-spacing: 0.04em;
}

/* Project card */
.project-card {
    background: var(--bg-card);
    border: 1px solid var(--border-soft);
    border-radius: 10px;
    padding: 1.4rem 1.6rem;
    height: 100%;
    transition: border-color 0.25s, box-shadow 0.25s;
}
.project-card:hover {
    border-color: var(--accent-blue);
    box-shadow: 0 0 16px rgba(74,144,196,0.12);
}
.project-title {
    font-family: 'Cinzel', serif;
    font-size: 1.05rem;
    color: var(--accent-gold);
    margin-bottom: 0.3rem;
}
.project-role { font-size: 0.82rem; color: var(--accent-glow); margin-bottom: 0.6rem; }
.project-desc { font-size: 0.9rem; color: var(--text-secondary); line-height: 1.55; }

/* Timeline */
.timeline-item {
    border-left: 2px solid var(--border-soft);
    padding-left: 1.2rem;
    margin-bottom: 1.4rem;
    position: relative;
}
.timeline-item::before {
    content: '◆';
    position: absolute;
    left: -0.6rem;
    top: 0;
    color: var(--accent-gold);
    font-size: 0.7rem;
    line-height: 1.6;
}
.timeline-year { font-size: 0.78rem; color: var(--accent-gold); letter-spacing: 0.1em; }
.timeline-label { font-size: 0.95rem; color: var(--text-primary); font-weight: 600; margin-top: 0.1rem; }
.timeline-desc { font-size: 0.87rem; color: var(--text-secondary); margin-top: 0.2rem; line-height: 1.5; }

/* Metric style override */
[data-testid="stMetric"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: 10px !important;
    padding: 1rem 1.2rem !important;
}
[data-testid="stMetricLabel"] { color: var(--text-secondary) !important; font-size: 0.82rem !important; }
[data-testid="stMetricValue"] { color: var(--accent-gold) !important; font-family: 'Cinzel', serif !important; }

/* Tab styling */
[data-testid="stTabs"] [data-baseweb="tab"] {
    color: var(--text-secondary) !important;
    font-family: 'Cinzel', serif !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.08em !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
    color: var(--accent-gold) !important;
    border-bottom-color: var(--accent-gold) !important;
}

/* Input overrides */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div {
    background: var(--bg-card) !important;
    border-color: var(--border-soft) !important;
    color: var(--text-primary) !important;
    border-radius: 6px !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #1a2035, #2a3050) !important;
    border: 1px solid var(--accent-gold) !important;
    color: var(--accent-gold) !important;
    font-family: 'Cinzel', serif !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.1em !important;
    border-radius: 6px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #2a3050, #3a4070) !important;
    box-shadow: 0 0 12px rgba(200,169,110,0.25) !important;
}

/* Sidebar nav links */
.nav-link {
    display: block;
    padding: 0.5rem 0.75rem;
    border-radius: 6px;
    color: var(--text-secondary);
    font-size: 0.9rem;
    cursor: pointer;
    transition: background 0.2s, color 0.2s;
    text-decoration: none;
    margin-bottom: 0.2rem;
}
.nav-link:hover { background: rgba(200,169,110,0.08); color: var(--accent-gold); }

/* Download button */
.stDownloadButton > button {
    background: linear-gradient(135deg, #1a2a1a, #1e3520) !important;
    border: 1px solid rgba(100,200,120,0.4) !important;
    color: #80d898 !important;
    font-family: 'Cinzel', serif !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.08em !important;
    border-radius: 6px !important;
}

/* Progress bar override */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--accent-gold), var(--accent-glow)) !important;
}

/* Form submit */
[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #1a2035, #2a3050) !important;
    border: 1px solid var(--accent-gold) !important;
    color: var(--accent-gold) !important;
    font-family: 'Cinzel', serif !important;
    letter-spacing: 0.1em !important;
    border-radius: 6px !important;
    width: 100% !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, [data-testid="stToolbar"] { display: none !important; }

/* Alert override */
.stSuccess { background: rgba(100,200,120,0.1) !important; border-color: rgba(100,200,120,0.3) !important; }
.stWarning { background: rgba(200,169,110,0.1) !important; border-color: rgba(200,169,110,0.3) !important; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "active_section" not in st.session_state:
    st.session_state.active_section = "Home"
if "feedback_sent" not in st.session_state:
    st.session_state.feedback_sent = False
if "visitor_count" not in st.session_state:
    st.session_state.visitor_count = 1
if "theme_dark" not in st.session_state:
    st.session_state.theme_dark = True

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1.2rem 0 1rem;'>
        <div style='font-family: Cinzel, serif; font-size: 1.1rem; color: #c8a96e; letter-spacing:0.1em;'>⚔️ KURT</div>
        <div style='font-size: 0.75rem; color: #6a6458; letter-spacing:0.15em; margin-top:0.2rem;'>BSCS 3 · F1</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    sections = {
        "🏠  Home":        "Home",
        "📖  Autobiography": "Autobiography",
        "🎓  Education":   "Education",
        "🛠️  Skills":      "Skills",
        "🎮  Projects":    "Projects",
        "📬  Contact":     "Contact",
    }

    for label, key in sections.items():
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.active_section = key

    st.divider()

    st.markdown("<div style='font-size:0.75rem; color:#6a6458; letter-spacing:0.1em; margin-bottom:0.5rem;'>QUICK STATS</div>", unsafe_allow_html=True)
    st.metric("Year", "3rd Year")
    st.metric("Graduating", "2028")
    st.metric("Status", "Open 🟢")

    st.divider()

    # Theme toggle checkbox
    dark = st.checkbox("Dark Mode", value=st.session_state.theme_dark)
    st.session_state.theme_dark = dark

    st.markdown("<div style='font-size:0.72rem; color:#6a6458; margin-top:1.5rem; text-align:center;'>CIT University · CSIT 349</div>", unsafe_allow_html=True)

# ── Helper: section divider ───────────────────────────────────────────────────
def section_header(title: str):
    st.markdown(f"""
    <div class="section-divider">
        <div class="divider-line"></div>
        <div class="divider-title">{title}</div>
        <div class="divider-line" style="background:linear-gradient(90deg,transparent,#c8a96e);"></div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  HOME
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.active_section == "Home":

    # Hero
    col_info, col_img = st.columns([2, 1], gap="large")

    with col_info:
        st.markdown("""
        <div class="hero-banner">
            <div class="hero-name">Kurt Justin J. Malubay</div>
            <div class="hero-subtitle">BSCS 3 · F1 &nbsp;·&nbsp; CIT University</div>
            <div class="hero-tagline">"Curious by nature. Building by choice."</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style="margin-bottom:1rem;">
            <div style="font-family:Cinzel,serif; font-size:0.85rem; color:#c8a96e; margin-bottom:0.6rem; letter-spacing:0.1em;">ABOUT</div>
            <p style="color:#a09880; font-size:0.95rem; line-height:1.7; margin:0;">
            I'm a third-year BSCS student from San Juan, Southern Leyte — a province kid who grew up between
            the sea and the mountains and got hooked on technology the moment his mother handed him a Blackberry
            phone. That early spark of curiosity has never left. Today I build UIs, write code, and explore
            game development — currently working on <strong style="color:#c8a96e;">Infinitus</strong>, a collaborative
            project where I wear multiple hats: designer, developer, and project lead.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # CTA buttons
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button("📖  My Story", use_container_width=True):
                st.session_state.active_section = "Autobiography"
                st.rerun()
        with b2:
            if st.button("🎮  Projects", use_container_width=True):
                st.session_state.active_section = "Projects"
                st.rerun()
        with b3:
            if st.button("📬  Contact", use_container_width=True):
                st.session_state.active_section = "Contact"
                st.rerun()

    with col_img:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #1c2130, #1a2035);
            border: 1px solid rgba(200,169,110,0.25);
            border-radius: 10px;
            height: 260px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 0.6rem;
        ">
            <div style="font-size:3.5rem;">🧑‍💻</div>
            <div style="font-family:Cinzel,serif; font-size:0.8rem; color:#c8a96e; letter-spacing:0.15em;">KURT MALUBAY</div>
            <div style="font-size:0.72rem; color:#6a6458; text-align:center; padding: 0 1rem; line-height:1.5;">
                Replace this with <code>profile.jpg</code><br>inside <code>assets/</code>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Highlights row ──
    section_header("HIGHLIGHTS")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Projects", "2+", "active")
    m2.metric("Languages", "5+", "known")
    m3.metric("Graduating", "2028", "on track")
    m4.metric("Seeking", "Internship", "open")

    # ── Skills snapshot ──
    section_header("SKILL SNAPSHOT")
    skills_snap = {
        "Python":           75,
        "C / C++ / C#":     70,
        "HTML & CSS":       68,
        "UI / UX Design":   72,
        "Prompt Engineering": 80,
        "DSA Fundamentals": 74,
    }
    c1, c2 = st.columns(2)
    items = list(skills_snap.items())
    for i, (skill, val) in enumerate(items):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"<div style='font-size:0.82rem; color:#a09880; margin-bottom:0.15rem;'>{skill}</div>", unsafe_allow_html=True)
            st.progress(val / 100)

# ═══════════════════════════════════════════════════════════════════════════════
#  AUTOBIOGRAPHY
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.active_section == "Autobiography":

    st.markdown("""
    <div class="hero-banner">
        <div class="hero-name" style="font-size:2rem;">My Story</div>
        <div class="hero-subtitle">San Juan, Southern Leyte → Cebu City</div>
    </div>
    """, unsafe_allow_html=True)

    tab_origin, tab_spark, tab_now = st.tabs(["🌊  Origins", "⚡  The Spark", "🚀  Now"])

    with tab_origin:
        st.markdown("""
        <div class="card">
            <div style="font-family:Cinzel,serif; font-size:0.85rem; color:#c8a96e; margin-bottom:0.8rem; letter-spacing:0.1em;">GROWING UP IN THE PROVINCE</div>
            <p style="color:#a09880; font-size:0.95rem; line-height:1.8;">
            I grew up in San Juan, Southern Leyte — a small town uniquely sandwiched between the sea and the
            mountains. The ocean was always within reach, and the forest trails of the highlands were just as
            accessible. It was the kind of place that bred curiosity: every wave and every tree root was something
            to explore, take apart in your mind, and understand.
            </p>
            <p style="color:#a09880; font-size:0.95rem; line-height:1.8; margin-top:0.8rem;">
            Growing up in a loving, close-knit family gave me a strong foundation. I was the kid who always
            asked <em style="color:#c8a96e;">"how does this work?"</em> — whether it was a sea creature washed ashore,
            a machine in the market, or later, a glowing screen. The province taught me patience, resourcefulness,
            and the value of figuring things out on your own when there is no one else to ask.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with tab_spark:
        st.markdown("""
        <div class="card">
            <div style="font-family:Cinzel,serif; font-size:0.85rem; color:#c8a96e; margin-bottom:0.8rem; letter-spacing:0.1em;">THE BLACKBERRY MOMENT</div>
            <p style="color:#a09880; font-size:0.95rem; line-height:1.8;">
            The turning point came when my mother got a Blackberry phone. I picked it up, opened a tiny
            <em style="color:#c8a96e;">Assassin's Creed</em> game, and something clicked — not just with the game,
            but with the <em>device</em> itself. How could this small slab of plastic and glass run a world like that?
            Who made it? How?
            </p>
            <p style="color:#a09880; font-size:0.95rem; line-height:1.8; margin-top:0.8rem;">
            That question became a quiet obsession all through elementary and high school. I taught myself
            what I could through online resources, forums, and plain old experimentation — no formal classes,
            just curiosity and stubborn trial-and-error. I didn't have a job, and I didn't need one to learn:
            the internet was my classroom, and I was its most motivated student.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with tab_now:
        st.markdown("""
        <div class="card">
            <div style="font-family:Cinzel,serif; font-size:0.85rem; color:#c8a96e; margin-bottom:0.8rem; letter-spacing:0.1em;">WHERE I AM TODAY</div>
            <p style="color:#a09880; font-size:0.95rem; line-height:1.8;">
            Today I'm a third-year BSCS student at CIT University — a school I chose deliberately because of
            its reputation for competitive, rigorous computer science education. Game development was the
            thread that led me here, and it continues to pull me forward.
            </p>
            <p style="color:#a09880; font-size:0.95rem; line-height:1.8; margin-top:0.8rem;">
            I'm currently co-developing <strong style="color:#c8a96e;">Infinitus</strong> alongside teammates
            Glenshayne Belarmino and Wilmark Racho, where I serve as both a core developer and an informal
            project manager — handling UI, code architecture, design, and coordination. It is the most
            complete expression of everything I've learned so far, and it's still growing.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ── Milestones timeline ──
    section_header("MILESTONES")
    milestones = [
        ("Early Years",    "Growing up in San Juan",      "Raised near the sea and mountains of Southern Leyte. Developed a deep curiosity about the natural and technological world."),
        ("~2015",          "The Blackberry Spark",        "First encounter with mobile gaming on a Blackberry phone. Sparked an obsession with understanding how technology is built."),
        ("Elementary–SHS", "Self-taught Exploration",     "Spent years researching, experimenting, and quietly building skills outside any formal curriculum."),
        ("2022",           "Entered CIT University",      "Passed multiple state university entrance exams but chose CIT for its competitive CS program and its alignment with game dev."),
        ("2023",           "TLGMS Prototype",             "Completed first game development prototype — the applied result of first-year learnings."),
        ("2024–Present",   "Infinitus (Ongoing)",         "Co-developing Infinitus: handling UI/UX, coding, design, and project coordination alongside two teammates."),
        ("2028",           "Expected Graduation",         "On track to graduate with a BSCS degree from CIT University."),
    ]
    for year, label, desc in milestones:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-year">{year}</div>
            <div class="timeline-label">{label}</div>
            <div class="timeline-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  EDUCATION
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.active_section == "Education":

    st.markdown("""
    <div class="hero-banner">
        <div class="hero-name" style="font-size:2rem;">Education</div>
        <div class="hero-subtitle">Public schools · State university entrance exams · CIT University</div>
    </div>
    """, unsafe_allow_html=True)

    section_header("ACADEMIC JOURNEY")

    edu_data = [
        {
            "level": "Elementary",
            "school": "Public Elementary School",
            "location": "San Juan, Southern Leyte",
            "note": "Foundational years in a provincial public school. Curiosity and self-directed learning began here."
        },
        {
            "level": "Junior High School",
            "school": "Public Junior High School",
            "location": "San Juan, Southern Leyte",
            "note": "Continued in the public school system. Interest in technology grew alongside academic studies."
        },
        {
            "level": "Senior High School",
            "school": "Public Senior High School",
            "location": "Southern Leyte",
            "note": "Maintained academic performance while deepening self-study in programming and tech."
        },
        {
            "level": "College (Current)",
            "school": "CIT University",
            "location": "Cebu City",
            "note": "Passed entrance exams for multiple state universities. Chose CIT for its competitive CS program and strong alignment with game development and applied technology. Currently in 3rd Year."
        },
    ]

    for edu in edu_data:
        level_color = "#c8a96e" if edu["level"] == "College (Current)" else "#6ab0e0"
        st.markdown(f"""
        <div class="card" style="margin-bottom:0.8rem; {'border-color:rgba(200,169,110,0.4);' if edu['level']=='College (Current)' else ''}">
            <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.4rem;">
                <span style="font-family:Cinzel,serif; font-size:0.75rem; color:{level_color}; letter-spacing:0.1em;">{edu['level'].upper()}</span>
            </div>
            <div style="font-size:1rem; color:#e8e0d0; font-weight:600;">{edu['school']}</div>
            <div style="font-size:0.82rem; color:#6ab0e0; margin:0.15rem 0 0.5rem;">📍 {edu['location']}</div>
            <div style="font-size:0.9rem; color:#a09880; line-height:1.6;">{edu['note']}</div>
        </div>
        """, unsafe_allow_html=True)

    section_header("PROGRAM")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card">
            <div style="font-family:Cinzel,serif;font-size:0.82rem;color:#c8a96e;letter-spacing:0.1em;margin-bottom:0.5rem;">DEGREE</div>
            <div style="font-size:1.05rem;color:#e8e0d0;font-weight:600;">Bachelor of Science in Computer Science</div>
            <div style="font-size:0.85rem;color:#a09880;margin-top:0.3rem;">CIT University · BSCS 3 F1</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
            <div style="font-family:Cinzel,serif;font-size:0.82rem;color:#c8a96e;letter-spacing:0.1em;margin-bottom:0.5rem;">FOCUS AREA</div>
            <div style="font-size:1.05rem;color:#e8e0d0;font-weight:600;">Game Development & Applied AI</div>
            <div style="font-size:0.85rem;color:#a09880;margin-top:0.3rem;">UI/UX · Systems · Project Management</div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SKILLS
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.active_section == "Skills":

    st.markdown("""
    <div class="hero-banner">
        <div class="hero-name" style="font-size:2rem;">Skills</div>
        <div class="hero-subtitle">Self-taught · Curiosity-driven · Fundamentals-first</div>
    </div>
    """, unsafe_allow_html=True)

    # Slider for context
    section_header("PROFICIENCY OVERVIEW")
    selected_skill = st.selectbox(
        "Explore a skill area:",
        ["Python", "C / C++ / C#", "HTML & CSS", "UI / UX Design", "Prompt Engineering", "DSA Fundamentals"]
    )

    skill_details = {
        "Python": {
            "level": 75,
            "desc": "My primary scripting and automation language. Used for data handling, small tools, and applied AI projects. Comfortable with standard libraries and fundamentals.",
            "tags": ["scripting", "automation", "data basics", "applied AI"],
        },
        "C / C++ / C#": {
            "level": 70,
            "desc": "Core systems languages covered in academic coursework and personal projects. C# is particularly relevant to game development via Unity.",
            "tags": ["systems", "game dev", "academic use", "Unity pipeline"],
        },
        "HTML & CSS": {
            "level": 68,
            "desc": "Comfortable with structuring and styling web content. Experience with basic website frameworks and layout fundamentals.",
            "tags": ["web basics", "layout", "styling", "Streamlit"],
        },
        "UI / UX Design": {
            "level": 72,
            "desc": "Hands-on experience from leading UI on Infinitus. Focus on usability, visual hierarchy, and accessible dark-mode design.",
            "tags": ["visual hierarchy", "dark mode", "usability", "prototyping"],
        },
        "Prompt Engineering": {
            "level": 80,
            "desc": "Strong grasp of prompt structuring, context management, and leveraging AI tools effectively. DSA and DAA knowledge helps reason about optimization and user intent.",
            "tags": ["context management", "DSA-informed", "optimization reasoning", "AI tools"],
        },
        "DSA Fundamentals": {
            "level": 74,
            "desc": "Solid grounding in data structures and algorithm analysis — applied to making programs efficient and reasoning through design decisions.",
            "tags": ["data structures", "algorithm analysis", "DAA", "optimization"],
        },
    }

    d = skill_details[selected_skill]
    st.markdown(f"""
    <div class="card" style="margin-bottom:1rem;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
            <div style="font-family:Cinzel,serif;font-size:1rem;color:#c8a96e;">{selected_skill}</div>
            <div style="font-size:0.85rem;color:#6ab0e0;">{d['level']}%</div>
        </div>
        <div style="font-size:0.9rem;color:#a09880;line-height:1.6;margin-bottom:0.8rem;">{d['desc']}</div>
        <div>{''.join(f'<span class="skill-tag">{t}</span>' for t in d['tags'])}</div>
    </div>
    """, unsafe_allow_html=True)
    st.progress(d["level"] / 100)

    # ── Full table ──
    section_header("SKILLS TABLE")

    skills_df = pd.DataFrame({
        "Skill": ["Python", "C", "C++", "C#", "HTML", "CSS", "UI / UX Design", "Prompt Engineering", "DSA / DAA"],
        "Category": ["Language", "Language", "Language", "Language", "Web", "Web", "Design", "AI Tools", "Theory"],
        "Proficiency": [75, 70, 70, 70, 68, 68, 72, 80, 74],
        "Context": ["Scripting, tools", "Academic / systems", "Academic / systems", "Game dev", "Web basics", "Styling", "Infinitus UI", "Applied AI", "Academic + applied"],
    })

    st.dataframe(
        skills_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Proficiency": st.column_config.ProgressColumn("Proficiency (%)", min_value=0, max_value=100, format="%d%%"),
        }
    )

    section_header("CATEGORY BREAKDOWN")
    # Chart
    category_avg = skills_df.groupby("Category")["Proficiency"].mean().reset_index()
    chart_data = pd.DataFrame(
        {cat: [val] for cat, val in zip(category_avg["Category"], category_avg["Proficiency"])}
    )
    st.bar_chart(chart_data, use_container_width=True, height=220)

    # Multiselect filter
    section_header("FILTER BY CATEGORY")
    cats = st.multiselect(
        "Select categories to view:",
        options=skills_df["Category"].unique().tolist(),
        default=skills_df["Category"].unique().tolist(),
    )
    filtered = skills_df[skills_df["Category"].isin(cats)]
    st.dataframe(filtered, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  PROJECTS
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.active_section == "Projects":

    st.markdown("""
    <div class="hero-banner">
        <div class="hero-name" style="font-size:2rem;">Projects</div>
        <div class="hero-subtitle">Built from curiosity. Refined through collaboration.</div>
    </div>
    """, unsafe_allow_html=True)

    section_header("FEATURED WORK")

    # Radio filter
    filter_opt = st.radio(
        "Show:",
        ["All", "Collaborative", "Solo"],
        horizontal=True,
    )

    projects = [
        {
            "title": "Infinitus",
            "type": "Collaborative",
            "role": "UI Designer · Developer · Project Lead",
            "tools": ["Unity / C#", "UI/UX Design", "Python", "Project Management"],
            "status": "Active",
            "desc": (
                "A collaborative game development project built together with teammates "
                "Glenshayne Belarmino and Wilmark Racho. I lead UI design, core code "
                "architecture, and overall project coordination — bridging the gap between "
                "design vision and technical execution."
            ),
            "links": {"GitHub": "https://github.com/KurtJustinMalubay"},
        },
        {
            "title": "TLGMS",
            "type": "Solo",
            "role": "Solo Developer",
            "tools": ["Game Dev tools", "C#", "Prototyping"],
            "status": "Completed",
            "desc": (
                "My first completed game development prototype — a personal milestone marking "
                "the start of my game dev journey after first year. Built entirely by myself "
                "as a practical application of core academic knowledge and self-taught skills."
            ),
            "links": {"itch.io": "https://sashimiproductions.itch.io/"},
        },
    ]

    show = [p for p in projects if filter_opt == "All" or p["type"] == filter_opt]

    for p in show:
        with st.container():
            st.markdown(f"""
            <div class="project-card" style="margin-bottom:1rem;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                    <div>
                        <div class="project-title">{p['title']}</div>
                        <div class="project-role">🎭 {p['role']}</div>
                    </div>
                    <span style="font-size:0.75rem; padding:0.2rem 0.6rem; border-radius:4px;
                        background:{'rgba(100,200,120,0.12)' if p['status']=='Active' else 'rgba(100,120,200,0.12)'};
                        border:1px solid {'rgba(100,200,120,0.3)' if p['status']=='Active' else 'rgba(100,120,200,0.3)'};
                        color:{'#80d898' if p['status']=='Active' else '#8090d8'};">
                        {'🟢 ' if p['status']=='Active' else '✅ '}{p['status']}
                    </span>
                </div>
                <div class="project-desc" style="margin:0.6rem 0;">{p['desc']}</div>
                <div style="margin-top:0.5rem;">
                    <span style="font-size:0.78rem;color:#6a6458;margin-right:0.4rem;">TOOLS:</span>
                    {''.join(f'<span class="skill-tag">{t}</span>' for t in p['tools'])}
                </div>
            </div>
            """, unsafe_allow_html=True)

            link_cols = st.columns(len(p["links"]) + 3)
            for i, (label, url) in enumerate(p["links"].items()):
                with link_cols[i]:
                    st.link_button(f"🔗 {label}", url)
            st.markdown("")

    # Download resume placeholder
    section_header("DOCUMENTS")
    resume_text = """Kurt Justin J. Malubay
BSCS 3 · CIT University
justinkurt837@gmail.com | github.com/KurtJustinMalubay | sashimiproductions.itch.io

SKILLS: Python, C/C++/C#, HTML/CSS, UI Design, Prompt Engineering, DSA/DAA
PROJECTS: Infinitus (active), TLGMS (completed)
GRADUATING: 2028 | SEEKING: Internship
"""
    st.download_button(
        label="⬇️  Download Resume (placeholder)",
        data=resume_text,
        file_name="KurtMalubay_Resume.txt",
        mime="text/plain",
    )

# ═══════════════════════════════════════════════════════════════════════════════
#  CONTACT
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.active_section == "Contact":

    st.markdown("""
    <div class="hero-banner">
        <div class="hero-name" style="font-size:2rem;">Get in Touch</div>
        <div class="hero-subtitle">Open to internship opportunities · Let's build something.</div>
    </div>
    """, unsafe_allow_html=True)

    col_links, col_form = st.columns([1, 1.4], gap="large")

    with col_links:
        section_header("CONTACT")
        contacts = [
            ("📧", "Email",    "justinkurt837@gmail.com",          None),
            ("📱", "Phone",    "09928330407",                      None),
            ("🐙", "GitHub",   "KurtJustinMalubay",                "https://github.com/KurtJustinMalubay"),
            ("🎮", "itch.io",  "sashimiproductions.itch.io",       "https://sashimiproductions.itch.io/"),
        ]
        for icon, label, value, url in contacts:
            if url:
                st.markdown(f"""
                <a href="{url}" target="_blank" style="text-decoration:none;">
                <div class="card" style="margin-bottom:0.6rem; cursor:pointer;">
                    <div style="display:flex;align-items:center;gap:0.8rem;">
                        <span style="font-size:1.3rem;">{icon}</span>
                        <div>
                            <div style="font-size:0.75rem;color:#6a6458;letter-spacing:0.1em;">{label.upper()}</div>
                            <div style="font-size:0.9rem;color:#6ab0e0;">{value}</div>
                        </div>
                    </div>
                </div>
                </a>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="card" style="margin-bottom:0.6rem;">
                    <div style="display:flex;align-items:center;gap:0.8rem;">
                        <span style="font-size:1.3rem;">{icon}</span>
                        <div>
                            <div style="font-size:0.75rem;color:#6a6458;letter-spacing:0.1em;">{label.upper()}</div>
                            <div style="font-size:0.9rem;color:#e8e0d0;">{value}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        section_header("INTERNSHIP")
        st.markdown("""
        <div class="card">
            <div style="font-size:0.9rem;color:#a09880;line-height:1.7;">
            I'm currently seeking an internship where I can apply my skills in programming,
            UI/UX design, and project coordination — and grow beyond them. I'm especially
            interested in roles involving game development, applied AI, or product-facing
            software, where I can contribute meaningfully from day one while continuing to
            learn from experienced developers and designers.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_form:
        section_header("SEND A MESSAGE")

        if not st.session_state.feedback_sent:
            with st.form("contact_form"):
                name  = st.text_input("Your Name")
                email = st.text_input("Your Email")
                subject = st.selectbox(
                    "Subject",
                    ["Internship Inquiry", "Project Collaboration", "General Feedback", "Other"],
                )
                msg = st.text_area("Message", height=130, placeholder="Write your message here...")
                rating = st.slider("How did you find this portfolio?", 1, 5, 4)
                agree  = st.checkbox("I agree to have my message stored for review.")

                submitted = st.form_submit_button("⚔️  Send Message")

                if submitted:
                    if name and email and msg and agree:
                        st.session_state.feedback_sent = True
                        st.session_state.last_sender   = name
                        st.rerun()
                    else:
                        st.warning("Please fill in all fields and accept the terms.")
        else:
            sender = st.session_state.get("last_sender", "Traveler")
            st.markdown(f"""
            <div class="card" style="border-color:rgba(100,200,120,0.4); text-align:center; padding:2rem;">
                <div style="font-size:2rem; margin-bottom:0.6rem;">✅</div>
                <div style="font-family:Cinzel,serif;font-size:1rem;color:#80d898;margin-bottom:0.5rem;">Message Received</div>
                <div style="font-size:0.9rem;color:#a09880;line-height:1.6;">
                    Thanks, <strong style="color:#c8a96e;">{sender}</strong>! I'll get back to you
                    as soon as I can. Appreciate you taking the time to reach out.
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Send another message"):
                st.session_state.feedback_sent = False
                st.rerun()

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-top:3rem; padding-top:1.2rem; border-top:1px solid rgba(200,169,110,0.12);
     text-align:center; font-size:0.78rem; color:#6a6458; letter-spacing:0.1em;">
    Kurt Justin J. Malubay &nbsp;·&nbsp; BSCS 3 F1 &nbsp;·&nbsp; CIT University &nbsp;·&nbsp; CSIT 349 Applied AI
</div>
""", unsafe_allow_html=True)
