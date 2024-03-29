
from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase

class CrawlerBase:
    def __init__(self) -> None:
        self.URL = ""
        self.OP = ""
        pass

    def SetOp(self, op):
        self.OP = op
    def SetURL(self, url):
        self.URL = url

    def IsEnabled(self, context :'CrawlContext'):
        '''
        this crawler can be disabled
        '''
        return True

    def Crawl(self, context :'CrawlContext', crawler_driver :CrawlerDriverBase):
        # 网络端获取url的网页数据
        s = crawler_driver.Get(self.OP, self.URL)
        if s == b'':
            return False
        # 交给派生类解析
        succ = self.Parse(context, s)
        return succ
        

    def Parse(self, context :'CrawlContext', s):
        pass