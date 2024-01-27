
class CrawlContext:
    def __init__(self) -> None:
        self.DataContainer = None
        self.CrawlerDriver = None
        self.CrawlerQueue = []
        pass

    def Init(self, container : 'NodeContainer', crawler_driver : 'CrawlerDriverBase', crawler_queue):
        self.DataContainer = container
        self.CrawlerDriver = crawler_driver
        self.CrawlerQueue = crawler_queue

    def AddCrawler(self, crawler :'CrawlerBase'):
        '''
        add a crawler at the end of the q
        '''
        self.CrawlerQueue.append(crawler)