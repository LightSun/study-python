# -*- coding: UTF-8 -*-
"""
梯度下降学习: https://zhuanlan.zhihu.com/p/33321183

"""
import numpy as np

# Size of the points dataset.
m = 20

# Points x-coordinate and dummy value (x0, x1).
X0 = np.ones((m, 1))
# print("X0", X0)
X1 = np.arange(1, m+1).reshape(m, 1)
X = np.hstack((X0, X1)) # 将2个相同行的矩阵堆叠到一起.eg: 2个2行1列的堆叠后就是  2行2列的。(列堆叠)
     # vstack 也是堆叠，不过列不变。行堆叠
     # stack 既可行堆叠也可以列堆叠。
print("X", X)

# Points y-coordinate
y = np.array([
    3, 4, 5, 5, 2, 4, 7, 8, 11, 8, 12,
    11, 13, 13, 16, 17, 18, 17, 19, 21
]).reshape(m, 1)

# The Learning Rate alpha.
alpha = 0.01

def error_function(theta, X, y):
    '''Error function J definition.代价函数（损失函数）'''
    diff = np.dot(X, theta) - y
    return (1./2*m) * np.dot(np.transpose(diff), diff)

def gradient_function(theta, X, y):
    '''Gradient of the function J definition.'''
    diff = np.dot(X, theta) - y
    return (1./m) * np.dot(np.transpose(X), diff)

def gradient_descent(X, y, alpha):
    '''Perform gradient descent.'''
    theta = np.array([1, 1]).reshape(2, 1)
    gradient = gradient_function(theta, X, y)
    while not np.all(np.absolute(gradient) <= 1e-5):
        theta = theta - alpha * gradient
        gradient = gradient_function(theta, X, y)
    return theta

optimal = gradient_descent(X, y, alpha)
print('optimal:', optimal)
print('error function:', error_function(optimal, X, y)[0,0])
"""
问题：theta为什么初始是1 ?  梯度下降的目的是从1开始(起点)找到梯度逼近0的点. (梯度即微分)
      转置transpose在这里的意义是什么？
"""