import streamlit as st
from streamlit_lottie import st_lottie
from utils import load_lottieurl

def show_home():
    # Load Animasi Robot
    lottie_ai = load_lottieurl("https://lottie.host/6253507d-9d7a-40a2-9721-65476a6d635a/lK8XW2lG8X.json")

    # Membagi layar jadi 2 kolom (Kiri: Teks, Kanan: Animasi)
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.title("Dominate the Chessboard ♟️")
        st.markdown("""
        Selamat datang di **Sistem Pendukung Keputusan Magic Chess**.
        
        Aplikasi ini membantu Anda menganalisis strategi terbaik menggunakan algoritma **Machine Learning**.
        
        **Fitur Utama:**
        * 📊 **Prediksi Akurat**: Menggunakan data historis Mythic match.
        * 🤖 **AI Powered**: Didukung Random Forest & XGBoost.
        * ⚡ **Cepat**: Hasil analisis instan.
        """)
        
        st.info("Silakan pilih menu **'Prediksi AI'** di atas untuk mulai!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if lottie_ai:
            st_lottie(lottie_ai, height=350, key="anim_home")