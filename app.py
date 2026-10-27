import streamlit as st
import pandas as pd
import numpy as np

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Kurt Justin J. Malubay | Portfolio",
    page_icon="⚔️",
    layout="wide",
)

# ─── Global Theme / CSS ──────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Import Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    background-color: #0d1117 !important;
    color: #c9d1d9 !important;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Main container ── */
.block-container {
    padding: 2rem 3rem 4rem 3rem !important;
    max-width: 1200px;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background-color: #0a0e14 !important;
    border-right: 1px solid #1c2333;
}
section[data-testid="stSidebar"] * { color: #c9d1d9 !important; }

/* ── Typography ── */
h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
    color: #e8d5a3 !important;
    letter-spacing: 0.02em;
}
h1 { font-size: 2.2rem !important; font-weight: 700 !important; }
h2 { font-size: 1.4rem !important; font-weight: 600 !important; }
h3 { font-size: 1.1rem !important; font-weight: 600 !important; }
p, li, span, label, .stMarkdown {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.92rem !important;
    line-height: 1.7 !important;
    color: #c9d1d9 !important;
}

/* ── Divider ── */
hr { border-color: #1c2333 !important; margin: 1.5rem 0 !important; }

/* ── Cards ── */
.card {
    background: #161b22;
    border: 1px solid #1c2333;
    border-radius: 8px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
}
.card-gold {
    background: #12181f;
    border: 1px solid #3d3018;
    border-left: 3px solid #e8d5a3;
    border-radius: 0 8px 8px 0;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
}
.badge {
    display: inline-block;
    background: #1c2333;
    border: 1px solid #2d3748;
    border-radius: 4px;
    padding: 2px 10px;
    font-size: 0.75rem !important;
    color: #a8b3c1 !important;
    margin-right: 6px;
    margin-bottom: 4px;
    font-family: 'Inter', sans-serif !important;
}
.tag-gold {
    display: inline-block;
    background: #1e1a0f;
    border: 1px solid #4a3c1a;
    border-radius: 4px;
    padding: 2px 10px;
    font-size: 0.75rem !important;
    color: #e8d5a3 !important;
    margin-right: 6px;
    margin-bottom: 4px;
    font-family: 'Inter', sans-serif !important;
}

/* ── Metric cards ── */
[data-testid="metric-container"] {
    background: #161b22 !important;
    border: 1px solid #1c2333 !important;
    border-radius: 8px !important;
    padding: 1rem 1.2rem !important;
}
[data-testid="metric-container"] label {
    color: #8b949e !important;
    font-size: 0.78rem !important;
    font-family: 'Inter', sans-serif !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #e8d5a3 !important;
    font-family: 'Cinzel', serif !important;
    font-size: 1.4rem !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid #1c2333 !important;
    gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #8b949e !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    padding: 0.6rem 1.4rem !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
}
.stTabs [aria-selected="true"] {
    color: #e8d5a3 !important;
    border-bottom: 2px solid #e8d5a3 !important;
    background: transparent !important;
}

/* ── Buttons ── */
.stButton > button {
    background: transparent !important;
    color: #e8d5a3 !important;
    border: 1px solid #4a3c1a !important;
    border-radius: 5px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
    padding: 0.4rem 1.2rem !important;
    transition: background 0.15s ease;
}
.stButton > button:hover {
    background: #1e1a0f !important;
}

/* ── Inputs ── */
.stTextInput > div > input,
.stTextArea > div > textarea,
.stSelectbox > div,
.stRadio > div {
    background-color: #161b22 !important;
    border-color: #1c2333 !important;
    color: #c9d1d9 !important;
    font-family: 'Inter', sans-serif !important;
    border-radius: 6px !important;
}

/* ── Slider ── */
.stSlider [data-baseweb="slider"] div[role="slider"] {
    background-color: #e8d5a3 !important;
}

/* ── DataFrame ── */
.stDataFrame { border-radius: 8px; overflow: hidden; }
.stDataFrame table {
    background: #161b22 !important;
    color: #c9d1d9 !important;
    border-color: #1c2333 !important;
}

/* ── Section hero ── */
.hero-name {
    font-family: 'Cinzel', serif !important;
    font-size: 2.6rem !important;
    font-weight: 700 !important;
    color: #e8d5a3 !important;
    line-height: 1.2;
    margin-bottom: 0.2rem;
}
.hero-sub {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    color: #8b949e !important;
    margin-bottom: 1.2rem;
}
.section-label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.7rem !important;
    color: #e8d5a3 !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
    opacity: 0.7;
}
.internship-callout {
    background: linear-gradient(135deg, #12181f 0%, #0d1117 100%);
    border: 1px solid #2d3018;
    border-left: 3px solid #e8d5a3;
    border-radius: 0 8px 8px 0;
    padding: 1.5rem 2rem;
    margin-top: 1rem;
}
.internship-callout p {
    color: #c9d1d9 !important;
    font-style: italic;
    font-size: 0.93rem !important;
    line-height: 1.8 !important;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    # Profile image
    import os
    profile_path = "assets/profile.jpg"
    if os.path.exists(profile_path):
        st.image(profile_path, use_container_width=True, caption="Kurt Justin J. Malubay")
    else:
        st.image(
            "https://via.placeholder.com/300x300/161b22/e8d5a3?text=KJM",
            use_container_width=True,
            caption="Kurt Justin J. Malubay",
        )

    st.markdown("---")
    st.markdown("<p class='section-label'>Contact</p>", unsafe_allow_html=True)
    st.markdown("""
<div style="line-height:2;">
  📧 <a href='mailto:justinkurt837@gmail.com' style='color:#a8b3c1;text-decoration:none;font-size:0.82rem;'>justinkurt837@gmail.com</a><br>
  📱 <span style='color:#a8b3c1;font-size:0.82rem;'>09928330407</span><br>
  💻 <a href='https://github.com/KurtJustinMalubay' target='_blank' style='color:#a8b3c1;text-decoration:none;font-size:0.82rem;'>github.com/KurtJustinMalubay</a><br>
  🎮 <a href='https://sashimiproductions.itch.io/' target='_blank' style='color:#a8b3c1;text-decoration:none;font-size:0.82rem;'>sashimiproductions.itch.io</a>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<p class='section-label'>Quick Stats</p>", unsafe_allow_html=True)
    st.metric("Year Level", "3rd Year")
    st.metric("Scholarship", "CHED Merit")
    st.metric("Projects", "2 Shipped")

    st.markdown("---")
    st.markdown("<p class='section-label'>Filter Skills</p>", unsafe_allow_html=True)
    skill_filter = st.slider("Min proficiency (%)", min_value=0, max_value=100, value=0, step=5)

    show_tools = st.checkbox("Show tool badges on projects", value=True)

    st.markdown("---")
    st.markdown(
        "<p style='font-size:0.72rem;color:#484f58;text-align:center;'>⚔️ Built with Streamlit · 2026</p>",
        unsafe_allow_html=True,
    )


# ─── Header ─────────────────────────────────────────────────────────────────────
col_h1, col_h2 = st.columns([2, 1])
with col_h1:
    st.markdown("<p class='section-label'>Portfolio · 2026</p>", unsafe_allow_html=True)
    st.markdown("<p class='hero-name'>Kurt Justin J. Malubay</p>", unsafe_allow_html=True)
    st.markdown(
        "<p class='hero-sub'>BSCS 3-F1 · Cebu Institute of Technology – University · Expected 2028 · CHED Merit Scholar</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<span class='tag-gold'>Game Developer</span>"
        "<span class='badge'>Computer Science</span>"
        "<span class='badge'>C# / Godot</span>"
        "<span class='badge'>Unity</span>"
        "<span class='badge'>Python</span>",
        unsafe_allow_html=True,
    )

with col_h2:
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Year", "3rd")
    c2.metric("Status", "Scholar")
    c3.metric("Projects", "2")

st.markdown("---")


# ─── Tab Navigation ──────────────────────────────────────────────────────────────
tab_bio, tab_skills, tab_projects, tab_contact = st.tabs(
    ["✦ Autobiography", "✦ Skills", "✦ Projects", "✦ Contact"]
)


# ════════════════════════════════════════════════════════════════════════════════
# TAB 1 — AUTOBIOGRAPHY
# ════════════════════════════════════════════════════════════════════════════════
with tab_bio:
    st.markdown("### A Story From the Provinces to the Code")
    st.write(
        "Computer Science student, game developer, and curious tinkerer — born at the confluence "
        "of sea and mountain in Southern Leyte, now building digital worlds from a desk in Cebu."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Chapters presented as radio-driven accordion so the user navigates at their own pace
    chapter_options = [
        "🌊  Childhood & Background",
        "✨  The Spark of Curiosity",
        "🎓  Education & Transition",
        "💻  Current Life & Outlook",
    ]
    selected_chapter = st.radio(
        "Read a chapter:",
        chapter_options,
        horizontal=True,
        label_visibility="collapsed",
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if selected_chapter == chapter_options[0]:
        st.markdown("""
<div class='card-gold'>
<h3>Childhood & Background</h3>
<p>
I grew up in <strong style='color:#e8d5a3;'>San Juan, Southern Leyte</strong> — a quiet municipality
where the sea stretches to the horizon in one direction and green mountain slopes press in from the other.
Life there moved slowly and deliberately, and I absorbed that pace.
</p>
<p>
As a child I spent hours watching how things worked: how water carved paths through soil after rain,
how the tides followed a rhythm I could eventually predict, how a broken radio could be coaxed
back to life with enough patience and the right nudge. That instinct — to understand systems from the inside —
turned out to be the earliest version of the programmer I am becoming.
</p>
</div>
""", unsafe_allow_html=True)

    elif selected_chapter == chapter_options[1]:
        st.markdown("""
<div class='card-gold'>
<h3>The Spark of Curiosity</h3>
<p>
The turning point arrived when my mother came home with a <strong style='color:#e8d5a3;'>BlackBerry phone</strong>.
That small, rectangular device felt impossibly sophisticated — a world compressed into glass and circuitry.
I was transfixed less by the phone itself than by the idea that a person could <em>make</em> something like that.
</p>
<p>
The catalyst that crystallised everything was <strong style='color:#e8d5a3;'>Assassin's Creed</strong>.
Playing it didn't just entertain me — it rewired something. The open world, the systems layered on systems,
the narrative stitched into the architecture: I needed to know how that was built, and who built it.
</p>
<p>
That curiosity carried me through elementary school at
<strong style='color:#e8d5a3;'>San Juan Central Elementary School</strong> (until 2018)
and high school at <strong style='color:#e8d5a3;'>San Juan National High School</strong> (until 2024),
where I quietly fed a growing obsession with software, games, and the logic underneath both.
</p>
</div>
""", unsafe_allow_html=True)

    elif selected_chapter == chapter_options[2]:
        st.markdown("""
<div class='card-gold'>
<h3>Education & Transition to College</h3>
<p>
After high school I navigated the gauntlet of university entrance exams and passed several —
but <strong style='color:#e8d5a3;'>Cebu Institute of Technology – University (CIT-U)</strong>
stood apart. Its Computer Science programme has a reputation for being genuinely competitive,
and competitive is what I needed: an environment that would sharpen me rather than accommodate complacency.
</p>
<p>
The early semesters were a reckoning. Shifting from provincial public school rhythms to a rigorous
CS curriculum demanded a full reinvention of how I studied and how I thought.
Game development became my survival mechanism — every new concept I could connect to a mechanic,
a shader, or a system in a project I cared about, I retained. Theory met practice, and I stayed afloat.
</p>
</div>
""", unsafe_allow_html=True)

    elif selected_chapter == chapter_options[3]:
        st.markdown("""
<div class='card-gold'>
<h3>Current Life & Outlook</h3>
<p>
Today I am a <strong style='color:#e8d5a3;'>3rd-year BS Computer Science student</strong>
at CIT-U, holding a <strong style='color:#e8d5a3;'>CHED Merit Scholarship</strong>.
By this point in the programme I have built solid foundations in Data Structures & Algorithms
and Design & Analysis of Algorithms — the bedrock that makes everything else learnable fast.
</p>
<p>
Outside coursework I collaborate with peers on game and software projects, currently
serving as Project Manager, Environment Artist, and UI/UX Designer on
<em style='color:#e8d5a3;'>Infinitus</em>, a multiplayer wizard battle game in Godot 4.
I believe the best engineers are made at the intersection of deep fundamentals and hands-on craft —
and I'm building both simultaneously.
</p>
</div>
""", unsafe_allow_html=True)

    # Internship callout inside bio tab
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div class='internship-callout'>
<p class='section-label' style='margin-bottom:0.6rem;'>Open to Opportunities</p>
<p>
Actively seeking internship opportunities where I can apply my foundational computer science background,
game development experience, and passion for optimised software engineering.
Eager to learn from industry mentors, tackle complex engineering challenges, and contribute meaningfully
to innovative tech and gaming teams.
</p>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# TAB 2 — SKILLS
# ════════════════════════════════════════════════════════════════════════════════
with tab_skills:
    st.markdown("### Technical Proficiency")

    st.markdown("""
<div class='card'>
<p>
By the third year of a rigorous CS programme, the most valuable outcome is not expert mastery
of every framework — it is the <strong style='color:#e8d5a3;'>solid core fundamentals</strong>
(Data Structures, Algorithm Design & Analysis) that make picking up any new tool
a matter of days rather than months. The percentages below reflect genuine working confidence
with each language, not marketing copy.
</p>
</div>
""", unsafe_allow_html=True)

    # ── Skill Data ──
    skill_data = {
        "Language": ["C#", "C++", "C", "Python"],
        "Proficiency (%)": [78, 75, 70, 50],
        "Primary Context": ["Godot 4 / Unity game dev", "Systems / coursework", "Low-level / coursework", "Data science / automation"],
        "Confidence Note": ["Primary language", "Comfortable", "Comfortable", "Actively growing"],
    }
    df_skills = pd.DataFrame(skill_data)

    # Apply sidebar filter
    df_filtered = df_skills[df_skills["Proficiency (%)"] >= skill_filter].reset_index(drop=True)

    col_t, col_c = st.columns([1, 1], gap="large")

    with col_t:
        st.markdown("<p class='section-label'>Proficiency Table</p>", unsafe_allow_html=True)
        if df_filtered.empty:
            st.info("No languages meet the current filter. Lower the slider on the left.")
        else:
            st.dataframe(
                df_filtered,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Language": st.column_config.TextColumn("Language"),
                    "Proficiency (%)": st.column_config.ProgressColumn(
                        "Proficiency",
                        min_value=0,
                        max_value=100,
                        format="%d%%",
                    ),
                    "Primary Context": st.column_config.TextColumn("Used For"),
                    "Confidence Note": st.column_config.TextColumn("Level"),
                },
            )

    with col_c:
        st.markdown("<p class='section-label'>Visual Comparison</p>", unsafe_allow_html=True)
        if not df_filtered.empty:
            chart_df = df_filtered.set_index("Language")[["Proficiency (%)"]]
            st.bar_chart(chart_df, color="#e8d5a3", use_container_width=True, height=260)
        else:
            st.info("No data to chart.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p class='section-label'>Also Comfortable With</p>", unsafe_allow_html=True)
    additional_tools = {
        "Godot 4": "Game engine (primary)",
        "Unity": "Game engine (prototyping)",
        "Blender": "3D modelling & environment art",
        "Figma": "UI/UX design",
        "Aseprite": "2D pixel art & sprites",
        "Git": "Version control",
    }
    tool_cols = st.columns(3)
    for i, (tool, desc) in enumerate(additional_tools.items()):
        with tool_cols[i % 3]:
            st.markdown(f"""
<div class='card' style='padding:0.9rem 1.1rem;margin-bottom:0.6rem;'>
  <p style='color:#e8d5a3;font-weight:600;margin-bottom:0.1rem;font-size:0.88rem;'>{tool}</p>
  <p style='color:#8b949e;font-size:0.78rem;margin:0;'>{desc}</p>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# TAB 3 — PROJECTS
# ════════════════════════════════════════════════════════════════════════════════
with tab_projects:
    st.markdown("### Shipped Projects")

    # ── Project selector ──
    selected_project = st.selectbox(
        "Browse project:",
        ["Infinitus — Multiplayer Wizard Battle", "TLGMS — The Last Glensh Man Standing"],
        label_visibility="visible",
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if selected_project.startswith("Infinitus"):
        p_col1, p_col2 = st.columns([1, 1], gap="large")

        with p_col1:
            inf_path = "assets/infinitus.jpg"
            if os.path.exists(inf_path):
                st.image(inf_path, use_container_width=True, caption="Infinitus — in-engine screenshot")
            else:
                st.image(
                    "https://via.placeholder.com/600x340/161b22/e8d5a3?text=Infinitus",
                    use_container_width=True,
                    caption="Infinitus — placeholder",
                )

        with p_col2:
            st.markdown("""
<div class='card'>
<h3>Infinitus</h3>
<p style='color:#8b949e;font-size:0.8rem;margin-bottom:0.8rem;'>Multiplayer · Godot 4 · C# · 2025 – 2026</p>
<p>
A multiplayer wizard battle game where players cast spells and navigate a meticulously crafted environment.
Each arena is hand-designed to reward spatial awareness, and the spell system balances reaction speed
against strategic cooldown management.
</p>
</div>
""", unsafe_allow_html=True)

            st.markdown("""
<div class='card' style='padding:0.9rem 1.2rem;'>
<p class='section-label'>My Roles</p>
<p>Project Manager · Environment Artist · Model Designer<br>
Skill Effects Designer · UI/UX Designer · Sound Designer</p>
<p style='margin-top:0.6rem;'><em style='color:#8b949e;font-size:0.82rem;'>
Coordinated requirement definitions and scoped tasks across the team throughout the full dev cycle.
</em></p>
</div>
""", unsafe_allow_html=True)

            st.markdown("""
<div class='card' style='padding:0.9rem 1.2rem;'>
<p class='section-label'>Collaborators</p>
<p>Glenshayne Belarmino &nbsp;·&nbsp; Wilmark Racho</p>
</div>
""", unsafe_allow_html=True)

            if show_tools:
                st.markdown(
                    "<p class='section-label'>Built With</p>"
                    "<span class='tag-gold'>Godot 4</span>"
                    "<span class='badge'>C#</span>"
                    "<span class='badge'>Blender</span>"
                    "<span class='badge'>Figma</span>"
                    "<span class='badge'>Audio Tools</span>",
                    unsafe_allow_html=True,
                )

    else:
        p_col1, p_col2 = st.columns([1, 1], gap="large")

        with p_col1:
            tlg_path = "assets/tlgms.jpg"
            if os.path.exists(tlg_path):
                st.image(tlg_path, use_container_width=True, caption="TLGMS — gameplay screenshot")
            else:
                st.image(
                    "https://via.placeholder.com/600x340/161b22/e8d5a3?text=TLGMS",
                    use_container_width=True,
                    caption="TLGMS — placeholder",
                )

        with p_col2:
            st.markdown("""
<div class='card'>
<h3>TLGMS</h3>
<p style='color:#8b949e;font-size:0.8rem;margin-bottom:0.8rem;'>Survival Shooter · Unity · C# · 2024 (1st-year prototype)</p>
<p>
<em>The Last Glensh Man Standing</em> is a survival shooting game set on the war-torn world of
<strong style='color:#e8d5a3;'>Earth 122</strong>. As the last surviving member of the Glensh species,
the player fights relentless waves of enemies in a desperate struggle for survival.
</p>
<p>
Originally conceived as a 3D RPG-style shooter with a 45-degree top-down camera, TLGMS was my
first complete game prototype — built entirely solo after the first year of university to prove
the concept and validate the workflow.
</p>
</div>
""", unsafe_allow_html=True)

            st.markdown("""
<div class='card' style='padding:0.9rem 1.2rem;'>
<p class='section-label'>My Role</p>
<p>Sole Developer — concept, design, code, and assets, start to finish.</p>
</div>
""", unsafe_allow_html=True)

            if show_tools:
                st.markdown(
                    "<p class='section-label'>Built With</p>"
                    "<span class='tag-gold'>Unity</span>"
                    "<span class='badge'>C#</span>"
                    "<span class='badge'>Aseprite</span>",
                    unsafe_allow_html=True,
                )

    st.markdown("---")

    # ── Internship callout in projects tab ──
    st.markdown("""
<div class='internship-callout'>
<p class='section-label' style='margin-bottom:0.6rem;'>Looking for Internship</p>
<p>
Actively seeking internship opportunities where I can apply my foundational computer science background,
game development experience, and passion for optimised software engineering.
Eager to learn from industry mentors, tackle complex engineering challenges, and contribute meaningfully
to innovative tech and gaming teams.
</p>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# TAB 4 — CONTACT / FEEDBACK
# ════════════════════════════════════════════════════════════════════════════════
with tab_contact:
    st.markdown("### Get in Touch")
    st.write("Whether you have an internship opening, a project idea, or just want to connect — feel free to reach out.")

    st.markdown("<br>", unsafe_allow_html=True)

    c_left, c_right = st.columns([3, 2], gap="large")

    with c_left:
        with st.form("contact_form", clear_on_submit=True):
            st.markdown("<p class='section-label'>Send a Message</p>", unsafe_allow_html=True)

            form_name = st.text_input("Your name", placeholder="e.g. Jane Santos")
            form_email = st.text_input("Your email", placeholder="e.g. jane@company.com")
            form_subject = st.selectbox(
                "Subject",
                ["Internship Opportunity", "Project Collaboration", "General Inquiry", "Other"],
            )
            form_message = st.text_area(
                "Message",
                placeholder="Write your message here...",
                height=140,
            )

            submitted = st.form_submit_button("Send Message")

            if submitted:
                if form_name.strip() and form_email.strip() and form_message.strip():
                    st.success(
                        f"Message received — thank you, {form_name.split()[0]}! "
                        "Kurt will get back to you soon."
                    )
                else:
                    st.warning("Please fill in all required fields before sending.")

    with c_right:
        st.markdown("""
<div class='card' style='margin-bottom:0.8rem;'>
<p class='section-label'>Direct Contact</p>
<p>📧 <a href='mailto:justinkurt837@gmail.com' style='color:#a8b3c1;'>justinkurt837@gmail.com</a></p>
<p>📱 09928330407</p>
</div>
<div class='card' style='margin-bottom:0.8rem;'>
<p class='section-label'>Online Profiles</p>
<p>💻 <a href='https://github.com/KurtJustinMalubay' target='_blank' style='color:#a8b3c1;'>GitHub</a></p>
<p>🎮 <a href='https://sashimiproductions.itch.io/' target='_blank' style='color:#a8b3c1;'>Itch.io</a></p>
</div>
<div class='card'>
<p class='section-label'>Location</p>
<p>Cebu City, Philippines</p>
<p style='font-size:0.8rem;color:#8b949e;'>Open to remote internships and Cebu-based on-site roles.</p>
</div>
""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⬇  Download Resume (placeholder)"):
            st.info("Resume download would be wired to a PDF in production.")