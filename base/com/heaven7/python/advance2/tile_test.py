# coding:utf-8

"""
格式：tile（A,reps） 
* A：array_like 
*      输入的array 
* reps：array_like 
*       A沿各个维度重复的次数
"""
from numpy.lib.shape_base import tile

A=[1,2] 
print tile(A,2)  # [1 2 1 2]

"""
[[1 2 1 2 1 2]
 [1 2 1 2 1 2]]
"""
# 理解 2,3这里2，3代表:  行的维度平铺2次， 列的维度 平铺3次. 最终得到 2行，6列的数组 (A是2个元素的数组* 3).
print tile(A, (2,3))
