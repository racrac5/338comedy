import sys
import list
import nltk
import random
from nltk.tokenize import word_tokenize


name = input("What would you like to enter? Enter: \n\"0 x \" for an Animal, \n\"1 x \" for a Place, or \n\"2 x \" for an Occupation, replacing x with your prompt. \n>")
inputPair = word_tokenize(name)


#Check to see if input is valid in our lists

if inputPair[1].lower() in list.dictdict[int(inputPair[0], 10)].values():
    print("Given category is correct")

    #Pick two other random values from the list 

    randval1 = random.choice(random.choice(list.dictdict))
    randval2 = random.choice(random.choice(list.dictdict))
    print(inputPair[1])
    print(randval1)
    print(randval2)

else:
    print("ERROR: given category does not match input")


