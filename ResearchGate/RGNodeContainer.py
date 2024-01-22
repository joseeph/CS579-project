from ResearchGate.RGGraphPersonNode import RGGraphPersonNode
from ResearchGate.RGGraphPaperNode import RGGraphPaperNode

class RGNodeContainer:
    def __init__(self) -> None:        
        self.PersonList = []
        self.PaperList = []
        pass
    
    def GetNodeCount(self):
        '''
        获得节点数量
        '''
        person_count = len(self.PersonList)
        paper_count = len(self.PaperList)
        return person_count + paper_count

    def SearchPersonNode(self, url):
        '''
        搜索person节点
        '''
        person_node :RGGraphPersonNode = None
        for person_node in self.PersonList:
            cur_url = person_node.GetURL()
            if cur_url == url:
                return person_node
        return None
        
    def SearchPaperNode(self, doi):
        paper_node :RGGraphPaperNode = None
        for paper_node in self.PaperList:
            cur_doi = paper_node.GetDOI()
            if cur_doi == doi:
                return paper_node
        return paper_node

    def AddPerson(self, node :RGGraphPersonNode):
        '''
        添加 person节点
        '''
        found_node :RGGraphPersonNode = self.SearchPersonNode(node.GetURL())
        if found_node != None:
            self.PersonList.remove(found_node)

        self.PersonList.append(node)
        

    def AddPaper(self, node :RGGraphPaperNode):
        '''
        添加paper节点
        '''
        found_node :RGGraphPaperNode = self.SearchPaperNode(node.GetDOI())
        if found_node != None:
            self.PaperList.remove(found_node)
        self.PaperList.append(node)
        

    def Save(self, filepath):
        '''
        保存所有节点
        '''




        pass
