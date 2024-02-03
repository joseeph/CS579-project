from ArxivCrawler.ArxivAuthorNode import ArxivAuthorNode


from Framework.CrawlContext import CrawlContext
from Framework.NodeContainer import NodeContainer
from Framework.NodeCrawlerBase import NodeCrawlerBase
from ArxivCrawler.ArxivCrawlerUtils import ArxivCrawlerUtils

class ArxivAuthorCrawler(NodeCrawlerBase):
    def __init__(self, author_name) -> None:
        super().__init__()
        self.AuthorName = author_name
        self.SetURL("au:" + '"' + self.AuthorName + '"')
        

    def Parse(self, context: CrawlContext, result):
        # check if the author exists
        data_container :NodeContainer = context.DataContainer
        author_id = ArxivCrawlerUtils.GetAuthorUID(self.AuthorName)
        is_exist = data_container.InNodeExistByUID(author_id)
        if is_exist:
            return True
         # 列出该author下的paper
        paper_infos = []
        for paper_info in result:
            paper_infos.append(paper_info)
        if len(paper_infos) == 0:
            print("没有爬到该作者的文章:" + self.AuthorName)
            # something is wrong add to blacklist
            data_container.AddBlackList(author_id)
            return True
        
        author_node = ArxivAuthorNode()
        author_node.SetAuthor(self.AuthorName)
        # add to the data contianer
        data_container.AddNode(author_node)
        
        for paper_info in paper_infos:
            paper_name = paper_info.title
            author_node.AddPaper(paper_name)

            paper_uid = ArxivCrawlerUtils.GetPaperUID(paper_name)
            paper_exist = data_container.InNodeExistByUID(paper_uid)
            if not paper_exist:
                from ArxivCrawler.ArxivPaperCrawler import ArxivPaperCrawler
                crawler = ArxivPaperCrawler(paper_name)
                context.AddDataCrawler(crawler)
            
        return True

       
            


        

