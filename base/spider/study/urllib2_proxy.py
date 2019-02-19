# -*- coding: utf-8 -*-
# author:root
# dateTime:19-2-19
import urllib2

proxyswitch=True

httpproxy_handler=urllib2.ProxyHandler({"http":"114.249.116.88:9000"})
nullproxy_handler=urllib2.ProxyHandler({})

if proxyswitch:
    opener=urllib2.build_opener(httpproxy_handler)
else:
    opener=urllib2.build_opener(nullproxy_handler)

urllib2.install_opener(opener)

ua_headers={
    "User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}

request=urllib2.Request("http://www.baidu.com",headers=ua_headers)
# response=urllib2.urlopen(request)
response=opener.open(request)
print response.read().decode("utf-8")