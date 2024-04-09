from Framework.NodeContainer import NodeContainer
from Framework.NodeCrawlerBase import NodeCrawlerBase
from Framework.CrawlContext import CrawlContext
from StanfordCitationNetwork.CitationPaperNode import CitationPaperNode

class ArxivCitationPaperCrawler(NodeCrawlerBase):
    def __init__(self) -> None:
        super().__init__()
        self.PaperID = ""
        self.CrawlOrder = ["hep-ph/", "hep-th/"]
        self.CurCrawlIdx = 0
        

    def SetPaperID(self, paper_id :str):
        self.PaperID = paper_id
        
        prefix = self.CrawlOrder[self.CurCrawlIdx]
        self.SetURL(prefix + self.PaperID)
        self.SetOp("query_idlist")

    def SetCrawlOrderByPhFirst( self, ph_first):
        if ph_first:
            self.CrawlOrder = ["hep-ph/", "hep-th/", "hep-lat/"]
        else:
            self.CrawlOrder = ['hep-th/', 'hep-ph/', "hep-lat/"]
    
    def GetCrawlOrder(self):
        return self.CrawlOrder
    
    def SetCrawlOrder(self, order):
        self.CrawlOrder = order

    def SetCurCrawlIdx(self, idx):
        self.CurCrawlIdx = idx

    def Parse(self, context: CrawlContext, result):
        info_list = []
        for info in result:
            info_list.append(info)
        if len(info_list) == 0:
            next_idx = self.CurCrawlIdx + 1
            if next_idx >= len(self.CrawlOrder):
                # this is the last crawler, return
                return True
            # if nothing is extracted, then create a new crawler for hep-th
            new_crawler = ArxivCitationPaperCrawler()
            new_crawler.SetCurCrawlIdx(next_idx)
            new_crawler.SetCrawlOrder(self.CrawlOrder)
            new_crawler.SetPaperID(self.PaperID)
            context.AddDataCrawler(new_crawler, False)
            return True
        
        # fill the information of this paper
        data_container :NodeContainer = context.DataContainer
        node :CitationPaperNode = data_container.FindNodeWithType("CitationPaperNode", self.PaperID)
        assert(node != None)
        
        paper_info = info_list[0]
        title = paper_info.title
        node.SetName(title)
        for cur_author in paper_info.authors:
            node.AddAuthor(cur_author.name)
        
        node.SetDate(paper_info.published) 

        print("update info:" + title)
        return True
            
        
        
        

    

