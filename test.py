#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bayes
listOPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
print myVocabList


trainMat = []
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))






p0V, p1V, pAb = bayes.trainNbO(trainMat, listClasses)

print sum
print p0V
print p1V
print pAb

