import arxiv
from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase


class ArxivCrawlerDriver(CrawlerDriverBase):
    def __init__(self) -> None:
        super().__init__()
        self.Client = arxiv.Client()

    def Get(self, qstr):
        search = arxiv.Search(
            query = qstr,
            max_results = 10,
            sort_by = arxiv.SortCriterion.SubmittedDate
        )
        results = self.Client.results(search)
        return results
    
        