import streamlit as st

def setup_page_config():
    st.set_page_config(
        page_title="TalentScout AI Assistant",
        page_icon="👨‍💼",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def custom_theme():
    return {
        "primaryColor": "#1976d2",
        "backgroundColor": "#ffffff",
        "secondaryBackgroundColor": "#f8f9fa",
        "textColor": "#262730",
        "font": "sans-serif"
    } 