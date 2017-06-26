# coding:utf-8

# 使用决策树预测隐形眼镜类型

import CA 

### ===================== functions ===========================

def createGlassesTree(filename, debug =False):
    fr = open(filename);
    lences = [inst.strip().split('\t') for inst in fr.readlines()];
    lencesLabels = ['age','prescript','astigmatic','tearRate'];
    if(debug):
        print "lences = %s, lencesLabels = %s" % (lences, lencesLabels)
    # 等价于 for inst in fr.readline()  lences = [inst.strip().split('\t')] 
    lencesTree = CA.createTree(lences, lencesLabels, None);
    return lencesTree;


### ================ start test ==================
tree = createGlassesTree('lenses.txt', True); # txt文件有问题
print "tree = ", tree

CA.createPlot(tree);  #显示决策树
