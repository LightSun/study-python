# coding:utf-8

# 使用shape计算矩阵的行和列
# [[0,1,2],[2,1,3]] 表示2行，3列

import numpy
a = numpy.array([[1,2,3],[4,5,6]])

#shape属性，是一个(行，列)形式的元组
print a.shape

# 结果还是 2维数组，取行index 范围【0,2】， 所有的列
print a[0:2,:]  # [[1 2 3]
                #   [4 5 6]]

# result 1维数组
print a[1,:]  # [4 5 6]

# result 2维数组。 行index >=1
print a[1:,:] # [[4 5 6]]

# result 1维数组. 取index = 1 的 列
print a[:,1]  # [2 5]


#result 2维数组, 取列index >=1的
print a[:,1:]  #[[2 3]
               #  [5 6]]
               
a = numpy.array([1,2,3])
print a[:1]  # 对于1维，【index:cout】  表示从哪个index开始(不写表示所有)， count表示个数
print a[:2]
print a[:0]
