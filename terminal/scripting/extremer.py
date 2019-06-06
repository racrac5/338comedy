import nltk
import sys
import tagging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from tagging import * # used to be ../scripting/tagging.py
import re
import random



#I'm gonna be honest it is SO hard to find good scaling systems online. 
#Basically the only good, big one I found was for country sizes.
#So this opens the fridge and exaggerates how big the prompt in the fridge was.


countrysizearray = []
#make this global to be used throughout program


def nextline(prompt, state): 
    if(state == "A"):
        jokeline = "I can't believe it, yesterday I opened my fridge and there was a "
        jokeline = jokeline + prompt
        jokeline = jokeline + " the size of"
        prompt = " a country!"
        state = len(countrysizearray)
        #^setup the first line, using the prompt and implying that its size is important. 
        #change state to the full length of the array so that we go into the else
        #in a position to randomly choose from countries bigger than the last one
    else:
        jokeline = "You think that's crazy? Yesterday I opened MY fridge and there was one the size of "
        #the response line
        state = random.randint(0, state)
        #set state to a random number between the biggest country's index of the array, 0, and the current one
        #so you never get a smaller one.
        prompt = countrysizearray[state]
        #get the name of that country 
    print(jokeline + prompt)
    #put the koke together.
    name = input("Go deeper? Y or N? \n")
    #lets user repeat until we hit Russia.
    if(name.lower() == "y"):
        nextline(prompt, state)

  
def main():

    os.chdir("../text_files")
    myfile = open("countriesbysize.txt", encoding="utf8")
    lines = myfile.readlines()
    for line in lines:
        countrysizearray.append(line)
    name = input("What is your prompt? \n>")
    inputWord = word_tokenize(name)
    myfile.close()
    nextline(inputWord[0], "A")




main()







