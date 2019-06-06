import nltk
import sys
import tagging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from tagging import * # used to be ../scripting/tagging.py
import re
import random

searchword2 = "war"
searchword1 = "dancer" ## this will need to be linked to the front end


def nextline(prompt): 
    #go back and forth between canned responses of A,B form
    corpus = []
    relevance = 0
    max_amount = 0
    index = -1
    printlin = 0
    strengthmax = 0
    bestFitIndex = random.randint(0, len(final) - 1) #this should be a random number of all the scripts

    for x in final:
        if prompt in x.tags:
            if strengthmax < x.strengths[(x.tags.index(prompt))]:
                strengthmax = x.strengths[(x.tags.index(prompt))]
                bestFitIndex = final.index(x)

    bestFitScript = final[bestFitIndex].name  #grabs name of most relevant file as determined by tagger

    # not necessary to seach whole folder now, they are working on tags as object feature
    os.chdir("../sketches txt files")
    myfile = open(bestFitScript, encoding="utf8")
    lines = myfile.readlines()

    for line in lines:
        index += 1
        if prompt in line.lower(): relevance += 1
        if ":" not in line: relevance = -5
        if (relevance > max_amount):
            printlin = index
            max_amount = relevance
        relevance = 0

    edited = lines[0]

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
    
    
  #  sentence = nltk.sent_tokenize(edited)
    nouns = []



    myfile.close()

    name = input("Next line or new choice? C for new Choice, L for next Line \n>")
    if(name.lower() == "l"):
        newprompt = prompt
        stop = set(stopwords.words('english'))

       # search = nltk.word_tokenize(str(re.sub(r"\([^()]*\)|\[[^\[\]]*\]", "",edited)))
        search = nltk.word_tokenize(str(edited))

        for word,pos in nltk.pos_tag(search):
            if (pos[0] == 'N'):
                nouns.append(word)



        nouns_no_stop_words_punct = [t for t in nouns if t not in stop and t not in string.punctuation]
        if(prompt in nouns_no_stop_words_punct):
            nouns_no_stop_words_punct.remove(prompt)
        if(len(nouns_no_stop_words_punct) > 0):
            newprompt = nouns_no_stop_words_punct[random.randint(0, len(nouns_no_stop_words_punct) - 1)]
      #  print(nouns_no_stop_words_punct)
     #   print(newprompt)
        nextline(newprompt)
    elif(name.lower() == "c"):
        newchoice(str(edited))
    else:
        print("error")



def newchoice(lastline): 
    #new choice takes a line and spits out the same line with the last verb changed. 

    casenum = 0
    lastverb = ""
    verbs = []
    finsentence = ""
    search = nltk.word_tokenize(str(lastline))

    #tokenize the line so that you can make an array of the verbs in it below

    for word,pos in nltk.pos_tag(search):
        if (pos[0] == 'V'):
            verbs.append(word)
                if(pos == "VBD"):
                    casenum = 1
                if(pos == "VBG"):
                    casenum = 2
                if(pos == "VBZ"):
                    casenum = 3



    verbs = verbs[::-1]


    #reverse the array of verbs, now you have the last verb as the first element of the array

    os.chdir("../text_files")


    #open a file of all the verbs in English, pick a random one and place it in "finsentence" with the newline cut out.
    myfile = open("verblist.txt", encoding="utf8")
    lines = myfile.readlines()
    finsentence += lines[random.randint(0, len(lines) - 1)]

    if("\n" in finsentence):
        finsentence = finsentence.replace("\n", "")
    if(casenum == "1"):
        firstsentence += "ed"
    if(casenum == "2"):
        firstsentence += "ing"
    if(casenum == "3"):
        firstsentence += "s"

        
    if(len(verbs) > 0):
        #if there are verbs in the sentence:
        if verbs[0] in lastline:
            #reverse the last line so that you can replace the FIRST instance of that verb - replace just does the first one 
            lastline = lastline[::-1]
            #reverse the verb so that when you replace it into a reversed sentence, it's not backwards
            verbs[0] = verbs[0][::-1]
            finsentence = finsentence[::-1]
            #replace the verb in the reversed sentence with the reversed random verb
            lastverb = lastline.replace(verbs[0],finsentence,1)
            #reverse it back to forwards
            lastverb = lastverb[::-1]
            #print the new version of the line 
            print(lastverb)


            name = input("Next line or new choice? C for new Choice, L for next Line \n>")
            if(name.lower() == "l"):
                newprompt = "kaleidoscope"
                stop = set(stopwords.words('english'))

               # search = nltk.word_tokenize(str(re.sub(r"\([^()]*\)|\[[^\[\]]*\]", "",edited)))
                search = nltk.word_tokenize(str(lastverb))

                for word,pos in nltk.pos_tag(search):
                    if (pos[0] == 'N'):
                        nouns.append(word)


                nouns_no_stop_words_punct = [t for t in nouns if t not in stop and t not in string.punctuation]

                if(len(nouns_no_stop_words_punct) > 0):
                    newprompt = nouns_no_stop_words_punct[random.randint(0, len(nouns_no_stop_words_punct) - 1)]
              #  print(nouns_no_stop_words_punct)
             #   print(newprompt)
                nextline(newprompt)
            elif(name.lower() == "c"):
                newchoice(str(lastverb))
            else:
                print("error")

    else:
        print("error no verbs")
    myfile.close()



  
def main():
    name = input("What is your prompt? \n>")
    inputWord = word_tokenize(name)
    nextline(inputWord[0])









main()







