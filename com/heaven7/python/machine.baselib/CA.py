# coding:utf-8

# 决策树相关
from math import log

# 计算数据集的 香农熵(概念见 machine_study/ct_idea.py) 

# 度量数据集的无序程度
def calcShannonEnt(dataSet,debug=True):
    numEntries = len(dataSet); # dataSet 可能是某个函数返回的多个value.
    
    labelCounts = {}; #key-value是  dataSet最后一列的数值
    for featVec in dataSet:
        currentLabel = featVec[-1];
        if debug:
            print "currentLabel = " , currentLabel
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0;
        labelCounts[currentLabel] += 1;  
    # print "labelCounts = " , labelCounts # like :  {(0, 1, 'yes'): 1, 'flippers': 1}
    
    shannonEnt = 0.0
    for key in labelCounts:
        # 计算 这个标签出现的概率
        prob = float(labelCounts[key])/numEntries;  
        # print "prob = ", prob # like : 0.5
        shannonEnt -= prob * log(prob, 2);    #log2 n 求2为底的对数
    return shannonEnt;    

def splitDataSet(dataSet, axis, value, callback=None):
    # 按照给定特征划分数据集
    '''''
    dataSet: 待划分的数据集
    axis :   划分数据集的特征
    value:  特征的返回值
    callback: 回调
    '''
    print "axis = %s , value = %s " % (axis, value)
    retDataSet = [];
    for featVec in dataSet:
        # 检查 dataSet的每行，第axis列 == value
        # featVec >>> like:  [1, 1, 'yes']
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis];
            # featVec[axis + 1 :] like : [1, 'yes']
            reducedFeatVec.extend(featVec[axis + 1 :])
            # append增加元素（也可能是数组）到数组， 而且原数组个数只加1. 而不是遍历所有 reducedFeatVec中的元素添加进去
            retDataSet.append(reducedFeatVec); 
            if(callback is not None):
                callback(featVec, reducedFeatVec, featVec[axis + 1 :])
    return retDataSet;     

def chooseBestFeatureToSplit(dataSet, callback = None):
    # 选择最好的数据集划分方式
    '''''
    Requires: 
        1, dataSet 是有2维数/矩阵组成的。
        2, dataSet 最后一列应是当前或者实例的最后一个元素 是类别标签.
    '''
    debug = callback is not None;
    numFeatures = len(dataSet[0]) - 1; # 列数-1   
    baseEntropy = calcShannonEnt(dataSet, debug);
    if(debug):
        print "baseEntropy = " , baseEntropy
    
    bestInfoGain = 0.0;
    bestFeature = -1;
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet];
        if(debug):
            print "featList = ", featList
        uniqueVals = set(featList); # 唯一分类的标签集
        newEntropy = 0.0
        # 计算每种划分方式的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value, callback);
            prob = len(subDataSet) / float(len(dataSet));
            newEntropy += prob * calcShannonEnt(dataSet, debug);
            if(debug):
                print "prob = %s , newEntropy = %s " % (prob, newEntropy)
            
        infoGain = baseEntropy - newEntropy;
        if(debug):
            print "infoGain = ", infoGain 
        # 计算最好的信息增益
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain;
            bestFeature = 1;
    return bestFeature;            
