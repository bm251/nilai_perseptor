from config.database import get_connection

def get_mata_kuliah():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM mata_kuliah")
    return cur.fetchall()

def get_item_penilaian(mk_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT ip.id, ap.cpmk, ap.materi, ip.deskripsi FROM item_penilaian ip JOIN aspek_penilaian ap ON ip.aspek_id = ap.id WHERE ap.mk_id = %s", (mk_id,))
    return cur.fetchall()
