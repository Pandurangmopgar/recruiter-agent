import streamlit as st

def show_feedback(message_type: str, message: str):
    if message_type == "success":
        st.success(message)
    elif message_type == "error":
        st.error(message)
    elif message_type == "info":
        st.info(message)
    elif message_type == "warning":
        st.warning(message) 