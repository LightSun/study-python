# coding:utf-8

# map(function, sequence) ：
#                 对sequence中的item依次执行function(item)，见执行结果组成一个List返回：

map1 = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
print map1

def f(x):
    return x * x
# map()函数不改变原有的 list，而是返回一个新的 list。
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# 利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。

def format_name(s):
    # 这里 0-2表示从 【0，2) 的元素变成大写， (2+]变小写
    s1 = s[0:2].upper() + s[2:].lower();
    return s1;

print map(format_name, ['adam', 'LISA', 'barT']) # ['Adam', 'Lisa', 'Bart']
