from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase
from Framework.CrawlContext import CrawlContext
from Framework.NodeContainer import NodeContainer
from Framework.CrawlerBase import CrawlerBase
from Framework.CrawlerQueue import CrawlerQueue
from time import sleep
class CrawlerRunner:
    def __init__(self, CrawlerDriver : CrawlerDriverBase) -> None:
        # 最大节点数
        self.MaxNode = 500        
        self.SleepTime = 1
        # 爬虫队列
        self.Crawlers = CrawlerQueue()
        self.NodeContainer = NodeContainer()
        self.Context = CrawlContext()
        self.Context.Init(self.NodeContainer, CrawlerDriver, self.Crawlers)
        self.CrawlerDriver = CrawlerDriver
    
    def SetMaxNode(self, max_node):
        self.MaxNode = max_node

    def SetSleepTime(self, sleep_time):
        self.SleepTime = sleep_time

    def AddDataCrawler(self, Crawler :CrawlerBase):
        '''
        添加下一个爬虫
        '''
        self.Crawlers.AddDataCrawler(Crawler)
    


    def GetNextDataCrawler(self)->CrawlerBase:
        '''
        get next queued crawler
        '''
        if self.Crawlers.IsDataCrawlerEmpty():
            return None
        
        # get next queued crawler
        CurCrawler = self.Crawlers.NextDataCrawler()
        return CurCrawler
    

    def BeginCrawl(self):
        while self.NodeContainer.GetNodeCount() < self.MaxNode:
            # crawl next data crawler to create a new data node
            
            # get next data crawler
            CurDataCrawler = self.GetNextDataCrawler()
            if CurDataCrawler == None:
                # there is no more data crawlers
                return
            if CurDataCrawler.IsEnabled(self.Context):                
                CurDataCrawler.Crawl(self.Context, self.CrawlerDriver )
                sleep(self.SleepTime)

            # crawl all info crawlers to supply information of the existing data node
            info_crawlers = self.Crawlers.GetAllInfoCrawlers()
            cur_infocrawler :CrawlerBase
            for cur_infocrawler in info_crawlers:
                cur_infocrawler.Crawl(self.Context, self.CrawlerDriver)
                sleep(self.SleepTime)
            
            
