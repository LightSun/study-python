# coding:utf-8

# 测试手写输入

from numpy import *
import operator
import handwriting_lib as hw
from os import listdir


testVector = hw.img2Vector("testDigits/0_13.txt");
print testVector[0, 0:31]
print testVector[0,32:63]


print "============== start >>> 使用K-近邻算法  ->识别手写数字 ============"

# 手写测试
def handwritingClassTest(k=3):
    hwLabels = []; #分类的标签
    trainingFileList = listdir('trainingDigits'); # 遍历目录
    m = len(trainingFileList);
    
    trainingMat = zeros((m,1024)); # 创建2维矩阵, 每行存放一个 文件代表的图像
    for i in range(m):
        fileNameStr = trainingFileList[i];
        fileStr = fileNameStr.split('.')[0];
        classNumStr = int(fileStr.split('_')[0]); # eg: '0_13.txt' 得到分类‘0’
        hwLabels.append(classNumStr);
        trainingMat[i, :] = hw.img2Vector("trainingDigits/%s" % fileNameStr);
        
    testFileList = listdir('testDigits');
    mTest = len(testFileList);  
      
    errorCount = 0.0
    for i in range(mTest):
        fileNameStr = testFileList[i];
        fileStr = fileNameStr.split('.')[0];
        classNumStr = int(fileStr.split('_')[0]);
        vectorUnderTest = hw.img2Vector('testDigits/%s' % fileNameStr);
        
        classifierResult = hw.classify0(vectorUnderTest, trainingMat, hwLabels, k);
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if(classifierResult != classNumStr):
            errorCount += 1.0
            
    print "\n the total number of errors is: %d " % errorCount     
    print "\n the total error rate is: %f " % (errorCount / float(mTest))  
    
handwritingClassTest(); # 错误率 0.011628 

       