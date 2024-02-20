from ArxivCrawler.ArxivNodeFactory import ArxivNodeFactory
from ArxivCrawler.ArxivPaperNode import ArxivPaperNode
from Framework.NodeContainer import NodeContainer


class CleanData:
    def __init__(self) -> None:
        self.DataContainer :NodeContainer = None
        self.KeepMaxCoauthorNodeNum = 500
        pass

    def LoadDataset(self, save_path):
        self.DataContainer = NodeContainer()
        node_factory = ArxivNodeFactory()
        self.DataContainer.Load(save_path, node_factory)
        
    def DoClean(self):
        '''
        1. Convert the Paper nodes to author-coauthor nodes
        2. keep the top 500 authors with the max coauthors
        '''
        papernode_list = self.DataContainer.GetDataNodeListByType("ArxivPaperNode")
        papernode :ArxivPaperNode = None
        for papernode in papernode_list:
            author_list = papernode.AuthorList
            if len(author_list) > 0:
                main_author = author_list[0]
                co_authors = author_list[1:]
