from config.database import get_connection

def simpan_nilai(nim, nilai_dict):
    conn = get_connection()
    cur = conn.cursor()

    for item_id, nilai in nilai_dict.items():
        cur.execute("""
            INSERT INTO nilai (nim, item_id, nilai)
            VALUES (%s, %s, %s)
        """, (nim, item_id, nilai))

    conn.commit()
