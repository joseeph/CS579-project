class ArxivCrawlerUtils:
    @staticmethod
    def GetAuthorUID(author_name):
        return "Author:" + author_name
    
    @staticmethod
    def GetPaperUID(paper_name):
        return "Paper:" + paper_name
