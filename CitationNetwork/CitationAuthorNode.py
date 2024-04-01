from Framework.GraphDataNodeBase import GraphDataNodeBase


class CitationAuthorNode(GraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__('CitationAuthorNode')
        self.ID = 0

    def SetAuthorID(self, id):
        self.ID = id


        
    