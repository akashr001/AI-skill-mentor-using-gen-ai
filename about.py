import streamlit as st

def about_page():
    st.title("📘 About This App")
    st.markdown("""
    **AI Skill Mentor** is a GenAI-powered Streamlit application that guides engineering students by providing:

    - Personalized skill growth plans
    - Real-world project ideas
    - Learning resources (free)
    - Career tips to bridge the college–industry gap

    Built with ❤️ using **LLaMA2**, **Ollama**, and **Streamlit**.
    """)
