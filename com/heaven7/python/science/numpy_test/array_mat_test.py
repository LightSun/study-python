# coding:utf-8

import numpy as np
from numpy.matrixlib.defmatrix import mat
from numpy.core.numeric import ones

# 从范围【10，30) 返回以10开始，等差值为5的数列. 不包含30
print np.arange(10, 30, 5)   #[10 15 20 25]

print np.arange(0 , 2, 0.5)  

# 从范围[-1,0] , 5个元素组成的等差元素的数组.
print np.linspace(-1, 0, 5)  


x = np.array([[1, 2], [3, 4]]);
print mat(x);  # 转化为numpy数组
print mat(x).transpose();

# transpose numpy矩阵转化. 这里从1行4列，变成，4行1列.
x = np.array((1,2,3,4));
print mat(x);
print mat(x).transpose(); 

# transpose numpy矩阵转化. 这里从3行2列，变成，2行3列. 并且将每列的数据 合并成1行。
x = np.array([[1, 2], [3, 4], [5,6]]);
print mat(x); # [[1 2][3 4] [5 6]]
print mat(x).transpose(); # [[1 3 5][2 4 6]]

# 矩阵个
x1 = mat([[1, 2, 3], [4,5,6], [7,8,9], [10,11,12]]); #转化为numpy数组， 4行3列.
x2 = ones((x1.shape[1], 1)); # 【生成 x1列数=3】行1列的数组
print type(x1).__name__  # matrix
print type(x2).__name__  # ndarray
result = (x1 * x2);       # 计算矩阵的积。然后求和。得到类似x2的矩阵.
print type(result).__name__ # matrix
print "x1 * x2 = %s " % (result);


