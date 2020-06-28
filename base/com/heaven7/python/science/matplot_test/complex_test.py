# coding:utf-8

# 
import numpy as np
import matplotlib.pyplot as plt

# 1维数据
x = [1, 2, 3, 4, 5]
y = [2.3, 3.4, 1.2, 6.6, 7.0]

# 图像的比例 figsize
plt.figure(figsize=(12,6))

plt.subplot(231)
plt.plot(x, y)    # 以线段的形式
plt.title("plot")

plt.subplot(232)
plt.scatter(x, y) # 以点的形式
plt.title("scatter")

plt.subplot(233)
plt.pie(y)        # 整个是圆形。各个成分含量
plt.title("pie")

plt.subplot(234)
plt.bar(x, y)     # 柱形图
plt.title("bar")


# 2维数据
delta = 0.025;
x = y = np.arange(-3.0, 3.0, delta);
x, y = np.meshgrid(x, y);
z    = y **2 + x **2;
# print "x = %s\n , y = %s\n, z = %s \n" % (x, y,z)

plt.subplot(235)
plt.contour(x, y ,z)  # 周线
plt.colorbar()        # 右侧条形栏
plt.title("contour")


# read image
import matplotlib.image as mpimg

img = mpimg.imread('line_test_demo.png')

plt.subplot(236)
plt.imshow(img)
plt.title("imshow")

#plt.savefig("matplot_sample.jpg")

plt.show();
# ValueError: Only know how to handle extensions: [u'png']; with Pillow installed matplotlib can handle more images

