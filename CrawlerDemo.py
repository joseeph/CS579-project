from selenium import webdriver
from Crawlers.CrawlerWin import CrawlerWin

if __name__ == "__main__":
    crawler = CrawlerWin()
    s = crawler.Get("https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration")
    pos = s.find("http://dx.doi.org")
    print(pos)
    pass