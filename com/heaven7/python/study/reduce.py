# coding:utf-8

def add(x, y): 
    return x + y 

# range 返回一个序列， 这里[1,11)

# reduce(function, sequence, starting_value) :
#          对sequence中的item顺序迭代调用function，
#          如果有starting_value，还可以作为初始值调用，例如可以用来对List求和：
list1 = reduce(add, range(1, 11)) 
print list1
