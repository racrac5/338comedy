# python3 -m http.server --cgi 8000
#!/usr/bin/python
import cgi, cgitb
import sqlite3
import bs4
from urllib.request import urlopen
import database_helpers

conn = database_helpers.create_or_replace_table()

form = cgi.FieldStorage()
prompt = form.getvalue('prompt')

print("Content-type:text/html")
print("")
print("")
print(""" 
	<head>
    	<meta charset="utf-8"/> 
    	<link rel="stylesheet" type="text/css" href="http://localhost:8000/style.css">
 	</head>
	""")

# Make sure entries in database are unique?
database_helpers.insert_all_values_into_database(conn, "walk into a bar", "standard", prompt)
database_helpers.insert_all_values_into_database(conn, "off a cliff", "dark", prompt)
database_helpers.insert_all_values_into_database(conn, "off a cliff", "dark", "dog")

rows = database_helpers.get_matching_value_from_column(conn, "humor", "dark") #get rows that have the term "dark" in the "humor" column
table = database_helpers.get_table(conn)

print("""
 <body>
     <p>This was your prompt: %s</p>
 	 <p class="tableBox">Here is the entire table: %s</p>
	 <p>Searched rows: %s</p>
 </body>
""" % (prompt, table, rows))