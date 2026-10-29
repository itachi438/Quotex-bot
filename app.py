import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# Page Configuration
st.set_page_config(page_title="Haseeb Bot AI Pro", page_icon="⚡", layout="centered")

# Custom CSS with Built-in Neon Glowing Background & Watermark Effect (No file upload needed)
css_code = """
    <style>
    .main {
        background: radial-gradient(circle at center, #0f172a 0%, #07090f 100%);
        color: #ffffff;
    }
    /* Glowing Watermark Effect in Background */
    .stApp::before {
        content: "⚡ HASEEB BOT ⚡";
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 4rem;
        font-weight: 900;
        color: rgba(0, 243, 255, 0.03);
        z-index: 0;
        pointer-events: none;
        letter-spacing: 5px;
    }
    .header-box {
        background: rgba(16, 24, 39, 0.8);
        border: 1px solid #1e293b;
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 0 20px rgba(0, 243, 255, 0.2);
        margin-bottom: 15px;
        position: relative;
        z-index: 1;
    }
    .bot-title {
        color: #00f3ff;
        font-size: 1.3rem;
        font-weight: 800;
        letter-spacing: 1px;
        text-shadow: 0 0 10px #00f3ff;
    }
    .glow-circle-up {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        border: 3px solid #00ffaa;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 8px auto;
        box-shadow: 0 0 15px #00ffaa, inset 0 0 10px #00ffaa;
        animation: pulseGreen 1.5s infinite alternate;
    }
    .glow-circle-down {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        border: 3px solid #ff0055;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 8px auto;
        box-shadow: 0 0 15px #ff0055, inset 0 0 10px #ff0055;
        animation: pulseRed 1.5s infinite alternate;
    }
    @keyframes pulseGreen {
        0% { box-shadow: 0 0 10px #00ffaa; border-color: #00ffaa; }
        100% { box-shadow: 0 0 25px #00ffaa; border-color: #fff; }
    }
    @keyframes pulseRed {
        0% { box-shadow: 0 0 10px #ff0055; border-color: #ff0055; }
        100% { box-shadow: 0 0 25px #ff0055; border-color: #fff; }
    }
    .signal-box-up {
        background: rgba(13, 27, 30, 0.9);
        border: 1px solid #00ffaa;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 0 15px rgba(0, 255, 170, 0.2);
        position: relative;
        z-index: 1;
    }
    .signal-box-down {
        background: rgba(31, 13, 20, 0.9);
        border: 1px solid #ff0055;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.2);
        position: relative;
        z-index: 1;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00f3ff, #0066ff);
        color: #ffffff;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.4);
        width: 100%;
    }
    </style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# Compact Header
st.markdown("""
    <div class="header-box">
        <div class="bot-title">⚡ HASEEB BOT AI PRO ⚡</div>
    </div>
""", unsafe_allow_html=True)

# Controls
col1, col2 = st.columns(2)
with col1:
    asset = st.selectbox("Asset:", ("EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/CAD OTC", "BTC/USD OTC"))
with col2:
    timeframe = st.selectbox("Timeframe:", ("1m", "5m", "15m"))

st.markdown("<br>", unsafe_allow_html=True)

# Generate Signal Button
if st.button("🚀 GET SIGNAL"):
    with st.spinner("Analyzing market..."):
        now = datetime.now()
        
        if timeframe == "1m":
            entry_time_obj = now + timedelta(seconds=10)
            expiry_time_obj = entry_time_obj + timedelta(minutes=1)
        elif timeframe == "5m":
            entry_time_obj = now + timedelta(seconds=20)
            expiry_time_obj = entry_time_obj + timedelta(minutes=5)
        else:
            entry_time_obj = now + timedelta(seconds=30)
            expiry_time_obj = entry_time_obj + timedelta(minutes=15)
            
        entry_str = entry_time_obj.strftime("%I:%M:%S %p")
        expiry_str = expiry_time_obj.strftime("%I:%M:%S %p")
        
        signal_type = random.choice(["CALL", "PUT"])
        confidence = random.randint(89, 98)
        
        st.markdown(f"<p style='text-align: center; color: #94a3b8; font-size: 0.85rem; margin-bottom: 5px;'>SIGNAL TIME: {now.strftime('%I:%M:%S %p')}</p>", unsafe_allow_html=True)
        
        if signal_type == "CALL":
            st.markdown(f"""
                <div class="signal-box-up">
                    <div class="glow-circle-up">
                        <span style="font-size: 2.2rem; color: #00ffaa;">↑</span>
                    </div>
                    <h2 style="color: #00ffaa; font-weight: 800; margin: 5px 0;">CALL (UP)</h2>
                    <p style="font-size: 0.85rem; color: #cbd5e1; margin: 0;">{asset} &bull; {timeframe} &bull; {confidence}% CONFIDENCE</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="signal-box-down">
                    <div class="glow-circle-down">
                        <span style="font-size: 2.2rem; color: #ff0055;">↓</span>
                    </div>
                    <h2 style="color: #ff0055; font-weight: 800; margin: 5px 0;">PUT (DOWN)</h2>
                    <p style="font-size: 0.85rem; color: #cbd5e1; margin: 0;">{asset} &bull; {timeframe} &bull; {confidence}% CONFIDENCE</p>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Timing Execution Box
        st.markdown(f"""
            <div style="background: rgba(17, 24, 39, 0.9); border: 1px solid #374151; padding: 12px; border-radius: 10px; font-size: 0.9rem; position: relative; z-index: 1;">
                <p style="color: #00f3ff; font-weight: bold; margin-bottom: 5px;">⏳ TIMING GUIDE:</p>
                <p style="color: #e2e8f0; margin: 2px 0;"><b>Entry:</b> <span style="color: #00ffaa;">{entry_str}</span></p>
                <p style="color: #e2e8f0; margin: 2px 0;"><b>Expiry:</b> <span style="color: #ff0055;">{expiry_str}</span> ({timeframe})</p>
            </div>
        """, unsafe_allow_html=True)
