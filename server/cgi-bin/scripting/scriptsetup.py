# -*- coding: utf-8 -*-
import sys
import nltk
import os

path = sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'sketches txt files')))
filenames = []
for filename in os.listdir(path):
    if filename.endswith(".txt"):
        filenames.append(filename)

for items in filenames:
    print(items)