# This Python file uses the following encoding: utf-8
__author__ = 'perise'

import urllib2 as urllib
import string

class StockInfo:
    def __init__(self, StockCode):
        if(string.atoi(StockCode)>599999):
            self.StockCode = "sh"+StockCode
        elif(string.atoi(StockCode)>299999):
            self.StockCode = "sz"+StockCode
        else:
            self.StockCode = "sz"+StockCode
        return

    def getInfo(self):
        htmlUri = "http://hq.sinajs.cn/list="+str(self.StockCode)
        try:
            req = urllib.Request(htmlUri)
            page = urllib.urlopen(req)
            commentBytes = page.read()
            tempWebInfo =  commentBytes.decode("gbk").split("=")[1]
            tempWebInfo = tempWebInfo.replace('\"','')
            page.close()
        except:
            return None
        return tempWebInfo

if __name__ == '__main__':
    test = StockInfo(600151)
    test.getInfo()