# coding:utf-8

# matplotlib scatter 函数测试. 

import numpy as np
import matplotlib.pyplot as plt

# 1维数据
x = [1, 2, 3, 4, 5]
y = [2.3, 3.4, 1.2, 6.6, 7.0]

fig = plt.figure()

plt.subplot(232)
plt.scatter(x, y) # 以点的形式
plt.title("scatter")

xcord1 = [1.4,
           2.3, 
           4.6, 
           4.9, 
           3.7, 
           2.7,  
           8.4, 
           6.3
        ];
ycord1= [1,1, 1,1, 1,1, 1,1];
xcord2 = [11.4,
           12.3, 
           14.6, 
           14.9, 
           13.7, 
           12.7,  
           18.4, 
           16.3
        ];
ycord2= [0,0, 0,0, 0,0, 0,0];

ax = fig.add_subplot(111)
plt.scatter(xcord1, ycord1, s=30, c='red', marker='s')
plt.scatter(xcord2, ycord2, s=30, c='green')

plt.show()