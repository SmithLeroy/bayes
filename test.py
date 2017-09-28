#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bayes
import feedparser
# listOPosts, listClasses = bayes.loadDataSet()
# myVocabList = bayes.createVocabList(listOPosts)
# print myVocabList
#
#
# trainMat = []
# for postinDoc in listOPosts:
#     trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))

# p0V, p1V, pAb = bayes.trainNbO(trainMat, listClasses)
#
# print sum
# print p0V
# print p1V
# print pAb

# result = bayes.testingNB()
# bayes.spamTest()
# bayes.validation()

#测试rss源
# ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
#
# print ny['entries']
# print len(ny['entries'])


#rss源有问题，造成
ny = feedparser.parse("http://newyork.craigslist.org/stp/index.rss")
sf = feedparser.parse("http://sfbay.craigslist.org/stp/index.rss")

# vocabList, pNF, pSF = bayes.localWords(ny, sf)
#
# vocabList, pNF, pSF = bayes.localWords(ny, sf)


bayes.getTopWord(ny, sf)

