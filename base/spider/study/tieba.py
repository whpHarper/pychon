# -*- coding: utf-8 -*-
# author:root
# dateTime:19-2-18
import urllib2
import urllib

def loadPage(url,page):
    """
    下载网页
    :param url:
    :return:
    """
    print "正在下载第"+str(page)+"页"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    writePage(response.read(),"第"+str(page)+"页.html")
    #print response.read()

def writePage(html,filename):
    """
    写入文件
    :param html:
    :return:
    """
    print "正在保存"+filename
    with open(filename,"w") as f:
        f.write(html)
def teibaSpider(url,beginPage,endPage):
    """
    爬取贴吧网页
    :return:
    """
    for page in range(beginPage,endPage+1):
        pn=(page-1)*50
        fullurl=url+"&pn="+str(pn)
        print fullurl
        loadPage(fullurl,page)


if __name__=="__main__":
    kw=raw_input("请输入贴吧名:")
    beginPage=int(raw_input("请输入起始页:"))
    endPage=int(raw_input("请输入终止页:"))
    url="http://tieba.baidu.com/f?"
    key=urllib.urlencode({"kw":kw})

    fullurl=url+key
    teibaSpider(fullurl,beginPage,endPage)
