import streamlit as st
from datetime import date

import yfinance as yf
from plotly import graph_objs as go

def show_about_page():
    st.title("JII30 Stock Prediction App")