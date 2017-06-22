# coding:utf-8

"""
Python 文档解释：
dict.items(): Return a copy of the dictionary’s list of (key, value) pairs.
dict.iteritems(): Return an iterator over the dictionary’s (key, value) pairs.
dict.items()返回的是一个完整的列表，而dict.iteritems()返回的是一个迭代器
dict.items()返回列表list的所有列表项，形如这样的二元组list：［
          (key,value),(key,value),...］,dict.iteritems()是generator, yield 2-tuple。
          相对来说，前者需要花费更多内存空间和时间，但访问某一项的时间较快(KEY)。
          后者花费很少的空间，通过next()不断取下一个值，但是将花费稍微多的时间来生成下一item。
"""
d = {
 'Adam': 95,
 'Lisa': 85,
 'Bart': 59
 }

if 'Lisa' in d:
    print d['Lisa']
    
    
print d.iteritems()    