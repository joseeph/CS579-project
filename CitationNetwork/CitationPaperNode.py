from Framework.GraphDataNodeBase import GraphDataNodeBase
import CitationNetwork.CitationUtils as CitationUtils
from xml.etree import ElementTree as ET


class CitationPaperNode(GraphDataNodeBase):
    def __init__(self) -> None:
        super().__init__('CitationPaperNode')
        self.ID = -1
        self.PaperName = ""
        self.Year = -1
        self.AuthorIDs = []
        self.RefIDs = []
        self.DOI = ""
        self.DocType = ""
        self.CitationNum = 0

    def SetID(self, id):
        self.ID = int(id)

    def SetPaperName(self, paper_name):
        self.PaperName = paper_name

    def SetYear(self, year):
        self.Year = int(year)

    def AddAuthor(self, author_id):
        self.AuthorIDs.append(int(author_id))

    def AddReference(self, ref_id):
        self.RefIDs.append(int(ref_id))
    
    def SetDOI(self, doi):
        self.DOI = doi

    def SetDocType(self, doc_type):
        self.DocType = doc_type

    def SetCitationNum(self, citation_num):
        self.CitationNum = int(citation_num)

    def GetUniqueString(self):
        return CitationUtils.BuildCitationPaperUID(self.ID)

    def Serialize(self, parent_node):
        paper_node = ET.Element("CitationPaperNode")
        parent_node.append(paper_node)
        paper_node.set("ID", str(self.ID))
        paper_node.set("Name", self.PaperName)
        paper_node.set("Year", str(self.Year))
        paper_node.set("DOI", self.DOI)
        paper_node.set("DocType", self.DocType)
        paper_node.set("CitationNum", str(self.CitationNum))
        # the authors node
        authors_node = ET.Element("Authors")
        paper_node.append(authors_node)
        # every author
        for author_id in self.AuthorIDs:
            author_node = ET.Element("Author")
            author_node.set("ID", str(author_id))
            authors_node.append(author_node)

        # the reference node
        references_node = ET.Element("References")
        paper_node.append(references_node)

        for ref_id in self.RefIDs:
            ref_node =  ET.Element("Ref")
            ref_node.set("ID", str(ref_id))
            references_node.append(ref_node)

    
    def Unserialize(self, node :ET.Element):
        # node: CitationPaperNode
        self.ID = node.get("ID")
        self.ID = int(self.ID)
        self.PaperName = node.get("Name")
        self.Year = node.get("Year")
        self.Year = int(self.Year)
        self.DOI = node.get("DOI")
        self.DocType = node.get("DocType")
        self.CitationNum = node.get("CitationNum")
        self.CitationNum = int(self.CitationNum)
        for child_node in node:
            if child_node.tag == "Authors":
                self.UnserializeAuthors(child_node)
            elif child_node.tag == "References":
                self.UnserializeReferences(child_node)
    
    def UnserializeAuthors(self, authors_node :ET.Element):
        author_node :ET.Element
        for author_node in authors_node:
            author_id = author_node.get("ID")
            self.AuthorIDs.append(author_id)
        

    def UnserializeReferences(self, references_node :ET.Element):
        ref_node :ET.Element
        for ref_node in references_node:
            author_id = ref_node.get("ID")
            self.RefIDs.append(author_id)
        