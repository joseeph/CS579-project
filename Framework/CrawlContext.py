
class CrawlContext:
    def __init__(self) -> None:
        self.DataContainer = None
        self.CrawlerDriver = None
        self.Crawlers = []        
        pass

    def Init(self, container : 'NodeContainer', crawler_driver : 'CrawlerDriverBase', crawler_queue :'Framework.CrawlerQueue.CrawlerQueue'):
        self.DataContainer = container
        self.CrawlerDriver = crawler_driver
        self.Crawlers = crawler_queue
        

    def AddDataCrawler(self, crawler :'CrawlerBase', is_append = True):
        '''
        add a crawler at the end of the q
        '''
        self.Crawlers.AddNodeCrawler(crawler, is_append)

    def AddInfoCrawler(self, crawler :'CrawlerBase'):
        self.Crawlers.AddInfoCrawler(crawler)