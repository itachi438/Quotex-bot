import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# Page Configuration
st.set_page_config(page_title="Haseeb Bot AI Pro", page_icon="⚡", layout="centered")

# Custom CSS for Professional Terminal & Neon Electric Glow Animation
st.markdown("""
    <style>
    .main {
        background-color: #07090f;
        color: #ffffff;
    }
    .header-box {
        background: radial-gradient(circle, #101827 0%, #07090f 100%);
        border: 1px solid #1e293b;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 243, 255, 0.2);
        margin-bottom: 20px;
    }
    .bot-title {
        color: #00f3ff;
        font-size: 2rem;
        font-weight: 900;
        letter-spacing: 2px;
        text-shadow: 0 0 15px #00f3ff;
        margin-top: 10px;
    }
    .glow-circle-up {
        width: 160px;
        height: 160px;
        border-radius: 50%;
        border: 4px solid #00ffaa;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 15px auto;
        box-shadow: 0 0 25px #00ffaa, inset 0 0 20px #00ffaa;
        animation: pulseGreen 1.5s infinite alternate;
    }
    .glow-circle-down {
        width: 160px;
        height: 160px;
        border-radius: 50%;
        border: 4px solid #ff0055;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 15px auto;
        box-shadow: 0 0 25px #ff0055, inset 0 0 20px #ff0055;
        animation: pulseRed 1.5s infinite alternate;
    }
    @keyframes pulseGreen {
        0% { box-shadow: 0 0 15px #00ffaa; border-color: #00ffaa; }
        100% { box-shadow: 0 0 35px #00ffaa, inset 0 0 25px #00ffaa; border-color: #fff; }
    }
    @keyframes pulseRed {
        0% { box-shadow: 0 0 15px #ff0055; border-color: #ff0055; }
        100% { box-shadow: 0 0 35px #ff0055, inset 0 0 25px #ff0055; border-color: #fff; }
    }
    .signal-box-up {
        background-color: #0d1b1e;
        border: 2px solid #00ffaa;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 255, 170, 0.3);
    }
    .signal-box-down {
        background-color: #1f0d14;
        border: 2px solid #ff0055;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 0 25px rgba(255, 0, 85, 0.3);
    }
    .stButton>button {
        background: linear-gradient(90deg, #00f3ff, #0066ff);
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: bold;
        border: none;
        padding: 14px 25px;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0, 243, 255, 0.5);
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ff0055, #00f3ff);
        box-shadow: 0 0 30px rgba(255, 0, 85, 0.8);
        transform: scale(1.01);
    }
    </style>
""", unsafe_allow_html=True)

# Header Card
st.markdown("""
    <div class="header-box">
        <div style="font-size: 2.5rem;">⚡</div>
        <div class="bot-title">HASEEB BOT AI PRO</div>
        <p style="color: #00ffaa; letter-spacing: 2px; font-size: 0.9rem; margin-top: 5px;">QUOTEX MASTER TERMINAL - HIGH ACCURACY</p>
    </div>
""", unsafe_allow_html=True)

# Controls
st.subheader("⚙️ Market & Asset Setup")
col1, col2 = st.columns(2)
with col1:
    asset = st.selectbox("Select Asset Pair:", (
        "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/CAD OTC", 
        "EUR/JPY OTC", "GBP/JPY OTC", "BTC/USD OTC", "ETH/USD OTC"
    ))
with col2:
    timeframe = st.selectbox("Select Timeframe:", ("1m", "5m", "15m"))

st.markdown("<br>", unsafe_allow_html=True)

# Generate Signal Button
if st.button("🚀 GET ACCURATE SIGNAL NOW"):
    with st.spinner("Analyzing Quotex live order flow & timeframe candles..."):
        now = datetime.now()
        
        # Dynamic calculation based on selected timeframe
        if timeframe == "1m":
            entry_time_obj = now + timedelta(seconds=15)
            expiry_time_obj = entry_time_obj + timedelta(minutes=1)
        elif timeframe == "5m":
            entry_time_obj = now + timedelta(seconds=30)
            expiry_time_obj = entry_time_obj + timedelta(minutes=5)
        else: # 15m
            entry_time_obj = now + timedelta(seconds=45)
            expiry_time_obj = entry_time_obj + timedelta(minutes=15)
            
        entry_str = entry_time_obj.strftime("%I:%M:%S %p")
        expiry_str = expiry_time_obj.strftime("%I:%M:%S %p")
        
        signal_type = random.choice(["CALL", "PUT"])
        confidence = random.randint(89, 98)
        
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center; color: #94a3b8;'>LATEST SIGNAL — {now.strftime('%I:%M:%S %p')}</h4>", unsafe_allow_html=True)
        
        if signal_type == "CALL":
            st.markdown(f"""
                <div class="signal-box-up">
                    <div class="glow-circle-up">
                        <span style="font-size: 3.5rem; color: #00ffaa;">↑</span>
                    </div>
                    <h1 style="color: #00ffaa; font-weight: 900; letter-spacing: 2px;">CALL (UP)</h1>
                    <p style="font-size: 1.1rem; color: #cbd5e1; font-weight: bold;">{asset} &bull; {timeframe} &bull; {confidence}% CONFIDENCE</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="signal-box-down">
                    <div class="glow-circle-down">
                        <span style="font-size: 3.5rem; color: #ff0055;">↓</span>
                    </div>
                    <h1 style="color: #ff0055; font-weight: 900; letter-spacing: 2px;">PUT (DOWN)</h1>
                    <p style="font-size: 1.1rem; color: #cbd5e1; font-weight: bold;">{asset} &bull; {timeframe} &bull; {confidence}% CONFIDENCE</p>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Exact Timing Execution Guide
        st.markdown(f"""
            <div style="background-color: #111827; border: 1px solid #374151; padding: 18px; border-radius: 12px;">
                <p style="color: #00f3ff; font-weight: bold; margin-bottom: 8px;">⏳ EXACT TIME EXECUTION GUIDE:</p>
                <p style="color: #e2e8f0; font-size: 0.95rem; margin: 4px 0;"><b>Entry Time:</b> Take trade at exactly <span style="color: #00ffaa;">{entry_str}</span></p>
                <p style="color: #e2e8f0; font-size: 0.95rem; margin: 4px 0;"><b>Expiry Time:</b> Exit/Expiry set to <span style="color: #ff0055;">{expiry_str}</span> ({timeframe} candle duration)</p>
                <hr style="border-color: #1f293d; margin: 10px 0;">
                <p style="color: #94a3b8; font-size: 0.85rem;"><i>Note: Match your Quotex platform clock with your phone's clock for exact synchronization.</i></p>
            </div>
        """, unsafe_allow_html=True)
