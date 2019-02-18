# -*- coding: utf-8 -*-
import urllib
import urllib2

url="http://www.baidu.com/s"
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
keyword=raw_input("请输入要搜索内容：")
wd={"wd":keyword}
wd=urllib.urlencode(wd)
fullurl=url+"?"+wd

request=urllib2.Request(fullurl,headers=headers)
response=urllib2.urlopen(request)

print(response.read())
