import streamlit as st
from services.matakuliah import get_mata_kuliah, get_item_penilaian
from services.penilaian import simpan_nilai

def show_form():
    st.title("📝 Form Penilaian Perseptor")

    nim = st.text_input("NIM Mahasiswa")

    mk = get_mata_kuliah()
    mk_nama = [m["nama"] for m in mk]
    pilih = st.selectbox("Mata Kuliah", mk_nama)

    mk_id = next(m["id"] for m in mk if m["nama"] == pilih)

    items = get_item_penilaian(mk_id)

    nilai = {}
    for item in items:
        st.markdown(f"**CPMK:** {item['cpmk']}")
        nilai[item["id"]] = st.number_input(
            item["deskripsi"], 0, 100
        )

    if st.button("Simpan"):
        simpan_nilai(nim, nilai)
        st.success("Nilai tersimpan")
