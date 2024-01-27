
from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase

class CrawlerBase:
    def __init__(self) -> None:
        self.URL = ""
        pass

    def SetURL(self, url):
        self.URL = url

    def Crawl(self, context :'CrawlContext', crawler_driver :CrawlerDriverBase):
        # 网络端获取url的网页数据
        s = crawler_driver.Get(self.URL)
        # 交给派生类解析
        self.Parse(context, s)
        pass

    def Parse(self, context :'CrawlContext', s):
        pass