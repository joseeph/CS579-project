from Framework.NodeContainer import NodeContainer
from Framework.NodeCrawlerBase import NodeCrawlerBase
from Framework.CrawlContext import CrawlContext
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode

class ArxivCitationPaperCrawler(NodeCrawlerBase):
    def __init__(self) -> None:
        super().__init__()
        self.PaperID = ""

    def SetPaperID(self, paper_id :str):
        self.PaperID = paper_id
        self.SetURL('hep-ph/' + self.PaperID)
        self.SetOp("query_idlist")

    def Parse(self, context: CrawlContext, result):
        info_list = []
        for info in result:
            info_list.append(info)
        if len(info_list) == 0:
            return True
        
        # fill the information of this paper
        data_container :NodeContainer = context.DataContainer
        node :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", self.PaperID)
        if node == None:
            return True
        paper_info = info_list[0]
        title = paper_info.title
        node.SetName(title)
        for cur_author in paper_info.authors:
            node.AddAuthor(cur_author.name)
        print("update info:" + title)
        return True
            
        
        
        

    

