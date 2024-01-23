from selenium import webdriver
from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase


class CrawlerDriverEdgeWin(CrawlerDriverBase):
    def __init__(self) -> None:
        super().__init__()

        driver_path = "./edgedriver/msedgedriver_x86.exe"
        self.Driver = webdriver.Edge(driver_path, capabilities={})
        self.Driver.implicitly_wait(10)
        self.Driver.set_page_load_timeout(10)
        pass

    def Get(self, url):
        try:
            self.Driver.get(url)
        except Exception as e:
            print("timeout")

        return self.Driver.page_source

