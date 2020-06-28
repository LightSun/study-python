# coding:utf-8

import numpy as np  
a = np.array([[1, 5, 3], [4, 2, 6]])  
print(a.min())  # 无参，所有中的最小值  
print(a.min(0))  # axis=0; 每列的最小值  , 组成 相同列数的数组.
print(a.min(1))  # axis=1；每行的最小值 , 组成 相同行数的数组.
