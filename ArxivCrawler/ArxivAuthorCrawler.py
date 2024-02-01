from Framework.CrawlContext import CrawlContext
from Framework.NodeCrawlerBase import NodeCrawlerBase


class ArxivAuthorCrawler(NodeCrawlerBase):
    def __init__(self, author_name) -> None:
        super().__init__()
        self.AuthorName = author_name
        self.SetURL("au:" + '"' + self.AuthorName + '"')

    def Parse(self, context: CrawlContext, result):
        # 列出该author下的paper
        papers = []
        for paper in result:
            papers.append(paper.title)

        # 构造数据        

