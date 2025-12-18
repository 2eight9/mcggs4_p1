import streamlit as st
import base64

# --- Import Modul ---
from utils import load_model_assets, get_all_commanders
from components.header import render_header
from components.footer import render_footer
from views.navbar import create_navbar 

# --- Import Halaman ---
import views.home as view_home
import views.prediction as view_pred
import views.about as view_about
import views.contact as view_contact

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Magic Chess AI",
    page_icon="♟️",
    layout="wide",
    # "auto" = Terbuka di Desktop, Tertutup (Hamburger) di HP
    initial_sidebar_state="auto" 
)

# 2. SETUP STYLE & BACKGROUND
def setup_app_style(css_file, image_file):
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    with open(image_file, "rb") as f:
        data = f.read()
    b64_img = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        :root {{ --bg-image: url("data:image/png;base64,{b64_img}"); }}
        </style>
        """,
        unsafe_allow_html=True
    )

setup_app_style("assets/style.css", "assets/background.png")

# 3. LOAD DATA
model, le_comm, le_gogo = load_model_assets()
all_commanders = get_all_commanders()

# 4. TAMPILKAN HEADER (Di Konten Utama)
render_header()

# 5. TAMPILKAN NAVBAR (Di Sidebar)
selected_menu = create_navbar()

# 6. LOGIKA HALAMAN
# Bungkus konten dalam container agar rapi
main_container = st.container()

with main_container:
    if selected_menu == "Home":
        view_home.show_home()

    elif selected_menu == "Prediksi AI":
        if model:
            view_pred.show_prediction(model, le_comm, le_gogo, all_commanders)
        else:
            st.error("⚠️ Model AI belum siap!")

    elif selected_menu == "About":
        view_about.show_about()

    elif selected_menu == "Contact":
        view_contact.show_contact()

# 7. FOOTER
render_footer()