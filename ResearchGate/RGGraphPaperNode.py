from ResearchGate.RGGraphDataNodeBase import RGGraphDataNodeBase

class RGGraphPaperNode(RGGraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__()
        self.DOI = ""
        pass

    def Init(self, doi):
        self.DOI = doi


    def GetDOI(self):
        return self.DOI