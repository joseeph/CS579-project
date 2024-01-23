from Framework.NodeContainer import NodeContainer

class CrawlContext:
    def __init__(self) -> None:
        self.NodeContainer = None
        pass

    def Init(self, container :NodeContainer):
        self.NodeContainer = container