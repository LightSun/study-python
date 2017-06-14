# coding:UTF8

import json
print json.__file__  # E:\study\python\lib\json\__init__.pyc

data = '{"spam" : "foo", "parrot" : 42}'
in_json = json.dumps(data)  # Encode the data
print in_json

obj = json.loads(in_json)  # Decode into a Python object
json.JSONDecoder
print obj
print json.dumps(data,
                  sort_keys=True,
                   indent=4,
                   separators=(',', ': '),
                   encoding="gbk",
                    ensure_ascii=True)
"""
Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，
                     设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key

ensure_ascii：默认值True，如果dict内含有non-ASCII的字符，则会类似\uXXXX的显示数据，设置成False后，就能正常显示

indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty-printed json

separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(',',':')；
                         这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。

encoding：默认是UTF-8，设置json数据的编码方式。

sort_keys：将数据根据keys的值进行排序。

 Decode过程，是把json对象转换成python对象的一个过程，常用的两个函数是loads和load函数。区别跟dump和dumps是一样的。
"""
