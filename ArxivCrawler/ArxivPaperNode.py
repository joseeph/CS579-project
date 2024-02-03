from Framework.GraphDataNodeBase import GraphDataNodeBase
from xml.etree import ElementTree as ET
from ArxivCrawler.ArxivCrawlerUtils import ArxivCrawlerUtils

class ArxivPaperNode(GraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__("ArxivPaperNode")
        self.PaperName = ""
        self.AuthorList = []
    
    def SetPaperName(self, paper_name):
        self.PaperName = paper_name

    def AddAuthor(self, author_name):
        self.AuthorList.append(author_name)

    def GetUniqueString(self):
        return ArxivCrawlerUtils.GetPaperUID(self.PaperName)

    def Serialize(self, parent_node :ET.Element):
        paper_node = ET.Element("ArxivPaperNode")
        parent_node.append(paper_node)

        name_node= ET.Element("PaperName")
        name_node.set("value", self.PaperName)
        paper_node.append(name_node)

        authorlist_node =ET.Element("AuthorList")
        paper_node.append(authorlist_node)
        for author_name in self.AuthorList:
            author_node = ET.Element("Author")
            author_node.set("Name", author_name)
            authorlist_node.append(author_node)


    
    def Unserialize(self, node):
        self.AuthorList = []
        # node :PaperNode
        child_node :ET.Element
        for child_node in node:
            if child_node.tag == "PaperName":
                self.PaperName = child_node.get("value")
            elif child_node.tag == "AuthorList":
                self.UnserializeAuthorList(child_node)

    def UnserializeAuthorList(self, authorlist_node :ET.Element):
        for child_node in authorlist_node:
            if child_node.tag == "Author":
                author = child_node.get("Name")
                self.AuthorList.append(author)