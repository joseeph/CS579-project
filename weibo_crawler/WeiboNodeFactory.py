from Framework.NodeFactoryBase import NodeFactoryBase
from weibo_crawler.WeiboUserDataNode import WeiboUserDataNode


class WeiboNodeFactory(NodeFactoryBase):
    def __init__(self) -> None:
        super().__init__()
    
    def CreateNode(self, node_name):
        node = None
        if node_name == "WeiboUserData":
            node = WeiboUserDataNode()
        return node