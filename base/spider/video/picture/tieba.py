# -*- coding: utf-8 -*-
# author:root
# dateTime:19-2-19
import urllib
import urllib2
from lxml import etree

def loadPage(url):
    """
    作用：根据url发送请求，获取服务器响应文件
    :param url: url地址
    :return:
    """
    requst=urllib2.Request(url)
    response=urllib2.urlopen(requst)
    html=response.read()

    #解析html为HTML DOM模型
    content=etree.HTML(html)
    link_list=content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@herf')

    for link in link_list:
        fulllink="http://tieba.baidu.com"+link
        loadImage(fulllink)

def loadImage(link):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    request=urllib2.Request(link,headers=headers)
    html=urllib2.urlopen(request).read()

    content=etree.HTML(html)
    # link_list=content.xpath('//img[@class="BDE_Image"]/@src')
    link_list=content.xpath('//div[@class="post_bubble_middle"]')
    for link in link_list:
        print link


def writeImage(link):
    """
    保存图片到本地
    :param link:
    :return:
    """
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    request=urllib2.Request(link,headers=headers)
    image=urllib2.urlopen(request).read()
    filename=link[-10:]

    with open(filename,"wb") as f:
        f.write(image)
    print "已经成功下载"+filename


def teibaSpider(url,beginPage,endPage):
    """
    作用：贴吧爬虫调度器，组合处理每隔页面的url
    :param url:
    :param beginPage:
    :param endPage:
    :return:
    """
    for page in range(beginPage,endPage+1):
        pn=(page-1)*50
        fullurl=url+"&pn="+str(pn)
        loadPage(fullurl)

    print "谢谢使用！"

if __name__ =="__main__":
    kw=raw_input("请输入要爬取的贴吧名：")
    beginPage=int(raw_input("请输入起始页码："))
    endpage=int(raw_input("请输入终止页："))

    url="http://tieba.baidu.com/f?"
    key=urllib.urlencode({"kw":kw})
    fullurl=url+key
