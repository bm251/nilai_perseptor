from config.database import get_connection
import pandas as pd

def rekap_detail_mahasiswa(nim):
    conn = get_connection()
    query = """
    SELECT
      mk.nama AS mata_kuliah,
      ap.materi AS aspek,
      ip.deskripsi AS item_penilaian,
      n.nilai
    FROM nilai n
    JOIN item_penilaian ip ON n.item_id = ip.id
    JOIN aspek_penilaian ap ON ip.aspek_id = ap.id
    JOIN mata_kuliah mk ON ap.mk_id = mk.id
    WHERE n.nim = %s
    ORDER BY mk.nama, ap.id, ip.id
    """
    return pd.read_sql(query, conn, params=(nim,))
def rekap_cpmk_mahasiswa(nim):
    conn = get_connection()
    query = """
    SELECT
      mk.nama AS mata_kuliah,
      ap.materi AS aspek,
      ROUND(AVG(n.nilai),2) AS rata_cpmk
    FROM nilai n
    JOIN item_penilaian ip ON n.item_id = ip.id
    JOIN aspek_penilaian ap ON ip.aspek_id = ap.id
    JOIN mata_kuliah mk ON ap.mk_id = mk.id
    WHERE n.nim = %s
    GROUP BY mk.id, ap.id
    """
    return pd.read_sql(query, conn, params=(nim,))
def rekap_nilai_akhir(nim):
    conn = get_connection()
    query = """
    SELECT
      mk.nama AS mata_kuliah,
      ROUND(AVG(n.nilai),2) AS nilai_akhir
    FROM nilai n
    JOIN item_penilaian ip ON n.item_id = ip.id
    JOIN aspek_penilaian ap ON ip.aspek_id = ap.id
    JOIN mata_kuliah mk ON ap.mk_id = mk.id
    WHERE n.nim = %s
    GROUP BY mk.id
    """
    return pd.read_sql(query, conn, params=(nim,))

