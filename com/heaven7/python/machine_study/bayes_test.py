# coding:utf-8

# 朴素贝叶斯 算法分类（即朴素贝叶斯分类器）测试

import numpy as np;
import bayes_lib as bys;
import log_lib as log;

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him']
                 , ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
                 ]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

lg = log.Logger();

postList, classVec = loadDataSet();
myVocabList = bys.createVocabList(postList);
print "sum(classVec) = %s " % (sum(classVec))
print "myVocabList = %s " % myVocabList

resultVector = bys.setOfWords2Vector(myVocabList, postList[0]);
print "inputSet = postList[0] >>> resultVector = ", resultVector;

resultVector = bys.setOfWords2Vector(myVocabList, postList[3]);
print "inputSet = postList[3] >>> resultVector = ", resultVector;

lg.start("从词向量计算概率");

traimMat = [];
for postinDoc in postList:
    traimMat.append(bys.setOfWords2Vector(myVocabList, postinDoc))
    
p0V, p1V, pAb = bys.trainNB0(traimMat, classVec);    
print "pAb = " , pAb
print "p0V = " , p0V
print "p1V = " , p1V
lg.end()


def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = bys.createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(bys.setOfWords2Vector(myVocabList, postinDoc))
    p0V,p1V,pAb = bys.trainNB2(np.array(trainMat),np.array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = np.array(bys.setOfWords2Vector(myVocabList, testEntry))
    print testEntry,'classified as: ',bys.classifyNB(thisDoc,p0V,p1V,pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(bys.setOfWords2Vector(myVocabList, testEntry))
    print testEntry,'classified as: ',bys.classifyNB(thisDoc,p0V,p1V,pAb)

            