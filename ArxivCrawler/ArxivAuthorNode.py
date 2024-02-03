from Framework.GraphDataNodeBase import GraphDataNodeBase
from xml.etree import ElementTree as ET
from ArxivCrawler.ArxivCrawlerUtils import ArxivCrawlerUtils

class ArxivAuthorNode(GraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__("ArxivAuthorNode")
        self.Author = ""
        self.PaperNameList = []
    
    def GetUniqueString(self):
        return ArxivCrawlerUtils.GetAuthorUID(self.Author)
    
    def SetAuthor(self, author):
        self.Author = author
    
    def AddPaper(self, paper):
        self.PaperNameList.append(paper)

    def Serialize(self, parent_node :ET.Element):
        author_node = ET.Element("ArxivAuthorNode")
        parent_node.append(author_node)

        authorname_node = ET.Element("AuthorName")
        authorname_node.set("value", self.Author)
        author_node.append(authorname_node)

        paperlist_node = ET.Element("PaperList")
        author_node.append(paperlist_node)

        for paper_name in self.PaperNameList:
            paper_node = ET.Element("Paper")
            paper_node.set("Name", paper_name)
            paperlist_node.append(paper_node)



    
    def Unserialize(self, node):
        # node :AuthorNode
        self.PaperNameList = []
        for child_node in node:
            if child_node.tag == "AuthorName":
                self.Author = child_node.get("value")
            elif child_node.tag == "PaperList":
                self.UnserializePaperList(child_node)
    
    def UnserializePaperList(self, parent_node):
        for child_node in parent_node:
            if child_node.tag == "Paper":
                paper_name = child_node.get("Name")
                self.PaperNameList.append(paper_name)
