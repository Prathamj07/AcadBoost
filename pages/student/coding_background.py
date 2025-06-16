import streamlit as st

from utils.auth import role_required
from utils.ui import show_header, show_notification

@role_required(["student"])
def show_coding_background():
    """Show the coding background page for students."""
    user = st.session_state.user
    email = st.session_state.email
    
    show_header("Coding Background", "Track your coding history and achievements")
    
    # Placeholder for future implementation
    st.info("This feature is coming soon! Here you will be able to:")
    st.markdown("""
    - Connect your GitHub profile to track your coding activity
    - Link your LeetCode account to showcase your problem-solving skills
    - View detailed analysis of your coding history
    - Get insights into your coding patterns and progress
    - Share your coding achievements with teachers and potential employers
    """)
    
    # Input fields for future implementation
    st.markdown("### Profile Links")
    github_url = st.text_input("GitHub Profile URL", placeholder="https://github.com/username")
    leetcode_url = st.text_input("LeetCode Profile URL", placeholder="https://leetcode.com/username")
    
    if st.button("Save Profile Links"):
        st.info("This feature is coming soon! Your profile links will be saved and used to track your coding activity.") 