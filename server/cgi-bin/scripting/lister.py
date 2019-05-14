import sys
import os
import nltk
from nltk.tokenize import word_tokenize

class Prompt: 
	def __init__(self, name, category):
		self.n = name
		self.c = category

animaldict = dict()
placedict = dict()
occupationdict = dict()
dictdict = dict()

path_animal = os.path.abspath(os.path.join(os.path.dirname(__file__), "text_files/listanimals.txt"))
path_places = os.path.abspath(os.path.join(os.path.dirname(__file__), "text_files/places.txt"))
path_occupations = os.path.abspath(os.path.join(os.path.dirname(__file__), "text_files/occupations.txt"))

try:
	with open(path_animal, encoding = "utf8") as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i = 0
	for newitem in grabAnimal :
		entry = newitem.lower()
		animaldict[i] = entry
		i = i + 1
	myfile.close()

	with open(path_places, encoding = "utf8") as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i=0
	for newitem in grabAnimal :
		entry = newitem.lower()
		placedict[i] = entry
		i = i + 1
	myfile.close()

	with open(path_occupations, encoding = "utf8") as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i=0
	for newitem in grabAnimal :
		newitem = newitem.lower()
		entry = newitem
		occupationdict[i] = entry
		i = i + 1
	myfile.close()

	dictdict[0] = animaldict
	dictdict[1] = placedict
	dictdict[2] = occupationdict

except IOError:
   print("There was an error writing to", file_name)
   sys.exit()