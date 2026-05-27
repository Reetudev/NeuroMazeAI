import streamlit as st
import random

# PAGE CONFIG

st.set_page_config(
    page_title="NeuroMaze AI",
    page_icon="🧠",
    layout="wide"
)

# LOAD CSS

with open("assets/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# BACKGROUND MUSIC

audio_file = open("assets/sounds/background.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mp3", loop=True)

# SESSION STATES

if "page" not in st.session_state:
    st.session_state.page = "home"

if "score" not in st.session_state:
    st.session_state.score = 0

# HERO SECTION

st.markdown("""
<div class='hero-box'>

<h1>🧠 NeuroMaze AI</h1>

<h2>🚀 AI Engineering Puzzle Platform</h2>

<p>
Cyberpunk • AI Challenges • Developer Logic • Engineering Puzzles
</p>

</div>
""", unsafe_allow_html=True)

# TEAM SECTION

st.markdown("""
<div class='team-box'>

<h2>🌈 TEAM NEUROMAZE 🌈</h2>

<h3>
🤩 REETU &nbsp;&nbsp; 💗 MANJULA &nbsp;&nbsp; 🚀 SANJANA &nbsp;&nbsp; 😎 PUSHPA
</h3>

<p>
⚡ Smart Logic + AI + Innovation ⚡
</p>

</div>
""", unsafe_allow_html=True)

# HOME PAGE

if st.session_state.page == "home":

    st.image(
        "https://images.unsplash.com/photo-1518770660439-4636190af475",
        use_container_width=True
    )

    st.markdown("""
    <div class='feature-card'>

    <h2>🎮 Welcome To NeuroMaze AI</h2>

    <p>
    NeuroMaze AI is a futuristic engineering puzzle platform
    designed for developers, engineers and AI enthusiasts.
    Solve real-world inspired software and logic challenges.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("🧠 SYSTEM DESIGN CHALLENGE"):

            st.session_state.page = "system"
            st.rerun()

    with col2:

        if st.button("🔐 AI CODE BREAKER"):

            st.session_state.page = "code"
            st.rerun()

    with col3:

        if st.button("☁️ CLOUD ARCHITECTURE MAZE"):

            st.session_state.page = "cloud"
            st.rerun()

    st.write("")

    st.image(
        "https://images.unsplash.com/photo-1484417894907-623942c8ee29",
        use_container_width=True
    )

# SYSTEM DESIGN CHALLENGE

elif st.session_state.page == "system":

    st.image(
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3",
        use_container_width=True
    )

    st.markdown("""
    <div class='feature-card'>

    <h2>🧠 SYSTEM DESIGN CHALLENGE</h2>

    <p>
    Solve real-world backend engineering problems
    used in scalable applications.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.warning("""
    QUESTION:

    A streaming platform receives millions of requests
    during live events.

    Which technology helps distribute user traffic
    efficiently across multiple servers?

    A) Compiler
    B) Load Balancer
    C) Variable
    D) Loop
    """)

    answer = st.radio(
        "Choose Correct Answer",
        [
            "Compiler",
            "Load Balancer",
            "Variable",
            "Loop"
        ]
    )

    if st.button("🚀 SUBMIT SYSTEM DESIGN"):

        click_file = open("assets/sounds/click.mp3", "rb")
        click_bytes = click_file.read()

        st.audio(click_bytes, format="audio/mp3")

        if answer == "Load Balancer":

            st.success("🎉 Correct Engineering Solution")

            st.balloons()

            st.session_state.score += 15

        else:

            st.error("❌ Incorrect Answer")

    st.markdown("""
    <div class='feature-card'>

    <h2>💡 INDUSTRY CONNECTION</h2>

    <p>
    Load balancing is widely used in Kubernetes,
    cloud computing, AI systems, DevOps pipelines,
    and scalable web applications.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button("🏠 BACK TO HOME"):

        st.session_state.page = "home"
        st.rerun()

# AI CODE BREAKER

elif st.session_state.page == "code":

    st.image(
        "https://images.unsplash.com/photo-1515879218367-8466d910aaa4",
        use_container_width=True
    )

    st.markdown("""
    <div class='feature-card'>

    <h2>🔐 AI CODE BREAKER</h2>

    <p>
    Decode engineering-based logic puzzles
    used in cybersecurity and AI systems.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.warning("""
    QUESTION:

    Binary values are used in computers.

    Convert this binary to decimal:

    1010

    A) 8
    B) 10
    C) 12
    D) 16
    """)

    answer = st.radio(
        "Choose Correct Answer",
        [
            "8",
            "10",
            "12",
            "16"
        ]
    )

    if st.button("⚡ DECODE ANSWER"):

        click_file = open("assets/sounds/click.mp3", "rb")
        click_bytes = click_file.read()

        st.audio(click_bytes, format="audio/mp3")

        if answer == "10":

            st.success("🎉 Binary Decoded Successfully")

            st.balloons()

            st.session_state.score += 15

        else:

            st.error("❌ Incorrect Conversion")

    st.markdown("""
    <div class='feature-card'>

    <h2>💡 INDUSTRY CONNECTION</h2>

    <p>
    Binary systems are fundamental in
    artificial intelligence, operating systems,
    embedded systems and software engineering.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button("🏠 RETURN HOME"):

        st.session_state.page = "home"
        st.rerun()

# CLOUD ARCHITECTURE MAZE

elif st.session_state.page == "cloud":

    st.image(
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa",
        use_container_width=True
    )

    st.markdown("""
    <div class='feature-card'>

    <h2>☁️ CLOUD ARCHITECTURE MAZE</h2>

    <p>
    Solve infrastructure and cloud computing
    decision-making challenges.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.warning("""
    QUESTION:

    Which cloud service model provides
    virtual machines, storage and networking resources?

    A) SaaS
    B) PaaS
    C) IaaS
    D) DNS
    """)

    answer = st.radio(
        "Choose Correct Answer",
        [
            "SaaS",
            "PaaS",
            "IaaS",
            "DNS"
        ]
    )

    if st.button("☁️ DEPLOY SOLUTION"):

        click_file = open("assets/sounds/click.mp3", "rb")
        click_bytes = click_file.read()

        st.audio(click_bytes, format="audio/mp3")

        if answer == "IaaS":

            st.success("🎉 Cloud Infrastructure Solved")

            st.balloons()

            st.session_state.score += 15

        else:

            st.error("❌ Incorrect Architecture")

    st.markdown("""
    <div class='feature-card'>

    <h2>💡 INDUSTRY CONNECTION</h2>

    <p>
    IaaS platforms like AWS, Azure and Google Cloud
    are widely used in AI deployment,
    DevOps automation and enterprise applications.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button("🏠 GO BACK HOME"):

        st.session_state.page = "home"
        st.rerun()

# SCOREBOARD

st.write("---")

st.markdown(f"""
<div class='score-box'>

🏆 TOTAL SCORE : {st.session_state.score}

</div>
""", unsafe_allow_html=True)

# FOOTER

st.markdown("""
<div class='footer-box'>

<h2>⚡ NeuroMaze AI — Competition Edition ⚡</h2>

<p>
AI • Cloud Computing • Cybersecurity • Engineering Logic • Software Systems
</p>

</div>
""", unsafe_allow_html=True)