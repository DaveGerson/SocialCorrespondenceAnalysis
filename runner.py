# -*- coding: utf-8 -*-
__author__ = 'gerson64'
import foodList
import itertools
from nltk.corpus import stopwords
s=set(stopwords.words('english'))

def unique(inList):
    return list(set(inList))

def wordcounter(inlist):
    wordcount = {}
    for word in inlist:
        if word.lower() not in wordcount:
            wordcount[word.lower()] = 1
        else:
            wordcount[word.lower()] += 1
    return wordcount

restList = ["%40burgerking", "%40mcdonalds", "%40pizzahut", "%40tacobell", "%40chipotletweets", "%40qdobamexgrill",
            "%40wendys", "%40kfc", "%40ChickfilA"]

BK, mcD, pizzahut, tacobell, chipotle, qdoba, wendys, kfc, CFilA = [foodList.foodwordList(x) for x in restList]

allLists = [BK, mcD, pizzahut, tacobell, chipotle, qdoba, wendys, kfc, CFilA]
allUnique = [ unique(inlist) for inlist in allLists]
all = list(itertools.chain(*allUnique))

wordsToKeep = []
for k, v in wordcounter(all).items():
    if v in [3,4,5,6]  :
        wordsToKeep.append(k)
        print k, v

wordsToKeep =  filter(lambda w: not w in s,wordsToKeep)

BK, mcD, pizzahut, tacobell, chipotle, qdoba, wendys, kfc, CFilA \
    = [ [ i.lower() for i in list if i.lower() in wordsToKeep] for list in allLists ]

allLists = [BK, mcD, pizzahut, tacobell, chipotle, qdoba, wendys, kfc, CFilA]
allWordCount = [wordcounter(inlist) for inlist in allLists]

#print allLists

outMatrix = []
outMatrix.append(['names'] + restList)
for word in wordsToKeep:
    tmpList = [word]
    for wordCountObj in allWordCount:
        tmpList = tmpList + [ unicode(wordCountObj.get(word,0))]
    outMatrix.append(tmpList)

outMatrix = zip(*outMatrix)

import csv
with open("output.csv", "wb") as f:
    writer = csv.writer(f, delimiter='~')
    for outrow in outMatrix:
        writer.writerow([s.encode('ascii', 'ignore') for s in outrow])

#Use Gensim for Topic modeling in Python
#LDAavis for R visual analysis of topics.