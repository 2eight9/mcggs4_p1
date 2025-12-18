import streamlit as st
from streamlit_option_menu import option_menu

def create_navbar():
    # HAPUS kode "with st.sidebar:" agar menu pindah ke tengah halaman
    
    selected = option_menu(
        menu_title=None,  # Hapus judul menu agar lebih rapi di atas
        options=["Home", "Prediksi AI", "About", "Contact"], 
        icons=["house", "cpu", "info-circle", "envelope"], 
        menu_icon="cast", 
        default_index=0,
        orientation="horizontal",  # <--- INI KUNCINYA (Supaya jadi memanjang ke samping)
        styles={
            "container": {"padding": "0!important", "background-color": "rgba(0,0,0,0.3)"}, # Background semi-transparan
            "icon": {"color": "orange", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "center", "margin": "5px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )
    
    return selected