from Framework.GraphDataNodeBase import GraphDataNodeBase


class CitationPaperNode(GraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__('CitationPaperNode')
        self.ID = -1
        self.PaperName = ""
        self.Year = -1
        self.AuthorIDs = []

    def SetID(self, id):
        self.ID = id

    def SetPaperName(self, paper_name):
        self.PaperName = paper_name

    def SetYear(self, year):
        self.Year = year

    def AddAuthor(self, author_id):
        self.AuthorIDs.append(author_id)

    



    