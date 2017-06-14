#coding:utf-8

## 读取文件
# 文件操作的api说明： http://www.open-open.com/lib/view/open1413527388231.html

from sys import argv

script, filename = argv

txt = open(filename)

print "here's your file %r: " % filename
print txt.read() #可读行，或者指定最大字节数

print "type the filename again: will return string from read line"
file_again = raw_input("> ")

txt_again = open(file_again);

print txt_again.readline()