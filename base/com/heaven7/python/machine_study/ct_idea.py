# coding:utf-8

# 决策树伪代码
'''''
def createBranch():
    检测数据集中的每个子项是否属于同一分类
  if so return 类标签;
  else
            寻找划分数据集的最好特征.
            划分数据集 
            创建分支节点
         for 每个划分的子集
                              递归调用函数createBranch() 并增加返回结果到分支节点中             
      return 分支节点.                                  
'''
'''''
 数构造算法只适用标称型数据， 数值型数据必须离散化.
信息增益：
        在划分数据集之前之后信息发生的变化叫做信息增益.  

计算信息增益，集合信息的度量方式称为香农熵 (shang)--- idea from 信息论之父 -> 克劳德-香农        

基尼不纯度(Gini impurty): 从一个数据集中随机选取子项， 度量其被错误分类到其他分组里的概率
'''