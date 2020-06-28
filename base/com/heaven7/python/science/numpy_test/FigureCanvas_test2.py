# coding:utf-8

# from http://www.cnblogs.com/vamei/archive/2013/01/30/2879700.html

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

fig    = Figure()
canvas = FigureCanvas(fig)

# first axes
# add_axes method : *left*, *bottom*, *width*, *height*]
ax1    = fig.add_axes([0.1, 0.1, 0.2, 0.2])
line,  = ax1.plot([0,1], [0,1])     # 线段的形势
ax1.set_title("ax1")

# second axes
ax2    = fig.add_axes([0.4, 0.4, 0.4, 0.5])
sca    = ax2.scatter([1,3,5],[2,1,2]) # 点的形势, 3个点.(1,2), (3,1), (5,2)
ax2.set_title("ax2")

# ax3    = fig.add_axes([0.9, 0.1, 0.4, 0.5])
# sca    = ax3.scatter([1,3,5],[2,1,2]) 
# ax3.set_title("ax3")

canvas.print_figure('FigureCanvas_test2.jpg')


