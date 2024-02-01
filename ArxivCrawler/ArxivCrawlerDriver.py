import requests
from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase


class ArxivCrawlerDriver(CrawlerDriverBase):
    def __init__(self) -> None:
        super().__init__()

    def Get(self, url):
        s = requests.get(url).content
        return s