#!/usr/bin/python
import cgi, cgitb
import sqlite3
import bs4
from urllib.request import urlopen
import database_helpers

conn = database_helpers.create_or_replace_table()

form = cgi.FieldStorage()
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print("Content-type:text/html")
print("")
print("")
print("   Hello %s %s" % (first_name, last_name))
print("")
print("")

# Make sure entries in database are unique -> use id 
database_helpers.insert_into_database(conn, "walk into a bar", "surreal", first_name)
row = database_helpers.get_matching_values(conn, "Cee")
print(row)
