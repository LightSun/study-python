# coding:utf-8


"""
http://www.cnblogs.com/yyxayz/p/4033736.html

"""

import numpy as np

### ================= start in 2维数组 =======================

# 对于2维数组，sum(axis = 1 )表示将矩阵的每一行向量相加

A = [[0,1,2],[2,1,3]];
arr = np.sum(A, axis=1)
print arr

#所有数组元素之和
print arr.sum()

# sum(axis =0 ) 表示将矩阵的每一列向量相加
arr = np.sum(A, axis=0)
print arr

a = np.array([[0, 2, 1]])

print a.sum()
print a.sum(axis=0)
print a.sum(axis=1)

###
### ================= in 1维 数组 =======================
a = np.array([[0, 2, 1]])
### 对一维数组，只有第0轴，没有第1轴


