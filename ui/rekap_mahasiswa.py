import streamlit as st
from services.rekap import (
    rekap_detail_mahasiswa,
    rekap_cpmk_mahasiswa,
    rekap_nilai_akhir
)

def show_rekap_mahasiswa():
    st.title("📊 Rekap Nilai Mahasiswa")

    nim = st.text_input("Masukkan NIM Mahasiswa", key="nim_input_rekap")

    if nim:
        st.subheader("📋 Detail Penilaian")
        st.dataframe(rekap_detail_mahasiswa(nim))

        st.subheader("📘 Rekap CPMK")
        st.dataframe(rekap_cpmk_mahasiswa(nim))

        st.subheader("🎓 Nilai Akhir Mata Kuliah")
        st.dataframe(rekap_nilai_akhir(nim))
