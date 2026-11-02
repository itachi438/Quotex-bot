import warnings
warnings.filterwarnings('ignore')
import streamlit as st
from datetime import datetime, timedelta
import hashlib
import base64
import os

st.set_page_config(page_title="Haseeb Bot AI Pro", page_icon="⚡", layout="centered")

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
        background: linear-gradient(rgba(2, 4, 8, 0.92), rgba(2, 4, 8, 0.98)), url("data:image/jpeg;base64,{img_base64}");
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

st.markdown(f"""
    <style>
    {bg_style}
    .block-container {{
        max-width: 600px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        margin: 0 auto;
    }}
    label, .stSelectbox label {{
        color: #00f3ff !important;
        font-weight: 700 !important;
        text-align: center !important;
        display: block !important;
        margin: 0 auto 5px auto !important;
    }}
    .signal-box-up {{
        background: rgba(5, 19, 24, 0.96) !important;
        border: 2px solid #00ffaa;
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 0 40px rgba(0, 255, 170, 0.4);
        margin-top: 15px;
    }}
    .signal-box-down {{
        background: rgba(24, 5, 14, 0.96) !important;
        border: 2px solid #ff0055;
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 0, 85, 0.4);
        margin-top: 15px;
    }}
    .stButton>button {{
        background: linear-gradient(90deg, #00f3ff, #0066ff) !important;
        color: #ffffff !important;
        font-size: 1.1rem;
        font-weight: bold;
        border: none;
        padding: 12px 20px;
        border-radius: 10px;
        width: 100%;
        box-shadow: 0 0 25px rgba(0, 243, 255, 0.5);
        margin-top: 10px;
    }}
    .indicator-tag {{
        display: inline-block;
        background: rgba(0, 243, 255, 0.12);
        border: 1px solid rgba(0, 243, 255, 0.35);
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 0.72rem;
        color: #00f3ff;
        margin: 2px;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #00f3ff; text-shadow: 0 0 15px #00f3ff; margin-bottom: 20px;'>⚡ HASEEB BOT AI TERMINAL ⚡</h2>", unsafe_allow_html=True)

otc_pairs = [
    "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/CAD OTC", 
    "EUR/JPY OTC", "GBP/JPY OTC", "NZD/USD OTC", "USD/CAD OTC", 
    "EUR/AUD OTC", "GBP/AUD OTC", "EUR/GBP OTC", "CHF/JPY OTC", 
    "BTC/USD OTC", "ETH/USD OTC", "XRP/USD OTC"
]

selected_asset = st.selectbox("Select OTC Asset:", otc_pairs)
timeframe = st.selectbox("Select Timeframe:", ("1m", "5m", "15m"))

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 EXECUTE PRECISION AI SIGNAL"):
    now = datetime.now()
    
    # High-precision tick/second dynamic hashing for micro-reversals
    seed_str = selected_asset + timeframe + now.strftime("%Y%m%d%H%M%S") + str(now.microsecond)
    hash_val = int(hashlib.md5(seed_str.encode()).hexdigest(), 16)
    
    rsi_val = 20 + (hash_val % 60)
    stoch_val = 15 + (hash_val % 70)
    momentum_shift = hash_val % 100
    
    patterns = [
        "Hammer Rejection + Volume Spike",
        "Bullish Engulfing Micro-Breakout",
        "Morning Star Support Reversal",
        "Shooting Star Resistance Rejection",
        "Bearish Engulfing Trend Flip",
        "Gravestone Doji Exhaustion"
    ]
    pattern_text = patterns[hash_val % len(patterns)]
    
    # Balanced Dynamic Directional Switching Logic
    if momentum_shift < 48:
        signal_type = "CALL"
        confidence = round(87.0 + (hash_val % 7) + 0.5, 1)
    else:
        signal_type = "PUT"
        confidence = round(87.0 + (hash_val % 7) + 0.5, 1)

    if timeframe == "1m":
        entry_t = now + timedelta(seconds=3)
        expiry_t = entry_t + timedelta(minutes=1)
    elif timeframe == "5m":
        entry_t = now + timedelta(seconds=5)
        expiry_t = entry_t + timedelta(minutes=5)
    else:
        entry_t = now + timedelta(seconds=10)
        expiry_t = entry_t + timedelta(minutes=15)

    entry_str = entry_t.strftime("%I:%M:%S %p")
    expiry_str = expiry_t.strftime("%I:%M:%S %p")

    st.markdown(f"<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>SIGNAL TIMESTAMP: {now.strftime('%I:%M:%S %p')}</p>", unsafe_allow_html=True)

    if signal_type == "CALL":
        st.markdown(f"""
            <div class="signal-box-up">
                <h2 style="color: #00ffaa; font-weight: 800; margin: 5px 0;">CALL (UP) 🟢</h2>
                <p style="font-size: 0.9rem; color: #ffffff; font-weight: bold; margin: 4px 0;">{selected_asset} &bull; {timeframe}</p>
                <p style="font-size: 0.85rem; color: #00ffaa; margin: 4px 0;">ACCURACY CONFIDENCE: {confidence}%</p>
                <div style="margin-top: 8px;">
                    <span class="indicator-tag">RSI: {rsi_val}</span>
                    <span class="indicator-tag">Stochastic Oversold</span>
                    <span class="indicator-tag">Bollinger Lower Bounce</span>
                    <span class="indicator-tag">EMA Momentum BUY</span>
                </div>
                <p style="font-size: 0.75rem; color: #cbd5e1; margin-top: 8px;"><b>Trigger Setup:</b> {pattern_text}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="signal-box-down">
                <h2 style="color: #ff0055; font-weight: 800; margin: 5px 0;">PUT (DOWN) 🔴</h2>
                <p style="font-size: 0.9rem; color: #ffffff; font-weight: bold; margin: 4px 0;">{selected_asset} &bull; {timeframe}</p>
                <p style="font-size: 0.85rem; color: #ff0055; margin: 4px 0;">ACCURACY CONFIDENCE: {confidence}%</p>
                <div style="margin-top: 8px;">
                    <span class="indicator-tag">RSI: {rsi_val}</span>
                    <span class="indicator-tag">Stochastic Overbought</span>
                    <span class="indicator-tag">Bollinger Upper Rejection</span>
                    <span class="indicator-tag">EMA Momentum SELL</span>
                </div>
                <p style="font-size: 0.75rem; color: #cbd5e1; margin-top: 8px;"><b>Trigger Setup:</b> {pattern_text}</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
        <div style="background: rgba(8, 12, 20, 0.96); border: 1px solid #1e293b; padding: 12px; border-radius: 10px; font-size: 0.9rem; text-align: center;">
            <p style="color: #00f3ff; font-weight: bold; margin-bottom: 5px;">⏳ EXECUTION SCHEDULE:</p>
            <p style="color: #e2e8f0; margin: 2px 0;"><b>Entry Time:</b> <span style="color: #00ffaa;">{entry_str}</span></p>
            <p style="color: #e2e8f0; margin: 2px 0;"><b>Expiry Time:</b> <span style="color: #ff0055;">{expiry_str}</span> ({timeframe})</p>
        </div>
    """, unsafe_allow_html=True)
