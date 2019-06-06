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




#Now that I know wordnet a bit, I'm going to try escalating a different way.
#I'll replace what was in the fridge either with a holonym (i.e. face->eyes) or a hypernym (i.e. red -> color)


def nextline(prompt, state):
    #go back and forth between canned responses of A,B form
    if(state == "A"):
        jokeline = "I can't believe it, yesterday I opened my fridge and there was a "
        jokeline = jokeline + prompt
        print(jokeline)
        state = 1
    else:
        jokeline = "You think that's crazy? I opened my fridge and there was a "
       # prompt = wn.synset('prompt.n.01')
        next = prompt + ".n.01"
        #put the prompt into the right format for wordnet
        next = wn.synset(next)
        if(len(next.member_holonyms()) > 0):
            prompt = next.member_holonyms()[0].name().split(".")[0]
        #if there's a holonym, make prompt that
        else:
            prompt = next.hypernyms()[0].name().split(".")[0]
            #else, make it a hypernym
        jokeline = jokeline + prompt
        print(jokeline)
    name = input("Go deeper? Y or N? \n")
    #lets user repeat until we hit Russia.
    if(name.lower() == "y"):
        nextline(prompt, state)

def main():


    while True:
        name = input("Wait what did you find? \n>")
        inputWord = word_tokenize(name)
        if(inputWord[0] == "end"):
            #a way to end the whole shebang
            break
        nextline(inputWord[0], "A")





main()
