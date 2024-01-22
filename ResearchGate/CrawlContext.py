from ResearchGate.RGNodeContainer import RGNodeContainer

class CrawlContext:
    def __init__(self) -> None:
        self.NodeContainer = None
        pass

    def Init(self, container :RGNodeContainer):
        self.NodeContainer = container