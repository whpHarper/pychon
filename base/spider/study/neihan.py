# -*- coding: utf-8 -*-
# author:root
# dateTime:19-2-19

import urllib2
import re



class Spider_test:
    def __init__(self):
        self.page=1
        self.switch=True

    def loadPage(self):
        """
        下载page页面
        :return:
        """
        print "正在下载数据……"
        url="http://www.neihan8.com/article/list_5_" + str(self.page) + ".html"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        html=response.read()
        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)
        content_list=pattern.findall(html)
        self.dealPage(content_list)

    def dealPage(self,content_list):
        """
        解析元素
        :param content_list:
        :return:
        """
        for item in content_list:
            item=item.replace("<p>","").replace("<br>","")
            self.writPage(item)

    def writPage(self,item):
        """
        写入文件
        :param item:
        :return:
        """
        print("正在写入数据……")
        with open("duanzi.txt","a") as f:
            f.write(item)

    def startWork(self):
        """
        控制爬虫运行
        :return:
        """
        while self.switch:
            self.loadPage()
            command=raw_input("如果继续爬取，请按回车键（退出输入quit）：")
            if command=="quit":
                self.switch=False
            self.page+=1
        print "谢谢使用！"


if __name__ =="__main__":
    duanziSpider=Spider_test()
    duanziSpider.startWork()
