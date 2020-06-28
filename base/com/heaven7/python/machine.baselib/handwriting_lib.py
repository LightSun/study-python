# coding:utf-8

# 机器学习- 手写识别系统(利用k-近邻算法)
"""
  k近邻算法缺点： 时间复杂度，空间复杂度高。
                              无法给出任何数据的基础结构信息， 因此我们也无法知晓平均实例样本和典型实例样本的特征。
"""

from numpy import *
import operator

DEBUG = False;

#  inX 向量, 
#  dataSet 数据样本 训练集，
#  labels 分类的标签--1维数组  , 
#  k 选择最近邻居的数目
# ps: 点（0, 0）与（1，2）的距离计算为：
#                           根号((1-0)平方 + (2-0)平方)
def classify0(inX, dataSet, labels, k):
    ## 利用欧式距离公式， 计算距离 ##
    dataSetSize = dataSet.shape[0];   #行数  here is 4
    # tile平铺，按照行数 = dataSetSize，列数1
    tileResult = tile(inX, (dataSetSize, 1));
    if DEBUG:
        print "tileResult >>> tile(inX, (dataSetSize, 1) = " , tileResult
    
    diffMat = tileResult - dataSet;
    #平方. 即原始矩阵所有的每个元素 平方得到新的 矩阵， 行列数相同
    sqDiffMat = diffMat **2;  
    if DEBUG:
        print "diffMat = %s, sqDiffMat = %s." % (diffMat, sqDiffMat)
    
    sqDistances = sqDiffMat.sum(axis=1);  # 得到矩阵的每行之和 的数组
    distances = sqDistances **0.5;  #开方
    if DEBUG:
        print "sqDistances = %s, distances = %s." % (sqDistances, distances)
    
    sortedDistIndices = distances.argsort();  #排序并返回  '原对应索引的数组'.升序
    if DEBUG:
        print "sortedDistIndices = " , sortedDistIndices
    
    #选取距离最小的k点，排序
    classCount = {}
    for i in range(k):
        # sortedDistIndices = 2,3,1,0
        voteIlabel = labels[sortedDistIndices[i]];
        # 次数+1并 存到字典-dict / map 中，默认0
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1;
        if DEBUG:
            print " i = %s, voteIlabel = %s" % ( i, voteIlabel)
    # operator.itemgetter(1) 按照value排序   
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), 
                        reverse= True); #降序
    if DEBUG:                    
        print "sortedClassCount = ", sortedClassCount
    return sortedClassCount[0][0]; #得到出现次数最少的 .key-value中的key

# 将图像数据转化为 1* 1024的2维矩阵
def img2Vector(filename):
    returnVect = zeros((1,1024));
    fr = open(filename)
    # 将每行的头32个字符转化为int , 存储到矩阵中
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i + j] = int(lineStr[j]);
    return returnVect;        