from Framework.GraphDataNodeBase import GraphDataNodeBase
from xml.etree import ElementTree as ET

from Framework.NodeFactoryBase import NodeFactoryBase
class NodeContainer:
    def __init__(self) -> None:        
        self.NodeMapByType = {}
        self.BlackList = []
        pass

    
    def GetNodeCount(self):
        '''
        get all the node number
        '''
        node_num = 0
        keys = self.NodeMapByType.keys()
        for data_type in keys:
            node_map = self.NodeMapByType[data_type]
            node_num += len(node_map)

        return node_num
    
    def InNodeExistByUID(self, node_uid):
        node = self.FindNode(node_uid)
        return node != None

    def GetDataTypes(self):
        return self.NodeMapByType.keys()
    
    def GetAllNodesByType(self, data_type):
        node_list = self.NodeMapByType.get(data_type)
        return node_list
    
    def FindNode(self, node_uid):
        '''
        search the node by unique string
        '''
        keys = self.NodeMapByType.keys()
        for data_type in keys:
            found_node = self.FindNodeWithType(data_type, node_uid)
            if found_node != None:
                return found_node
        return None
        
    def FindNodeWithType(self, data_type, node_uid):
        node_map = self.NodeMapByType.get(data_type)
        if node_map == None:
            return None
        if node_uid in node_map:
            return node_map[node_uid]
        return None

    def AddNode(self, node :GraphDataNodeBase):
        
        found_node = self.FindNode(node.GetUniqueString())
        if found_node != None:
            raise Exception("Duplicated data")
        
        node_map = self.NodeMapByType.get(node.GetDataType())
        if node_map == None:
            self.NodeMapByType[node.GetDataType()] = {}
            node_map = self.NodeMapByType[node.GetDataType()]
        node_map[node.GetUniqueString()] = node

        node_count = self.GetNodeCount()
        print("Add data node：" + node.GetUniqueString() + " Number：" + str(node_count))

    def AddBlackList(self, uid):
        if uid not in self.BlackList:
            self.BlackList.append(uid)
        

    def IsInBlackList(self, uid):
        return uid in self.BlackList
        

    def Save(self, filepath):
        '''
        保存所有节点
        '''
        node_root = ET.Element("DataNodes")
        # 序列化
        self.Serialize(node_root)

        # 存盘
        s = ET.tostring(node_root, encoding='utf-8', method='xml')
        s = s.decode('utf-8')
        f = open(filepath, "w", encoding='utf-8')
        f.write(s)
        f.close()
        pass

    def Load(self, filepath, node_factory :NodeFactoryBase):
        '''
        读取所有节点
        '''
        tree = ET.parse(filepath)
        # DataNodes
        root = tree.getroot() # 获取root tag        
        
        self.Unserialize(root, node_factory)
        

    def Serialize(self, xml_node :ET.Element):
        nodelist_ele = ET.Element("NodeList")
        xml_node.append(nodelist_ele)

        keys = self.NodeMapByType.keys()
        if keys == None:
            return
        for key in keys:
            # data type element
            datatype_ele = ET.Element("DataType")
            datatype_ele.set("value", key)
            nodelist_ele.append(datatype_ele)

            node_map = self.NodeMapByType[key]
            node :GraphDataNodeBase
            for k in node_map:
                node = node_map[k]
                node.Serialize(datatype_ele)

        blacklist_ele = ET.Element("BlackList")
        xml_node.append(blacklist_ele)
        for black_uid in self.BlackList:
            black_ele = ET.Element("BlackUID")
            black_ele.set("value", black_uid)
            blacklist_ele.append(black_ele)


    def Unserialize(self, root_ele :ET.Element, node_factory :NodeFactoryBase):
        # root_ele: DataNodes

        self.NodeMapByType = {}
        self.BlackList = []

        for ele in root_ele:
            if ele.tag == "NodeList":
                list_ele = ele
                for datatype_ele in list_ele:
                    datatype = datatype_ele.get("value")
                    self.NodeMapByType[datatype] = {}
                    node_map = self.NodeMapByType[datatype]
                    for data_ele in datatype_ele:
                        data_node = node_factory.CreateNode( data_ele.tag)
                        data_node.Unserialize(data_ele)
                        node_map[data_node.GetUniqueString()] = data_node
                        
            elif ele.tag == "BlackList":
                blacklist_ele = ele
                for black_ele in blacklist_ele:
                    black_uid = black_ele.get("value")
                    self.BlackList.append(black_uid)
        
        
