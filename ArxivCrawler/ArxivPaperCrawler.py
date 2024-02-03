
from ArxivCrawler.ArxivAuthorNode import ArxivAuthorNode
from ArxivCrawler.ArxivPaperNode import ArxivPaperNode
from Framework.CrawlContext import CrawlContext
from Framework.NodeContainer import NodeContainer
from Framework.NodeCrawlerBase import NodeCrawlerBase
from ArxivCrawler.ArxivCrawlerUtils import ArxivCrawlerUtils

class ArxivPaperCrawler(NodeCrawlerBase):
    def __init__(self) -> None:
        super().__init__()
        self.CrawlType = ""
        self.PaperName = ""
        self.PaperID = ""
        pass
    def CrawlByName(self, paper_name):
        self.PaperName = paper_name
        self.CrawlType = "Name"
        self.SetURL("ti:" + '"' + self.PaperName + '"')
        self.SetOp("query")
    
    def CrawlByID(self, paper_name, paper_id):
        self.PaperID = paper_id
        self.PaperName = paper_name
        self.CrawlType = "ID"
        self.SetURL(str(self.PaperID))
        self.SetOp("idlist")

    def Parse(self, context: CrawlContext, result):
        # check if the node exist
        data_container :NodeContainer = context.DataContainer
        paper_uid = ArxivCrawlerUtils.GetPaperUID(self.PaperName)
        is_exist = data_container.InNodeExistByUID(paper_uid)
        if is_exist:
            return True
        
        paper_infolist = []
        for paper_info in result:
            paper_infolist.append(paper_info)

        if len(paper_infolist) == 0:
            print("没有爬到paper:" + self.PaperName)
            # something is wrong, add to black list
            data_container.AddBlackList(paper_uid) 
            return True
        
        # only get the first paper
        paper_info = paper_infolist[0]
        
        # create paper node
        paper_node = ArxivPaperNode()
        paper_node.SetPaperName(self.PaperName)
        search_id = ArxivCrawlerUtils.EntryID2SearchID(paper_info.entry_id) 
        paper_node.SetEntryID(search_id) 
        
        paper_authors = paper_info.authors
        # add the paper node to the data container
        data_container.AddNode(paper_node)
        for author_info in paper_authors:
            author_name = author_info.name
            paper_node.AddAuthor(author_name)
            # if the author doesn't in the data container, create a crawler
            author_uid = ArxivCrawlerUtils.GetAuthorUID(author_name)
            author_exist = data_container.InNodeExistByUID(author_uid)
            if not author_exist:
                from ArxivCrawler.ArxivAuthorCrawler import ArxivAuthorCrawler
                author_crawler = ArxivAuthorCrawler(author_name)
                context.AddDataCrawler(author_crawler)
        return True
