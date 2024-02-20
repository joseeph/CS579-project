from ArxivCrawler.ArxivAuthorRelationship import ArxivAuthorRelationship
from ArxivCrawler.ArxivAuthorRelationshipCollection import ArxivAuthorRelationshipCollection
from ArxivCrawler.ArxivNodeFactory import ArxivNodeFactory
from ArxivCrawler.ArxivPaperNode import ArxivPaperNode
from Framework.NodeContainer import NodeContainer


class CleanData:
    def __init__(self) -> None:
        self.DataContainer :NodeContainer = None
        pass

    def LoadDataset(self, save_path):
        self.DataContainer = NodeContainer()
        node_factory = ArxivNodeFactory()
        self.DataContainer.Load(save_path, node_factory)
        
    def DoClean(self, output_path):
        '''
        Convert the Paper nodes to author-coauthor nodes
        '''
        relationship_collection = ArxivAuthorRelationshipCollection()
        papernode_list = self.DataContainer.GetDataNodeListByType("ArxivPaperNode")
        papernode :ArxivPaperNode = None
        for papernode in papernode_list:
            author_list = papernode.AuthorList
            if len(author_list) > 0:
                main_author = author_list[0]
                co_authors = author_list[1:]
                relationship = ArxivAuthorRelationship()
                relationship.SetAuthorName(main_author)
                for cur_coauthor in co_authors:
                    relationship.AddCoauthor(cur_coauthor)
                relationship_collection.AddRelationship(relationship)
        relationship_collection.Save(output_path)

def Main():
    src_path = "result.xml"
    dst_path = "cleaned_result.xml"
    solver = CleanData()
    solver.LoadDataset(src_path)
    solver.DoClean(dst_path)
def Main2():
    collection = ArxivAuthorRelationshipCollection()
    collection.Load("cleaned_result.xml")
    pass

if __name__ == '__main__':
    Main()