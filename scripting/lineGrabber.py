import nltk
import sys
import tagging
from tagging import * # used to be ../scripting/tagging.py

def main():
 
    searchword = "park" ## this will need to be linked to the front end
    corpus = []
    relevance = 0
    max_amount = 0
    index = -1
    printlin = 0
    strengthmax = 0
    bestFitIndex = -1

    for x in final:
        if searchword in x.tags:
            if strengthmax < x.strengths[(x.tags.index(searchword))]:
                strengthmax = x.strengths[(x.tags.index(searchword))]
                bestFitIndex = final.index(x)

    bestFitScript = final[bestFitIndex].name  #grabs name of most relevant file as determined by tagger

    # not necessary to seach whole folder now, they are working on tags as object feature
    os.chdir("../sketches txt files")
    myfile = open(bestFitScript, encoding="utf8")
    lines = myfile.readlines()

    for line in lines:
        index += 1
        if searchword in line.lower(): relevance += 1
        if (relevance > max_amount): printlin = index
        relevance = 0

    if printlin != -1:
       print(lines[printlin])



main()

