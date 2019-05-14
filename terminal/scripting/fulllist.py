# -*- coding: utf-8 -*-
import sys
import nltk

from nltk.tokenize import word_tokenize


dictdict = dict()
fulldict = dict()

try:
	with open('text_files/allnounslist.txt', 'r') as myfile:
		data = myfile.read()
	grabAnimal = word_tokenize(data)
	i = 0
	for newitem in grabAnimal :
		entry = newitem.lower()
		fulldict[i] = entry
		i = i + 1
	myfile.close()

	dictdict[0] = fulldict




except IOError:
   print("There was an error writing to", file_name)
   sys.exit()