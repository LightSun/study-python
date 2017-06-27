# coding:utf-8

# 朴素贝叶斯相关

from numpy import *


def createVocabList(dataSet):
    '''''
    创建一个包含在所有文档中出现的不重复的列表.
    Require:
        dataSet  2维数组/矩阵  
    '''
    vocabSet = set([]);
    # 将每篇文档返回的新词集合放到 vocabSet 中
    for doc in dataSet: 
        vocabSet = vocabSet | set(doc); # 并集
    return list(vocabSet);    

def setOfWords2Vector(vocabList, inputSet):
    '''''
    将文档中所有的 ‘假设词语' 加上标记。出现则为1,不出现为0. 返回标记集合 list。
    Params:
        vocabList 词汇表
        inputSet  文档. 1维矩阵/数组
    '''
    returnVec = [0] * len(vocabList); # 创建和词汇表等长的向量(相当于 1维数组).
    # print "returnVec =  %s" % returnVec
    
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1;
        else: # vocabulary 词汇的意思
            print "the word: %s is not in my vocabulary! " % word;
    return returnVec;


def trainNB0(trainMatrix, trainCategory):
    """
    trainMatrix 文档矩阵.2维
    trainCategory 每篇文档类别标签所构成的向量.1维矩阵/数组
    """
    """
============[从词向量计算概率】：--- 伪代码---=====================
     计算每个类别中的文档数目.
    对每篇 训练文档：
          对每个类别 :
                  如果词条出现文档中 ->增加该词条的计数值.
                  增加所有词条的计数值
          对每个类别 :
                  对每个词条:
                           将该词条的数据除以总词条数目，得到条件概率.     
         返回每个类别的条件概率.    
    """
    numTrainDocs = len(trainMatrix);
    numWords = len(trainMatrix[0]);
    # 计算所有辱骂词语的概率
    pAbusive = sum(trainCategory) / float(numTrainDocs); # eg: 3/6
    # 初始化 1维矩阵 p0Num, p1Num
    p0Num = zeros(numWords);
    p1Num = zeros(numWords); # 侮辱词语概率
    
    p0Denom = p1Denom = 0.0; # 初始化概率
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i];
            p1Denom += sum(trainMatrix[i]);
        else:
            p0Num += trainMatrix[i];
            p0Denom += sum(trainMatrix[i]);
    
    p1Vect = p1Num/p1Denom; 
    p0Vect = p0Num/p0Denom; 
    return p0Vect, p1Vect, pAbusive;

def trainNB2(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); 
    p1Num = ones(numWords)      #change to ones() 
    p0Denom = 2.0; 
    p1Denom = 2.0
                            #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # 求对数，避免下溢出或者 浮点数舍入后为0.得不到正确的. 所以这库取对数. log(a*b) = log(a) + log(b) 
    # log（x） 和f(x)  在相同区域内递增或者递减。 并在相同点上取得极值. 取值不同，结果相同   .    
    p1Vect = log(p1Num/p1Denom)          #change to log()
    p0Vect = log(p0Num/p0Denom)          #change to log()
    return p0Vect,p1Vect,pAbusive


def classifyNB(vec2Classify , p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1);
    p0 = sum(vec2Classify * p0Vec) + log(1 - pClass1);
    if( p1 > p0):
        return 1;
    else:
        return 0;
    
    
