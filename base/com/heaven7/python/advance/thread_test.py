# -*- coding: UTF-8 -*-

#Python线程锁
# 类型转化： http://blog.csdn.net/oyzl68/article/details/8007153

import thread
from time import sleep

lock = thread.allocate_lock()
g_FinishCount = 0

def loop(id):
    lock.acquire()  #申请锁
    for i in range (0,4):
        print "Thread ",id," working"
        sleep(1)
    lock.release()  #释放锁
    global g_FinishCount
    g_FinishCount = g_FinishCount + 1

thread.start_new_thread(loop,(1,))
thread.start_new_thread(loop,(2,))
thread.start_new_thread(loop,(3,))

while g_FinishCount < 3:
    sleep(1)
    
