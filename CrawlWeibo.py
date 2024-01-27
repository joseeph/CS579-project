
from Framework.CrawlerRunner import CrawlerRunner
from weibo_crawler.CrawlerDriverForWeibo import CrawlerDriverForWeibo
from weibo_crawler.WeiboFollowingPageNumberCrawler import WeiboFollowingPageNumberCrawler
import json


def Main(config_path):
    config = None
    with open(config_path) as f:        
        config = json.loads(f.read())
    cookie = config['cookie']
    user_id_list = config['user_id_list']
    user_id = user_id_list[0]
    driver = CrawlerDriverForWeibo(cookie)
    Runner = CrawlerRunner(driver)
    first_crawler = WeiboFollowingPageNumberCrawler(user_id)
    Runner.AddCrawler(first_crawler)
    Runner.BeginCrawl()
    


if __name__ == "__main__":
    Main("./weibo_crawler/config.json")