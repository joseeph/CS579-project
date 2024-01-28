class CrawlerQueue:
    def __init__(self) -> None:
        self.DataCrawlers = []
        self.InfoCrawlers = []
        pass

    def AddDataCrawler(self ,crawler):
        self.DataCrawlers.append(crawler)

    def AddInfoCrawler(self, crawler):
        self.InfoCrawlers.append(crawler)

    def IsDataCrawlerEmpty(self):
        return len(self.DataCrawlers) == 0
    
    
    def NextDataCrawler(self):
        if len(self.DataCrawlers) == 0:
            return None
        crawler = self.DataCrawlers.pop(0)
        return crawler
    
    def GetAllInfoCrawlers(self):
        InfoCrawlers = self.InfoCrawlers
        self.InfoCrawlers = []
        return InfoCrawlers