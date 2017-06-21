# coding:UTF8


# ============= 流程控制 =================
# 4.1 if 语句
# 4.2 for 语句
# 4.3 range() 函数
# 4.4 break 和 continue 语句，以及 Loops 中的 else 子句
# 4.5 pass 语句
# 4.6 定义函数
# 4.7 深入函数定义
# 4.7.1 参数默认值
# 4.7.2 参数关键字
# 4.7.3 可变参数表
# 4.7.4 Lambda 形式
# 4.7.5 文档字符串
# ============================


# >>> if 
x = int(raw_input("Please enter an integer: "))
if x < 0:
    x = 0
"""
if (not skipkeys and ensure_ascii and
        check_circular and allow_nan and
        cls is None and indent is None and separators is None and
        encoding == 'utf-8' and default is None and not sort_keys and not kw):
        return _default_encoder.encode(obj)
    if cls is None:
        cls = JSONEncoder
    return cls(
        skipkeys=skipkeys, ensure_ascii=ensure_ascii,
        check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        separators=separators, encoding=encoding, default=default,
        sort_keys=sort_keys, **kw).encode(obj)
  判断是否为null ----- > if hold is not None:        
"""    
    

# >>> for    
a = ['cat', 'window', 'defenestrate']
for x in a:
    print x, len(x) 
    
for x in a[:]:  # 复制list  make a slice copy of the entire list
    if len(x) > 6: 
        a.insert(0, x)  # 原list中insert
print a

# >>> range
print range(5, 10)  # [5,10)



# >>> break and continue 
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n / x
            break
        else:
            print n, 'is a prime number'
            
            
# >>> pass
# <code> while True:
#          pass  # Busy-wait for keyboard interrupt
# </code>


# === 参数关键字
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "Volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

# all ok
parrot(1000)
parrot(action='VOOOOOM', voltage=1000000)
parrot('a thousand', state='pushing up the daisies')
parrot('a million', 'bereft of life', 'jump')    

# 不过以下几种调用是无效的：
#parrot()                     # required argument missing（缺少必要参数）
#parrot(voltage=5.0, 'dead')  # non-keyword argument following keyword （在关键字后面有非关键字参数）
#parrot(110, voltage=220)     # duplicate value for argument（对参数进行了重复赋值）
#parrot(actor='John Cleese')  # unknown keyword（未知关键字）


# >>> 可变参数
def fprintf(file, format, *args):
    file.write(format % args)


# >>> Lambda形式 (lambda相当于一个函数)
a = lambda x, y: x + y
print a(42,8)


# >>> 文档字符串
"""
dsfdsfsfdsfdsf
wr25rfsdfdsfg34t
"""







