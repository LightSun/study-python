# coding:utf-8

# 朴素贝叶斯 算法分类（即朴素贝叶斯分类器）测试

import numpy as np;
import bayes_lib as bys;
import log_lib as logg;
from bayes_lib import textParse, createVocabList, bagOfWords2VecMN, trainNB2,\
    classifyNB
from numpy import random
import numpy.core.umath as math

print math.log(1/25.0)

def loadDataSet():
    # 生成 6组 array组成的2维数组
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him']
                 , ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
                 ]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec

log1 = logg.Logger("bayes_test");
log1.setLogLevel(logg.LEVEL_DEBUG, True);

postList, classVec = loadDataSet();
myVocabList = bys.createVocabList(postList);
print "sum(classVec) = %s " % (sum(classVec))
print "myVocabList = %s\n , myVocabList.size = %s " % (myVocabList, len(myVocabList))

resultVector = bys.setOfWords2Vector(myVocabList, postList[0]);
print "inputSet = postList[0] >>> resultVector = ", resultVector;

resultVector = bys.setOfWords2Vector(myVocabList, postList[3]);
print "inputSet = postList[3] >>> resultVector = ", resultVector;

log1.logTS("从词向量计算概率");

traimMat = [];
for postinDoc in postList:
    traimMat.append(bys.setOfWords2Vector(myVocabList, postinDoc))
    print "postinDoc = %s\n , trainMat = %s" % (postinDoc, traimMat)
    
p0V, p1V, pAb = bys.trainNB0(traimMat, classVec, lg=log1);    
print "pAb = " , pAb
print "p0V = " , p0V
print "p1V = " , p1V


### >>>>============= 用朴素贝叶斯 --- 过滤恶意留言 =================
def testingNB():
    """
    过滤恶意留言
    """
    # listClasses 分类。 1维数组
    listOPosts, listClasses = loadDataSet()
    
    # 根据指定文档，得到不重复的列表
    myVocabList = bys.createVocabList(listOPosts)
    
    # trainMat: 所有文档单词的标记数组。2维
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(bys.setOfWords2Vector(myVocabList, postinDoc))
    
    log1.logTMS("testingNB", "trainMat = %s,\n np.array(trainMat) = %s " % (trainMat, np.array(trainMat)));            
    p0V, p1V, pAb = bys.trainNB2(np.array(trainMat), np.array(listClasses))
    log1.logTMS("testingNB", "pAb = %s ,\n p0V = %s ,\n p1V = %s " % (pAb, p0V, p1V));
    
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = np.array(bys.setOfWords2Vector(myVocabList, testEntry))
    log1.logTMS("testingNB",">>> 1 thisDoc = %s" % thisDoc);
    print testEntry, 'classified as: ', bys.classifyNB(thisDoc, p0V, p1V, pAb)
    
    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(bys.setOfWords2Vector(myVocabList, testEntry))
    log1.logTMS("testingNB",">>> 1 thisDoc = %s" % thisDoc);
    print testEntry, 'classified as: ', bys.classifyNB(thisDoc, p0V, p1V, pAb)

testingNB();

### ===========>>> 使用贝叶斯过滤垃圾邮件 ============================

def spamTest():
    """
    垃圾邮件过滤测试
    """
    docList = []; # 2维数组
    classList = [];
    fullText =[];
    
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList);
        fullText.extend(wordList);
        classList.append(1);
        # log1.logTMS("spamTest", "spam ----> wordList = %s " % wordList);
    
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList);
        fullText.extend(wordList);
        classList.append(0);
        # log1.logTMS("spamTest", "ham ----> wordList = %s " % wordList);
        
    # 去重复后的list
    vocabList = createVocabList(docList);
    
    trainingSet = range(50); # [0, 49)
    testSet = []; # 随机存放的set
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet))); # uniform随机 产生
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    
    log1.logTMS("spamTest", "befor 训练， classList = %s " % classList)    
    # 训练后的数据集
    traimMat = []; 
    trainClasses =[]; # 分类特征
    for docIndex in trainingSet:
        traimMat.append(bagOfWords2VecMN(vocabList, docList[docIndex])); 
        trainClasses.append(classList[docIndex]);
    # 得到概率.    
    p0v, p1v , pSpam = trainNB2(np.array(traimMat), np.array(trainClasses));
    
    # 计算错误率
    errorCount = 0;
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if(classifyNB(np.array(wordVector), p0v, p1v, pSpam) != classList[docIndex]):
            errorCount +=1;
            print "classifycation error ", docList[docIndex];
    print "the error rate is %s , errorCount = %s, size = %s " % (float(errorCount) / len(testSet) \
                    , errorCount, len(testSet));
    return vocabList, fullText;        
     
spamTest();        
    
    