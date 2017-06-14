# coding:utf-8

import string

# copy
str = 'abc'
# 拷贝str字符串，并且移除其中的a 字符.
str_copy = string.strip(str, "a")  # 第2个参数可以为None

print str_copy
sStr1 = 'abc'
sStr2 = sStr1
# 复制指定长度的 字符串
sStr1 = sStr2[0:2]


# 连接 concat/join
sStr1 = 'strcat'
sStr2 = 'append'
sStr1 += sStr2
print sStr1

delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)  # 相当于加入间隔符


# 查找 find /index
print "start 查找"
print sStr1.index(sStr2)
print sStr1.find(sStr2)
print "end 查找"

# cmp  比较
print cmp(sStr1, sStr2)


# 追加指定长度的字符串
n = 3
sStr1 += sStr2[0:n]

# 大小写转换
print sStr1.upper()
print sStr2.lower()

# 字符串长度比较.
sStr1 = '12345'
sStr2 = '123bc'
n = 3  # 指定比较 [0,3)
print cmp(sStr1[0:n], sStr2[0:n])


# 替换
sStr1 = '12345'
ch = 'r'
n = 3
# 拼接字符 。前n个为 ch= 'r' 后面的取 sStr1索引>=3以后的
sStr1 = n * ch + sStr1[3:]
print sStr1


# 翻转字符串
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print sStr1


# 分割
sStr1.split(",")

print "start test addslashes()"

def addslashes(s):
    # map
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)
s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print s
print addslashes(s)


# 只保留字母和数字
def OnlyCharNum(s, oth=''):
    s2 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
            if not c in fomart:
                    s = s.replace(c, '');
    return s;
    
print OnlyCharNum("a000 aa-b")


