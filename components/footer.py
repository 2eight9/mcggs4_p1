import streamlit as st
from datetime import datetime

def render_footer():
    year = datetime.now().year
    st.markdown(f"""
    <div class="custom-footer">
        <p>&copy; {year} <strong>Developed by <strong>Apriliano Boimau</strong></p>
    </div>
    """, unsafe_allow_html=True)