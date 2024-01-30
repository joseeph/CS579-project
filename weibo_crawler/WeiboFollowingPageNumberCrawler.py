from Framework.CrawlContext import CrawlContext
from Framework.NodeCrawlerBase import NodeCrawlerBase
from weibo_crawler.WeiboUserDataNode import WeiboUserDataNode
from lxml import etree

class WeiboFollowingPageNumberCrawler(NodeCrawlerBase):
    def __init__(self, user_id) -> None:
        super().__init__()
        # the use id
        self.UserID = user_id
        self.SetURL("https://weibo.cn/%s/follow" % self.UserID)

    def IsEnabled(self, context :CrawlContext):
        # if the node is already created, then we don't crawl this user again
        node = context.DataContainer.FindNode(self.UserID)
        if node != None:
            return False
        return True
        

    def Parse(self, context :CrawlContext, s):
        selector = etree.HTML(s)
        # the page number of the followings of this user
        page_num = 0
        if selector.xpath("//input[@name='mp']") == []:
            page_num = 1
        else:
            page_num = (int)(selector.xpath("//input[@name='mp']")[0].attrib['value'])
        # I only create the User Data Node here
        UserDataNode = WeiboUserDataNode()
        UserDataNode.SetUserID(self.UserID)
        if context.DataContainer.IsNodeExist( UserDataNode):
            raise BaseException("Already create the node!!!")
        # add the node to container
        context.DataContainer.AddNode(UserDataNode)
        # firstly crawl the user's profile
        from weibo_crawler.WeiboUserProfileCrawler import WeiboUserProfileCrawler
        crawler = WeiboUserProfileCrawler(self.UserID)
        context.AddInfoCrawler(crawler)

        # now we get how many pages of followings, now crawl these pages one by one
        for page_id in range(1, page_num + 1):
            from weibo_crawler.WeiboFollowingsInPageCrawler import WeiboFollowingsInPageCrawler
            crawler = WeiboFollowingsInPageCrawler(self.UserID, page_id)
            context.AddInfoCrawler(crawler)
            
        return True

   

    