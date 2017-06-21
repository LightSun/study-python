# coding:utf-8

# 测试 extend and append

a = range(1,4)
b = range(4,7)
a.append(b)

print a  # [1, 2, 3, [4, 5, 6]]


a = range(1,4)
b = range(4,7)
a.extend(b);

print a  # [1, 2, 3, 4, 5, 6]