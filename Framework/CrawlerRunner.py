from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase
from Framework.CrawlContext import CrawlContext
from Framework.NodeContainer import NodeContainer
from Framework.CrawlerBase import CrawlerBase
class CrawlerRunner:
    def __init__(self) -> None:
        # 最大节点数
        self.MaxNode = 500        
        # 爬虫队列
        self.CrawlerQueue = []
        self.NodeContainer = NodeContainer()
        self.Context = CrawlContext()
        self.Context.Init(self.NodeContainer)
        self.CrawlerDriver = None
        pass

    def SetCrawlerDriver(self, CrawlerDriver : CrawlerDriverBase):
        self.CrawlerDriver = CrawlerDriver

    def AddCrawler(self, Crawler :CrawlerBase):
        '''
        添加下一个爬虫
        '''
        self.CrawlerQueue.append(Crawler)
        pass

    def GetNextCrawler(self)->CrawlerBase:
        '''
        获取下一个爬虫
        '''
        if len(self.CrawlerQueue) == 0 :
            return None
        # 取出第一个爬虫
        CurCrawler = self.CrawlerQueue[0]
        self.CrawlerQueue = self.CrawlerQueue[1:]
        return CurCrawler
    
    def HasNextCrawler(self)->bool:
        return len(self.CrawlerQueue) > 0

    def BeginCrawl(self):
        while self.NodeContainer.GetNodeCount() < self.MaxNode:
            # 是否还有爬虫
            if self.HasNextCrawler() == False:
                return
            
            # 获得下一个爬虫
            CurCrawler = self.GetNextCrawler()
            CurCrawler.Crawl(self.Context, self.CrawlerDriver )
            
