import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import yfinance as yf
import pandas as pd

st.title("🤖 Quotex AI Signal Generator Dashboard")
st.write("یہ ویب ایپ لائیو مارکیٹ ڈیٹا (EMA اور RSI) کا تجزیہ کر کے سگنل فراہم کرتی ہے۔")

ticker = st.selectbox("کرنسی پیئر منتخب کریں (Select Currency Pair):", ("EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X", "BTC-USD"))

if st.button("📊 مارکیٹ کا تجزیہ کریں اور سگنل لیں"):
    with st.spinner("ڈیٹا لوڈ ہو رہا ہے، براہ کرم انتظار کریں..."):
        data = yf.download(tickers=ticker, period="1d", interval="1m", progress=False)
        
        if data.empty:
            st.error("موجودہ ڈیٹا حاصل نہیں ہو سکا۔ براہ کرم دوبارہ کوشش کریں۔")
        else:
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.droplevel(1)
                
            # Calculate EMA and RSI using pure pandas
            data['EMA_9'] = data['Close'].ewm(span=9, adjust=False).mean()
            data['EMA_21'] = data['Close'].ewm(span=21, adjust=False).mean()
            
            delta = data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            data['RSI'] = 100 - (100 / (1 + rs))
            
            current_price = float(data['Close'].iloc[-1])
            ema9 = float(data['EMA_9'].iloc[-1])
            ema21 = float(data['EMA_21'].iloc[-1])
            rsi = float(data['RSI'].iloc[-1])
            
            st.metric(label="موجودہ قیمت (Current Price)", value=f"{current_price:.5f}")
            
            col1, col2 = st.columns(2)
            col1.metric(label="EMA 9", value=f"{ema9:.5f}")
            col1.metric(label="EMA 21", value=f"{ema21:.5f}")
            col2.metric(label="RSI (14)", value=f"{rsi:.2f}")
            
            signal = "HOLD (کوئی سگنل نہیں - انتظار کریں)"
            
            if (ema9 > ema21) and (40 <= rsi <= 55):
                signal = "🚀 STRONG BUY / CALL (اوپر جانے کا موقع)"
                st.success(f"### سگنل: {signal}")
            elif (ema9 < ema21) and (45 <= rsi <= 60):
                signal = "🔻 STRONG SELL / PUT (نیچے آنے کا موقع)"
                st.error(f"### سگنل: {signal}")
            else:
                st.warning(f"### سگنل: {signal}")
