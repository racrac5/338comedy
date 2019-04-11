import sqlite3
import bs4
from urllib.request import urlopen

# ('nu.db', subdirectory='results')
def get_file_path(path, subdirectory=None):
    import sys
    import os
    dir_path = os.path.dirname(sys.argv[0]) #helpers.py
    if subdirectory:
        return os.path.join(dir_path, subdirectory, path)
    else:
        return os.path.join(dir_path, path)


def create_or_replace_table():
    conn = sqlite3.connect(get_file_path('nu.db', subdirectory='results'))
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Pages')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS "Pages" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
        "url" CHAR(2000),
        "title" CHAR(2000),
        "summary" TEXT,
        "body" TEXT,
        "words" TEXT,
        "featured_image" TEXT,
        "page_rank" INTEGER)
    ''')
    return conn #this was added

def insert_into_database(conn, counter, row, page_count=1):
    print('You are going to insert the extracted data into the database:', list(row.keys()))
    cur = conn.cursor()
    cur.execute("INSERT INTO Pages VALUES (?, ?, ?, ? ,?, ?, ?, ?)", (counter, row['url'], row['title'], row['summary'], row['body'], row['words'], row['image'], page_count))
    
    conn.commit()  #save to database

def get_matching_pages(conn, search_term):
    print('You are going to query the database to find all of the search results and then return them...')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Pages WHERE lower(title) LIKE ?", ('%'+search_term+'%',))
    rows = cur.fetchall()

    results = []
    for row in rows:
        results.append(row)
    return results

def update_page_rank(conn, visited):
    cur = conn.cursor()
    for key in visited:
        cur.execute("UPDATE Pages SET page_rank=? WHERE url = ?", (visited[key], key))

import os
import sys
# print(sys.argv[0]) # prints helpers.py
# print(os.path.dirname(sys.argv[0])) #prints nothing
# print(os.path.dirname(os.path.abspath(sys.argv[0]))) #prints C:\Users\jairr\Downloads\hw05\hw05

print(get_file_path('nu.db', subdirectory='results')) # prints results\nu.db or nu.db