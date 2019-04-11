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

try:
	with open('listanimals.txt', 'r') as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i = 0
	for newitem in grabAnimal :
		entry = newitem
		animaldict[i] = entry
		i = i + 1
	myfile.close()

	with open('places.txt', 'r') as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i=0
	for newitem in grabAnimal :
		entry = newitem
		placedict[i] = entry
		i = i + 1
	myfile.close()

	with open('occupations.txt', 'r') as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i=0
	for newitem in grabAnimal :
		entry = newitem
		occupationdict[i] = entry
		i = i + 1
	myfile.close()

	dictdict[0] = animaldict
	dictdict[1] = placedict
	dictdict[2] = occupationdict

	print(dictdict[2][3])




except IOError:
   print("There was an error writing to", file_name)
   sys.exit()