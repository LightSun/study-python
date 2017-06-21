# coding:utf-8

# k-近邻算法 及其应用-- > 约会数据分析

from numpy import *
import operator
DEBUG = False;

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0] , [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    #labels = {'A', 'A', 'B', 'B'} set集合
    return group, labels;

# inX 向量, dataSet 数据样本 训练集，labels 标签向量--1维数组  ,  k 选择最近邻居的数目
# 点（0, 0）与（1，2）的距离计算为：
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
    
    classLabelVector = []; # 1维数组
    index = 0;
    for line in arrayOlines :
        line = line.strip(); #去掉回车
        listFromLine = line.split('\t');
        # 2维数组赋值. 将第index行的所有列 -- 赋值为指定的 数组.
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

# ======================== 数据归一化  (规范到-1 ~ 1)===============================
# 数据归一化。 newValue= (oldvalue-min)/(max-min)  
#          即差值 /范围 
print "============= >>> start 数据归一化  ==============="
# 数据归一化  (规范到-1 ~ 1)
def autoNorm(dataSet):
    # 每列的最大or最小值.组成的数组 ，个数为列数
    minVals = dataSet.min(0)  
    maxVals = dataSet.max(0)  
    ranges = maxVals - minVals;
    
    print "called autoNorm(dataSet): minVals = %s, ranges = %s"  % (minVals, ranges)
    # shape函数得到矩阵的维数
    #normDataSet = zeros(shape(dataSet));
    m = dataSet.shape[0]; #行数
    # print "m = ", m  #1000
    # eg: [1,2,3] -> 1000个 [1,2,3]
    normDataSet = dataSet - tile(minVals, (m, 1));
    
    # 具体特征值相除. 某些软件中可能是矩阵除法，numpy中矩阵除法需要用linalg.solve(matA , matB) 
    normDataSet = normDataSet / tile(ranges, (m,1)); 
    print "normDataSet.shape[0] = %s, shape[1] = %s " % (normDataSet.shape[0],normDataSet.shape[1])
    return normDataSet, ranges, minVals;

# normalMat --> here 1000 row, 3 column
normalMat, ranges, minVals = autoNorm(datingDataMat)
print "normalMat = %s, ranges = %s , minVals = %s" %(normalMat, ranges, minVals)

# ======================== matplotlib显示 可视化数据 ===============================
print "============= start >>> matplotlib显示 可视化数据  =================="

import matplotlib
import matplotlib.pyplot as plt;

fig =  plt.figure();
ax = fig.add_subplot(111);
# 显示第2 ，3列数据
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2]); #scatter 分散的意思

# 以不同色彩，尺寸显示. 根据datingLabel数组值
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 
       15.0*array(datingLabel), 15.0*array(datingLabel) ); 

#plt.show(); # 显示图形化界面后，后面的程序需要等待.暂时注释


## ======================== 测试： 验证分类器 ==============================

print "=============== >>> start 测试： 验证分类器 ===================="

# 测试错误率
def datingClassTest(hoRatio=0.10, k=3):
    
    #hoRatio = 0.10;  #测试的比率. 这里是训练样本的10%用于测试
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt');
    normalMat, ranges, minVals = autoNorm(datingDataMat);
    m = normalMat.shape[0];
    numTestVesc = int(m*hoRatio); # 100
    
    errorCount = 0.0;
    for i in range(numTestVesc):
        # 选取距离最小的k点
        # normalMat[numTestVesc:m, :] 取 剩余的90%作为 样本数据 去验证。
        # normalMat[i,:] 取 第i行的 所有列数据
        classifierResult = classify0(normalMat[i,:], normalMat[numTestVesc:m, :], 
                                     datingLabels[numTestVesc:m], k);
        print "the classifier came back with : %d, the real answer is : %d "\
                   % (classifierResult, datingLabels[i])
        if(classifierResult != datingLabels[i]):
            errorCount += 1.0;
    print "the total error rate is %f " % (errorCount / float(numTestVesc))                   

# 错误率 随 hoRatio的比率增大而 增大
datingClassTest(0.1,9);    


### ====================== 约会网站预测函数 ====================== ###
print "============= >>> start 约会网站预测函数 ================="

# 根据已知样本。分析某个对象是否是她中意的.
def classifyPerson(k=3):
    resultList = ['not at all', 'in small doses','in large doses'];
    personTats = float(raw_input("percentage of time spent playing video games ?")); # 玩视频游戏花费的时间
    ffMiles = float(raw_input("frequent flier miles earned per year?"));             # 飞行英里
    iceCream = float(raw_input("liters of ice cream consumed per year ?"));          # 消耗的冰淇淋. xx公升
    # datingLabels 文件中最后一行的标签值
    datingDataMat, datingLabels = file2matrix("datingTestSet2.txt");
    normalMat, ranges, minVals = autoNorm(datingDataMat);
    
    inArr = array([ffMiles, personTats, iceCream]);
    # (inArr - minVals)/ ranges --> 得到规范化的值
    classifierResult = classify0((inArr - minVals)/ ranges, 
                                 normalMat, datingLabels, k); # 从文件中得知classifierResult值的范围 【1,3】 
    print "you will probably like this person: " , resultList[classifierResult - 1]                             

classifyPerson();
