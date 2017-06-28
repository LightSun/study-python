# coding:utf-8

# 封装一些常用的工具


def isDict(value):
    '''''
    返回是否是字典(dict).
    '''
    return type(value).__name__=='dict' # # type(str1).__name__ = str

def writeObject(obj, filename):
    '''''
    存储/写对象到硬盘.利用python模块pickle序列化对象
    '''
    import pickle
    fw = open(filename, 'w');
    pickle.dump(obj, fw, None);
    fw.close();
    return True;
               
def readObject(filename):
    '''''
    从硬盘获取对象，利用python模块pickle反序列化对象
    '''
    import pickle
    fr = open(filename)
    return pickle.load(fr);