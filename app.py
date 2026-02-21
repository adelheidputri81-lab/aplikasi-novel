import streamlit as st
import google.generativeai as genai

# Tampilan Aplikasi
st.set_page_config(page_title="Penulis Novel AI", page_icon="✍️")
st.title("✍️ Generator Novel Otomatis")

# Kunci API kamu (Sudah saya masukkan berdasarkan fotomu)
api_key = "AIzaSyCc1JzfMMbaLaW6iofoRAjOCs-TO..." 

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    judul = st.text_input("Judul Novel Anda:")
    genre = st.selectbox("Pilih Genre:", ["Romance", "Horor", "Fantasy", "Action"])
    
    if st.button("Mulai Menulis"):
        with st.spinner("Sedang menulis..."):
            prompt = f"Tuliskan bab satu novel {genre} berjudul {judul}."
            response = model.generate_content(prompt)
            st.markdown("---")
            st.write(response.text)
