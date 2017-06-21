# coding:utf-8

import numpy as np

#假设这里只有6个元素
x = np.array([1, 4, 3, -1, 6, 9])

y = x.argsort()  # 不改变原数组/矩阵
print y          # [3 0 2 1 4 5]
# 将矩阵中的元素从小到大排列, 提取 与原数组对应的index（索引）,然后输出到y.
# 例如：x[3]=-1最小，所以y[0]=3,x[5]=9最大，所以y[5]=5。

"""
x.argsort()[num]
当num>=0时，np.argsort()[num]就可以理解为y[num];
"""

print y[0],y[1],y[2]
print y[-1],y[-2],y[-3]  #反向输出 , 相当于y[-1] 是最大值, y[-2]是第二大值...etc.