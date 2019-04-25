import sys
import list
import sorting
import nltk
import random
from nltk.tokenize import word_tokenize



with open('text_files/elephanttext.txt', 'r+') as myfile:
	lines = myfile.read()
	sentences = nltk.sent_tokenize(lines)
	nouns = []

	for sentence in sentences:
		for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
			if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
				nouns.append(word)
	


	for x in nouns:
		for group in list.dictdict:
			if x.lower() in list.dictdict[group].values():
				print("Yes")
				print(x)
				tag = " !!! tags: "
				myfile.write(tag + x.lower()) 
				break
		#I'd probably write tags at the top and then check all the dicts and append those instead 


myfile.close()





