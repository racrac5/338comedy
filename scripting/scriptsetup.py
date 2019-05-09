# -*- coding: utf-8 -*-
import sys
import nltk
import os


filenames = []

for filename in os.listdir("sketches txt files"):
    if filename.endswith(".txt"):
        filenames.append(filename)

#for items in filenames:
   # print(items)
