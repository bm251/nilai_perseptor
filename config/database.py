import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["host"],
        user=st.secrets["user"],
        password=st.secrets["password"],
        database=st.secrets["database"],
        port=int(st.secrets["port"])
    )

