import streamlit as st

def render_header():
    # Menggunakan HTML custom untuk judul gradasi warna
    st.markdown("""
    <div class="custom-header">
        <h1 style="font-size: 3rem; background: -webkit-linear-gradient(left, #00C9FF, #92FE9D); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Magic Chess Predictor AI
        </h1>
        <p style="font-size: 1.2rem; font-style: italic; opacity: 0.8; color: white;">
            "Prediksi Kemenangan Anda Sebelum Pertandingan Dimulai"
        </p>
    </div>
    """, unsafe_allow_html=True)