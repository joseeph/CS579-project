from Framework.GraphDataNodeBase import GraphDataNodeBase
from xml.etree import ElementTree as ET

class ArxivAuthorNode(GraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__("ArxivAuthorNode")
        self.Author = ""
        self.PaperNameList = []
    
    def GetUniqueString(self):
        return "Author:" + self.Author
    

    def Serialize(self, parent_node :ET.Element):
        author_node = ET.Element("AuthorNode")
        parent_node.append(author_node)

        authorname_node = ET.Element("AuthorName")
        author_node.append(authorname_node)

        paperlist_node = ET.Element("PaperList")
        author_node.append(paperlist_node)

        for paper_name in self.PaperNameList:
            paper_node = ET.Element("Paper")
            paper_name.set("Name", paper_name)
            paperlist_node.append(paper_node)



    
    def Unserialize(self, node):
        # node :AuthorNode
        self.PaperNameList = []
        for child_node in node:
            if child_node.tag == "AuthorName":
                child_node.get()
