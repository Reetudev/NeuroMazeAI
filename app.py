import streamlit as st
import streamlit.components.v1 as components
import random

# PAGE CONFIG
st.set_page_config(
    page_title="NeuroMaze AI - Toy Edition",
    page_icon="🧠",
    layout="wide"
)

# ==========================================
# 1. ANIMATED TOYS (CSS/HTML)
# ==========================================

# Function to render the toys
def render_toy(toy_type):
    # CSS Styles for Toys
    st.markdown(f"""
    <style>
        /* Container to center the toy */
        .toy-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 150px;
            margin-bottom: 20px;
            perspective: 200px;
        }}
        
        /* --- TOY DEFINITIONS --- */

        /* 1. ROBOT DOLL (Home) */
        .robot-toy {{
            width: 60px; height: 80px;
            background: #00f2ff;
            border-radius: 10px;
            position: relative;
            animation: robot-dance 1s infinite alternate;
            box-shadow: 0 0 15px #00f2ff;
        }}
        .robot-toy::before {{ /* Head */
            content: ''; position: absolute; top: -30px; left: 10px;
            width: 40px; height: 30px; background: #00f2ff;
            border-radius: 10px 10px 0 0;
        }}
        .robot-toy::after {{ /* Eyes */
            content: ''; position: absolute; top: -20px; left: 20px;
            width: 20px; height: 10px; background: #000;
            box-shadow: 5px 0 0 #fff;
        }}
        @keyframes robot-dance {{
            0% {{ transform: rotate(-10deg) translateY(0); }}
            100% {{ transform: rotate(10deg) translateY(-10px); }}
        }}

        /* 2. SPINNING TOP (System Design) */
        .spinner-toy {{
            width: 0; height: 0;
            border-left: 30px solid transparent;
            border-right: 30px solid transparent;
            border-bottom: 60px solid #ff0055;
            animation: spin-me 2s infinite linear;
            filter: drop-shadow(0 0 10px #ff0055);
        }}
        @keyframes spin-me {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}

        /* 3. BOUNCING BALL (Code Breaker) */
        .ball-toy {{
            width: 50px; height: 50px;
            background: radial-gradient(circle at 10px 10px, #fff, #8c00ff);
            border-radius: 50%;
            animation: bounce-me 0.6s infinite alternate;
            box-shadow: 0 0 20px #8c00ff;
        }}
        @keyframes bounce-me {{
            0% {{ transform: translateY(0) scaleX(1.1); }}
            100% {{ transform: translateY(-40px) scaleX(1); }}
        }}

        /* 4. WOBBLING DOLL (Cloud) */
        .doll-toy {{
            width: 60px; height: 80px;
            background: #ffcc00;
            border-radius: 30px 30px 10px 10px;
            position: relative;
            animation: wobble-me 2s infinite ease-in-out;
            box-shadow: 0 0 15px #ffcc00;
        }}
        .doll-toy::before {{ /* Head */
            content: ''; position: absolute; top: -25px; left: 10px;
            width: 40px; height: 40px; background: #fff;
            border-radius: 50%; border: 3px solid #ffcc00;
        }}
        @keyframes wobble-me {{
            0%, 100% {{ transform: rotate(-15deg); }}
            50% {{ transform: rotate(15deg); }}
        }}

        /* 5. FLOATING CUBE (Generic) */
        .cube-toy {{
            width: 50px; height: 50px;
            background: linear-gradient(45deg, #00f2ff, #ff0055);
            animation: float-me 3s infinite ease-in-out;
            box-shadow: 0 0 15px rgba(0, 242, 255, 0.5);
            border-radius: 5px;
        }}
        @keyframes float-me {{
            0%, 100% {{ transform: translateY(0) rotate(0deg); }}
            50% {{ transform: translateY(-20px) rotate(180deg); }}
        }}
        
        /* 6. PULSING STAR */
        .star-toy {{
            font-size: 60px;
            color: #ff0055;
            animation: pulse-star 1s infinite alternate;
            text-shadow: 0 0 20px #ff0055;
        }}
        @keyframes pulse-star {{
            0% {{ transform: scale(0.8) rotate(0deg); opacity: 0.7; }}
            100% {{ transform: scale(1.2) rotate(20deg); opacity: 1; }}
        }}
    </style>
    """, unsafe_allow_html=True)
    
    # HTML to render specific toy
    html = f"<div class='toy-container'><div class='{toy_type}'></div></div>"
    st.markdown(html, unsafe_allow_html=True)

# ==========================================
# 2. DATA: QUESTION BANKS WITH TOY TYPES
# ==========================================

system_questions = [
    {"q": "A streaming platform receives millions of requests during live events. Which technology helps distribute user traffic efficiently across multiple servers?", "options": ["Compiler", "Load Balancer", "Variable", "Loop"], "ans": "Load Balancer", "info": "Load balancing is critical for high-availability systems.", "toy": "spinner-toy"},
    {"q": "Which database type is best suited for storing unstructured data like social media posts?", "options": ["Relational DB", "NoSQL", "Spreadsheet", "File System"], "ans": "NoSQL", "info": "NoSQL databases handle flexible schemas efficiently.", "toy": "cube-toy"},
    {"q": "What pattern is used to prevent a system from crashing when a remote service is down?", "options": ["Adapter Pattern", "Circuit Breaker", "Singleton", "Observer"], "ans": "Circuit Breaker", "info": "Circuit Breaker pattern increases system resilience.", "toy": "robot-toy"},
    {"q": "Which caching strategy writes data to the cache and the database simultaneously?", "options": ["Write-through", "Write-back", "Read-through", "Lazy Loading"], "ans": "Write-through", "info": "Write-through ensures data consistency.", "toy": "spinner-toy"},
    {"q": "In Microservices architecture, which component acts as a single entry point for all client requests?", "options": ["API Gateway", "Load Balancer", "Database", "Message Queue"], "ans": "API Gateway", "info": "API Gateway handles routing and protocol translation.", "toy": "cube-toy"},
    {"q": "According to the CAP Theorem, which property ensures every request receives a response?", "options": ["Consistency", "Availability", "Partition Tolerance", "Durability"], "ans": "Availability", "info": "Availability ensures the system stays operational.", "toy": "robot-toy"},
    {"q": "What mechanism allows two different services to communicate asynchronously?", "options": ["HTTP Request", "Message Queue", "Function Call", "WebSocket"], "ans": "Message Queue", "info": "Message Queues decouple services for better scaling.", "toy": "spinner-toy"},
    {"q": "Which technique routes a user's request to the nearest server location?", "options": ["DNS Routing", "GeoDNS", "Round Robin", "Firewall"], "ans": "GeoDNS", "info": "GeoDNS reduces latency by serving content locally.", "toy": "cube-toy"}
]

code_questions = [
    {"q": "Convert the binary value '1010' to decimal.", "options": ["8", "10", "12", "16"], "ans": "10", "info": "Binary 1010 equals 10.", "toy": "ball-toy"},
    {"q": "What is the time complexity of searching in a sorted array using Binary Search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "ans": "O(log n)", "info": "Binary Search halves the search space every step.", "toy": "star-toy"},
    {"q": "Which data structure operates on a LIFO (Last In, First Out) principle?", "options": ["Queue", "Stack", "Array", "Tree"], "ans": "Stack", "info": "Stacks are used in function call management.", "toy": "cube-toy"},
    {"q": "In cybersecurity, what is 'SQL Injection'?", "options": ["A virus", "A code injection technique", "A firewall", "An encryption"], "ans": "A code injection technique", "info": "SQL Injection inserts malicious queries.", "toy": "ball-toy"},
    {"q": "What does 'HTTPS' stand for?", "options": ["HyperText Transfer Protocol Secure", "High Tech Protocol", "HyperText Transit", "Home Transfer"], "ans": "HyperText Transfer Protocol Secure", "info": "HTTPS encrypts communication.", "toy": "star-toy"},
    {"q": "What is the primary function of a 'Hash Function'?", "options": ["Encrypt emails", "Generate fixed-size output", "Speed up internet", "Create backups"], "ans": "Generate fixed-size output", "info": "Hash functions are essential for integrity.", "toy": "cube-toy"},
    {"q": "Which Git command saves changes to the local repository?", "options": ["git push", "git commit", "git add", "git pull"], "ans": "git commit", "info": "Git commit creates a snapshot.", "toy": "ball-toy"},
    {"q": "What is the Hexadecimal representation of decimal 15?", "options": ["A", "F", "10", "Z"], "ans": "F", "info": "Hexadecimal uses 0-9 and A-F.", "toy": "star-toy"}
]

cloud_questions = [
    {"q": "Which cloud service model provides virtual machines and storage?", "options": ["SaaS", "PaaS", "IaaS", "DNS"], "ans": "IaaS", "info": "IaaS offers raw computing resources.", "toy": "doll-toy"},
    {"q": "What technology packages an application with its dependencies?", "options": ["Virtual Machine", "Container (Docker)", "Bare Metal", "Compiler"], "ans": "Container (Docker)", "info": "Containers ensure consistency.", "toy": "cube-toy"},
    {"q": "Which AWS service is used for object storage?", "options": ["EC2", "Lambda", "S3", "DynamoDB"], "ans": "S3", "info": "Amazon S3 is standard for storage.", "toy": "doll-toy"},
    {"q": "What does 'Serverless' computing eliminate the need for?", "options": ["Writing Code", "Managing Servers", "Internet", "Databases"], "ans": "Managing Servers", "info": "Serverless focuses on code logic.", "toy": "star-toy"},
    {"q": "What does CI/CD stand for?", "options": ["Continuous Integration / Deployment", "Central Intelligence", "Computer Design", "Cloud Data"], "ans": "Continuous Integration / Deployment", "info": "CI/CD automates delivery.", "toy": "doll-toy"},
    {"q": "Which tool is used for container orchestration?", "options": ["Docker", "Kubernetes", "Jenkins", "Ansible"], "ans": "Kubernetes", "info": "Kubernetes manages containers.", "toy": "cube-toy"},
    {"q": "What is the main benefit of a CDN?", "options": ["Security", "Low Latency", "Storage", "Coding"], "ans": "Low Latency", "info": "CDNs reduce load times.", "toy": "doll-toy"},
    {"q": "Which cloud model is exclusive to a single organization?", "options": ["Public Cloud", "Private Cloud", "Hybrid Cloud", "Community Cloud"], "ans": "Private Cloud", "info": "Private clouds offer greater security.", "toy": "star-toy"}
]

# ==========================================
# 3. CSS & THEME (Glassmorphism)
# ==========================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');
    
    .stApp {
        background: #050510;
        background-image: radial-gradient(circle at 10% 20%, #1a0b2e 0%, #050510 90%);
        font-family: 'Rajdhani', sans-serif;
        color: #fff;
    }
    
    .glass-card {
        background: rgba(10, 10, 26, 0.7);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        border-color: rgba(0, 242, 255, 0.3);
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.2);
    }

    h1, h2, h3 { font-family: 'Orbitron', sans-serif; text-transform: uppercase; letter-spacing: 2px; }
    
    .hero-title {
        font-size: 3rem;
        background: linear-gradient(to right, #00f2ff, #ff0055);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
    }
    
    .stButton>button {
        background: transparent; border: 2px solid #00f2ff; color: #00f2ff;
        font-family: 'Orbitron', sans-serif; font-weight: 700; padding: 12px 30px;
        border-radius: 10px; transition: 0.3s; width: 100%;
    }
    
    .stButton>button:hover {
        background: #00f2ff; color: #000; box-shadow: 0 0 20px #00f2ff;
    }
    
    div[role="radiogroup"] { padding: 10px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.1); }
    
    label[data-baseweb="radio"] {
        background: rgba(255, 255, 255, 0.05); border-radius: 8px;
        padding: 10px 15px; margin: 5px 0; border: 1px solid transparent; transition: 0.2s;
    }
    
    label[data-baseweb="radio"]:hover {
        border-color: #ff0055; background: rgba(255, 0, 85, 0.1);
    }

    .score-card {
        font-size: 1.5rem; color: #ff0055; text-align: center;
        font-family: 'Orbitron', sans-serif; text-shadow: 0 0 10px rgba(255, 0, 85, 0.5);
    }
    
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. SESSION STATES
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "home"
    
if "score" not in st.session_state:
    st.session_state.score = 0
    
if "sys_q_idx" not in st.session_state:
    st.session_state.sys_q_idx = random.randint(0, len(system_questions)-1)
    
if "code_q_idx" not in st.session_state:
    st.session_state.code_q_idx = random.randint(0, len(code_questions)-1)
    
if "cloud_q_idx" not in st.session_state:
    st.session_state.cloud_q_idx = random.randint(0, len(cloud_questions)-1)


# ==========================================
# 5. UI RENDERING
# ==========================================

# HERO SECTION
st.markdown("""
<div class='glass-card' style='text-align: center; border: none; background: transparent;'>
    <h1 class='hero-title'>NEUROMAZE AI</h1>
    <p style='color: #aaa; letter-spacing: 1px;'>COMPETITION EDITION • FUN MODE</p>
</div>
""", unsafe_allow_html=True)

# TEAM SECTION
st.markdown("""
<div class='glass-card' style='text-align: center; margin-top: -20px;'>
    <h3 style='color: #ff0055; margin: 0;'>TEAM NEUROMAZE</h3>
    <p style='font-size: 1.1rem; margin-top: 5px;'>
        🤩 REETU &nbsp; 💗 MANJULA &nbsp; 🚀 SANJANA &nbsp; 😎 PUSHPA
    </p>
</div>
""", unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == "home":
    
    # Render Robot Toy on Home
    render_toy("robot-toy")
    
    st.markdown("""
    <div class='glass-card' style='text-align: center;'>
        <h2 style='color: #00f2ff;'>WELCOME, BCA BUDDIES</h2>
        <p>Choose your path. Solve challenges. Have fun!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🧠 SYSTEM DESIGN"):
            st.session_state.page = "system"
            st.rerun()
            
    with col2:
        if st.button("🔐 AI CODE BREAKER"):
            st.session_state.page = "code"
            st.rerun()
            
    with col3:
        if st.button("☁️ CLOUD MAZE"):
            st.session_state.page = "cloud"
            st.rerun()
            
    st.write("")
    st.markdown(f"<div class='glass-card score-card'>CURRENT SCORE: {st.session_state.score}</div>", unsafe_allow_html=True)


# --- SYSTEM DESIGN PAGE ---
elif st.session_state.page == "system":
    
    q_data = system_questions[st.session_state.sys_q_idx]
    
    # Render unique toy for this question
    render_toy(q_data['toy'])
    
    st.markdown("<div class='glass-card'><h2 style='color: #00f2ff;'>SYSTEM DESIGN CHALLENGE</h2></div>", unsafe_allow_html=True)
    st.warning(f"**QUESTION:**\n\n{q_data['q']}")
    answer = st.radio("Select Answer:", q_data['options'], key="sys_radio")
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        if st.button("✅ SUBMIT", key="sys_submit"):
            if answer == q_data['ans']:
                st.success("✅ Correct! System Stable.")
                st.balloons()
                st.session_state.score += 10
                st.session_state.sys_q_idx = random.randint(0, len(system_questions)-1)
            else:
                st.error("❌ System Failure. Try again.")
                
    with col_b:
        if st.button("🔄 NEXT PUZZLE"):
            st.session_state.sys_q_idx = random.randint(0, len(system_questions)-1)
            st.rerun()

    st.info(f"💡 **INDUSTRY INSIGHT:** {q_data['info']}")
    if st.button("🏠 HOME"):
        st.session_state.page = "home"
        st.rerun()


# --- CODE BREAKER PAGE ---
elif st.session_state.page == "code":
    
    q_data = code_questions[st.session_state.code_q_idx]
    
    # Render unique toy for this question
    render_toy(q_data['toy'])
    
    st.markdown("<div class='glass-card'><h2 style='color: #00ff00;'>AI CODE BREAKER</h2></div>", unsafe_allow_html=True)
    st.warning(f"**CHALLENGE:**\n\n{q_data['q']}")
    answer = st.radio("Decode Answer:", q_data['options'], key="code_radio")
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        if st.button("⚡ DECODE", key="code_submit"):
            if answer == q_data['ans']:
                st.success("🔓 Access Granted.")
                st.balloons()
                st.session_state.score += 10
                st.session_state.code_q_idx = random.randint(0, len(code_questions)-1)
            else:
                st.error("🔒 Firewall Blocked. Incorrect.")
                
    with col_b:
        if st.button("🔄 NEXT HACK"):
            st.session_state.code_q_idx = random.randint(0, len(code_questions)-1)
            st.rerun()

    st.info(f"💡 **LOGIC INSIGHT:** {q_data['info']}")
    if st.button("🏠 HOME"):
        st.session_state.page = "home"
        st.rerun()


# --- CLOUD MAZE PAGE ---
elif st.session_state.page == "cloud":
    
    q_data = cloud_questions[st.session_state.cloud_q_idx]
    
    # Render unique toy for this question
    render_toy(q_data['toy'])
    
    st.markdown("<div class='glass-card'><h2 style='color: #ff0055;'>CLOUD ARCHITECTURE MAZE</h2></div>", unsafe_allow_html=True)
    st.warning(f"**MISSION:**\n\n{q_data['q']}")
    answer = st.radio("Deploy Solution:", q_data['options'], key="cloud_radio")
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        if st.button("☁️ DEPLOY", key="cloud_submit"):
            if answer == q_data['ans']:
                st.success("🚀 Deployment Successful.")
                st.balloons()
                st.session_state.score += 10
                st.session_state.cloud_q_idx = random.randint(0, len(cloud_questions)-1)
            else:
                st.error("⚠️ Infrastructure Error.")
                
    with col_b:
        if st.button("🔄 NEW MISSION"):
            st.session_state.cloud_q_idx = random.randint(0, len(cloud_questions)-1)
            st.rerun()

    st.info(f"💡 **CLOUD INSIGHT:** {q_data['info']}")
    if st.button("🏠 HOME"):
        st.session_state.page = "home"
        st.rerun()

# FOOTER
st.write("---")
st.markdown(f"""
<div style='text-align: center; padding: 20px; opacity: 0.6;'>
    <p>⚡ NeuroMaze AI • Toy Edition • {st.session_state.score} Points Scored ⚡</p>
</div>
""", unsafe_allow_html=True)