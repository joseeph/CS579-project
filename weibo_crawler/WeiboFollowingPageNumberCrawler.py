from Framework.CrawlContext import CrawlContext
from Framework.CrawlerBase import CrawlerBase
from weibo_crawler.WeiboUserDataNode import WeiboUserDataNode
from lxml import etree

class WeiboFollowingPageNumberCrawler(CrawlerBase):
    def __init__(self, user_id) -> None:
        super().__init__()
        # the use id
        self.UserID = user_id
        self.SetURL("https://weibo.cn/%s/follow" % self.UserID)

    def Parse(self, context :CrawlContext, s):
        selector = etree.HTML(s)
        # the page number of the followings of this user
        page_num = 0
        if selector.xpath("//input[@name='mp']") == []:
            page_num = 1
        else:
            page_num = (int)(selector.xpath("//input[@name='mp']")[0].attrib['value'])
        # I only create the User Data Node here
        UserDataNode = WeiboUserDataNode(self.UserID)
        if context.DataContainer.IsNodeExist( UserDataNode):
            raise BaseException("Already create the node!!!")
        # add the node to container
        context.DataContainer.AddNode(UserDataNode)
        # firstly crawl the user's profile
        from weibo_crawler.WeiboUserProfileCrawler import WeiboUserProfileCrawler
        crawler = WeiboUserProfileCrawler(self.UserID)
        context.AddCrawler(crawler)

        # now we get how many pages of followings, now crawl these pages one by one
        for page_id in range(1, page_num + 1):
            from weibo_crawler.WeiboFollowingsInPageCrawler import WeiboFollowingsInPageCrawler
            crawler = WeiboFollowingsInPageCrawler(self.UserID, page_id)
            context.AddCrawler(crawler)


   

    def get_follow_list(self):
        """获取关注用户主页地址"""
        page_num = self.get_page_num()
        print(u'用户关注页数：' + str(page_num))
        # 随机挑选要的页码
        page1 = 0
        random_pages = random.randint(1, 5)
        for page in tqdm(range(1, page_num + 1), desc=u'关注列表爬取进度'):
            # 获取一页
            self.get_one_page(page)
            
            if page - page1 == random_pages and page < page_num:
                sleep(random.randint(6, 10))
                page1 = page
                random_pages = random.randint(1, 5)

        print(u'用户关注列表爬取完毕')