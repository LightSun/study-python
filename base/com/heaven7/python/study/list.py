# coding:utf-8

# define array/list
a = [0, 1, 2]
a1 = [[0 for x in range(10)] for y in range(10)]
b = [[0] * 10] * 10

a.append('5')
print a
print a1 == b


c = [] 
for i in range(10): 
    c.append('x') 
print c    

c.insert(2, 'insert')
# c.index(value, )
def test():
    print "function for key"
def test_cmp():
    print "test function for cmp"    

# cmp 可指定函数， 排序前最先调用    
# key 可以指定函数，排序前调用. 默认None
#    reverse = True 代表倒序
c.sort(cmp=test_cmp(), key=test(), reverse=True) 

print c.count('x')  # 'x'的个数
print c  

print "start extend"
c.extend(a)  # 将a 数组的元素添加到c末尾.
print "a = ", a
print "c = ", c 


print "start test sort"  # 字典顺序 / 升序
print sorted([1, 4, 5, 2, 3, 6])

# 默认值是 list, 累积到list中
def f(a, L=[]):
    L.append(a)
    return L
print f(1)
print f(2)
print f(3)
# 如果你不想在不同的函数调用之间共享参数默认值，可以如下面的实例一样编写函数：
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

