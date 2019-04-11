#!/usr/bin/python

import cgi, cgitb

first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
print("Content-type:text/html")
print("")
print("")
print("Hello - Second CGI Program")
print("")
print("")
print("   Hello %s %s" % (first_name, last_name))
print("")
print("")