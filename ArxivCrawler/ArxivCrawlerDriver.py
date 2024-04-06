import arxiv
from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase


class ArxivCrawlerDriver(CrawlerDriverBase):
    def __init__(self) -> None:
        super().__init__()
        self.Client = arxiv.Client()
        self.MaxResult = 50

    def Get(self, op, qstr):
        
        if op == "query_papername":
            search = arxiv.Search(
                query = qstr,
                max_results = self.MaxResult,
                sort_by = arxiv.SortCriterion.SubmittedDate
            )
        elif op == "query_author":
            search = arxiv.Search(
                query = qstr,
                max_results = self.MaxResult,
                sort_by = arxiv.SortCriterion.SubmittedDate
            )
        elif op == "query_idlist":
            search = arxiv.Search(
                id_list=[qstr],
            )
        results = None
        try:
            if search != None: 
                results = self.Client.results(search)
        except Exception as e:
            print(e)
            
        return results
    
        