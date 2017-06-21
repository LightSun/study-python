# coding:utf-8

# k-近邻算法 及其应用

from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0] , [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    #labels = {'A', 'A', 'B', 'B'} set集合
    return group, labels;

# inX 向量, dataSet 数据样本 训练集，labels 标签向量, k 选择最近邻居的数目
def classify0(inX, dataSet, labels, k):
    ## 利用欧式距离公式， 计算距离 ##
    dataSetSize = dataSet.shape[0];   #行数  here is 4
    # tile平铺，按照行数 = dataSetSize，列数1
    tileResult = tile(inX, (dataSetSize, 1));
    print "tileResult >>> tile(inX, (dataSetSize, 1) = " , tileResult
    
    diffMat = tileResult - dataSet;
    #平方. 即原始矩阵所有的每个元素 平方得到新的 矩阵， 行列数相同
    sqDiffMat = diffMat **2;  
    print "diffMat = %s, sqDiffMat = %s." % (diffMat, sqDiffMat)
    
    sqDistances = sqDiffMat.sum(axis=1);  # 得到矩阵的每行之和
    distances = sqDistances **0.5;  #开方
    print "sqDistances = %s, distances = %s." % (sqDistances, distances)
    
    sortedDistIndices = distances.argsort();  #排序并返回  '原对应索引的数组'.升序
    print "sortedDistIndices = " , sortedDistIndices
    
    #选取距离最小的k点，排序
    classCount = {}
    for i in range(k):
        #2,3,1,0
        voteIlabel = labels[sortedDistIndices[i]];
        # 次数+1并 存到字典-dict / map 中，默认0
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1;
        print " i = %s, voteIlabel = %s" % ( i, voteIlabel)
        
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), 
                        reverse= True); #降序
    print "sortedClassCount = ", sortedClassCount
    return sortedClassCount[0][0];
    
group, labels= createDataSet()

print classify0([0,0], group, labels, 3)   
    
# ======================== 改进约会网站 ===================================

print "=========== start >>> 改进约会网站  ============="

def file2matrix(filename):
    fr = open(filename);
    arrayOlines = fr.readlines();
    numberOfLines = len(arrayOlines); #行数
    # 创建 2维矩阵, 等同于zeros([numberOfLines,3])
    returnMat = zeros((numberOfLines, 3)) 
    
    classLabelVector = []; 
    index = 0;
    for line in arrayOlines :
        line = line.strip(); #去掉回车
        listFromLine = line.split('\t');
        # 2维数组赋值. 将第index行的所有列 赋值为指定的 数组.
        returnMat[index,:] = listFromLine[0:3]; 
        if listFromLine[-1].isdigit():
            classLabelVector.append(int(listFromLine[-1])); #加入int元素
        index +=1 ;
        # print "returnMat = %s , classLabelVector = %s" %(returnMat, classLabelVector)
        
    return  returnMat, classLabelVector;  

datingDataMat, datingLabel = file2matrix('datingTestSet2.txt');
print datingDataMat
print datingLabel[0:20] #从0开始的20个元素


## functions

# ======================== 数据归一化  ===============================
# 数据归一化。 newValue= (oldvalue-min)/(max-min)  
#          即差值 /范围 
print "============= >>> start 数据归一化  ==============="

def autoNorm(dataSet):
    minVals = dataSet.min(0)  # 每列的最小值.组成的数组
    maxVals = dataSet.max(0)  # 每列的最大值.组成的数组
    ranges = maxVals - minVals;
    # shape函数得到矩阵的维数
    #normDataSet = zeros(shape(dataSet));
    m = dataSet.shape[0]; #行数
    # print "m = ", m  #1000
    # eg: [1,2,3] -> 1000个 [1,2,3]
    normDataSet = dataSet - tile(minVals, (m, 1));
    normDataSet = normDataSet / tile(ranges, (m,1));
    return normDataSet, ranges, minVals;

normalMat, ranges, minVals = autoNorm(datingDataMat)
print "normalMat = %s, ranges = %s , minVals = %s" %(normalMat, ranges, minVals)

# ======================== matplotlib显示 可视化数据 ===============================
print "============= start >>> matplotlib显示 可视化数据  =================="

import matplotlib
import matplotlib.pyplot as plt;

fig =  plt.figure();
ax = fig.add_subplot(111);
# 显示第2 ，3列数据
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2]);

# 以不同色彩，尺寸显示. 根据datingLabel数组值
ax.scatter(datingDataMat[:,1], datingDataMat[:,2],
       15.0*array(datingLabel), 15.0*array(datingLabel) );

plt.show();





    
