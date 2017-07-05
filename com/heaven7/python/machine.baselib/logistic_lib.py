# coding:utf-8

from numpy import *;
import log_lib as log;


def sigmoid(inX):
    return 1.0 /(1 + exp(-inX)); # exp指数运算。底数为e

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
    weights = ones((n,1)); # n行1列.ndarray
    
    debug.logTMS("gradAscent-梯度上升", "weights = %s " % (weights));
    
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights); #计算积 然后求总和。得到 类似weights矩阵的 结果。
        error = (labelMat - h); # 计算真实类别与预测类别的差值
        weights = weights + alpha * dataMatrix.transpose()*error; # 按照差值方向调整回归系数
    return weights;    


