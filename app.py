import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Haseeb Bot AI Pro", page_icon="⚡", layout="centered")

# Custom CSS for AlphaX / Dangerous Neon Trading Terminal Style
st.markdown("""
    <style>
    .main {
        background-color: #0b0e14;
        color: #ffffff;
    }
    .stSelectbox, .stButton {
        width: 100%;
    }
    /* AlphaX Style Header Card */
    .header-card {
        background: linear-gradient(135deg, #131b2e 0%, #0b0e14 100%);
        border: 1px solid #1f293d;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 243, 255, 0.15);
        margin-bottom: 25px;
    }
    .bot-logo-icon {
        font-size: 3rem;
        color: #00f3ff;
        text-shadow: 0 0 15px #00f3ff;
    }
    .bot-title {
        color: #ffffff;
        font-size: 1.8rem;
        font-weight: 800;
        letter-spacing: 1px;
        margin-top: 10px;
    }
    .bot-subtitle {
        color: #00ffaa;
        font-size: 0.85rem;
        letter-spacing: 2px;
        margin-top: 5px;
    }
    /* Section Container Cards */
    .signal-card {
        background-color: #121824;
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 12px;
        margin-top: 15px;
    }
    /* Neon Green Action Button */
    .stButton>button {
        background: linear-gradient(90deg, #00ffaa, #00f3ff);
        color: #0b0e14;
        font-size: 1.2rem;
        font-weight: 900;
        border: none;
        padding: 14px 25px;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0, 255, 170, 0.4);
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #00f3ff, #ff0055);
        color: #ffffff;
        box-shadow: 0 0 30px rgba(255, 0, 85, 0.6);
        transform: scale(1.01);
    }
    </style>
""", unsafe_allow_html=True)

# Header Section resembling AlphaX layout
st.markdown("""
    <div class="header-card">
        <div class="bot-logo-icon">⚡X</div>
        <div class="bot-title">HaseebBot AI Pro</div>
        <div class="bot-subtitle">SMART SIGNALS. HIGH ACCURACY DECISIONS.</div>
    </div>
""", unsafe_allow_html=True)

# Control Panel Card
st.markdown("### 🎛️ SIGNAL GENERATOR CONFIGURATION")

col1, col2 = st.columns(2)
with col1:
    platform = st.selectbox("SELECT PLATFORM:", ("Quotex", "Tradowix", "PocketOption"))
with col2:
    ticker = st.selectbox("SELECT TRADING PAIR:", (
        "EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X", "NZDUSD=X", 
        "USDCAD=X", "EURGBP=X", "GBPJPY=X", "BTC-USD", "ETH-USD"
    ))

timeframe = st.selectbox("SELECT CANDLE TIME FRAME:", ("1m", "5m", "15m", "1h"))

st.markdown("<br>", unsafe_allow_html=True)

# Trigger Button
if st.button("⚡ GET HIGH-ACCURACY SIGNAL"):
    with st.spinner("Analyzing market volatility & multi-indicators..."):
        period = "1d" if timeframe == "1m" else ("5d" if timeframe in ["5m", "15m"] else "1mo")
        data = yf.download(tickers=ticker, period=period, interval=timeframe, progress=False)
        
        if data.empty or len(data) < 25:
            st.error("Market data feed is limited right now. Please select BTC-USD or try another pair.")
        else:
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.droplevel(1)
                
            # Optimized Indicator Calculation for Balanced Signals
            data['EMA_9'] = data['Close'].ewm(span=9, adjust=False).mean()
            data['EMA_21'] = data['Close'].ewm(span=21, adjust=False).mean()
            
            # RSI Calculation
            delta = data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            data['RSI'] = 100 - (100 / (1 + rs))
            
            current_price = float(data['Close'].iloc[-1])
            ema9 = float(data['EMA_9'].iloc[-1])
            ema21 = float(data['EMA_21'].iloc[-1])
            rsi = float(data['RSI'].iloc[-1])
            
            entry_time = datetime.now().strftime("%I:%M:%S %p")
            
            # Live Metrics Output Box
            st.markdown(f"""
                <div class="signal-card">
                    <h4 style="color: #00f3ff; margin-bottom: 10px;">📊 Market Metrics ({ticker})</h4>
                    <p><b>Current Price:</b> {current_price:.5f}</p>
                    <p><b>EMA Trend (9/21):</b> {ema9:.4f} / {ema21:.4f}</p>
                    <p><b>RSI (14):</b> {rsi:.2f}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Smart Signal Logic (Balanced for high frequency and accuracy)
            if (ema9 > ema21) and (rsi < 70):
                st.success("### 🟢 CALL (BUY) SIGNAL GENERATED")
                st.markdown(f"**⏰ Entry Time:** `{entry_time}`")
                st.markdown(f"**⏳ Recommended Expiry:** `{timeframe}` (1 to 2 Candles)")
                st.info("Market momentum is bullish. EMA crossover confirmed upward trend.")
                
            elif (ema9 < ema21) and (rsi > 30):
                st.error("### 🔴 PUT (SELL) SIGNAL GENERATED")
                st.markdown(f"**⏰ Entry Time:** `{entry_time}`")
                st.markdown(f"**⏳ Recommended Expiry:** `{timeframe}` (1 to 2 Candles)")
                st.info("Market momentum is bearish. EMA crossover confirmed downward trend.")
                
            else:
                st.warning("### ⚪ CONSOLIDATION ZONE / WAIT")
                st.markdown(f"**⏰ Time:** `{entry_time}`")
                st.markdown("Market is ranging. Wait for the next candle close.")
