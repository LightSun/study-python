# coding:utf-8

# 测试 del  函数

a = [-1, 3, 'aa', 85]
print a

del a[0] # 删除第0个元素
print a # [3, 'aa', 85]

del a[1:2] # 删除从第1个元素开始，到第2个为止的元素。包括头不包括尾
print a  # [3, 'aa']

del a # 删除整个list
#print a # NameError: name 'a' is not defined