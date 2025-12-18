import streamlit as st

def show_contact():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    st.title("📞 Hubungi Saya")

    # --- FORMULIR KONTAK (JANGAN UBAH SPASI DI BAWAH INI) ---
    # Kode HTML ini sengaja diratakan ke kiri agar tidak dianggap text biasa
    contact_form = """
    
<form action="https://formspree.io/f/mdannvwe" method="POST">
    <input type="text" name="name" placeholder="Nama Lengkap" required style="width:100%; padding:10px; margin-bottom:10px; border-radius:5px; border:1px solid #ccc;">
    <input type="email" name="email" placeholder="Alamat Email Anda" required style="width:100%; padding:10px; margin-bottom:10px; border-radius:5px; border:1px solid #ccc;">
    <textarea name="message" placeholder="Tulis pesan Anda di sini..." required style="width:100%; padding:10px; margin-bottom:10px; border-radius:5px; border:1px solid #ccc; min-height: 100px;"></textarea>
    <button type="submit" style="background-color:#00C9FF; color:black; padding:10px 20px; border:none; border-radius:5px; cursor:pointer; font-weight:bold;">Kirim Pesan 🚀</button>
</form>
"""
    # -------------------------------------------------------

    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.info("Silakan isi formulir di bawah. Pastikan email Anda benar agar saya bisa membalasnya.")
        st.markdown(contact_form, unsafe_allow_html=True)
    
    with col2:
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/contact-us-5795988-4849052.png")
    
    st.markdown('</div>', unsafe_allow_html=True)