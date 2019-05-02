# -*- coding: utf-8 -*-
import sys
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
eventdict = dict()

try:
	with open('text_files/listanimals.txt', 'r') as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i = 0
	for newitem in grabAnimal :
		entry = newitem.lower()
		animaldict[i] = entry
		i = i + 1
	myfile.close()

	with open('text_files/places.txt', 'r') as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i=0
	for newitem in grabAnimal :
		entry = newitem.lower()
		placedict[i] = entry
		i = i + 1
	myfile.close()

	with open('text_files/occupations.txt', 'r') as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i=0
	for newitem in grabAnimal :
		newitem = newitem.lower()
		entry = newitem
		occupationdict[i] = entry
		i = i + 1
	myfile.close()

	with open('text_files/events.txt', 'r') as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i=0
	for newitem in grabAnimal :
		newitem = newitem.lower()
		entry = newitem
		eventdict[i] = entry
		i = i + 1
	myfile.close()

	dictdict[0] = animaldict
	dictdict[1] = placedict
	dictdict[2] = occupationdict
	dictdict[3] = eventdict





except IOError:
   print("There was an error writing to", file_name)
   sys.exit()