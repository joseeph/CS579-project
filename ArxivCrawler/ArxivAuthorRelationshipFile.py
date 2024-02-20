from ArxivCrawler.ArxivAuthorRelationship import ArxivAuthorRelationship
from xml.etree import ElementTree as ET

class ArxivAuthorRelationshipFile:
    def __init__(self) -> None:
        self.RelationshipList = []

    def AddRelationshipo(self, relationship :ArxivAuthorRelationship):
        self.RelationshipList.append(relationship)
        

    def Serialize(self, parent_node):
        relationship :ArxivAuthorRelationship = None
        for relationship in self.RelationshipList:
            relationship.Serialize(parent_node)
        

    def Unserialize(self, node):
        for child_node in node:
            relationship = ArxivAuthorRelationship()
            relationship.Unserialize(child_node)
        
    def Save(self, filepath):
        '''
        保存所有节点
        '''
        node_root = ET.Element("AuthorRelationships")
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
        tree = ET.parse(filepath)
        # DataNodes
        root = tree.getroot() # 获取root tag        
        
        self.Unserialize(root)