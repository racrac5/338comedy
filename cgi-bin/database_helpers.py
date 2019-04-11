import sqlite3
import bs4
from urllib.request import urlopen

def create_or_replace_table():
    conn = sqlite3.connect('comedy338.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Pages')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS "COMEDY" (
        "trope" CHAR(2000),
        "humor" TEXT,
        "body" TEXT)
    ''')
    return conn

def insert_into_database(conn, trope, humor, body):
    cur = conn.cursor()
    cur.execute("INSERT INTO COMEDY VALUES (?, ?, ?)", (trope, humor, body))
    conn.commit()

def get_matching_values(conn, search_term):
    cur = conn.cursor()
    cur.execute("SELECT * FROM COMEDY WHERE body LIKE ?", ('%'+search_term+'%',))
    rows = cur.fetchall()
    return rows

###########################################################################################
# def update_page_rank(conn, visited):
    # cur = conn.cursor()
    # for key in visited:
    #     cur.execute("UPDATE Pages SET page_rank=? WHERE url = ?", (visited[key], key))

# import os
# import sys
# # print(sys.argv[0]) # prints helpers.py
# # print(os.path.dirname(sys.argv[0])) #prints nothing
# # print(os.path.dirname(os.path.abspath(sys.argv[0]))) #prints C:\Users\jairr\Downloads\hw05\hw05

# print(get_file_path('nu.db', subdirectory='results')) # prints results\nu.db or nu.db