# coding:utf-8

### 第4章. 朴素贝叶斯 -- > 基于概率论的分类方法   ###
"""
优点： 在数据较少的情况下，仍然有效，可处理多类别问题. (CA-ID3如果分类太多，会有问题)
缺点：对于输入数据的准备方式敏感.
适用数据类型： 标称型

实现一般有2种方式:
   1, 基于贝努利模型实现。 不考虑词在文档中出现的次数，只考虑初步出现。所以所有'假设词语' 权重都是相等的.
   2， 基于多项式实现 .   '假设词语' 权重都是不相等的.
   
贝叶斯准则：
    p(x|y) = p (y|x) * p(x)/ p(y)   
    
[从词向量计算概率】：--- 伪代码---
     计算每个类别中的文档数目.
    对每篇 训练文档：
          对每个类别 :
                  如果词条出现文档中 ->增加该词条的计数值.
                  增加所有词条的计数值
          对每个类别 :
                  对每个词条:
                           将该词条的数据除以总词条数目，得到条件概率.     
         返回每个类别的条件概率.                                      

"""
