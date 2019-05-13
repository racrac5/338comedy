import sys
import os
import nltk
import random
from nltk.tokenize import word_tokenize
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
import lister
from scriptsetup import *

#################################################################################################
#All of our comedy scripts will be in one folder. 
#We will make a list of FinalElements (A class we make here)
#This FinalElement exists 1 per comedy script, and has all the information on tags and their strengths. 

class FinalElement:
	def __init__(self, name, tags, strengths):
		self.name = name
		self.tags = tags
		self.strengths = strengths

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "sketches txt files"))
os.chdir(path)

#final is the list of all FinalElements, or the list of all filenames with their stored info.
final = []

#for every filename in a folder, we make an empty list of tags and strengths and make a FinalElement for it.
for filename in filenames:
	tags = []
	strengths = []

	curr = FinalElement(filename, tags, strengths)

	#now we open the file and begin to tokenize it.
	with open(filename, encoding = "utf8") as myfile:
		lines = myfile.read()
		sentences = nltk.sent_tokenize(lines)
		nouns = []

		for sentence in sentences:
			for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
				if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
					nouns.append(word)

		#after tokenizing all nouns (most likely tags, search to see if any of them match our tags (stored in dictionaries.)
		for x in nouns:
			for group in lister.dictdict:
				if x.lower() in lister.dictdict[group].values():
					#if noun is in our dictionaries, check and see if it's already been tagged. 
					if(x.lower() not in curr.tags):
						#if not, add it to the taggs list and also add a "1" to the strengths list
						curr.tags.append(x.lower())
						curr.strengths.append(1)
					else: 
						#if it is, get that element's index number and increase the strength for that element number by 1.
						i = curr.tags.index(x.lower())
						curr.strengths[i] = curr.strengths[i] + 1

	#close them files
	myfile.close()
	#add the FinalElement curr to the big list.
	final.append(curr)


#this example shows that in alurn.txt, there are two nouns that are in our dictionaries: park and bar. 
#park appears once, bar twice. And that's right if you check the file. And it works if you say bar again, for instance.