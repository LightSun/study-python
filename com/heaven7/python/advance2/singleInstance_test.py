# coding:utf-8

import thread
#import threading

Lock = thread.allocate_lock()


class Singleton(object):

    # 定义静态变量实例
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                Lock.acquire()
                # double check
                if not cls.__instance:
                    cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            finally:
                Lock.release()
        return cls.__instance


def test_singleton_in_thread():
    print id(Singleton())

if __name__ == "__main__":
    idx = 0
    while 1:
        thread.start_new_thread(test_singleton_in_thread, ()); # error
        idx += 1
        if idx > 0X100:
            break
        
# 2, 使用装饰器 ===============================
'''''
装饰器 singleton，返回了一个内部函数 getinstance，
该函数会判断某个类是否在字典 instances 中，如果不存在，
则会将 cls 作为 key，cls(*args, **kw) 作为 value 存到 instances 中，
否则，直接返回 instances[cls]。
'''
from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getInstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getInstance

@singleton
class MyClass(object):
    a = 1


# 3 。使用元类 =============== ====================
'''''
元类（metaclass）可以控制类的创建过程，它主要做三件事：

拦截类的创建
修改类的定义
返回修改后的类
'''
class Singleton2(type):
    _instances = {}
    def __call__(self, cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
 
# Python2
class MyClass2(object):
    __metaclass__ = Singleton2
 
# Python3
# class MyClass(metaclass=Singleton):
#    pass




        