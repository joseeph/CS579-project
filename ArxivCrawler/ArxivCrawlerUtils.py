class ArxivCrawlerUtils:
    @staticmethod
    def GetAuthorUID(author_name):
        return "Author:" + author_name
    
    @staticmethod
    def GetPaperUID(paper_name):
        return "Paper:" + paper_name

    @staticmethod
    def EntryID2SearchID(entry_id):
        # entry_id: http://arxiv.org/abs/0000.00000v0
        pos = entry_id.find("abs/") + len("abs/")
        search_id = entry_id[pos:]
        return search_id
        