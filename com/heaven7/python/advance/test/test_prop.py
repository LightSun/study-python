# coding:UTF8

# 动态添加PYTHONPATH
# import sys
# sys.path.append('xxx/xxx/xx.py')  

#import Properties  # 这样导入会有问题 error
from Properties import *

prop = Properties("test_prop.properties").getProperties()  
print prop  

# out : {'a': {'c': 'v2', 'b': {'d': 'v1'}}, 'd': {'e': 'v3'}, 'f': 'v4'}  