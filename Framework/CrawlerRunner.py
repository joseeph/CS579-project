from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase
from Framework.CrawlContext import CrawlContext
from Framework.NodeContainer import NodeContainer
from Framework.CrawlerBase import CrawlerBase
from Framework.CrawlerQueue import CrawlerQueue
from time import sleep
import os.path

from Framework.NodeFactoryBase import NodeFactoryBase
class CrawlerRunner:
    def __init__(self, CrawlerDriver : CrawlerDriverBase, save_path) -> None:
        # 最大节点数
        self.MaxNode = 500        
        self.SleepTime = 1
        self.SleepTimeWhenBlocked = 60 * 5
        # 爬虫队列
        self.Crawlers = CrawlerQueue()
        self.NodeContainer = NodeContainer()
        self.Context = CrawlContext()
        self.Context.Init(self.NodeContainer, CrawlerDriver, self.Crawlers)
        self.CrawlerDriver = CrawlerDriver
        self.SavePath = save_path


    def LoadNodes(self, node_factory :NodeFactoryBase):
        '''
        load the nodes from file
        '''
        if os.path.exists(self.SavePath):
            self.NodeContainer.Load(self.SavePath, node_factory)

    def SetMaxNode(self, max_node):
        self.MaxNode = max_node

    def SetSleepTime(self, sleep_time):
        self.SleepTime = sleep_time

    def AddDataCrawler(self, Crawler :CrawlerBase):
        '''
        添加下一个爬虫
        '''
        self.Crawlers.AddNodeCrawler(Crawler)
    


    def GetNextNodeCrawler(self)->CrawlerBase:
        '''
        get next queued crawler
        '''
        if self.Crawlers.IsNodeCrawlerEmpty():
            return None
        
        # get next queued crawler
        CurCrawler = self.Crawlers.NextNodeCrawler()
        return CurCrawler
    

    def BeginCrawl(self):
        while self.NodeContainer.GetNodeCount() < self.MaxNode:
            # crawl next data crawler to create a new data node
            
            # get next data crawler
            CurDataCrawler = self.GetNextNodeCrawler()
            if CurDataCrawler == None:
                # there is no more data crawlers
                return
            if CurDataCrawler.IsEnabled(self.Context):        
                self.DoCrawl(CurDataCrawler, self.Context, self.CrawlerDriver)                        
                sleep(self.SleepTime)

            # crawl all info crawlers to supply information of the existing data node
            info_crawlers = self.Crawlers.GetAllInfoCrawlers()
            cur_infocrawler :CrawlerBase
            for cur_infocrawler in info_crawlers:
                self.DoCrawl(cur_infocrawler, self.Context, self.CrawlerDriver)                
                sleep(self.SleepTime)

            # save
            self.NodeContainer.Save(self.SavePath)
            
    def DoCrawl(self, crawler :CrawlerBase, context, driver):
        while True:
            succ = crawler.Crawl(context, driver)
            if succ:
               # the crawler 
               return
            else:
                # sleep for a long time because of blocking
                print("爬虫被临时封禁，等待" + str(self.SleepTimeWhenBlocked) + "秒")
                sleep(self.SleepTimeWhenBlocked)