# coding:UTF8
class Properties(object):  
  
    def __init__(self, fileName):  
        self.fileName = fileName  
        self.properties = {}  
  
    def __getDict(self, keyStr, dictName, value):  
  
        if(keyStr.find('.') > 0):  
            k = keyStr.split('.')[0]  
            dictName.setdefault(k, {})  
            # keyStr 除开 k 以外的字符串递归
            return self.__getDict(keyStr[len(k) + 1:], dictName[k], value)  
        else:  
            dictName[keyStr] = value  
            return  
    def getProperties(self):  
        try:  
            pro_file = open(self.fileName, 'Ur')  
            for line in pro_file.readlines():  
                # 去掉中间的空格
                line = line.strip(" ").replace('\n', '').replace(" ", "")  
                # '#’代表注解
                if line.find("#") != -1:  
                    line = line[0:line.find('#')]  
                if line.find('=') > 0:  
                    strs = line.split('=')  
                    # get value
                    strs[1] = line[len(strs[0]) + 1:]  
                    
                    self.__getDict(strs[0].strip(), self.properties, strs[1].strip())  
        except Exception, e:  
            raise e  # raise 引发一个异常
        else:  
            pro_file.close()  
        return self.properties

    
    
