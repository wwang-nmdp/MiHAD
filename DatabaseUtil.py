import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def get_miha_rows(conn, size, offset):
    cur = conn.cursor()
    cur.execute("SELECT * FROM MiHAIP_output_cut_uniq_ord  LIMIT %s OFFSET %s ;" % (size, offset))
    return cur.fetchall()


def get_known_miha(conn, size, offset):
    cur = conn.cursor()
    cur.execute("SELECT * FROM KnowMiHA  LIMIT %s OFFSET %s ;" % (size, offset))
    return cur.fetchall()