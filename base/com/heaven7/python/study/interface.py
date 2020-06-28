#coding:utf-8

class interface(object):
    def Lee(self):
        pass  
      
    def Marlon(self):  
        pass  
    
#没有被  @abstractmethod 标记， 所以方法可以不实现/重写
class Realaize_interface(interface):  
    def __init__(self):  
        pass  
    def Lee(self):  
        print "实现接口中的Lee函数"  


class Realaize_interface2(interface):  
    def __init__(self):  
        pass  
    def Marlon(self):  
        print "实现接口中的Marlon函数"  
        
print "start test interface "        
obj=interface()  
obj.Lee()          
       
obj=Realaize_interface()  
obj.Lee()  
  
  
obj=Realaize_interface2()  
obj.Marlon()  