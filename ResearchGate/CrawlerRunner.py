from Crawlers.CrawlerBase import CrawlerBase
from ResearchGate.RGNodeContainer import RGNodeContainer
class CrawlerRunner:
    def __init__(self) -> None:
        # 最大节点数
        self.MaxNode = 500        
        # 爬虫队列
        self.CrawlerQueue = []
        self.NodeContainer = RGNodeContainer()
        pass


    def BeginCrawl(self, crawler :CrawlerBase, begin_url):
        while self.NodeContainer.GetNodeCount() < self.MaxNode:
            content = crawler.Get(begin_url)
            
