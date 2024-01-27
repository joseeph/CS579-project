from Framework.CrawlContext import CrawlContext
from Framework.CrawlerBase import CrawlerBase


class WeiboCrawlerFollower(CrawlerBase):
    def __init__(self) -> None:
        super().__init__()

    def Parse(self, context :CrawlContext, s):
        pass