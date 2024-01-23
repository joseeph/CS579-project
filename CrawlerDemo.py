from selenium import webdriver
from CrawlerDrivers.CrawlerDriverEdgeWin import CrawlerDriverEdgeWin
from CrawlerDrivers.CrawlerDriverEdgeMacM1 import CrawlerDriverEdgeMacM1
from ResearchGate.RGGraphCrawlerPaper import RGGraphPaperNode
from Framework.CrawlContext import CrawlContext
from Framework.NodeContainer import NodeContainer

if __name__ == "__main__":
    crawler = CrawlerDriverEdgeWin()
    s = crawler.Get("https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration")
    node = RGGraphPaperNode()

    context = CrawlContext()
    container = NodeContainer()
    context.Init(container)
    result = node.Parse(context, s)
    
    print(result)
    pass