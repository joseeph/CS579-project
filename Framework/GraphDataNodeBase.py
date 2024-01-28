class GraphDataNodeBase:
    def __init__(self) -> None:        
        pass

    def GetUniqueString(self):
        raise NotImplementedError
    

    def Serialize(self, node):
        raise NotImplementedError
    
    def Unserialize(self, node):
        raise NotImplementedError