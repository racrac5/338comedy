import nltk
import sys
import tagging
from nltk.tokenize import word_tokenize
from tagging import * # used to be ../scripting/tagging.py
import re
import random



def main():

    searchword2 = "hamburger"
    searchword1 = "obama" ## this will need to be linked to the front end
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

    for line in lines:
        index += 1
        if searchword1 in line.lower(): relevance += 1
        if ":" not in line: relevance = -5
        if (relevance > max_amount):
            printlin = index
            max_amount = relevance
        relevance = 0

    if printlin < len(lines):
        unedited = lines[printlin]
        if ":" in unedited:
            edited = unedited.split(':')[1]#unedited minus brackets or replace character names up until colon
            print("A:" +edited)
        else:
            print(unedited)
        #print(lines[printlin])
    else:
        randoline = len(lines)# random number here of all the lines
        print("THIS IS RANDOM, printlin was out of bounds (1)")
        print(lines[random.randint(0,randoline)])

    myfile.close()

    bestFitIndex = random.randint(0, len(final) - 1)

#get a second one
    for x in final:
        if searchword2 in x.tags:
            if strengthmax < x.strengths[(x.tags.index(searchword2))]:
                strengthmax = x.strengths[(x.tags.index(searchword2))]
                bestFitIndex = final.index(x)

    bestFitScript = final[bestFitIndex].name  #grabs name of most relevant file as determined by tagger

    # not necessary to seach whole folder now, they are working on tags as object feature
    os.chdir("../sketches txt files")
    myfile = open(bestFitScript, encoding="utf8")
    lines = myfile.readlines()
    printlin = 0

    for line in lines:
        index += 1
        if searchword2 in line.lower(): relevance += 1
        if ":" not in line: relevance = -5
        if (relevance > max_amount):
            printlin = index
            max_amount = relevance
        relevance = 0

    if printlin < len(lines):
        print(printlin)
        unedited = lines[printlin]
        if ":" in unedited:
            edited = unedited.split(':')[1]#unedited minus brackets or replace character names up until colon
            print("B:" +edited)
        else:
            print(unedited)
        #print(lines[printlin])
    else:
        randoline = len(lines)# random number here of all the lines
        print("THIS IS RANDOM, printlin was out of bounds (2)")
        print(lines[random.randint(0,randoline)])

    punchscripts = []
    curr = FinalElement("testpunch.txt", [], [])
    punchscripts.append(curr)

    bestFitIndex = random.randint(0, len(punchscripts) - 1)
    #punches is like final, but only of scripts that have punchlines in them
    bestFitScript = punchscripts[bestFitIndex].name
    myfile.close()
    bestFitScript = "testpunch.txt"
    os.chdir("../sketches txt files")
    myfile = open(bestFitScript, encoding="utf8")
    lines = myfile.readlines()

    for line in lines:
        if('!!!PUNCH!!!' in line):
            result = re.search('!!!PUNCH!!!(.*)!!!PUNCH!!!', line)
            print(result.group(1))
    myfile.close()

main()
