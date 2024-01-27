from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase
from Framework.CrawlContext import CrawlContext
from Framework.NodeContainer import NodeContainer
from Framework.CrawlerBase import CrawlerBase
from time import sleep
class CrawlerRunner:
    def __init__(self,  CrawlerDriver : CrawlerDriverBase) -> None:
        # 最大节点数
        self.MaxNode = 500        
        self.SleepTime = 1
        # 爬虫队列
        self.CrawlerQueue = []
        self.NodeContainer = NodeContainer()
        self.Context = CrawlContext()
        self.Context.Init(self.NodeContainer, CrawlerDriver, self.CrawlerQueue)
        self.CrawlerDriver = CrawlerDriver
        
    def SetSleepTime(self, sleep_time):
        self.SleepTime = sleep_time

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
            self.Context.CrawlerQueue = self.CrawlerQueue
            CurCrawler.Crawl(self.Context, self.CrawlerDriver )
            sleep(self.SleepTime)
            
            
