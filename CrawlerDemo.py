from selenium import webdriver
from CrawlerDrivers.CrawlerDriverWin import CrawlerDriverWin
from CrawlerDrivers.CrawlerDriverMacM1 import CrawlerDriverMacM1
from ResearchGate.RGGraphCrawlerPaper import RGGraphPaperNode
from ResearchGate.CrawlContext import CrawlContext
from ResearchGate.RGNodeContainer import RGNodeContainer

if __name__ == "__main__":
    crawler = CrawlerDriverWin()
    s = crawler.Get("https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration")
    node = RGGraphPaperNode()

    context = CrawlContext()
    container = RGNodeContainer()
    context.Init(container)
    result = node.Parse(context, s)
    
    print(result)
    pass