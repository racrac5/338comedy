# python3 -m http.server --cgi 8000
#!/usr/bin/python
import cgi, cgitb
import os
import sys
from urllib.request import urlopen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'scripting')))
import tagging
import lister
import nltk
import random
from nltk.tokenize import word_tokenize


#################################################################################################

form = cgi.FieldStorage()
dropdown = form.getvalue('dropdown')
prompt = form.getvalue('prompt')

index = 0
if dropdown == "Place": index = 1
elif dropdown == "Occupation": index = 2

randval1 = 0
randval2 = 0
#Check to see if input is valid in our lists
if prompt.lower() in lister.dictdict[index].values():
    #Pick two other random values from the list 
    randval1 = random.choice(random.choice(lister.dictdict))
    randval2 = random.choice(random.choice(lister.dictdict))

# add error check

print("Content-type:text/html")
print("")
print("")
print(""" 
	<head>
		<meta charset="utf-8"/> 
		<link rel="stylesheet" type="text/css" href="http://localhost:8000/style.css">
	</head>
	<body>
		<p class="wordBox">This was your topic: %s (Choice #%s)</p>
		<p class="wordBox">This was your prompt: "%s"</p>
		<p class="wordBox">Here is randval1: %s</p>
		<p class="wordBox">Here is randval2: %s</p>	
	</body>
""" % (dropdown, index, prompt, randval1, randval2))