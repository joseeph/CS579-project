from Framework.GraphDataNodeBase import GraphDataNodeBase
from xml.etree import ElementTree as ET
class NodeContainer:
    def __init__(self) -> None:        
        self.NodeList = []
        pass
    
    def GetNodeCount(self):
        '''
        get all the node number
        '''
        node_count = len(self.NodeList)
        return node_count

    def IsNodeExist(self, node :GraphDataNodeBase):
        for cur_node in self.NodeList:
            cur_uname = cur_node.GetUniqueString() 
            if node.GetUniqueString() == cur_uname:
                return True
        return False
    
    def InNodeExistByUStr(self, node_ustr):
        idx = self.FindNodeIndex(node_ustr)
        return idx >= 0
    
    def FindNodeIndex(self, node_ustr):
        for cur_idx in range(len(self.NodeList)):
            cur_node = self.NodeList[cur_idx]
            cur_uname = cur_node.GetUniqueString() 
            if node_ustr == cur_uname:
                return cur_idx            
        return -1
    
    def FindNode(self, node_ustr):
        '''
        search the node by unique string
        '''
        idx = self.FindNodeIndex(node_ustr)
        if idx >= 0:
            return self.NodeList[idx]
        else:
            return None

    def AddNode(self, node :GraphDataNodeBase):
        idx = self.FindNodeIndex(node.GetUniqueString())
        if idx >= 0:
            self.NodeList.pop(idx)
        self.NodeList.append(node)
        print("添加数据节点：" + node.GetUniqueString() + " 现在数量为：" + str(len(self.NodeList)))

        pass 

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

    def Load(self, filepath):
        '''
        读取所有节点
        '''
        
        
        pass

    def Serialize(self, xml_node :ET.Element):
        nodelist_ele = ET.Element("NodeList")
        xml_node.append(nodelist_ele)

        data_node :GraphDataNodeBase
        for data_node in self.NodeList:
            data_node.Serialize(nodelist_ele)
