#coding:utf-8
#抽象类加抽象方法就等于面向对象编程中的接口  
from abc import ABCMeta,abstractmethod  
  
class interface(object):  
    __metaclass__ = ABCMeta #指定这是一个抽象类  
    @abstractmethod  #抽象方法  
    def Lee(self):  
        pass  
      
    def Marlon(self):  
        pass  
  
  
class RelalizeInterfaceLee(interface):#必须实现interface中的所有函数，否则会编译错误  
    def __init__(self):      
        print '这是接口interface的实现'  
    def Lee(self):  
        print '实现Lee功能'          
    def Marlon(self):  
        pass     
   
  
class RelalizeInterfaceMarlon(interface): #必须实现interface中的所有函数，否则会编译错误  
    def __init__(self):      
        print '这是接口interface的实现'  
    def Lee(self):  
        pass        
    def Marlon(self):  
        print "实现Marlon功能"  
