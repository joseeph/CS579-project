from selenium import webdriver
from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase

class CrawlerDriverEdgeMacM1(CrawlerDriverBase):
    def __init__(self) -> None:
        super().__init__()
                
        driver_path = "./edgedriver/msedgedriver_m1"
        driver = webdriver.Edge(driver_path, capabilities={})
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(10)

        self.Driver = driver
        pass
    def Get(self, url):
        try:
            self.Driver.get(url)
        except Exception as e:
            print("timeout")

        return self.Driver.page_source
        
        
