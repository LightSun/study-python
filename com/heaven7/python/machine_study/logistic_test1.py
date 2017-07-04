# coding:utf-8

# logistic 回归测试

from numpy import *;
import log_lib as log;
import logistic_lib as llogistic;

log1 = log.Logger("logistic_回归测试");
log1.setLogLevel(log.LEVEL_DEBUG, True);

def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    #每行： x1,x2, 类别标签.
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

log1.logTS("start >>> logistic梯度上升...");
dataMat,labelMat = loadDataSet();
result = llogistic.gradAscent(dataMat, labelMat, debug=log1);
log1.logTS("result = %s" % result);
