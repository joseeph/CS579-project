from Framework.CrawlContext import CrawlContext
from Framework.NodeCrawlerBase import NodeCrawlerBase


class ArxivPaperCrawler(NodeCrawlerBase):
    def __init__(self, paper_name) -> None:
        super().__init__()
        self.PaperName = paper_name
        self.SetURL("ti:" + '"' + self.PaperName + '"')

    def Parse(self, context: CrawlContext, result):
        if len(result) == 0:
            return True
        paper_info = result[0]
        paper_authors = paper_info.authors
