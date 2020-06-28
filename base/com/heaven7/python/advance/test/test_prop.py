# coding:UTF8

# 动态添加PYTHONPATH
# import sys
# sys.path.append('xxx/xxx/xx.py')  

#import Properties  # 这样导入会有问题 error
from Properties import *
import json

prop = Properties("test_prop.properties").getProperties()  
print prop  #map
print json.dumps(prop)  #map转json

fp = file('test_prop_json.txt', 'wt')
json.dump(prop, fp)
fp.close()

for key, value in prop.items():
    print "\"%s\":\"%s\"" % (key, value)

# out : {'a': {'c': 'v2', 'b': {'d': 'v1'}}, 'd': {'e': 'v3'}, 'f': 'v4'}  