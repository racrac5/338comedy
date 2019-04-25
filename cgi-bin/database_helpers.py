# Make sure entries in database are unique?

import sqlite3
import bs4
from urllib.request import urlopen

def create_or_replace_table():
    conn = sqlite3.connect('comedy338.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Comedy')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS "Comedy" (
        "trope" TEXT,
        "humor" TEXT,
        "prompt" TEXT)
    ''')
    return conn

def insert_all_values_into_database(conn, trope, humor, prompt):
    cur = conn.cursor()
    cur.execute("INSERT INTO Comedy VALUES (?, ?, ?)", (trope, humor, prompt))
    conn.commit()

def get_matching_value_from_column(conn, column, search_term):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM Comedy WHERE (%s) LIKE ?" % (column), ('%'+search_term+'%',))
        rows = cur.fetchall()
        return rows
    except:
        print("An exception occurred")

def get_table(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Comedy")
    rows = cur.fetchall()
    return rows




# This function may not be used
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
###########################################################################################