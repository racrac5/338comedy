import sys
import list
import nltk
from nltk.tokenize import word_tokenize


name = input("What would you like to enter? Enter: \n\"0 x \" for an Animal, \n\"1 x \" for a Place, or \n\"2 x \" for an Occupation, replacing x with your prompt. \n>")
inputPair = word_tokenize(name)

if inputPair[1] in list.dictdict[int(inputPair[0], 10)].values():
    print("Given category is correct")
else:
    print("ERROR: given category does not match input")
