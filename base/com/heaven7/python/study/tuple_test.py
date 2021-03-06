# -*- coding: UTF-8 -*-

""" 元组(tuple)
Python的元组与列表类似，不同之处在于元组的元素不能修改；
            元组使用小括号()，列表使用方括号[]；
            元组创建很简单，只需要在括号中添加元素，并使用逗号(,)隔开即可
            
 创建空元组，例如：tup = ();
元组中只有一个元素时，需要在元素后面添加逗号，例如：tup1 = (50,);
元组与字符串类似，下标索引从0开始，可以进行截取，组合等。           
"""

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";


# nested list
a = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0], [1, 2]]
print "orginal:", a
try:
    print list(set(a)) # TypeError: unhashable type: 'list'
except TypeError, e:
    print "Error:", e
 
# tuple list
a = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 0), (1, 2)]
print "orginal:", a
print list(set(a))