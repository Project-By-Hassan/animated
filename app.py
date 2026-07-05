import streamlit as st
import requests
from streamlit_lottie import st_lottie

# =====================================================================
# 1. ARCHITECTURE & BROWSER INTERFACE SETUP
# =====================================================================
st.set_page_config(
    page_title="Hassan Raza | AI & Software Architect",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Helper function for fetching high-fidelity Lottie Vector assets
def load_lottie_telemetry(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# Fetching premium animated vectors
lottie_ai_core = load_lottie_telemetry("https://assets10.lottiefiles.com/packages/lf20_kvt84uoi.json") # Floating AI Brain
lottie_matrix = load_lottie_telemetry("https://assets5.lottiefiles.com/packages/lf20_tl523nbg.json")  # Tech grid element

# =====================================================================
# 2. HIGH-END CINEMATIC GRAPHICS ENGINE (CUSTOM CSS & ANIMATIONS)
# =====================================================================
st.markdown("""
<style>
    /* Dark Sci-Fi Canvas Background */
    .stApp {
        background: radial-gradient(circle at 30% 20%, #0d1117 0%, #07090e 100%);
        color: #e6edf3;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Global Cleanups */
    header, footer, .stDeployButton { visibility: hidden !important; }
    
    /* Neon Text Acceleration & Pulses */
    .hero-title {
        font-size: 65px;
        font-weight: 900;
        letter-spacing: -2px;
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #7f00ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        filter: drop-shadow(0px 4px 20px rgba(0, 242, 254, 0.25));
    }
    
    .hero-subtitle {
        font-size: 24px;
        font-weight: 400;
        color: #00f2fe;
        opacity: 0.9;
        margin-bottom: 25px;
        letter-spacing: 1px;
    }

    /* Premium Futuristic Glassmorphism Panels */
    .premium-panel {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 35px;
        margin-bottom: 30px;
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
    }
    
    /* Interactive Hover Kinetics */
    .premium-panel:hover {
        transform: translateY(-10px) scale(1.01);
        border-color: rgba(0, 242, 254, 0.4);
        box-shadow: 0 30px 60px rgba(0, 242, 254, 0.15);
        background: rgba(255, 255, 255, 0.04);
    }
    
    /* Animated Tech Badges */
    .badge-neon {
        background: linear-gradient(135deg, rgba(0, 242, 254, 0.1), rgba(79, 172, 254, 0.1));
        border: 1px solid rgba(0, 242, 254, 0.3);
        color: #00f2fe;
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 14px;
        font-weight: 600;
        display: inline-block;
        margin: 6px;
        transition: all 0.3s ease;
    }
    .badge-neon:hover {
        background: #00f2fe;
        color: #07090e;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.6);
        transform: scale(1.05);
    }

    /* Project Headers inside panels */
    .project-header {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 0;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# 3. KINETIC HERO INTERACTION GRID
# =====================================================================
hero_left, hero_right = st.columns([3, 2], gap="large")

with hero_left:
    st.markdown('<p class="hero-title">HASSAN RAZA</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Artificial Intelligence & Full-Stack Systems Developer</p>', unsafe_allow_html=True)
    st.write(
        "Architecting high-performance intelligent interfaces, neural network utilities, and interactive web ecosystems. "
        "Leveraging deep Python computation alongside robust layouts to bypass traditional runtime barriers."
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Render Interactive Tags
    st.markdown("""
        <span class="badge-neon">🧠 Generative AI Integration</span>
        <span class="badge-neon">⚡ Python Ecosystems</span>
        <span class="badge-neon">💻 C++ Core Logic</span>
        <span class="badge-neon">🌐 Streamlit & Flet UI</span>
    """, unsafe_allow_html=True)

with hero_right:
    if lottie_ai_core:
        st_lottie(lottie_ai_core, height=350, key="core_intelligence_vector")

st.markdown("<br><br>", unsafe_allow_html=True)

# =====================================================================
# 4. LIVE 3D PARTICLES SHOWROOM (SPLINE INTEGRATION)
# =====================================================================
st.markdown("### 🕹️ 3D Matrix Sandbox Space")
st.write("Drag, spin, and interact dynamically with the live particle architecture mapped directly inside the canvas layer.")

# 3D Mesh Engine Container
spline_mesh_embed = """
<iframe src="https://my.spline.design/futuristicparticles-49635b757e7f78abfb5fa28bc39b2da0/" 
        frameborder="0" width="100%" height="480px" 
        style="border-radius: 24px; border: 1px solid rgba(255, 255, 255, 0.1); background: #07090e;">
</iframe>
"""
st.components.v1.html(spline_mesh_embed, height=490)

st.markdown("<br><br>", unsafe_allow_html=True)

# =====================================================================
# 5. ENTERPRISE PROJECT MATRIX & TIMELINE
# =====================================================================
col_main_showroom, col_side_analytics = st.columns([2, 1], gap="large")

with col_main_showroom:
    st.markdown("### 🚀 Featured Deployments")
    
    # System 1: QR Attendance
    st.markdown("""
    <div class="premium-panel">
        <div class="project-header">📊 Dynamic QR Code Attendance Framework</div>
        <p style="color: #8b949e; font-size: 15px;">A contactless tracking utility engineered via advanced state loops. Optimizes multi-user ingestion seamlessly inside educational environments.</p>
        <div style="margin-top: 15px;">
            <span class="badge-neon" style="font-size:11px; padding:3px 10px;">Python Core</span>
            <span class="badge-neon" style="font-size:11px; padding:3px 10px;">Flet Engine</span>
            <span class="badge-neon" style="font-size:11px; padding:3px 10px;">Security Logic</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # System 2: AI Resume Maker
    st.markdown("""
    <div class="premium-panel">
        <div class="project-header">📄 AI Resume Parser & Telemetry Extractor</div>
        <p style="color: #8b949e; font-size: 15px;">Intelligent semantic text compiler that refactors unstructured PDF inputs into standard corporate templates using pipeline model embeddings.</p>
        <div style="margin-top: 15px;">
            <span class="badge-neon" style="font-size:11px; padding:3px 10px;">LLM Pipeline</span>
            <span class="badge-neon" style="font-size:11px; padding:3px 10px;">PyPDF Extractor</span>
            <span class="badge-neon" style="font-size:11px; padding:3px 10px;">UI Context</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_side_analytics:
    st.markdown("### 🧬 Development Telemetry")
    
    if lottie_matrix:
        st_lottie(lottie_matrix, height=180, key="system_matrix_telemetry")
        
    st.markdown("""
    <div class="premium-panel" style="text-align: center; border-color: rgba(127, 0, 255, 0.3);">
        <h5 style="margin:0; color:#7f00ff; letter-spacing:1px; font-weight:700;">ACTIVE PIPELINE</h5>
        <p style="font-size: 20px; font-weight:800; margin: 15px 0; color:#ffffff;">30-Day Python Portal</p>
        <div class="badge-neon" style="background:rgba(127,0,255,0.1); border-color:#7f00ff; color:#a370f7;">Compiling Assets...</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Education Card
    st.markdown("""
    <div class="premium-panel">
        <div style="font-weight: 700; color: #00f2fe; margin-bottom:5px;">BS Artificial Intelligence</div>
        <div style="font-size: 13px; color: #8b949e; margin-bottom:10px;">University of Rasul</div>
        <p style="font-size: 14px; margin:0; color:#c9d1d9;">Focusing on advanced automation, intelligent systems engineering, and stateful application architecture.</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# 6. TERMINAL RUNTIME FOOTER
# =====================================================================
st.markdown("<br><br><hr style='border-color: rgba(255,255,255,0.05);'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #484f58; font-family: monospace; font-size: 12px;'>[System: Core Node Online] • Developed by Hassan Raza</p>", unsafe_allow_html=True)
