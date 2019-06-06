import nltk
import sys
import tagging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from tagging import * # used to be ../scripting/tagging.py
import re
import random
from nltk.corpus import wordnet as wn



#ok this is an improv game called wordsmith. It's like new choice.
#the performers are doing a scene. After one says a sentence that ends in a noun,
#the caller can clap, making them replace that noun with a synonym of it
#and then does it again. You're supposed to go general with the first synonym, like a definition, 
#so that you can fit something into that category more easily.
#When we're practicing it in Mee-Ow, we always end with 'my ex.'
#To get the idea of this, run it and give it the prompt 'thorn'.

#We could potentially add more possible lines to the last line instead of just ex-wife? Make them relevant? idk


def nextline(prompt, state): 
    if(state == "A"):
        jokeline = "That sounds like a "
        jokeline = jokeline + prompt
        state = 1
        #^ this is just making the performer say a line with the prompt.
        print(jokeline)
        jokeline = "That sounds like " + wn.synsets(prompt)[0].definition()
        state = 2
        #^This is replacing the prompt with its definition
        print(jokeline)
        jokeline = "That sounds like my ex-wife!" 
        print(jokeline)
        #^Then we land the punch line and we go home.

  
def main():


    while True: 
        name = input("What is your prompt? \n>")
        inputWord = word_tokenize(name)
        if(inputWord[0] == "end"):
            break
        nextline(inputWord[0], "A")





main()







