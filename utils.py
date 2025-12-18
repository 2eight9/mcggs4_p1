import streamlit as st
import joblib
import base64
import os
import requests

# --- 1. FUNGSI DEKORASI (CSS, BG, LOTTIE) ---
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"File CSS {file_name} tidak ditemukan.")

def add_bg_from_local(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as file:
            encoded_string = base64.b64encode(file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True)

@st.cache_data 
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200: return None
        return r.json()
    except: return None

# --- 2. FUNGSI MODEL & DATA ---
@st.cache_resource 
def load_model_assets():
    try:
        # Pastikan path file .pkl benar
        model = joblib.load('model_magic_chess_final.pkl')
        le_comm = joblib.load('encoder_commander_name.pkl') 
        le_gogo = joblib.load('encoder_gogo_commander.pkl') 
        return model, le_comm, le_gogo
    except FileNotFoundError:
        return None, None, None

def safe_transform(encoder, val):
    try:
        clean_val = val.lower().replace(" ", "_") 
        return encoder.transform([clean_val])[0]  
    except:
        return 0 

def get_all_commanders():
    return sorted([
        "Aamon", "Angela", "Aurora", "Chou", "Cyclops", "Dyrroth", "Fanny", 
        "Guinevere", "Gusion", "Harley", "Johnson", "Kagura", "Karina", 
        "Lancelot", "Layla", "Ling", "Lukas", "Lunox", "Lylia", "Minotaur", 
        "Miya", "Moscov", "Nana", "Paquito", "Popol dan Kupa", "Vale", 
        "Valir", "Wanwan", "Yu Zhong", "Zilong"
    ])

# --- 3. LOGIKA TIER & LIMITS ---

def get_synergy_limits():
    """Mengembalikan batas maksimal input untuk slider/number input"""
    return {
        # --- ROLE ---
        "weapon_master": 6, "marksman": 6, "mage": 6,
        "defender": 6, "bruiser": 6, "dauntless": 6,    
        "stargazer": 6, "swiftblade": 6, "phasewarper": 4, 
        "scavenger": 3,   
        
        # --- FACTION ---
        "shadowcell": 10, "mortal_rival": 2, "kof": 11,
        "soul_vessels": 10, "starwing": 10, "luminexus": 10,
        "aspirant": 10, "toy_mischief": 10, "glory_league": 6,
        "metro_zero": 22, "beyond_the_clouds": 4, 
        "default": 10
    }

def get_synergy_tiers():
    """
    Daftar Tier Aktif untuk logika konversi dan validasi visual.
    """
    metro_tiers = list(range(2, 23)) # Metro Zero aktif dari 2 s.d 22

    return {
        # === FACTION KHUSUS ===
        "kof": [2, 4, 6, 11],
        "soul_vessels": [2, 4, 6, 10],
        "starwing": [2, 4, 6, 10],     
        "luminexus": [2, 4, 6, 10],
        "aspirant": [2, 4, 6, 10],     
        "toy_mischief": [2, 4, 6, 10],
        "shadowcell": [2, 4, 6, 10],
        "metro_zero": metro_tiers, 
        "mortal_rival": [1, 2], 
        "glory_league": [2, 4, 6],
        "beyond_the_clouds": [2, 4], 

        # === ROLE (CLASS) ===
        "weapon_master": [2, 4, 6],
        "marksman": [2, 4, 6],
        "mage": [2, 4, 6],
        "defender": [2, 4, 6], 
        "bruiser": [2, 4, 6],           
        "dauntless": [2, 4, 6],
        "stargazer": [2, 4, 6],
        "swiftblade": [2, 4, 6],
        "phasewarper": [2, 4],      
        "scavenger": [2, 3],
    }

def calculate_active_count(raw_count, synergy_key):
    """Mengubah input user menjadi tier aktif terdekat"""
    tiers_map = get_synergy_tiers()
    
    if synergy_key not in tiers_map:
        return raw_count
    
    # Urutkan tier dari terbesar ke terkecil
    tiers = sorted(tiers_map[synergy_key], reverse=True)
    
    for tier in tiers:
        if raw_count >= tier:
            return tier 
            
    return 0