import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from about_page import about_page

page = st.sidebar.selectbox("Explore or Predict", ("Explore", "Predict"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

about = st.sidebar.button("About page")

if about:
    show_predict_page()