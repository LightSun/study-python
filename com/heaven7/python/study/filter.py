# coding:utf-8

#使得，被2和3整除的数被过滤.
def f(x): 
    return x % 2 != 0 and x % 3 != 0 
list1 = filter(f, range(2, 25)) 
print list1
