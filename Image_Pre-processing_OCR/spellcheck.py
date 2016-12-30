#!/usr/bin/env python
#bug is that in this code last line of paragraph may skip some words 
#bug is that in code this occa-ssionaly is edited individually like occa is converted to coca by spelling checker
import nltk
import codecs
from nltk.tokenize import word_tokenize
import re
import pprint
from replacers import SpellingReplacer
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

f = open("separate_text.py",'r')
lines=f.readlines()
f.close()
f = open("separate_text.py",'w')
l=' '
for line in lines:
    if len(line.split())>4:

    	g=line.split()

    	for x in my_range(0, len(line.split())-1, 1):
    		replacer = SpellingReplacer()
    		
    		l+=(replacer.replace(g[x]) + ' ')
        f.write(l + '\n')
        l=' '

    	


    if len(line.split())==0:
        f.write(line)

