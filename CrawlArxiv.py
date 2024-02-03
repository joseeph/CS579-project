

from ArxivCrawler.ArxivAuthorCrawler import ArxivAuthorCrawler
from ArxivCrawler.ArxivAuthorNode import ArxivAuthorNode
from ArxivCrawler.ArxivCrawlerDriver import ArxivCrawlerDriver
from ArxivCrawler.ArxivNodeFactory import ArxivNodeFactory
from ArxivCrawler.ArxivPaperCrawler import ArxivPaperCrawler
from ArxivCrawler.ArxivPaperNode import ArxivPaperNode
from Framework.CrawlerRunner import CrawlerRunner
from Framework.NodeContainer import NodeContainer
from ArxivCrawler.ArxivCrawlerUtils import ArxivCrawlerUtils
def RecommandCrawlPaperAuthorName(data_container :NodeContainer):
    node_list = data_container.GetDataNodeListByType("ArxivPaperNode")
    node :ArxivPaperNode
    if node_list == None:
        return "Yan Yang"
    for node in node_list:
        author_list = node.AuthorList
        for author_name in author_list:
            author_id = ArxivCrawlerUtils.GetAuthorUID(author_name)
            # if we don't have this author crawled, then recommend this author name
            in_blacklist = data_container.IsInBlackList(author_id)
            if in_blacklist:
                continue
            found_node = data_container.FindNodeWithType("ArxivAuthorNode", author_id)
            if found_node == None:
                return author_name
    return "Yan Yang"

def RecommendCrawlPaperName(data_container :NodeContainer):
    node_list = data_container.GetDataNodeListByType("ArxivAuthorNode")
    if node_list == None:
        return "Deep Unsupervised Learning using Nonequilibrium Thermodynamics"
    node :ArxivAuthorNode
    for node in node_list:
        paper_list = node.PaperNameList
        for paper_name in paper_list:
            paper_id = ArxivCrawlerUtils.GetPaperUID(paper_name)
            in_blacklist = data_container.IsInBlackList(paper_id)
            if in_blacklist:
                continue
            found_node = data_container.FindNodeWithType("ArxivPaperNode", paper_id)
            if found_node == None:
                return paper_name
    return "Deep Unsupervised Learning using Nonequilibrium Thermodynamics"

def Main():
    crawl_driver = ArxivCrawlerDriver()
    node_factory = ArxivNodeFactory()

    save_path = "./result.xml"
    crawler_runner = CrawlerRunner(crawl_driver, save_path)
    crawler_runner.SetMaxNode(2000)
    crawler_runner.SetSleepTime(3)
    crawler_runner.LoadNodes(node_factory)

    recommend_paper = RecommendCrawlPaperName(crawler_runner.NodeContainer)
    recommand_author = RecommandCrawlPaperAuthorName(crawler_runner.NodeContainer)
    crawler = ArxivPaperCrawler(recommend_paper)
    crawler_runner.AddDataNodeCrawler(crawler)
    crawler = ArxivAuthorCrawler(recommand_author)
    crawler_runner.AddDataNodeCrawler(crawler)
    crawler_runner.BeginCrawl()
    pass

if __name__ == "__main__":
    Main()