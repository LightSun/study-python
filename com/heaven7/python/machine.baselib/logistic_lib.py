# coding:utf-8

from numpy import *;
import log_lib as log;
from numpy import ones
from scipy.constants.constants import alpha


def sigmoid(inX):
# e = 2.718281828459045...
    return 1.0 /(1 + exp(-inX)); # exp指数运算。底数为e

def stocGradAscent1(dataMatrix, classLabels, nulberIter=150,debug=log.EMPTY_LOG):
    """
    随机梯度上升算法-- 改进
    """
    m,n = shape(dataMatrix);
    weights = ones(n); # 1维数组 matrix. 个数等于n
    for j in range(nulberIter):
        dataIndex = range(m); # 0 ---- m-1
        for i in range(m):
            # j , i 这里避免严格下降。
            alpha = 4/(1.0 + j + i) + 0.01;  # 每次调整，缓解数据波动
            randIndex = int(random.uniform(0, len(dataIndex))); #随机选取样本更新回归系数
            h = sigmoid(sum(dataMatrix[randIndex] * weights));
            error = classLabels[randIndex] - h;
            weights = weights + alpha * error * dataMatrix[randIndex];
            del(dataIndex[randIndex]);
    
    return weights;    

def stocGradAscent0(dataMatrix, classLabels, debug=log.EMPTY_LOG):
    """
    随机梯度上升算法
    """
    m,n = shape(dataMatrix);
    alpha = 0.01
    weights = ones(n); # 1维数组 matrix. 个数等于n
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights)); # dataMatrix[i]= 1行3列，weights = 3行1列
        error = classLabels[i] - h;
        debug.logTMS("stocGradAscent0-随机梯度上升", "h = %s,error = %s" % (h,error));
        weights = weights + alpha * error * dataMatrix[i];
    return weights;    
    

def gradAscent(dataMatIn, classLabels, debug=log.EMPTY_LOG):
    """ 梯度上升 算法
    dataMatIn 2维，矩阵。这里 100*3. 100行3列, 300个元素
    classLabels 2维矩阵。这里 1* 100
    """
    dataMatrix = mat(dataMatIn); #convert to NumPy matrix
    
    # transpose 使得 从1行100列变成，100列1行. 
    labelMat = mat(classLabels).transpose(); #convert to NumPy matrix
    
    m,n = shape(dataMatIn);
    debug.logTMS("gradAscent-梯度上升", "数据集%s行%s列" % (m,n));
    alpha = 0.001;  # 向目标移动的步长
    maxCycles = 500; #迭代次数
    weights = ones((n,1)); # n行1列.matrix
    
    debug.logTMS("gradAscent-梯度上升", "weights = %s " % (weights));
    
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights); #计算积 然后求总和。得到 类似weights矩阵的 结果。
        error = (labelMat - h); # 计算真实类别与预测类别的差值
        weights = weights + alpha * dataMatrix.transpose()*error; # 按照差值方向调整回归系数
    return weights;    


