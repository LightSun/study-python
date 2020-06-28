# coding:utf-8

# random 测试： http://blog.csdn.net/u013920434/article/details/52507173
"""
1. 函数原型：  numpy.random.uniform(low,high,size)
功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
"""

import numpy.random as rd

print rd.uniform(1, 5, 3);  # [ 3.87347138  4.20840842  2.50151249]

#print int(rd.uniform(0, 5, 3)); # error
print int(rd.uniform(0, 5))