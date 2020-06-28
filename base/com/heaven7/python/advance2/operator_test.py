# coding:utf-8
import operator

a = [1,2,3] 
b = operator.itemgetter(1);  #获取  index = 1的对象
print b(a)  

d = {
 #key : value
 'Adam': 95, 
 'Lisa': 85,
 'Bart': 59,
 }
print d.iteritems()

b = operator.itemgetter(1,0) #获取 域 index = 1和  域index =0 的对象
print b(a)