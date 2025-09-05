import streamlit as st
from mentor import mentor_page
from about import about_page

# 👇 Your login logic (make sure username is stored)
def check_login():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.subheader("🔐 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "student" and password == "mentor123":
                st.session_state.logged_in = True
                st.session_state.username = username   # ✅ STORE username
                st.success("✅ Logged in successfully!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
        st.stop()

# ✅ Run login
check_login()

# ✅ 👋 Welcome message — after login
if st.session_state.logged_in and 'username' in st.session_state:
    st.sidebar.markdown(f"👋 Welcome, **{st.session_state.username.capitalize()}**")

# ✅ Navigation section
page = st.sidebar.selectbox("Navigate", ("Mentor", "About"))

if page == "Mentor":
    mentor_page()
elif page == "About":
    about_page()
