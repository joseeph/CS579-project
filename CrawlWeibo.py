
import time
from Framework.CrawlerRunner import CrawlerRunner
from Framework.NodeContainer import NodeContainer
from weibo_crawler.CrawlerDriverForWeibo import CrawlerDriverForWeibo
from weibo_crawler.WeiboFollowingPageNumberCrawler import WeiboFollowingPageNumberCrawler
import json

from weibo_crawler.WeiboNodeFactory import WeiboNodeFactory
from weibo_crawler.WeiboUserDataNode import WeiboUserDataNode


def FindRecommandCrawlUserID(data_container :NodeContainer, config):
    user_id_list = config['user_id_list']
    user_id = user_id_list[0]

    if len(data_container.NodeList) > 0:
        user_node :WeiboUserDataNode
        for user_node in data_container.NodeList:            
            for following_id in user_node.FollowingIDs:
                if not data_container.InNodeExistByUStr(following_id):
                    return following_id            
    return user_id


def Main(config_path):
    config = None
    with open(config_path) as f:        
        config = json.loads(f.read())
    cookie = config['cookie']
    
    driver = CrawlerDriverForWeibo(cookie)
    #driver.EnableProxy(True)

    save_path = "./result.xml"
    Runner = CrawlerRunner(driver, save_path)
    Runner.SetMaxNode(2000)
    node_factory = WeiboNodeFactory()
    Runner.LoadNodes(node_factory)

    user_id = FindRecommandCrawlUserID(Runner.NodeContainer, config)

    first_crawler = WeiboFollowingPageNumberCrawler(user_id)
    Runner.AddDataCrawler(first_crawler)
    Runner.BeginCrawl()
    
    
def Main2(config_path):
    config = None
    with open(config_path) as f:        
        config = json.loads(f.read())
    cookie = config['cookie']
    user_id_list = config['user_id_list']
    driver = CrawlerDriverForWeibo(cookie)
    s = driver.Get("https://weibo.cn/6501892483/profile")
    print(s)

def Main3():
    node_container = NodeContainer()
    node_factory = WeiboNodeFactory()
    node_container.Load("./result.xml", node_factory)
    pass

def Main4(config_path):
    config = None
    with open(config_path) as f:        
        config = json.loads(f.read())
    cookie = config['cookie']
    
    driver = CrawlerDriverForWeibo(cookie)
    driver.Get("https://weibo.cn/1708942053/")

if __name__ == "__main__":
    Main("./weibo_crawler/config.json")
