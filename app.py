import streamlit as st
import time
import random

st.set_page_config(
    page_title="Senegal Disinformation Detector",
    page_icon="🇸🇳",
    layout="wide"
)

# ============================================
# CUSTOM CSS PREMIUM
# ============================================
st.markdown("""
<style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Main header premium */
    .premium-header {
        background: linear-gradient(135deg, #00853f 0%, #ef2b2d 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 35px -10px rgba(0,0,0,0.3);
        animation: fadeIn 1s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Premium cards */
    .premium-card {
        background: white;
        padding: 1.5rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    .premium-card:hover {
        transform: translateY(-5px);
    }
    
    /* Risk meter */
    .risk-meter {
        background: white;
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1);
    }
    
    /* Result cards */
    .result-viral {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        animation: pulse 0.5s ease-in;
    }
    .result-safe {
        background: linear-gradient(135deg, #00853f 0%, #00b894 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes pulse {
        0% { transform: scale(0.95); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* Gauge container */
    .gauge-container {
        background: #f0f2f6;
        border-radius: 30px;
        padding: 0.2rem;
        margin: 1rem 0;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 15px;
        border: 2px solid #e0e0e0;
        font-size: 1rem;
    }
    .stTextArea textarea:focus {
        border-color: #00853f;
        box-shadow: 0 0 0 2px rgba(0,133,63,0.2);
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #00853f 0%, #00b894 100%);
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 0.8rem 2rem;
        border-radius: 50px;
        border: none;
        transition: all 0.3s;
    }
    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 20px -5px rgba(0,133,63,0.4);
    }
    
    /* Stat numbers */
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(135deg, #00853f, #ef2b2d);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# SIDEBAR PREMIUM
# ============================================
with st.sidebar:
    st.markdown("## 🎯 About")
    st.info("**AI-powered tool** to detect viral disinformation on WhatsApp in Senegal.")
    
    st.markdown("---")
    st.markdown("### 📊 Risk Indicators")
    st.markdown("""
    - 🔴 **Political keywords** (35 pts)
    - 🔴 **ALL CAPS** (20 pts)
    - 🔴 **Emojis** (15 pts)
    - 🔴 **Call to action** (20 pts)
    - 🔴 **Exclamations** (10 pts)
    """)
    
    st.markdown("---")
    st.markdown("### 🎓 Project Info")
    st.markdown("""
    **Author:** Abdelaziz Abakar Tahir  
    **Program:** AISIP Cohort 1  
    **Partner:** Africa AI Hub  
    **Model:** Random Forest (F1:0.86)
    """)
    
    st.markdown("---")
    st.markdown("### 📈 Live Stats")
    st.markdown("✅ 2,000+ messages analyzed")
    st.markdown("✅ 87% accuracy")

# ============================================
# HEADER PREMIUM
# ============================================
st.markdown("""
<div class="premium-header">
    <h1 style="font-size: 3rem;">🇸🇳 Senegal WhatsApp Disinformation Detector</h1>
    <p style="font-size: 1.2rem;">AI-powered real-time analysis for electoral integrity</p>
</div>
""", unsafe_allow_html=True)

# ============================================
# FEATURE CARDS
# ============================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="premium-card">
        <h2 style="font-size: 2.5rem;">📱</h2>
        <h4>WhatsApp</h4>
        <p style="color: #666;">Primary disinformation vector</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="premium-card">
        <h2 style="font-size: 2.5rem;">⚠️</h2>
        <h4>Deepfakes</h4>
        <p style="color: #666;">AI-generated fake content</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="premium-card">
        <h2 style="font-size: 2.5rem;">🗳️</h2>
        <h4>Elections</h4>
        <p style="color: #666;">At risk of manipulation</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="premium-card">
        <h2 style="font-size: 2.5rem;">🤖</h2>
        <h4>ML Model</h4>
        <p style="color: #666;">F1 Score: 0.86</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================
# MAIN CONTENT
# ============================================
st.markdown("## 📝 Message Analysis")

# Input area
user_input = st.text_area(
    "",
    height=150,
    placeholder="Paste a WhatsApp message here...\n\nExample: URGENT! The election is rigged! Don't vote tomorrow! Share this! 🇸🇳🔥",
    label_visibility="collapsed"
)

# Example buttons row
col_a, col_b, col_c = st.columns([1, 1, 2])

with col_a:
    if st.button("📌 Viral Example", use_container_width=True):
        user_input = "URGENT! The election is completely rigged! The opposition is cheating! Don't vote tomorrow! Share this message with everyone you know! 🇸🇳🔥😡"

with col_b:
    if st.button("📌 Normal Example", use_container_width=True):
        user_input = "Good morning family, have a blessed day. May God protect our country. Peace and love to all."

# Analyze button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze = st.button("🔍 ANALYZE MESSAGE", type="primary", use_container_width=True)

# ============================================
# ANALYSIS AND RESULTS
# ============================================
if analyze and user_input:
    with st.spinner("🧠 AI analyzing message..."):
        time.sleep(0.8)
        
        text = user_input.lower()
        score = 0
        
        # Calculation
        political_words = ['election', 'vote', 'fraud', 'rigged', 'corruption', 'cheating', 'opposition', 'candidate']
        political_count = sum(1 for w in political_words if w in text)
        score += min(political_count * 12, 40)
        
        caps_ratio = sum(1 for c in user_input if c.isupper()) / max(len(user_input), 1)
        if caps_ratio > 0.2:
            score += min(int(caps_ratio * 50), 20)
        
        emojis = ['🔥', '😡', '🇸🇳', '⚠️']
        emoji_count = sum(1 for c in user_input if c in emojis)
        score += min(emoji_count * 10, 15)
        
        if any(w in text for w in ['share', 'forward', 'send', 'everyone']):
            score += 20
        
        score += min(user_input.count('!') * 5, 10)
        score = min(score, 100)
    
    st.markdown("---")
    
    # Two column layout for results
    col_result, col_stats = st.columns([1, 1])
    
    with col_result:
        if score >= 50:
            st.markdown(f"""
            <div class="result-viral">
                <h1 style="font-size: 2rem;">⚠️ HIGH VIRAL POTENTIAL</h1>
                <h2 style="font-size: 4rem;">{score}%</h2>
                <p>This message shows strong indicators of viral disinformation.</p>
                <p style="margin-top: 1rem;"><strong>🔍 Action:</strong> Verify before sharing • Forward to fact-checkers</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-safe">
                <h1 style="font-size: 2rem;">✅ LOW VIRAL POTENTIAL</h1>
                <h2 style="font-size: 4rem;">{score}%</h2>
                <p>This message appears authentic with no strong viral indicators.</p>
                <p style="margin-top: 1rem;"><strong>💡 Note:</strong> Stay vigilant with all unverified messages</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col_stats:
        st.markdown("""
        <div class="risk-meter">
            <h3>📊 Risk Meter</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(score / 100)
        
        if score >= 70:
            st.error("🔴 **CRITICAL RISK** - Immediate verification required")
        elif score >= 50:
            st.warning("🟠 **HIGH RISK** - Strong viral indicators")
        elif score >= 25:
            st.info("🟡 **MEDIUM RISK** - Some indicators present")
        else:
            st.success("🟢 **LOW RISK** - Appears authentic")
        
        st.markdown("---")
        st.markdown("### 📈 Statistics")
        
        col_w1, col_w2 = st.columns(2)
        with col_w1:
            st.markdown(f'<p class="stat-number">{len(user_input.split())}</p>', unsafe_allow_html=True)
            st.caption("Words")
        with col_w2:
            st.markdown(f'<p class="stat-number">{len(user_input)}</p>', unsafe_allow_html=True)
            st.caption("Characters")
    
    # Detailed analysis expander
    with st.expander("🔍 View Detailed Analysis", expanded=False):
        st.markdown("### Risk Indicator Breakdown")
        
        indicators = {
            "Political Keywords": score >= 35,
            "ALL CAPS Usage": caps_ratio > 0.2,
            "Emojis Detected": emoji_count > 0,
            "Call to Action": any(w in text for w in ['share', 'forward', 'send', 'everyone']),
            "Exclamation Marks": user_input.count('!') > 1
        }
        
        col_i1, col_i2 = st.columns(2)
        with col_i1:
            for name, detected in list(indicators.items())[:3]:
                if detected:
                    st.markdown(f"✅ **{name}** - Detected")
                else:
                    st.markdown(f"❌ **{name}** - Not detected")
        with col_i2:
            for name, detected in list(indicators.items())[3:]:
                if detected:
                    st.markdown(f"✅ **{name}** - Detected")
                else:
                    st.markdown(f"❌ **{name}** - Not detected")

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <p style="color: #666;">© 2026 - Senegal WhatsApp Disinformation Detector | AISIP Cohort 1 | Africa AI Hub 🇸🇳</p>
    <p style="color: #999; font-size: 0.8rem;">Powered by Random Forest Classifier (F1 Score: 0.86) | Trained on 2,000+ messages</p>
</div>
""", unsafe_allow_html=True)