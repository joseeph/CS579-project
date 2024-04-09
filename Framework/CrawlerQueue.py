from Framework.InfoCrawlerBase import InfoCrawlerBase
from Framework.NodeCrawlerBase import NodeCrawlerBase


class CrawlerQueue:
    def __init__(self) -> None:
        self.NodeCrawlers = []
        self.InfoCrawlers = []
        pass

    def AddNodeCrawler(self ,crawler :NodeCrawlerBase, is_append):
        if is_append:
            self.NodeCrawlers.append(crawler)
        else:
            self.NodeCrawlers.insert(0, crawler)

    def AddInfoCrawler(self, crawler :InfoCrawlerBase):
        self.InfoCrawlers.append(crawler)

    def IsNodeCrawlerEmpty(self):
        return len(self.NodeCrawlers) == 0
    
    
    def NextNodeCrawler(self):
        if len(self.NodeCrawlers) == 0:
            return None
        crawler = self.NodeCrawlers.pop(0)
        return crawler
    
    def GetAllInfoCrawlers(self):
        InfoCrawlers = self.InfoCrawlers
        self.InfoCrawlers = []
        return InfoCrawlers