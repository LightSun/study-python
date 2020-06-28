# coding:utf-8
import operator

# 排序默认都是升序

a = [5, 2, 3, 1, 4]
a.sort(reverse=True)
print a  # 降序

a = [5, 2, 3, 1, 4]
print sorted(a);  # 原 list不变
print sorted(a, reverse=True);


d = {
 'Adam': 95,
 'Lisa': 38,
 'Bart': 59
 }
# 按照 字典 d 的value 降序排序
d2 = sorted(d.iteritems(), key = operator.itemgetter(1), 
                            reverse= True); # 降序排序
print d2          # 包含d字典key-value的list.            
print d2[0][0]    # 相当于取第 0个元素的 key     

# 按照 字典d 的key 降序排序
d2 = sorted(d.iteritems(), key = operator.itemgetter(0), 
                            reverse= True); # 降序排序
print d2

