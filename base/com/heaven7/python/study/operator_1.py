#coding:utf-8
from operator import *
from _ast import operator
from lib2to3.pgen2.tokenize import Operator
 
a = [1, 2, 3]
b = a
print 'a =', a
print 'b =', b

print operator.__hash__(564)
# TODO not done