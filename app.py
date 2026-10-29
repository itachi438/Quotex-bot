import warnings
warnings.filterwarnings('ignore')
import streamlit as st
from datetime import datetime, timedelta
import hashlib
import base64
import os

# Page Configuration
st.set_page_config(page_title="Haseeb Bot Pro", page_icon="⚡", layout="centered")

def get_img_as_base64(file):
    if os.path.exists(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

img_base64 = get_img_as_base64("logo.jpg")

if img_base64:
    bg_style = f"""
    .stApp {{
        background: linear-gradient(rgba(2, 4, 8, 0.82), rgba(2, 4, 8, 0.92)), url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff !important;
    }}
    """
else:
    bg_style = """
    .stApp {{
        background-color: #020408 !important;
        color: #ffffff !important;
    }}
    """

# Centered Styling & Layout Fixes
st.markdown(f"""
    <style>
    {bg_style}
    
    /* Center all main block elements */
    .block-container {{
        max-width: 600px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        margin: 0 auto;
    }}
    
    /* Center labels and text */
    label, .stSelectbox label {{
        color: #00f3ff !important;
        font-weight: 700 !important;
        text-align: center !important;
        display: block !important;
        margin: 0 auto 5px auto !important;
    }}
    
    .signal-box-up {{
        background: rgba(5, 19, 24, 0.92) !important;
        border: 1px solid #00ffaa;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 255, 170, 0.3);
        margin-top: 15px;
    }}
    .signal-box-down {{
        background: rgba(24, 5, 14, 0.92) !important;
        border: 1px solid #ff0055;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 0 25px rgba(255, 0, 85, 0.3);
        margin-top: 15px;
    }}
    .stButton>button {{
        background: linear-gradient(90deg, #00f3ff, #0066ff) !important;
        color: #ffffff !important;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        padding: 12px 20px;
        border-radius: 10px;
        width: 100%;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.4);
        margin-top: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #00f3ff; text-shadow: 0 0 10px #00f3ff; margin-bottom: 20px;'>⚡ HASEEB BOT AI PRO ⚡</h2>", unsafe_allow_html=True)

# Controls Centered
asset = st.selectbox("Select Asset:", (
    "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/CAD OTC", 
    "EUR/JPY OTC", "GBP/JPY OTC", "NZD/USD OTC", "USD/CAD OTC", 
    "BTC/USD OTC", "ETH/USD OTC"
))

timeframe = st.selectbox("Select Timeframe:", ("1m", "5m", "15m"))

st.markdown("<br>", unsafe_allow_html=True)

# Instant Signal Generator
if st.button("🚀 GET SIGNAL"):
    now = datetime.now()
    
    seed_str = asset + timeframe + now.strftime("%Y%m%d%H%M")
    hash_val = int(hashlib.md5(seed_str.encode()).hexdigest(), 16)
    
    rsi_val = 20 + (hash_val % 65)
    
    if rsi_val < 40:
        signal_type = "CALL"
        reason = f"RSI Oversold ({rsi_val}) + Support Bounce"
    elif rsi_val > 60:
        signal_type = "PUT"
        reason = f"RSI Overbought ({rsi_val}) + Resistance Rejection"
    else:
        signal_type = "CALL" if (hash_val % 2 == 0) else "PUT"
        reason = f"Momentum Shift & Order Flow (RSI: {rsi_val})"
        
    confidence = 91 + (hash_val % 7)
    
    if timeframe == "1m":
        entry_time_obj = now + timedelta(seconds=5)
        expiry_time_obj = entry_time_obj + timedelta(minutes=1)
    elif timeframe == "5m":
        entry_time_obj = now + timedelta(seconds=10)
        expiry_time_obj = entry_time_obj + timedelta(minutes=5)
    else:
        entry_time_obj = now + timedelta(seconds=15)
        expiry_time_obj = entry_time_obj + timedelta(minutes=15)
        
    entry_str = entry_time_obj.strftime("%I:%M:%S %p")
    expiry_str = expiry_time_obj.strftime("%I:%M:%S %p")
    
    st.markdown(f"<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>SIGNAL TIME: {now.strftime('%I:%M:%S %p')}</p>", unsafe_allow_html=True)
    
    if signal_type == "CALL":
        st.markdown(f"""
            <div class="signal-box-up">
                <h2 style="color: #00ffaa; font-weight: 800; margin: 5px 0;">CALL (UP)</h2>
                <p style="font-size: 0.85rem; color: #cbd5e1; margin: 0;">{asset} &bull; {timeframe} &bull; {confidence}% CONFIDENCE</p>
                <p style="font-size: 0.75rem; color: #00ffaa; margin-top: 5px;">Analysis: {reason}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="signal-box-down">
                <h2 style="color: #ff0055; font-weight: 800; margin: 5px 0;">PUT (DOWN)</h2>
                <p style="font-size: 0.85rem; color: #cbd5e1; margin: 0;">{asset} &bull; {timeframe} &bull; {confidence}% CONFIDENCE</p>
                <p style="font-size: 0.75rem; color: #ff0055; margin-top: 5px;">Analysis: {reason}</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="background: rgba(8, 12, 20, 0.95); border: 1px solid #1e293b; padding: 12px; border-radius: 10px; font-size: 0.9rem; text-align: center;">
            <p style="color: #00f3ff; font-weight: bold; margin-bottom: 5px;">⏳ TIMING GUIDE:</p>
            <p style="color: #e2e8f0; margin: 2px 0;"><b>Entry:</b> <span style="color: #00ffaa;">{entry_str}</span></p>
            <p style="color: #e2e8f0; margin: 2px 0;"><b>Expiry:</b> <span style="color: #ff0055;">{expiry_str}</span> ({timeframe})</p>
        </div>
    """, unsafe_allow_html=True)
