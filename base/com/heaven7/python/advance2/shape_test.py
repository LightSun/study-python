# coding:utf-8
from numpy.core.fromnumeric import shape
from numpy.core.numeric import array

#建立一个4×2的矩阵c, c.shape[1] 为第一维的长度(列)，c.shape[0] 为第二维的长度(行)。

c = array([[1,1],[1,2],[1,3],[1,4]])  

print shape(3) # 得到多少维度的数组.这里
print c.shape 
print c.shape[0] # 行数
print c.shape[1] #列数 
