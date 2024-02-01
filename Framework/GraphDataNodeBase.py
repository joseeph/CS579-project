class GraphDataNodeBase:
    def __init__(self, data_type :str) -> None:        
        # the data type of the node
        self.DataType = data_type
        pass

    def GetDataType(self):
        return self.DataType

    def GetUniqueString(self):
        raise NotImplementedError
    

    def Serialize(self, node):
        raise NotImplementedError
    
    def Unserialize(self, node):
        raise NotImplementedError