import nltk
import tagging
from tagging import *
from nltk.tokenize import word_tokenize
import sys
import os


inputname = input("Which file would you like to pull from?\n>")
#inputname = word_tokenize(name)
test = 0

for y in final:
	if (y.name == inputname):
		bingo = final.index(y)
		test = 1
		break

if(test == 1):
	with open(inputname, 'r+') as myfile:
			lines = myfile.read()
			sentences = nltk.sent_tokenize(lines)
			nouns = []

			for sentence in sentences:
				for z in final[bingo].tags:
					if z in sentence:
						print(sentence)

		#close them files
	myfile.close()




