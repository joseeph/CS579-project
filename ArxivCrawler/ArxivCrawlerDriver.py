import arxiv
from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase


class ArxivCrawlerDriver(CrawlerDriverBase):
    def __init__(self) -> None:
        super().__init__()
        self.Client = arxiv.Client()
        self.MaxResult = 50

    def Get(self, op, qstr):
        results = None
        if op == "query_papername":
            search = arxiv.Search(
                query = qstr,
                max_results = 50,
                sort_by = arxiv.SortCriterion.SubmittedDate
            )
            results = self.Client.results(search)
        elif op == "query_author":
            search = arxiv.Search(
                query = qstr,
                max_results = 5,
                sort_by = arxiv.SortCriterion.SubmittedDate
            )
            results = self.Client.results(search)
        elif op == "query_idlist":
            search = arxiv.Search(
                id_list=[qstr],
            )
            results = self.Client.results(search)
        return results
    
        