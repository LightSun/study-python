# coding:utf-8

"""
1、meshgrid函数用两个坐标轴上的点在平面上画格。
用法：
　　[X,Y]=meshgrid(x,y) 
　　[X,Y]=meshgrid(x)与 [X,Y]=meshgrid(x,x)是等同的 
　　[X,Y,Z]=meshgrid(x,y,z)生成三维数组，可用来计算三变量的函数和绘制三维立体图 

结论：
    meshgrid返回的两个矩阵X、Y必定是行数、列数相等的，且X、Y的行数都等
        于输入参数y中元素的总个数，X、Y的列数都等于输入参数x中元素总个数
"""

import numpy as np

# 生成  [-3, 3), 梯度为1的矩阵.
x = np.arange(-3,3, 1);  #[-3, 3) , 6个元素
y = np.arange(-2,2, 1);  #[-2, 2)   4个元素
X,Y = np.meshgrid(x,y); 

# X， Y均为2维数组，其中X 4行6列， Y， 4行6列
print "x = %s, X = %s" % (x,X) 
print "y = %s, Y = %s" % (y,Y)

