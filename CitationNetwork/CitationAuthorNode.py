from Framework.GraphDataNodeBase import GraphDataNodeBase
import StanfordCitationNetwork.CitationUtils as CitationUtils
from xml.etree import ElementTree as ET


class CitationAuthorNode(GraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__("CitationAuthorNode")
        self.AuthorName = ""
        self.ID = 0
        self.Organization = ""
        
    def SetAuthorName(self, name):
        self.AuthorName = name
    
    def SetAuthorID(self, id):
        self.ID = id

    def SetOrganization(self, org):
        self.Organization = org

    def GetUID(self):
        return CitationUtils.BuildCitationAuthorNodeUID(self.ID)

    def Serialize(self, parent_node :ET.Element):
        author_node = ET.Element("CitationAuthorNode")
        parent_node.append(author_node)
        author_node.set("ID", str(self.ID))
        author_node.set("Name", self.AuthorName)
        author_node.set("Org", self.Organization)
    
    def Unserialize(self, node :ET.Element):
        # node: CitationAuthorNode
        self.ID = node.get("ID")
        self.ID = int(self.ID)
        self.AuthorName = node.get("Name")
        self.Organization = node.get("Org")