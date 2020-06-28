# coding:UTF8

import pickle
data = {'k1', 123, 'k2', "hello"}

# 转化为只有python识别的字符串
p_str = pickle.dumps(data, None) # 第2个参数是数字
print p_str