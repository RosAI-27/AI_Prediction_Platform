"""Streamlit entry point for the AI Prediction Platform (academic project)."""

import streamlit as st

st.set_page_config(
    page_title="AI Prediction Platform",
    page_icon="🤖",
    layout="wide",
)

st.title("AI Prediction Platform")
st.write(
    "An academic deep-learning application with two modules: vegetable image "
    "classification and 20-trading-day Tesla (TSLA) price forecasting."
)

st.info("Choose a module from the pages in the sidebar to get started.")
