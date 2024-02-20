from xml.etree import ElementTree as ET


class ArxivAuthorRelationship:
    def __init__(self) -> None:
        self.AuthorName = ""
        self.CoauthorList = []
        pass

    def SetAuthorName(self, author_name):
        self.AuthorName = author_name

    def AddCoauthor(self, coauthor_name):
        self.CoauthorList.append(coauthor_name)

    def Serialize(self, parent_node :ET.Element):
        author_node = ET.Element("AuthorRelationshipNode")
        parent_node.append(author_node)

        authorname_node = ET.Element("AuthorName")
        authorname_node.set("value", self.AuthorName)
        author_node.append(authorname_node)

        coauthorlist_node = ET.Element("CoauthorList")
        author_node.append(coauthorlist_node)

        for coauthor_name in self.CoauthorList:
            coauthor_node = ET.Element("Coauthor")
            coauthor_node.set("Name", coauthor_name)
            coauthorlist_node.append(coauthor_node)
    
    def Unserialize(self, node):
        self.CoauthorList = []

        for child_node in node:
            if child_node.tag == 'AuthorName':
                self.AuthorName = child_node.get("value")
            elif child_node.tag == "CoauthorList":
                self.UnserializeCoauthorList(child_node)

    def UnserializeCoauthorList(self, parent_node):
        for child_node in parent_node:
            if child_node.tag == "Coauthor":
                coauthor_name = child_node.get("Name")
                self.CoauthorList.append(coauthor_name)


   