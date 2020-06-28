# coding:UTF8

import urllib,urllib2

url = "http://www.example.com"
body_value = {"package": "com.tencent.lian","version_code": "66" }
body_value  = urllib.urlencode(body_value)
request = urllib2.Request(url, body_value)
# request.add_header(keys, headers[keys])
result = urllib2.urlopen(request ).read()