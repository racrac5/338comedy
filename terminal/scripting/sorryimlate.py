import nltk
import sys
import tagging
from nltk.tokenize import word_tokenize
from tagging import * # used to be ../scripting/tagging.py
import re
import random

def main():
    #### set up ##########
    print("You're an hour late what the hell happened!? \n>")
    excuse = input("Tell us in a single word: Why are they late? \n>")

    looper()
    #### search function ####

    #### stolen from the how game

def cyclic(reps, next):
    global finsentencev1
    global respverb1
    wittyretort = [ [" Nope, after that a " , " came and blocked the road in front of my car!" ] ,
     [" Well its embarrasing but I ran over a " , " in the parking lot. " ] ,
     [" I stopped to post a picture of a " , " on my instagram. "] ,
     [" That's none of your goddamn business! Stop being so nosy! " ] ]

    if reps == 0:
        myfile = open("verblist.txt", encoding="utf8")
        lines = myfile.readlines()

        finsentence = ""
        finsentence += "Well there was a "

        finsentencev1 = lines[random.randint(0, len(lines) - 1)]
        finsentence += next
        finsentence += ""
        if("\n" in finsentence):
            finsentence = finsentence.replace("\n", "")

        respsentence = ""
        respsentence += "Why "
        respsentence += finsentencev1
        respsentence += " it when you could "

        respverb1 = lines[random.randint(0, len(lines) - 1)]
        respsentence += respverb1
        respsentence += " it? "
        if("\n" in respsentence):
            respsentence = respsentence.replace("\n", "")
        myfile.close()

        print(finsentence)
        #print(respsentence)
        return 1
    elif(reps > 5):
        print(wittyretort[3][0])
        return 0

    else:
        myfile = open("verblist.txt", encoding="utf8")
        lines = myfile.readlines()

        finsentence = ""
        finsentence += " You're right I should "

        finsentencev1 = respverb1
        finsentence += finsentencev1
        respverb1 = lines[random.randint(0, len(lines) - 1)]
        #respverb1 = finsentencev1
        #finsentencev1 = lines[random.randint(0, len(lines) - 1)]
        finsentence += " it"
        if("\n" in finsentence):
            finsentence = finsentence.replace("\n", "")
            retortselector = random.randint(0, len(wittyretort) -1)
            if (retortselector < 3):
                respsentence = ""
                respsentence += wittyretort[retortselector][0]
                #respsentence += finsentencev1
                respsentence += next
                respsentence += wittyretort[retortselector][1]
                finsentencev1 = lines[random.randint(0, len(lines) - 1)]
                respverb1 = lines[random.randint(0, len(lines) - 1)]
            else:
                respsentence = wittyretort[retortselector][0]
                #respverb1 = lines[random.randint(0, len(lines) - 1)]
                return

        ##respsentence += respverb1
        ##respsentence += " it? "
        if("\n" in respsentence):
            if (isinstance(respsentence, str)):
                respsentence = respsentence.replace("\n", "")
        myfile.close()

        #print(finsentence)
        print(respsentence)
        return 1


def looper():
    creps = 0
    searchword2 = "war"
    searchword1 = "dancer" ## this will need to be linked to the front end
    corpus = []
    relevance = 0
    max_amount = 0
    index = -1
    printlin = 0
    strengthmax = 0
    bestFitIndex = random.randint(0, len(final) - 1) #this should be a random number of all the scripts

    for x in final:
        if searchword1 in x.tags:
            if strengthmax < x.strengths[(x.tags.index(searchword1))]:
                strengthmax = x.strengths[(x.tags.index(searchword1))]
                bestFitIndex = final.index(x)

    bestFitScript = final[bestFitIndex].name  #grabs name of most relevant file as determined by tagger

    # not necessary to seach whole folder now, they are working on tags as object feature
    os.chdir("../sketches txt files")
    myfile = open(bestFitScript, encoding="utf8")
    lines = myfile.readlines()

    myfile.close()

    os.chdir("../text_files")
    myfile = open("allnounslist.txt", encoding="utf8")
    lines = myfile.readlines()
    obj1 = lines[random.randint(0, len(lines) - 1)]
    if("\n" in obj1):
        obj1 = obj1.replace("\n", "")

    myfile.close()
    myfile = open("verblist.txt", encoding="utf8")
    lines = myfile.readlines()
    line1 = "How do you deal with a " + obj1 + "?"

    finsentence = ""
    finsentence += "I "
    finsentence += lines[random.randint(0, len(lines) - 1)]
    finsentence += " it"
    if("\n" in finsentence):
        finsentence = finsentence.replace("\n", "")


    #print(line1)
    #print(finsentence)
    myfile.close()

    while True:
        query = ["Riveting. Is that the only reason? What else happened? \n>" , "... And? Is that all? What else did you run into? \n>" , "Seems like a lame excuse, is that it? \n>"]
        question = query[random.randint(0,2)]
        next = input(question)
        #next = input("Riveting. Is that the only reason? What else happened? \n>")
        if(next.lower() == "x"):
            break
        else:
            check = cyclic(creps, next)
            if(check == 0):
                break
            creps += 1



main()
