import streamlit as st

def show_about():   
    # Judul Halaman
    st.title("♟️Tentang Magic Chess AI")
    st.markdown("### Asisten Strategi Cerdas Anda")
    
    st.write("""
    **Magic Chess Go Go Predictor** adalah aplikasi berbasis kecerdasan buatan (AI) yang dirancang 
    untuk membantu pemain Magic Chess menyusun strategi terbaik. Aplikasi ini bukan sekadar alat pencatat, 
    melainkan sistem cerdas yang dapat memprediksi peluang kemenangan Anda sebelum pertandingan dimulai.
    """)
    
    st.markdown("---")

    # --- BAGIAN 2 KOLOM: CARA KERJA & FITUR ---
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚙️ Cara Kerja Sistem")
        st.info("""
        Sistem ini bekerja menggunakan **Machine Learning** (Pembelajaran Mesin). 
        
        1. **Analisis Data:** Model AI telah "belajar" dari ribuan data pertandingan sebelumnya.
        2. **Pola Kemenangan:** AI mengenali pola kombinasi Commander dan Sinergi yang sering menang (Top 4).
        3. **Prediksi Real-time:** Saat Anda memasukkan strategi, AI membandingkannya dengan pola yang dipelajari untuk menghitung persentase keberhasilan.
        """)

    with col2:
        st.subheader("🚀 Fitur Utama")
        st.success("""
        * **Prediksi Akurat:** Menggunakan algoritma klasifikasi tingkat lanjut.
        * **Analisis Sinergi:** Memperhitungkan kombinasi Role dan Faction.
        * **Support Commander:** Mendukung Commander utama dan sistem Gogo Commander terbaru.
        * **Antarmuka Modern:** Tampilan Dark Mode yang nyaman dan interaktif.
        """)

    st.markdown("---")

   # ... (Kode bagian atas tetap sama) ...

    st.markdown("---")

    # --- BAGIAN TEKNOLOGI (DENGAN LOGO & LINK) ---
    st.subheader("💻 Teknologi di Balik Layar")
    st.write("Klik ikon di bawah untuk mempelajari teknologi yang digunakan:")
    
    # CSS Khusus agar ikon bergoyang sedikit saat di-hover (Efek interaktif)
    st.markdown("""
    <style>
    .tech-card {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        transition: transform 0.3s, background-color 0.3s;
        height: 100%;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .tech-card:hover {
        transform: translateY(-5px); /* Naik sedikit saat hover */
        background-color: rgba(255, 255, 255, 0.1);
        border-color: #00C9FF;
    }
    .tech-card img {
        margin-bottom: 10px;
    }
    .tech-link {
        text-decoration: none;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Buat 4 Kolom
    c1, c2, c3, c4 = st.columns(4)

    # --- 1. PYTHON ---
    with c1:
        st.markdown("""
        <a href="https://www.python.org/" target="_blank" class="tech-link">
            <div class="tech-card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="60">
                <h4>Python 3.9+</h4>
                <p style="font-size:12px; opacity:0.7;">Bahasa Utama</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

    # --- 2. STREAMLIT ---
    with c2:
        st.markdown("""
        <a href="https://streamlit.io/" target="_blank" class="tech-link">
            <div class="tech-card">
                <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="60">
                <h4>Streamlit</h4>
                <p style="font-size:12px; opacity:0.7;">Framework Web</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

    # --- 3. SCIKIT-LEARN ---
    with c3:
        st.markdown("""
        <a href="https://scikit-learn.org/stable/" target="_blank" class="tech-link">
            <div class="tech-card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="80">
                <h4>Scikit-Learn</h4>
                <p style="font-size:12px; opacity:0.7;">Otak AI / ML</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

    # --- 4. PANDAS ---
    with c4:
        st.markdown("""
        <a href="https://pandas.pydata.org/" target="_blank" class="tech-link">
            <div class="tech-card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Pandas_mark.svg" width="55">
                <h4>Pandas</h4>
                <p style="font-size:12px; opacity:0.7;">Analisis Data</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

    