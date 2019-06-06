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
    antonyms = []
    synonyms = []
    drf = []
    pert = []

    os.chdir("../text_files")
    myfile = open("allnounslist.txt", encoding="utf8")
    lines = myfile.readlines()
    for w in lines:
        holder = wn.synsets(w)
        prompty = wn.synsets(prompt)
        #print(holder)
        #print(prompt)
        #print(prompty)
        if holder:
            score = wn.wup_similarity(prompty[0], holder[0])
            if score > .5:
                antonym = holder[0]
                break

    #obj1 = lines[random.randint(0, len(lines) - 1)]
    #if("\n" in antonym):
    #    antonym = antonym.replace("\n", "")

    myfile.close()

    if(state == "A"):
        #jokeline = "That sounds like a "
        #jokeline = jokeline + prompt
        state = 1
        #^ this is just making the performer say a line with the prompt.
        #print(jokeline)
        if wn.synsets(prompt):
            jokeline = "How the hell do you ingest " + wn.synsets(prompt)[0].definition()
            state = 2
            #^This is replacing the prompt with its definition
            print(jokeline)
            print("\n>")
            jokeline = "You've never had to sit through dinner with my inlaws!"
            print(jokeline)
            print("You're not gonna like it, but I do have a treatment for you. \n>")
            word = wn.synsets(prompt)[0]
            #for syn in wn.synsets(prompt):
            #    for l in syn.lemmas():
            #        synonyms.append(l.name())
            #        if l.antonyms():
            #            antonyms.append(l.antonyms()[0].name())
            #        if l.pertainyms():
            #            pert.append(l.pertainyms()[0].name())
            #        if l.derivationally_related_forms():
            #            drf.append(l.derivationally_related_forms()[0].name())
            #if antonyms:
            #    antonym = antonyms[0]     #[0].antonyms() #word.lemmas()[0].antonyms()[0]
            #elif pert:
            #    antonym = pert[0]
            #else:
            #    next = prompt + ".n.01"
                #put the prompt into the right format for wordnet
            #    next = wn.synset(next)
            #    if(len(next.member_holonyms()) > 0):
            #        antonym = next.member_holonyms()[0].name().split(".")[0]
                #if there's a holonym, make prompt that
            #    else:
            #        antonym = next.hypernyms()[0].name().split(".")[0]
        else:
            antonym = "arsenic"
        #elif drf:
        #    antonym = drf[0]
        #else:
        #    antonym = "cyanide"
        treat = wn.synsets(antonym)[0].definition()[0]
        print(antonym)
        print(treat)
        print("You're gonna have to take one dose of " + treat) #wn.synsets(prompt)[0].word())
        print("\n>")
        print("Doc that seems stupid \n>")
        print("Well I'm not the idiot eating a " + prompt + " now am I?")
        #^Then we land the punch line and we go home.


def main():
    print("[A man is waiting in the examination room and his doctor walks in.] \n>")
    print("Thank you for waiting, what brings you in today? \n>")
    name = input("Well ya see doc I swallowed a ... \n>")
    inputWord = word_tokenize(name)
    if(inputWord[0] == "end"):
        return
    nextline(inputWord[0], "A")

    #while True:
    #    name = input("What seems to be the issue today? \n>")
    #    inputWord = word_tokenize(name)
    #    if(inputWord[0] == "end"):
    #        break
    #    nextline(inputWord[0], "A")





main()
