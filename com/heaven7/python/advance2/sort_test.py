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
# 按照 字典 d 的value降序排序
d2 = sorted(d.iteritems(), key = operator.itemgetter(1), 
                            reverse= True); # 降序排序
print d2    # 仍然是一个字典               
print d2[0][0]         
