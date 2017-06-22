# coding:utf-8

# 决策树相关
from math import log
import operator
# plot 绘图
import matplotlib 
import matplotlib.pyplot as plt;

matplotlib.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签  
matplotlib.rcParams['axes.unicode_minus']=False   #用来正常显示负号  


def calcShannonEnt(dataSet, debug=True):
    '''''
       计算数据集的 香农熵(概念见 machine_study/ct_idea.py) 
   or  度量数据集的无序程度
    '''
    numEntries = len(dataSet);
    
    labelCounts = {}; #key-value =  dataSet最后一列的name-次数
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
    # 按照给定特征 划分数据集, 返回划分的结果集(比如某行的特征符合 value, 那么剩余的所有列, 作为一个list 放入结果集中)
    '''''
    dataSet: 待划分的数据集
    axis :   划分数据集的特征 index
    value:  特征的返回值
    callback: 回调
    '''
    print "axis = %s , value = %s " % (axis, value)
    retDataSet = [];
    
    #featVec is list ，取剩余所有列reducedFeatVec ,并存入结果集retDataSet.
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
    # 选择最好的数据集划分方式. return 最佳特征列的index.
    '''''
    Requires: 
        1, dataSet 是有2维数/矩阵组成的。 （且只有3列，2列特征，一列标签）
        2, dataSet 最后一列应是当前或者实例的最后一个元素 是类别标签.
    '''
    debug = callback is not None;
    numFeatures = len(dataSet[0]) - 1; # 列数-1 , 因为最后一列是标签。  
    
    if(numFeatures <= 0):
        raise ValueError('the dataSet donnot satisfy the Required case.'); 
    if(numFeatures == 1):
        return 0;  # return the first index of feature directly.
    
    # eg: 0.970950594455
    baseEntropy = calcShannonEnt(dataSet, debug);
    if(debug):
        print "baseEntropy = " , baseEntropy # 熵
    
    bestInfoGain = 0.0;
    bestFeature = -1;
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet];
        if(debug):
            print "featList = ", featList
        uniqueVals = set(featList); # 唯一分类的特征列
        newEntropy = 0.0
        # 计算每种划分方式的信息熵
        for value in uniqueVals:
            # 根据 特征列 uniqueVals中每个元素, 得到划分的子集
            subDataSet = splitDataSet(dataSet, i, value, callback);
            prob = len(subDataSet) / float(len(dataSet));
            newEntropy += prob * calcShannonEnt(subDataSet, debug);
            if(debug):
                print " in value(%s), prob = %s , newEntropy = %s ,subDataSet = %s " \
                      % (value, prob, newEntropy, subDataSet)
            
        infoGain = baseEntropy - newEntropy; #基尼指数
        if(debug):
            print "infoGain = ", infoGain 
        # 计算最好的信息增益
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain;
            bestFeature = 1;
    return bestFeature;        


def majorityCnt(classList):
    '''''
          多数表决 ->决定叶子节点的分类. 返回投票最多的 分类标签.
    '''
    # key-value = classList元素 --次数
    classCount = {};
    for vote in classList: # vote投票
        if vote not in classCount.keys():
            classCount[vote] = 0;
        classCount[vote] += 1;
    # 按照 value(这里是次数)降序排序
    sortedClassCount = sorted(classCount.iteritems(),
                               key = operator.itemgetter(1), reverse = True);   
    return sortedClassCount[0][0];                             

def createTree(dataSet, labels, callback=None):
    '''''
    创建树. returan 多层的dict 树
    dataSet: 数据集
    labels:  标签列表 (所有特征的标签.)
  Requires: 
    1, dataSet 是有2维数/矩阵组成的。 （且只有3列，2列特征，一列标签）
    2, dataSet 最后一列应是当前或者实例的最后一个元素 是类别标签.   
    '''
    debug = callback is not None;
    
    # 取得所有分类标签list
    classList = [example[-1] for example in dataSet]
    # count函数返回 指定value在list中出现的次数
    if(classList.count(classList[0]) == len(classList)):
        return classList[0]; # 如果所有 分类标签 相同.直接返回该标签
    
    if( len(dataSet[0]) == 1): # 如果只有1列数据.
        return majorityCnt(classList);
    
    if(debug):
        print ">>> start call [ chooseBestFeatureToSplit() ]： dataSet = %s" % dataSet
    # have a bug . when dataSet = [[1, 'yes'], [1, 'yes'], [0, 'no'], [0, 'no']]
    bestFeat = chooseBestFeatureToSplit(dataSet, None);
    if(debug):
        print "labels = %s, bestFeat = %s" % (labels, bestFeat)
    bestFeatLabel = labels[bestFeat];
    myTree = {bestFeatLabel:{}}; # 多重map/dict
    
    del(labels[bestFeat]); # 删除最佳特征 分类标签
    
    # 获得最佳 特征列 的所有数据
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues);
    
    if(debug):
        print "called [ createTree() ]: best uniqueVals = ", uniqueVals
        print "myTree = ", myTree
        
    for value in uniqueVals:  #所有的特征值：  0 and 1
        subLabels = labels[:];
        if debug:
            print "subLabels = " , subLabels
        # 递归
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value, None),
                                                   subLabels, None)
        print "myTree = ", myTree
    return myTree;    

# ======================= 图形化 ============================
# 定义文本框和箭头格式
decisionNode = dict(boxstyle = "sawtooth", fc = "0.8")  
leafNode = dict(boxstyle = "round4", fc = "0.8")  
arrow_args = dict(arrowstyle = "<-")  

# 绘制带箭头的注解. (将含义用箭头指向某个点.)
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    '''''
    绘制带箭头的注解.
    '''
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )

#  定义 createPlot.ax1 全局变量   .python 中变量默认是全局的
# def createPlot(): #绘制简单的示例
#     fig = plt.figure(1, facecolor='white')
#     fig.clf()
#     # frameon 使得科学图-x y 轴 是否有实线
#     createPlot.ax1 = plt.subplot(111, frameon=False) 
#     plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode) # 决策节点
#     plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)         # 叶子节点
#     plt.show()    
    
def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    #no ticks
    #createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses 
    # 存储树的宽度和深度
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
    plotTree(inTree, (0.5,1.0), '')
    plt.show()

def plotMidText(cntrPt, parentPt, txtString):
    '''''
    在父节点之间填充文本信息, 并计算中间位置
    '''
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)
    
def plotTree(myTree, parentPt, nodeTxt):#if the first key tells you what feat was split on
    '''''
    绘制决策树
    '''
    # 计算宽高
    numLeafs = getNumLeafs(myTree)  #this determines the x width of this tree
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]     #the text label for this node should be this
    
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key],cntrPt,str(key))        #recursion
        else:   #it's a leaf node print the leaf node
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD
#if you do get a dictonary you know it's a tree, and the first element will be another dict    
    
# ======================= 图形 ============================

def getNumLeafs(myTree):
    '''''
    获得叶子节点的数目
    '''
    numLeafs = 0;
    firstStr = myTree.keys()[0];
    secondDict = myTree[firstStr];
    
    for key in secondDict.keys():
        # >>> type 函数 判断子节点是否是 字典dict 类型
        if type(secondDict[key]).__name__ =='dict':
            numLeafs += getNumLeafs(secondDict[key]);
        else:
            numLeafs += 1
    return numLeafs;

def getTreeDepth(myTree):
    '''''
    获得树的层数
    '''
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict': # 判断是否是 字典dict
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:   
            thisDepth = 1
        if thisDepth > maxDepth: 
            maxDepth = thisDepth
    return maxDepth 