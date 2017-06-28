# coding:utf-8

# 使用 朴素贝叶斯 --> 发现地域相关的词
"""
universal feed parser 是python中最常用的RSS程序库
http://code.google.com/p/feedparser/

当一小部分单词占据了文本用词的大部分。产生这种现象的原因是语言中大部分都是冗余和结构性辅助性内容。
常用方法是移除高频词语，同时从预定词表中移除结构上的辅助词. 该词表称为 ‘停用词表’

多语言停用词表  
  http://www.ranks.nl/stopwords

"""

import numpy as np;
import bayes_lib as bys;
import log_lib as log;
import feedparser
from bayes_lib import textParse, createVocabList, bagOfWords2VecMN, trainNB2,\
    classifyNB
import numpy.random as  random

log1 = log.Logger("bayes_test");
log1.setLogLevel(log.LEVEL_DEBUG, True);

#ny = feedparser.parse("http://newyork.craigslist.org/stp/index.res");
ny = feedparser.parse("http://sfbay.craigslist.org/stp/index.res");
print ny


def calcMostFreq(vocabList,fullText):
    """
    计算出现的频率
    """
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token]=fullText.count(token)
    # value 降序(高->低)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True) 
    return sortedFreq[:30]       

def localWords(feed1,feed0):
    import feedparser
    docList=[]; classList = []; fullText =[]
    minLen = min(len(feed1['entries']),len(feed0['entries']))
    
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1) #NY is class 1
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
        
    vocabList = createVocabList(docList)#create vocabulary
    
    top30Words = calcMostFreq(vocabList,fullText)   #remove top 30 words
    for pairW in top30Words:
        if pairW[0] in vocabList: 
            vocabList.remove(pairW[0])
            
    trainingSet = range(2*minLen); 
    testSet=[]           #create test set
    
    for i in range(20):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB2(np.array(trainMat),np.array(trainClasses))
    
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(np.array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ',float(errorCount)/len(testSet)
    return vocabList,p0V,p1V


