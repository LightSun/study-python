# coding:utf-8

# 常量： http://www.cnblogs.com/Vito2008/p/5006255.html

class _const:
    class ConstError(TypeError) : pass

    def __setattr__(self, key, value):
            # self.__dict__
            if self.__dict__.has_key(key):
                raise self.ConstError,"constant reassignment error!"
            self.__dict__[key] = value

import sys

sys.modules[__name__] = _const() # 等价于 sys.modules['const'] = _const() 

