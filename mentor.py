import streamlit as st
import subprocess
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

def ask_llama(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'llama2'],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()

def get_mentor_advice(branch, semester, skills, interest):
    prompt = f"""
    You are an AI Career Mentor for engineering students.
    The student is in {semester} semester, studying {branch}.
    Their current skills are: {skills}.
    Their area of interest is: {interest}.

    Based on this, suggest:
    - 3 recommended technologies or tools to learn next
    - 2 practical project ideas
    - 2 free learning resources (YouTube, Docs, etc.)
    - One career tip to bridge college-to-industry gap
    Format your response in clear bullet points.
    """
    return ask_llama(prompt)

def mentor_page():
    st.title("🎓 AI Skill Mentor – Bridge College to Career")

    branch = st.selectbox("Your Branch", ["AI & DS", "CSE", "ECE", "EEE", "MECH"])
    semester = st.selectbox("Current Semester", ["5th", "6th", "7th", "8th"])
    skills = st.text_area("List Your Current Skills (comma-separated)",
                          placeholder="e.g. Python, HTML, ML, SQL")
    interest = st.selectbox("Area of Interest", ["ML", "GenAI", "Full Stack", "Cybersecurity", "Data Analytics"])
    
    # ✅ Always initialize advice
    if 'advice' not in st.session_state:
        st.session_state.advice = ""

    if st.button("🧠 Get Guidance"):
       if skills:
          with st.spinner("Thinking like a mentor..."):
            advice = get_mentor_advice(branch, semester, skills, interest)

          st.session_state.advice = advice  # ✅ store it
          st.success("✅ Here's your personalized learning plan:")
          st.markdown(advice)

# ✅ Always show if present
    if st.session_state.advice:
        st.success("✅ Here's your personalized learning plan:")
        
    st.markdown(st.session_state.advice)

    if st.button("🔊 Read Aloud"):
       speak_text(st.session_state.advice)

    
    if st.button("Read Aloud"):
                speak_text(advice)
    else:
            st.warning("Please list your current skills.")
