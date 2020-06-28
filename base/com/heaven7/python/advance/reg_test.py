# coding:utf-8

# 正则表达式

def textParse(bigString):    #input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString) #除字母，数字外的任意字符串。
    return [tok.lower() for tok in listOfTokens if len(tok) > 2] # 去掉字符长度不满足需求的


print textParse("haha, i am the best !");