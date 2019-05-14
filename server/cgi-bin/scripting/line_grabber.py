import nltk
from nltk.tokenize import word_tokenize
import sys
import os
import re
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from tagging import * # used to be ../scripting/tagging.py

def main():
 
    searchword = "park"
    searchword = "christmas" ## this will need to be linked to the front end
    corpus = []
    relevance = 0
    max_amount = 0
    index = -1
    printlin = 0
    strengthmax = 0
    bestFitIndex = random.randint(0, len(final) - 1) #this should be a random number of all the scripts

    for x in final:
        if searchword in x.tags:
            if strengthmax < x.strengths[(x.tags.index(searchword))]:
                strengthmax = x.strengths[(x.tags.index(searchword))]
                bestFitIndex = final.index(x)

    bestFitScript = final[bestFitIndex].name  #grabs name of most relevant file as determined by tagger

    # not necessary to seach whole folder now, they are working on tags as object feature
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "sketches txt files"))
    os.chdir(path)
    myfile = open(bestFitScript, encoding="utf8")
    lines = myfile.readlines()

    for line in lines:
        index += 1
        if searchword in line.lower(): relevance += 1
        if (relevance > max_amount): printlin = index
        relevance = 0

    if printlin != -1:
       print(lines[0])
    else: 
        printlin = len(lines)# random number here of all the lines 
        print(lines[random.randint(0,printlin)])


    myfile.close()

    bestFitIndex = random.randint(0, len(final) - 1)

    #get a second one 
    for x in final:
        if searchword in x.tags:
            if strengthmax < x.strengths[(x.tags.index(searchword))]:
                strengthmax = x.strengths[(x.tags.index(searchword))]
                bestFitIndex = final.index(x)

    bestFitScript = final[bestFitIndex].name  #grabs name of most relevant file as determined by tagger

    # not necessary to seach whole folder now, they are working on tags as object feature
    second_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "sketches txt files"))
    os.chdir(second_path)
    myfile = open(bestFitScript, encoding="utf8")
    lines = myfile.readlines()

    for line in lines:
        index += 1
        if searchword in line.lower(): relevance += 1
        if (relevance > max_amount): printlin = index
        relevance = 0

    if printlin != -1:
       print(lines[0])
    else: 
        printlin = len(lines)# random number here of all the lines 
        print(lines[random.randint(0,printlin)])

    punchscripts = []
    curr = FinalElement("testpunch.txt", [], [])
    punchscripts.append(curr)

    bestFitIndex = random.randint(0, len(punchscripts) - 1)
    #punches is like final, but only of scripts that have punchlines in them
    bestFitScript = punchscripts[bestFitIndex].name
    myfile.close()
    bestFitScript = "testpunch.txt"
    third_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "sketches txt files"))
    os.chdir(third_path)
    myfile = open(bestFitScript, encoding="utf8")
    lines = myfile.readlines()

    for line in lines:
        if('!!!PUNCH!!!' in line):
            result = re.search('!!!PUNCH!!!(.*)!!!PUNCH!!!', line)
            print(result.group(1))
    myfile.close()

main()