from ResearchGate.RGGraphDataNodeBase import RGGraphDataNodeBase

class RGGraphPersonNode(RGGraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__()
        self.AuthorType = ""
        self.AuthorName = ""
        self.URL = ""
        pass

    def Init(self, author_type, author_name, url):
        self.AuthorType = author_type
        self.AuthorName = author_name
        self.URL = url


    def GetURL(self):
        return self.URL