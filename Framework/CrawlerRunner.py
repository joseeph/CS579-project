from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase
from Framework import UtilFuncs
from Framework.CrawlContext import CrawlContext
from Framework.NodeContainer import NodeContainer
from Framework.CrawlerBase import CrawlerBase
from Framework.CrawlerQueue import CrawlerQueue
from time import sleep
import os.path

from Framework.NodeFactoryBase import NodeFactoryBase
class CrawlerRunner:
    def __init__(self, CrawlerDriver : CrawlerDriverBase, save_path, data_container = None) -> None:
        # 最大节点数
        self.MaxNode = 500        
        self.SleepTime = 1
        self.SleepTimeWhenBlocked = 60 * 5
        # 爬虫队列
        self.Crawlers = CrawlerQueue()
        if data_container == None:
            self.DataContainer = NodeContainer()
        else:
            self.DataContainer = data_container
        self.Context = CrawlContext()
        self.Context.Init(self.DataContainer, CrawlerDriver, self.Crawlers)
        self.CrawlerDriver = CrawlerDriver
        self.SavePath = save_path
        self.SaveOnFinish = True
        self.SaveFrequency = 1000

    def SetSaveOnFinish(self, is_save):
        self.SaveOnFinish = is_save

    def SetSaveFrequency(self, frequency):
        self.SaveFrequency = frequency

    def LoadNodes(self):
        '''
        load the nodes from file
        '''
        if os.path.exists(self.SavePath):
            self.DataContainer = UtilFuncs.PickleRead(self.SavePath)
        

    def SetMaxNode(self, max_node):
        self.MaxNode = max_node

    def SetSleepTime(self, sleep_time):
        self.SleepTime = sleep_time

    def AddDataNodeCrawler(self, Crawler :CrawlerBase):
        '''
        add next crawler
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
        crawl_num = 0
        while self.MaxNode < 0 or self.DataContainer.GetNodeCount() < self.MaxNode:
            # crawl next data crawler to create a new data node
            
            # get next data crawler
            CurDataCrawler = self.GetNextNodeCrawler()
            if CurDataCrawler == None:
                # there is no more data crawlers
                return
            if CurDataCrawler.IsEnabled(self.Context):        
                self.DoCrawl(CurDataCrawler, self.Context, self.CrawlerDriver)                        
                crawl_num += 1
                self.CheckSaveBreakpoint(crawl_num, self.DataContainer, self.SavePath)
                sleep(self.SleepTime)

            # crawl all info crawlers to supply information of the existing data node
            info_crawlers = self.Crawlers.GetAllInfoCrawlers()
            cur_infocrawler :CrawlerBase
            for cur_infocrawler in info_crawlers:
                self.DoCrawl(cur_infocrawler, self.Context, self.CrawlerDriver)                
                crawl_num += 1
                self.CheckSaveBreakpoint(crawl_num, self.DataContainer, self.SavePath)
                sleep(self.SleepTime)
                

        # save
        if self.SaveOnFinish:
            UtilFuncs.PickleWrite(self.DataContainer, self.SavePath)
            
    def CheckSaveBreakpoint(self, crawl_num, obj, save_path):
        if crawl_num % self.SaveFrequency == 0:
            UtilFuncs.PickleWrite(obj, save_path)

            
    def DoCrawl(self, crawler :CrawlerBase, context, driver):
        while True:
            succ = crawler.Crawl(context, driver)
            if succ:
               # the crawler 
               return
            else:
                # sleep for a long time because of blocking
                print("The crawler is blocked，waits for " + str(self.SleepTimeWhenBlocked) + " seconds")
                sleep(self.SleepTimeWhenBlocked)