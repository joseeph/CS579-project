from Framework.GraphDataNodeBase import GraphDataNodeBase
from xml.etree import ElementTree as ET

from Framework.NodeFactoryBase import NodeFactoryBase
class NodeContainer:
    def __init__(self) -> None:        
        self.NodeMap = {}
        self.BlackList = []
        pass

    
    def GetNodeCount(self):
        '''
        get all the node number
        '''
        node_num = 0
        keys = self.NodeMap.keys()
        for data_type in keys:
            node_list = self.NodeMap[data_type]
            node_num += len(node_list)

        return node_num
    
    def InNodeExistByUID(self, node_uid):
        node = self.FindNode(node_uid)
        return node != None

    def GetDataTypes(self):
        return self.NodeMap.keys()
    
    def GetDataNodeListByType(self, data_type):
        node_list = self.NodeMap.get(data_type)
        return node_list
    
    def FindNode(self, node_uid):
        '''
        search the node by unique string
        '''
        keys = self.NodeMap.keys()
        for data_type in keys:
            found_node = self.FindNodeWithType(data_type, node_uid)
            if found_node != None:
                return found_node
        return None
        
    def FindNodeWithType(self, data_type, node_uid):
        node_list = self.NodeMap.get(data_type)
        if node_list == None:
            return None
        node :GraphDataNodeBase 
        for node in node_list:
            cur_uid = node.GetUniqueString()
            if cur_uid == node_uid:
                return node 
        return None

    def AddNode(self, node :GraphDataNodeBase):
        
        found_node = self.FindNode(node.GetUniqueString())
        if found_node != None:
            raise Exception("添加节点重复")
        
        node_list = self.NodeMap.get(node.GetDataType())
        if node_list == None:
            self.NodeMap[node.GetDataType()] = []
            node_list = self.NodeMap[node.GetDataType()]
        node_list.append(node)

        node_count = self.GetNodeCount()
        print("添加数据节点：" + node.GetUniqueString() + " 现在数量为：" + str(node_count))

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

        keys = self.NodeMap.keys()
        if keys == None:
            return
        for key in keys:
            # data type element
            datatype_ele = ET.Element("DataType")
            datatype_ele.set("value", key)
            nodelist_ele.append(datatype_ele)

            node_list = self.NodeMap[key]
            node :GraphDataNodeBase
            for node in node_list:
                node.Serialize(datatype_ele)

        blacklist_ele = ET.Element("BlackList")
        xml_node.append(blacklist_ele)
        for black_uid in self.BlackList:
            black_ele = ET.Element("BlackUID")
            black_ele.set("value", black_uid)
            blacklist_ele.append(black_ele)


    def Unserialize(self, root_ele :ET.Element, node_factory :NodeFactoryBase):
        # root_ele: DataNodes

        self.NodeMap = {}
        self.BlackList = []

        for ele in root_ele:
            if ele.tag == "NodeList":
                list_ele = ele
                for datatype_ele in list_ele:
                    datatype = datatype_ele.get("value")
                    self.NodeMap[datatype] = []
                    node_list = self.NodeMap[datatype]
                    for data_ele in datatype_ele:
                        data_node = node_factory.CreateNode( data_ele.tag)
                        data_node.Unserialize(data_ele)
                        node_list.append(data_node)
            elif ele.tag == "BlackList":
                blacklist_ele = ele
                for black_ele in blacklist_ele:
                    black_uid = black_ele.get("value")
                    self.BlackList.append(black_uid)
        
        
