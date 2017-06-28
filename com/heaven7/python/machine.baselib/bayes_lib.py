# coding:utf-8

# 朴素贝叶斯相关: 词集模型 和 词袋模型
"""
词集模型: 单词出现与否作为特征。即不关心是否多次。 
词袋模型: 单词出现次数作为特征。(与词集模型相反).
"""

from numpy import *
import log_lib as logg;

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
    基于词集模型的 朴素贝叶斯.
    将文档中所有的 ‘假设词语' 加上标记。出现则为1,不出现为0. 返回标记集合 list。
    Params:
        vocabList 词汇表. 
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


def trainNB0(trainMatrix, trainCategory, lg = logg.EMPTY_LOG):
    """
    计算概率， 返回，条件概率-非侮辱单词的概率， 数组\
                               条件概率-侮辱单词的概率， 数组\
                              所有辱骂词的概率. float
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
    # 初始化 1维矩阵 p0Num, p1Num .按照指定个数
    # 非侮辱 and 侮辱词语个数 
    p0Num = zeros(numWords);
    p1Num = zeros(numWords); # 侮辱词语
    
    p0Denom = p1Denom = 0.0; # 初始化概率
    for i in range(numTrainDocs):
        lg.logTMS("trainNB0", "[ p1Num = %s ,p1Denom = %s ],\n   [ p0Num = %s ,p0Denom = %s ]" % \
                  (p1Num, p1Denom, p0Num, p0Denom));
        if trainCategory[i] == 1:
            lg.logTS("trainMatrix[i] == 1, \n trainMatrix[i] = %s " % trainMatrix[i]);
            p1Num += trainMatrix[i]; # 2矩阵各个元素求和
            p1Denom += sum(trainMatrix[i]);
        else:
            lg.logTS("trainMatrix[i] != 1, \n trainMatrix[i] = %s " % trainMatrix[i]);
            p0Num += trainMatrix[i]; # 矩阵
            p0Denom += sum(trainMatrix[i]);
    p1Vect = p1Num/p1Denom;  # 矩阵所有元素除以该元素
    p0Vect = p0Num/p0Denom; 
    # lg.logTMS("trainNB0", "at last >>> p1Vect(侮辱) = %s, p0Vect = %s " % (p1Vect, p0Vect));
    return p0Vect, p1Vect, pAbusive;

def trainNB2(trainMatrix,trainCategory):
    '''''
    为计算多个概率的乘积 以便获得文档中某个类别的概率。如果某个概率为0.最后为0.
    同 trainNB0. 修正了某个类别概率为0的情况.
    '''
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    '''''
     降低概率为0的影响
    '''
    # 初始化指定个数的1维数组。并且初始值为1.
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
    p0Vect = log(p0Num/p0Denom)          
    return p0Vect,p1Vect,pAbusive


def classifyNB(vec2Classify , p0Vec, p1Vec, pClass1):
    """
    获取概率大的类别标签。
    vec2Classify  需要分类的向量
    p0Vec, p1Vec, pClass1:  使用trainNB 计算得到的概率
    """
    p1 = sum(vec2Classify * p1Vec) + log(pClass1); # 矩阵/向量对应元素 相乘
    p0 = sum(vec2Classify * p0Vec) + log(1 - pClass1);
    if( p1 > p0):
        return 1; # 侮辱词汇 类别
    else:
        return 0;
    
def bagOfWords2VecMN(vocabList, inputSet):
    """
    基于词袋模型的 朴素贝叶斯
    将文档中所有的 ‘假设词语' 标记出现次数.
    """
    returnVec = [0] * len(vocabList);
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] +=1;
    return returnVec;

def textParse(bigString):    #input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString) #除字母，数字外的任意字符串。
    return [tok.lower() for tok in listOfTokens if len(tok) > 2] # 去掉字符长度不满足需求的


