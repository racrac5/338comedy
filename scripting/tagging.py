import sys
import list
import sorting
import nltk
import random
from scriptsetup import *
from nltk.tokenize import word_tokenize

class FinalElement:
	def __init__(self, name, tags, strengths):
		self.name = name
		self.tags = tags
		self.strengths = strengths


os.chdir("sketches txt files")

final = []



for filename in filenames:
	tags = []
	strengths = []

	curr = FinalElement(filename, tags, strengths)

	with open(filename, 'r+') as myfile:
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
					curr.tags.append(x)
					curr.strengths.append(3)
			#I'd probably write tags at the top and then check all the dicts and append those instead

	myfile.close()

	final.append(curr)

test = final[0].tags
test2 = final[0].strengths
print(final[0].name)
for item in test:
	print(item)

for items in test2:
	print(items)
