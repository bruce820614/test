# -*- coding: utf-8 -*-
"""

@author: Bruce
"""
from collections import Counter
import urllib2  # the lib that handles the url stuff

def bigram(sentence): 
    text = sentence.lower()
    words = text.split()
    return(zip(words, words[1:]))

def trigram(sentence): 
    text = sentence.lower()
    words = text.split()
    return(zip(words, words[1:], words[2:]))
    
data = urllib2.urlopen('https://raw.githubusercontent.com/livingbio/DeepLearningTutorial/master/raw_sentences.txt') # it's a file like object and works just like a file
data = data.readlines()

counts = Counter()
for line in data:
    counts.update(bigram(line))
for bigr, cnt in counts.items():
    if cnt > 1:
        print("{0[0]} {0[1]}: {1}".format(bigr, cnt))
        
counts = Counter()
for line in data:
    counts.update(trigram(line))
for bigr, cnt in counts.items():
    if cnt > 1:
        print("{0[0]} {0[1]} {0[2]} : {1}".format(bigr, cnt))
