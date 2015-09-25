# This Python file uses the following encoding: utf-8
__author__ = 'perise'

import urllib
import string

class StockInfo:
    def __init__(self, StockCode):
        if(int(StockCode)>599999):
            self.StockCode = "sh"+StockCode
        elif(int(StockCode)>299999):
            self.StockCode = "sz"+StockCode
        else:
            self.StockCode = "sz"+StockCode
        return

    def getInfo(self):
        htmlUri = "http://hq.sinajs.cn/list="+str(self.StockCode)
        print(htmlUri)
        try:
            page = urllib.request.urlopen(htmlUri)
            commentBytes = page.read()
            tempWebInfo =  commentBytes.decode("gbk").split("=")[1]
            tempWebInfo = tempWebInfo.replace('\"','')
            page.close()
        except:
            print("Error in get stock info from web")
            return None
        return tempWebInfo

if __name__ == '__main__':
    test = StockInfo(600151)
    test.getInfo()