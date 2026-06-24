import streamlit as st

st.set_page_config(
    page_title="Face Attendance System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🔐 Admin Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "admin123":
        st.session_state.logged_in = True
        st.switch_page("pages/1_dashboard.py")
    else:
        st.error("Invalid Credentials")