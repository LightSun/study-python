# coding:utf-8

# 测试决策树相关： 香农熵. ID3算法 
import CA 
import numpy

def createDataSet():
    # 每列依次代表:  【不浮出水面是否可以生存， 是否有脚蹼， 是否属于鱼类】
    dataSet = [
              # [1,1,'maybe'],
               [1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']
               ];
    labels = ['no surfacing', 'flippers'];     
    #labels = ['flippers', 'no surfacing'];     
    return dataSet, labels;
''''' ps:
list是可变类型, 无法进行hash, tuple就可以解决这个问题
'''
dataSet, labels = createDataSet();
print "dataSet = %s, column count = %s" % (dataSet, len(dataSet[0]))
print CA.calcShannonEnt(dataSet);      

def printCallback(featVec, reducedFeatVec, featVec_t):
    print "featVec = %s, reducedFeatVec = %s, featVec[axis + 1 :] = %s" % (featVec, reducedFeatVec, featVec_t); 

print "============ >>> start 数据划分方式 ==================="
print CA.splitDataSet(dataSet, 0, 1, printCallback);
print CA.splitDataSet(dataSet, 0, 0, printCallback);


print "============ >>> start 最好的数据划分方式 ================="
# this line just for test invalid  dataSet = [[1, 'yes'], [1, 'yes'], [0, 'no'], [0, 'no']];
features = CA.chooseBestFeatureToSplit(dataSet, printCallback);
print "features = ", features  # result 1 means 按照index =1的特征划分。 也就是第2列特征分组
print "raw dataSet = ", dataSet

print "============ >>> start 创建树  ================="
myTree = CA.createTree(dataSet, labels, printCallback);
print "MyTree = ", myTree   
'''''
{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
{'flippers': {0: 'no', 1: {'no surfacing': {0: 'no', 1: 'yes'}}}}
'''

'''''
    绘制注解
'''
# CA.createPlot() # old func ok . just make not blocking next

# 返回一个 决策tree。 用于测试
def retrieveTree(i):
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]

myTree = retrieveTree(0);
print CA.getNumLeafs(myTree)  
print CA.getTreeDepth(myTree) 

myTree['no surfacing'][3] ='maybe' #增加了映射  --- 3: 'maybe' ----
print "myTree = ", myTree
# CA.createPlot(myTree);  # OK , just for next.


### ======================= start 决策树分类函数 ==================================
print "================= >>> start 决策树分类函数 =================="
dataSet, labels = createDataSet();
print CA.classify(myTree, labels, [1,0],True);
# print CA.classify(myTree, labels, [1,1]);

### ======================= start 决策树的序列化和反序列化 ==================================
print "================= >>> start 决策树的序列化和反序列化 =================="
filename = 'classifierStorage.txt';
CA.storeTree(myTree, filename);
print CA.grabTree(filename)



