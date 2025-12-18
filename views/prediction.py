import streamlit as st
import pandas as pd
import os
from streamlit_lottie import st_lottie

# Import fungsi dari utils yang sudah diperbaiki
from utils import (
    safe_transform, 
    load_lottieurl, 
    get_synergy_limits, 
    calculate_active_count,
    get_synergy_tiers # Penting: Kita butuh ini untuk tahu batas minimal
)

def show_prediction(model, le_comm, le_gogo, all_commanders):
    # --- 1. LOAD ANIMASI ---
    lottie_win = load_lottieurl("https://lottie.host/5e00301a-12e0-410a-8c88-662584160408/sI7Z3Wn5z6.json") 
    lottie_lose = load_lottieurl("https://lottie.host/a0774df7-3803-49d7-83d8-ad9d08235210/c8uL4z6K8j.json") 

    st.title("🎮 Simulasi Strategi")
    st.caption("Atur kombinasi Commander, Role, dan Faction Anda.")

    # --- BAGIAN 2: PILIH COMMANDER ---
    col_c1, col_c2 = st.columns(2)
    
    def render_img(name):
        clean_name = name.lower().replace(" ", "_")
        path_png = f"images/{clean_name}.png"
        path_jpg = f"images/{clean_name}.jpg"
        
        if os.path.exists(path_png): st.image(path_png, width=130)
        elif os.path.exists(path_jpg): st.image(path_jpg, width=130)
        else: st.caption(f"Img: {clean_name}")

    with col_c1:     
        st.subheader("Commander Utama")
        pilih_comm = st.selectbox("Pilih Hero", all_commanders, key="main_c")
        render_img(pilih_comm)

    with col_c2:
        st.subheader("Gogo Commander")
        pilih_gogo = st.selectbox("Pilih Gogo", all_commanders, key="gogo_c")
        render_img(pilih_gogo)

    # --- 3. INPUT SINERGI (DENGAN PERINGATAN MERAH) ---
    st.markdown("### 🎛️ Konfigurasi Level Sinergi")
    
    # Ambil limits (max input) dan tiers (aturan aktif) dari utils
    limits = get_synergy_limits()
    all_tiers_map = get_synergy_tiers() 
    
    input_data = {} 

    # Definisi List Sinergi
    roles_list = [
        ("Weapon Master", "weapon_master"), ("Marksman", "marksman"), ("Mage", "mage"),
        ("Defender", "defender"), ("Bruiser", "bruiser"),("Dauntless", "dauntless"), ("Stargazer", "stargazer"),
        ("Swiftblade", "swiftblade"), ("Phasewarper", "phasewarper"), ("Scavenger", "scavenger"),
    ]
    factions_list = [
        ("Shadowcell", "shadowcell"), ("Mortal Rival", "mortal_rival"), ("K.O.F", "kof"),
        ("Soul Vessels", "soul_vessels"), ("Starwing", "starwing"), ("Luminexus", "luminexus"),
        ("Aspirants", "aspirant"), ("Toy Mischief", "toy_mischief"), ("Glory League", "glory_league"),
        ("Metro Zero", "metro_zero"), ("Beyond The Clouds", "beyond_the_clouds"),
    ]

    def render_inputs(synergy_list):
        cols = st.columns(2) 
        for i, (label, suffix) in enumerate(synergy_list):
            col = cols[i % 2]
            
            # Ambil Max Value dari utils
            max_val = limits.get(suffix, 10)
            db_key = f"synergy_count_{suffix}"
            
            with col:
                # 1. Kotak Input
                val = st.number_input(
                    label=label, min_value=0, max_value=max_val, value=0, step=1, key=db_key
                )
                input_data[db_key] = val
                
                # 2. Logika Peringatan (Warning Logic)
                if val > 0:
                    # Ambil daftar tier untuk sinergi ini (misal: [2, 4, 6])
                    tiers = all_tiers_map.get(suffix, [])
                    
                    if tiers:
                        # Cari angka minimal agar sinergi aktif (angka terkecil di list)
                        min_req = min(tiers)
                        
                        # Cek: Apakah input user di bawah batas minimal?
                        if val < min_req:
                            # Tampilkan peringatan merah
                            st.caption(f":red[⚠️ Belum Aktif (Min. {min_req})]")
                        else:
                            # Hitung level aktifnya (untuk konfirmasi hijau)
                            active_now = calculate_active_count(val, suffix)
                            st.caption(f":green[✅ Aktif (Tier {active_now})]")

    with st.expander("🛠️ Klik untuk Buka Panel Sinergi", expanded=True):
        tab_role, tab_faction = st.tabs(["🛡️ ROLE (Class)", "🏳️ FACTION (Origin)"])
        with tab_role: render_inputs(roles_list)
        with tab_faction: render_inputs(factions_list)

    # --- 4. EKSEKUSI ---
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("JALANKAN ANALISIS 🚀", use_container_width=True):
        
        if model is None:
            st.error("⚠️ Model tidak ditemukan!")
            return

        with st.spinner('AI sedang memproses tier sinergi...'):
            final_input = input_data.copy()
            final_input['commander_name'] = safe_transform(le_comm, pilih_comm)
            final_input['gogo_comander'] = safe_transform(le_gogo, pilih_gogo)
            
            # --- BERSIHKAN DATA SEBELUM MASUK AI ---
            # Pastikan yang dikirim ke AI adalah nilai tier (bukan input mentah)
            for key, val in input_data.items():
                if "synergy_count_" in key:
                    pure_name = key.replace("synergy_count_", "")
                    active_val = calculate_active_count(val, pure_name)
                    final_input[key] = active_val

            # List kolom wajib
            required_cols = [
                'commander_name', 'gogo_comander', 
                'synergy_count_shadowcell', 'synergy_count_mortal_rival', 'synergy_count_kof', 
                'synergy_count_soul_vessels', 'synergy_count_starwing', 'synergy_count_luminexus', 
                'synergy_count_aspirant', 'synergy_count_toy_mischief', 'synergy_count_glory_league', 
                'synergy_count_metro_zero', 'synergy_count_beyond_the_clouds', 
                'synergy_count_defender', 'synergy_count_dauntless',
                'synergy_count_weapon_master', 'synergy_count_marksman', 'synergy_count_stargazer', 
                'synergy_count_swiftblade', 'synergy_count_mage', 'synergy_count_phasewarper', 
                'synergy_count_scavenger'
            ]
            
            # Filter Data
            data_vals = {k: [v] for k, v in final_input.items() if k in required_cols}
            for col in required_cols:
                if col not in data_vals: data_vals[col] = [0]
            
            df_pred = pd.DataFrame(data_vals)[required_cols]
            
            try:
                pred = model.predict(df_pred)[0]
                prob = model.predict_proba(df_pred)[0]
                win_prob = prob[1]
                lose_prob = prob[0]
                
                st.markdown("---")
                if pred == 1:
                    st.balloons()
                    c1, c2 = st.columns([1, 2])
                    with c1: 
                        if lottie_win: st_lottie(lottie_win, height=180, key="w")
                        else: st.header("🏆")
                    with c2:
                        st.markdown(f"""
                        <div style="background:rgba(40,167,69,0.2);padding:15px;border-radius:10px;border:1px solid #28a745;">
                            <h2 style="color:#28a745;margin:0;">🏆 POTENSI MENANG</h2>
                        </div>""", unsafe_allow_html=True)
                        st.write(f"Keyakinan: **{win_prob*100:.1f}%**")
                        st.progress(int(win_prob*100))
                else:
                    c1, c2 = st.columns([1, 2])
                    with c1: 
                        if lottie_lose: st_lottie(lottie_lose, height=180, key="l")
                        else: st.header("💀")
                    with c2:
                        st.markdown(f"""
                        <div style="background:rgba(220,53,69,0.2);padding:15px;border-radius:10px;border:1px solid #dc3545;">
                            <h2 style="color:#dc3545;margin:0;">💀 BERISIKO KALAH</h2>
                        </div>""", unsafe_allow_html=True)
                        st.write(f"Risiko: **{lose_prob*100:.1f}%**")
                        st.progress(int(lose_prob*100))

            except Exception as e:
                st.error(f"Error Model: {e}")