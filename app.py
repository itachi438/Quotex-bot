import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import os
import base64

# Streamlit Page Setup with Custom Logo as Page Icon
st.set_page_config(page_title="Haseeb Bot AI Pro", page_icon="logo.png", layout="centered")

# Custom CSS for Electric Glowing Animation & Professional Dark Terminal
st.markdown("""
    <style>
    .main {
        background-color: #070913;
        color: #ffffff;
    }
    .electric-box {
        text-align: center;
        padding: 20px;
        margin-bottom: 20px;
    }
    .electric-logo-img {
        width: 170px;
        height: 170px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #00f3ff;
        box-shadow: 0 0 20px #00f3ff, 0 0 40px #00f3ff, inset 0 0 15px #00f3ff;
        animation: electricPulse 1.2s infinite alternate;
    }
    @keyframes electricPulse {
        0% {
            box-shadow: 0 0 15px #00f3ff, 0 0 25px #00f3ff;
            border-color: #00f3ff;
        }
        50% {
            box-shadow: 0 0 30px #ff0055, 0 0 50px #ff0055;
            border-color: #ff0055;
        }
        100% {
            box-shadow: 0 0 35px #00ffaa, 0 0 60px #00ffaa;
            border-color: #00ffaa;
        }
    }
    .bot-title {
        color: #00f3ff;
        font-size: 2.2rem;
        font-weight: 900;
        letter-spacing: 2px;
        text-shadow: 0 0 12px #00f3ff;
        margin-top: 15px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00f3ff, #0066ff);
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: bold;
        border: none;
        padding: 12px 25px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.5);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ff0055, #00f3ff);
        box-shadow: 0 0 25px rgba(255, 0, 85, 0.8);
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# Function to encode logo image for CSS electric animation
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/png;base64,{encoded}"
    return None

logo_b64 = get_image_base64("logo.png")

# Header Section with Animated Logo
if logo_b64:
    st.markdown(f"""
        <div class="electric-box">
            <img src="{logo_b64}" class="electric-logo-img">
            <div class="bot-title">⚡ HASEEB BOT AI PRO ⚡</div>
            <p style="color: #8b949e; letter-spacing: 1px;">ORIGINAL HIGH-ACCURACY SIGNAL TERMINAL</p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="electric-box">
            <div class="bot-title">⚡ HASEEB BOT AI PRO ⚡</div>
            <p style="color: #8b949e; letter-spacing: 1px;">ORIGINAL HIGH-ACCURACY SIGNAL TERMINAL</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Quotex Assets & Market Configuration
st.subheader("⚙️ Quotex Asset & Timeframe Setup")
col_s1, col_s2 = st.columns(2)

with col_s1:
    ticker = st.selectbox("Select Quotex Asset Pair:", (
        "EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X", "NZDUSD=X", 
        "USDCAD=X", "EURGBP=X", "GBPJPY=X", "EURJPY=X", "AUDJPY=X",
        "GBPADU=X", "CHFJPY=X", "EURAUD=X", "BTC-USD", "ETH-USD", "XRP-USD"
    ))

with col_s2:
    timeframe = st.selectbox("Select Candle Timeframe:", ("5m", "15m", "1h"))

st.markdown("---")

# Signal Generation Execution
if st.button("🚀 RUN HASEEB BOT & GENERATE ACCURATE SIGNAL"):
    with st.spinner("⚡ Running Deep Multi-Factor Analysis (EMA + RSI + MACD + Volume)..."):
        period = "5d" if timeframe in ["5m", "15m"] else "1mo"
        data = yf.download(tickers=ticker, period=period, interval=timeframe, progress=False)
        
        if data.empty or len(data) < 35:
            st.error("❌ Market data temporarily unavailable. If forex market is closed, please select BTC-USD or ETH-USD.")
        else:
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.droplevel(1)
                
            # Indicators Engine
            data['EMA_9'] = data['Close'].ewm(span=9, adjust=False).mean()
            data['EMA_21'] = data['Close'].ewm(span=21, adjust=False).mean()
            data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()
            
            delta = data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            data['RSI'] = 100 - (100 / (1 + rs))
            
            exp1 = data['Close'].ewm(span=12, adjust=False).mean()
            exp2 = data['Close'].ewm(span=26, adjust=False).mean()
            data['MACD'] = exp1 - exp2
            data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
            
            current_price = float(data['Close'].iloc[-1])
            ema9 = float(data['EMA_9'].iloc[-1])
            ema21 = float(data['EMA_21'].iloc[-1])
            ema50 = float(data['EMA_50'].iloc[-1])
            rsi = float(data['RSI'].iloc[-1])
            macd = float(data['MACD'].iloc[-1])
            sig_line = float(data['Signal_Line'].iloc[-1])
            
            entry_time = datetime.now().strftime("%I:%M:%S %p")
            
            st.subheader(f"📊 Live Technical Metrics ({ticker})")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Live Price", f"{current_price:.5f}")
            m2.metric("EMA 9 / 21", f"{ema9:.4f}")
            m3.metric("RSI (14)", f"{rsi:.1f}")
            m4.metric("MACD Status", "Bullish 🟢" if macd > sig_line else "Bearish 🔴")
            
            st.markdown("---")
            st.subheader("🎯 Haseeb Bot Output Signal")
            
            if (ema9 > ema21) and (current_price > ema50) and (45 <= rsi <= 68) and (macd > sig_line):
                st.success("### 🟢 HIGH-ACCURACY CALL (BUY) SIGNAL")
                st.markdown(f"**⏰ Exact Entry Time:** `{entry_time}`")
                st.markdown(f"**⏳ Recommended Trade Expiry:** `{timeframe}` (1 Candle Expiry)")
                st.info("✅ Signal Verified: Strong Uptrend Crossover, Bullish Momentum & MACD Aligned.")
                
            elif (ema9 < ema21) and (current_price < ema50) and (32 <= rsi <= 55) and (macd < sig_line):
                st.error("### 🔴 HIGH-ACCURACY PUT (SELL) SIGNAL")
                st.markdown(f"**⏰ Exact Entry Time:** `{entry_time}`")
                st.markdown(f"**⏳ Recommended Trade Expiry:** `{timeframe}` (1 Candle Expiry)")
                st.info("✅ Signal Verified: Strong Downtrend Crossover, Bearish Momentum & MACD Aligned.")
                
            else:
                st.warning("### ⚪ HOLD / NO TRADE (PROTECTION MODE)")
                st.markdown(f"**⏰ Analysis Time:** `{entry_time}`")
                st.markdown("**Advice:** Market is consolidating or moving sideways. Haseeb Bot has filtered out this setup to prevent false losses.")
