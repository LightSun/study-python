# coding:utf-8

# 用pyplot 绘制 直线

import matplotlib.pyplot as plt

plt.plot([0, 3], [0, 3])      # plot/draw a line from point (0, 0) to  point (3, 3)
plt.title("a strait line")    # 这个图形的标题
plt.xlabel("x value")         # x轴标签
plt.ylabel("y value")         # y轴标签

plt.arrow(1.5, 2, 0.5, 0.5, True) # 绘制一个箭头

plt.savefig("line_test_demo.png")       # 将图形保存到 demo.png中。 该版本jpg不支持
plt.show()