# coding:utf-8

class Logger:
    def __init__(self, tag=''):  # 重载构造函数
        self.tag = tag        # 创建成员变量并赋初始值

    def start(self, tag):
        self.tag = tag 
        print "============= >>> start %s =============" % self.tag;
    
    def end(self):
        print "============= >>> end %s =============" % self.tag;   
        
