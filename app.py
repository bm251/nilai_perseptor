import streamlit as st
from ui.form_penilaian import show_form

from ui.rekap_mahasiswa import show_rekap_mahasiswa

menu = st.sidebar.selectbox(
    "Menu",
    ["Input Nilai", "Rekap Mahasiswa"]
)

if menu == "Input Nilai":
    show_form()
else:
    show_rekap_mahasiswa()
    
st.set_page_config(page_title="Penilaian Perseptor")

#show_form()
