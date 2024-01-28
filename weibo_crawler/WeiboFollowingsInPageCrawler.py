

from Framework.CrawlContext import CrawlContext
from Framework.CrawlerBase import CrawlerBase
from lxml import etree


from weibo_crawler.WeiboUserDataNode import WeiboUserDataNode

class WeiboFollowingsInPageCrawler(CrawlerBase):
    '''
    Crawl the followews in one page
    '''
    def __init__(self, user_id, page_id) -> None:
        super().__init__()
        self.UserID = user_id
        self.PageID = page_id
        url = 'https://weibo.cn/%s/follow?page=%d' % (self.UserID, self.PageID)
        self.SetURL(url)

    def Parse(self, context :CrawlContext, s):
        '''
        parse the following users from the current page
        '''
        selector = etree.HTML(s)
        # the node of this user id is already created in WeiboFollowingPageNumberCrawler
        cur_node :WeiboUserDataNode = context.DataContainer.FindNode(self.UserID)
        if cur_node == None:
            raise BaseException("WeiboFollowingsInPageCrawler: The User ID is not saved!!!")
        
        table_list = selector.xpath('//table')
        if (self.PageID == 1 and len(table_list) == 0):
            print("invalid cookie or user_id")
        else:
            for t in table_list:
                im = t.xpath('.//a/@href')[-1]
                # now get the uri and the nickname
                user_id = im.split('uid=')[-1].split('&')[0].split('/')[-1]
                # add following
                cur_node.AddFollowing(user_id)

                #nickname = t.xpath('.//a/text()')[0]
                # the 
                from weibo_crawler.WeiboFollowingPageNumberCrawler import WeiboFollowingPageNumberCrawler
                pagenum_crawler = WeiboFollowingPageNumberCrawler(user_id)
                context.AddDataCrawler(pagenum_crawler)

