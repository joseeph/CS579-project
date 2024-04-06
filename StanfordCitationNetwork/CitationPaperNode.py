from Framework.GraphDataNodeBase import GraphDataNodeBase
from datetime import datetime

class CitationPaperNode(GraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__('CitationPaperNode')
        self.ID = ""
        self.Name = ""
        self.Dt = None
        self.ReferenceIDs = []
        self.AuthorNames = []

    def SetID(self, id):
        self.ID = id

    def GetUID(self):
        return self.ID
    
    def SetName(self, name):
        self.Name = name
    
    def SetDate(self, dt):
        self.Dt = dt
        
    def AddAuthor(self, author_name):
        self.AuthorNames.append(author_name)

    def AddReference(self, id):
        self.ReferenceIDs.append(id)