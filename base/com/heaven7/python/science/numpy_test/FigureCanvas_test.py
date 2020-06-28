# coding:utf-8

# from http://www.cnblogs.com/vamei/archive/2013/01/30/2879700.html

"""
在matplotlib中，整个图像为一个Figure对象。在Figure对象中可以包含一个，
或者多个Axes对象。每个Axes对象都是一个拥有自己坐标系统的绘图区域
"""

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

fig    = Figure()
canvas = FigureCanvas(fig)
ax     = fig.add_axes([0.1, 0.1, 0.8, 0.8])

line,  = ax.plot([0,1], [0,1])
ax.set_title("a straight line (OO)")
ax.set_xlabel("x value")
ax.set_ylabel("y value")

canvas.print_figure('FigureCanvas_test.png')
''''
(yaxis同样有tick, label和tick label，没有画出)

尽管data是数据绘图的关键部分，也就是数据本身的图形化显示，但是必须和xaxis, yaxis, title一起，
才能真正构成一个绘图区域axes。一个单纯的，无法读出刻度的线是没有意义的。xaxis, yaxis, 
title合起来构成了数据的辅助部分(data guide)。

上面元素又包含有多种图形元素。比如说，我们的data对象是一条线(Line2D)。title, 
tick label和label都是文本(Text)，而tick是由短线(Line 2D)和tick label构成，
xaxis由坐标轴的线和tick以及label构成，ax由xaxis, yaxis, title, data构成，
ax自身又构成了fig的一部分。上面的每个对象，无论是Line2D, Text还是fig，
它们都来自于一个叫做Artist的基类。

OO绘图的原程序还有一个canvas对象。它代表了真正进行绘图的后端(backend)。
Artist只是在程序逻辑上的绘图，它必须连接后端绘图程序才能真正在屏幕上绘制出来(或者保存为文件)。
我们可以将canvas理解为绘图的物理(或者说硬件)实现。

在OO绘图程序中，我们并没有真正看到title, tick, tick label, xaxis,
 yaxis对象，而是使用ax.set_*的方法间接设置了这些对象。但这些对象是真实存在的，
 你可以从上层对象中找到其“真身”。比如，fig.axes[0].xaxis就是我们上面途中的xaxis对象。
 我们可以通过fig -> axes[0] (也就是ax) -> xaxis的顺序找到它。因此，
 重复我们刚才已经说过的，一个fig就构成了一个完整的图像。对于每个Artist类的对象，
 都有findobj()方法，来显示该对象所包含的所有下层对象。
'''
