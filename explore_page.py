import streamlit as st
from datetime import date

import yfinance as yf
from plotly import graph_objs as go

st.title("JII30 Stock Prediction App")
st.header("Explore JII30 closing price in the last 2 years")

stocks = ("ACES.JK", "ADRO.JK", "AKRA.JK", "ANTM.JK", "ASII.JK",
          "BRIS.JK", "BRMS.JK", "BRPT.JK", "CPIN.JK", "ESSA.JK",
          "EXCL.JK", "HRUM.JK", "ICBP.JK", "INCO.JK", "INDF.JK",
          "INDY.JK", "INKP.JK", "INTP.JK", "ITMG.JK", "KLBF.JK",
          "MDKA.JK", "MIKA.JK", "PGAS.JK", "PTBA.JK", "SCMA.JK",
          "SMGR.JK", "TLKM.JK", "TPIA.JK", "UNTR.JK", "UNVR.JK")

selected_stocks = st.selectbox("Select stock:", stocks)

@st.cache_data

def load_data(ticker):
    data = yf.download(ticker, period="2y")
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data...")
data = load_data(selected_stocks)
data_load_state.text("Loading data... done!")

st.subheader("Raw Data")
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

st.subheader("Time Series Data")
plot_raw_data()