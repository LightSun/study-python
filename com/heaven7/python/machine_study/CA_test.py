# coding:utf-8

# 测试决策树相关： 香农熵
import CA 
import numpy

def createDataSet():
    # 每列依次代表:  不浮出水面是否可以生存， 是否有脚蹼， 是否属于鱼类
    dataSet = [
              # [1,1,'maybe'],
               [1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'yes']
               ];
    #labels = ['no surfacing', 'flippers'];     
    labels = ['no surfacing', 'flippers'];     
    return dataSet, labels;
''''' ps:
list是可变类型, 无法进行hash, tuple就可以解决这个问题
'''
dataSet, labels = createDataSet();
print dataSet
print CA.calcShannonEnt(dataSet);      

def printCallback(featVec, reducedFeatVec, featVec_t):
    print "featVec = %s, reducedFeatVec = %s, featVec[axis + 1 :] = %s" % (featVec, reducedFeatVec, featVec_t); 

print "============ >>> start 数据划分方式 ==================="
print CA.splitDataSet(dataSet, 0, 1, printCallback);
print CA.splitDataSet(dataSet, 0, 0, printCallback);


print "============ >>> start 最好的数据划分方式 ================="
features = CA.chooseBestFeatureToSplit(dataSet, printCallback);
print features


