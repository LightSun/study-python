#coding:utf-8

# 例：类定义及使用
#self 代表this对象
class CAnimal:
    name = 'unname' # 成员变量 
    def __init__(self,voice='hello'):    # 重载构造函数
        self.voice = voice               # 创建成员变量并赋初始值
    def __del__(self):                   # 重载析构函数
        pass                # 空操作
    def Say(self):
        print self.voice

print "start 'cat' as CAnimal "
cat = CAnimal()        # 定义动物对象t
cat.Say()             # t说话

print "start 'dog' as CAnimal "           # 输出
dog = CAnimal('wow')    # 定义动物对象dog
dog.Say()            # dog说话


# =====================================================================
print "start test >>> class  extend "
class CDog(CAnimal):
    def SetVoice(self,voice):
        self.voice = voice
        self.name = "name_CDog"
    def Say(self):
        CAnimal.Say(self)    
        print "saied by CDog %s" % self.name
        

dog = CDog("12345");
dog.SetVoice(0.55)
dog.Say();

print dog  # <__main__.CDog instance at 0x038B9378>
