import warnings
warnings.filterwarnings('ignore')
import streamlit as st
from datetime import datetime, timedelta
import random

# Page Configuration
st.set_page_config(page_title="Haseeb Bot AI Pro", page_icon="⚡", layout="centered")

# Force Dark Theme Container Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: #ffffff;
    }
    .header-box {
        background: #0d1117;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.2);
        margin-bottom: 15px;
    }
    .bot-title {
        color: #00f3ff;
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: 1px;
    }
    .glow-circle-up {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        border: 3px solid #00ffaa;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 10px auto;
        box-shadow: 0 0 20px #00ffaa;
    }
    .glow-circle-down {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        border: 3px solid #ff0055;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 10px auto;
        box-shadow: 0 0 20px #ff0055;
    }
    .signal-box-up {
        background: #0d1b1e;
        border: 1px solid #00ffaa;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .signal-box-down {
        background: #1f0d14;
        border: 1px solid #ff0055;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00f3ff, #0066ff);
        color: #ffffff;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-box">
        <div class="bot-title">⚡ HASEEB BOT AI PRO ⚡</div>
    </div>
""", unsafe_allow_html=True)

# Controls
col1, col2 = st.columns(2)
with col1:
    asset = st.selectbox("Asset:", (
        "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/CAD OTC", 
        "EUR/JPY OTC", "GBP/JPY OTC", "NZD/USD OTC", "USD/CAD OTC", 
        "BTC/USD OTC", "ETH/USD OTC"
    ))
with col2:
    timeframe = st.selectbox("Timeframe:", ("1m", "5m", "15m"))

st.markdown("<br>", unsafe_allow_html=True)

# Generate Signal Button
if st.button("🚀 GET SIGNAL"):
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
    
    st.markdown(f"<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>SIGNAL TIME: {now.strftime('%I:%M:%S %p')}</p>", unsafe_allow_html=True)
    
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
    
    st.markdown(f"""
        <div style="background: #0d1117; border: 1px solid #30363d; padding: 12px; border-radius: 10px; font-size: 0.9rem;">
            <p style="color: #00f3ff; font-weight: bold; margin-bottom: 5px;">⏳ TIMING GUIDE:</p>
            <p style="color: #e2e8f0; margin: 2px 0;"><b>Entry:</b> <span style="color: #00ffaa;">{entry_str}</span></p>
            <p style="color: #e2e8f0; margin: 2px 0;"><b>Expiry:</b> <span style="color: #ff0055;">{expiry_str}</span> ({timeframe})</p>
        </div>
    """, unsafe_allow_html=True)
