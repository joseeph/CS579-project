from CrawlerDrivers.CrawlerDriverBase import CrawlerDriverBase
import requests
from lxml import etree
import traceback

class CrawlerDriverForWeibo(CrawlerDriverBase):
    def __init__(self, cookie) -> None:
        super().__init__()
        self.UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        self.Headers  = {
                'User_Agent': self.UserAgent,
                'Cookie': cookie,
                'Connection': 'close'
            }
    
    def Get(self, url):
        try:            
            html = requests.get(url, headers=self.Headers).content
            return html
        except Exception as e:
            print('Error: ', e)
            traceback.print_exc()