from ArxivCrawler.ArxivAuthorNode import ArxivAuthorNode
from ArxivCrawler.ArxivPaperNode import ArxivPaperNode
from Framework.NodeFactoryBase import NodeFactoryBase


class ArxivNodeFactory(NodeFactoryBase):
    def __init__(self) -> None:
        super().__init__()

    def CreateNode(self, node_type):
        node = None
        if node_type == "ArxivAuthorNode":
            node = ArxivAuthorNode()
        elif node_type == "ArxivPaperNode":
            node = ArxivPaperNode()
        return node