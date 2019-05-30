import nltk
import sys
import tagging
from nltk.tokenize import word_tokenize
from tagging import * # used to be ../scripting/tagging.py
import re
import random



def cyclic(reps):
    global finsentencev1
    global respverb1
    if reps == 0:
        myfile = open("verblist.txt", encoding="utf8")
        lines = myfile.readlines()

        finsentence = ""
        finsentence += "You're right I should "

        finsentencev1 = lines[random.randint(0, len(lines) - 1)]
        finsentence += finsentencev1
        finsentence += " it"
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
        print(respsentence)

    else:
        myfile = open("verblist.txt", encoding="utf8")
        lines = myfile.readlines()

        finsentence = ""
        finsentence += "I "

        finsentencev1 = respverb1
        finsentence += finsentencev1
        respverb1 = finsentencev1
        finsentencev1 = lines[random.randint(0, len(lines) - 1)]
        finsentence += " it"
        if("\n" in finsentence):
            finsentence = finsentence.replace("\n", "")

        respsentence = ""
        respsentence += "Why "
        respsentence += respverb1
        respsentence += " it when you could "

        respverb1 = finsentencev1
        respsentence += respverb1
        respsentence += " it? "
        if("\n" in respsentence):
            respsentence = respsentence.replace("\n", "")
        myfile.close()

        print(finsentence)
        print(respsentence)



def main():
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


    print(line1)
    print(finsentence)
    myfile.close()

    while True:
        name = input("New choice? C for yes. X to end.\n>")
        if(name.lower() == "c"):
            cyclic(creps)
            creps += 1
        elif(name.lower() == "x"):
            break






main()
