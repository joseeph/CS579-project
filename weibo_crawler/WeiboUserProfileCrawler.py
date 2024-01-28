from Framework.CrawlContext import CrawlContext
from Framework.CrawlerBase import CrawlerBase
from Framework.NodeContainer import NodeContainer
from lxml import etree
import html

from weibo_crawler.WeiboUserDataNode import WeiboUserDataNode
class WeiboUserProfileCrawler(CrawlerBase):
    def __init__(self, user_id) -> None:
        super().__init__()
        self.UserID = user_id
        self.SetURL("https://weibo.cn/%s/profile" % self.UserID)

    def Parse(self, context: CrawlContext, s):       
        selector = etree.HTML(s)
        nickname = selector.xpath('/html/body/div[4]/table/tr/td[2]/div/span[1]/text()[1]')[0]
        node : WeiboUserDataNode= context.DataContainer.FindNode(self.UserID)
        if node == None:
            raise BaseException("UserID不对")

        node.SetNickname(nickname)

        pass