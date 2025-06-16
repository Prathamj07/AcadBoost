import streamlit as st
import requests
import json

from utils.auth import role_required
from utils.ui import show_header, show_notification

# Gemini API configuration
GEMINI_API_KEY = "AIzaSyCwAgIkonxIC8aIHbrOV5aTcAMHsz8iChk"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def get_gemini_response(prompt):
    """Get response from Gemini API."""
    try:
        headers = {
            'Content-Type': 'application/json'
        }
        
        data = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

@role_required(["student"])
def show_career_sathi():
    """Show the Career Sathi page for students."""
    user = st.session_state.user
    email = st.session_state.email
    
    show_header("Career Sathi", "Your AI Career Guide")
    
    st.markdown("""
    Welcome to Career Sathi! I'm here to help you with:
    - Career guidance and counseling
    - Industry insights and trends
    - Skill development recommendations
    - Interview preparation tips
    - Resume and portfolio advice
    - Job search strategies
    """)
    
    # Initialize chat history
    if "career_chat_history" not in st.session_state:
        st.session_state.career_chat_history = []
    
    # Display chat history
    for message in st.session_state.career_chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    user_input = st.chat_input("Ask me anything about your career...")
    
    if user_input:
        # Add user message to chat history
        st.session_state.career_chat_history.append({"role": "user", "content": user_input})
        
        # Show user message
        with st.chat_message("user"):
            st.write(user_input)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_gemini_response(user_input)
                st.write(response)
                st.session_state.career_chat_history.append({"role": "assistant", "content": response})
    
    # Add some example questions
    st.markdown("### Example Questions")
    example_questions = [
        "What are the top skills needed for a software developer?",
        "How can I prepare for technical interviews?",
        "What career paths are available in data science?",
        "How can I improve my resume?",
        "What are the current trends in AI and machine learning?"
    ]
    
    for question in example_questions:
        if st.button(question, key=f"example_{question}"):
            st.session_state.career_chat_history.append({"role": "user", "content": question})
            with st.chat_message("user"):
                st.write(question)
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = get_gemini_response(question)
                    st.write(response)
                    st.session_state.career_chat_history.append({"role": "assistant", "content": response}) 