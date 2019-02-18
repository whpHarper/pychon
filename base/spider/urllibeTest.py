import random
import urllib2
import urllib

ua_list=[
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)"
]

user_agent=random.choice(ua_list)

ua_headers={
    "User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
url="http://www.baidu.com"
#request=urllib2.Request("http://www.baidu.com",headers=ua_headers)
request=urllib2.Request(url)
request.add_header("User-Agent",user_agent)

print request.get_header("User-agent")

response=urllib2.urlopen(request)
html=response.read()

print response.getcode()
print response.geturl()
print response.info()