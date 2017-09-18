# coding:utf-8

# logistic 回归测试

from numpy import *;
import log_lib as log;
import logistic_lib as llogistic;
from common_utils import typeName

log1 = log.Logger("logistic_回归测试");
log1.setLogLevel(log.LEVEL_DEBUG, True);

def loadDataSet():
    # dataMat 已知数据集 (n行3列)，  labelMat 标签列表。
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    # 每行： x1,x2, 类别标签.
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0] # 行数
    
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1]); ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1]); ycord2.append(dataArr[i, 2])
            
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    
    plt.xlabel('X1'); 
    plt.ylabel('X2');
    plt.show()

log1.logTS("start >>> logistic梯度上升...");
dataMat, labelMat = loadDataSet();
result = llogistic.gradAscent(dataMat, labelMat, debug=log1);
log1.logTS("result = %s" % result);

print typeName(result)
print result.getA()  # 从matrix -> ndarray
# 图形化
# plotBestFit(result.getA()); # ok

#weights = llogistic.stocGradAscent0(array(dataMat), labelMat, debug=log1);
weights = llogistic.stocGradAscent1(array(dataMat), labelMat, debug=log1);
plotBestFit(weights)






