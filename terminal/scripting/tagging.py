import sys
#import list
import fulllist
import nltk
import random
from scriptsetup import *
from nltk.tokenize import word_tokenize
import re

#All of our comedy scripts will be in one folder. 
#We will make a list of FinalElements (A class we make here)
#This FinalElement exists 1 per comedy script, and has all the information on tags and their strengths. 

class FinalElement:
	def __init__(self, name, tags, strengths, punchlines):
		self.name = name
		self.tags = tags
		self.strengths = strengths
		self.punchlines = punchlines


os.chdir("sketches txt files")

#final is the list of all FinalElements, or the list of all filenames with their stored info.
final = []
punchscripts = []


#for every filename in a folder, we make an empty list of tags and strengths and make a FinalElement for it.
for filename in filenames:
	tags = []
	strengths = []
	punchlines = []

	curr = FinalElement(filename, tags, strengths, punchlines)


	#now we open the file and begin to tokenize it.
	with open(filename, encoding="utf8") as myfile:
		lines = myfile.read()
		sentences = nltk.sent_tokenize(lines)
		nouns = []

		for sentence in sentences:
			for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
				if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
					nouns.append(word)


		#after tokenizing all nouns (most likely tags, search to see if any of them match our tags (stored in dictionaries.)
		for x in nouns:
			#for group in list.dictdict:
			for group in fulllist.dictdict:
				#if x.lower() in list.dictdict[group].values():
				if x.lower() in fulllist.dictdict[group].values():
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


	#Go through and find punchlines. Add punchlines into their FinalElem place and add those Currs to punchscripts
	with open(filename, encoding="utf8") as myfile:
		plines = myfile.readlines()
		for pline in plines:
			if("!!!PUNCH!!!" in pline):
				result = re.search('!!!PUNCH!!!(.*)!!!PUNCH!!!', pline)
				curr.punchlines.append(result.group(1))
				punchscripts.append(curr)
	myfile.close()

	#add the FinalElement curr to the big list.
	final.append(curr)

test = final[0].tags
test2 = final[0].strengths
print(final[0].name)
for item in test:
	print(item)

for items in test2:
	print(items)


#this example shows that in alurn.txt, there are two nouns that are in our dictionaries: park and bar. 
#park appears once, bar twice. And that's right if you check the file. And it works if you say bar again, for instance.