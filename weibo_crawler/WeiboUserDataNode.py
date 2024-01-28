from Framework.GraphDataNodeBase import GraphDataNodeBase
from xml.etree import ElementTree as ET

class WeiboUserDataNode(GraphDataNodeBase):
    def __init__(self, uid) -> None:
        super().__init__()
        self.UserID = uid        
        self.NickName = ""
        self.FollowingIDs = []
    
    def GetUniqueString(self):
        return self.UserID
    
    def SetNickname(self, nickname):
        self.NickName = nickname

    def AddFollowing(self, following_userid :str):
        '''
        add a following of this user
        '''
        self.FollowingIDs.append(following_userid)

    def Serialize(self, node):
        userdata_node = ET.Element("WeiboUserData")
        node.append(userdata_node)
        # user id
        userid_ele = ET.Element("UserID")
        userid_ele.set("value", self.UserID)
        userdata_node.append(userid_ele)

        # nick name
        nickname_ele = ET.Element("NickName")
        nickname_ele.set("value", self.NickName)
        userdata_node.append(nickname_ele)

        # follow list
        followlist_ele = ET.Element("FollowList")
        userdata_node.append(followlist_ele)
        for follow_id in self.FollowingIDs:
            followid_ele = ET.Element("FollowID")
            followid_ele.set("value", follow_id)
            followlist_ele.append(followid_ele)

    
    def Unserialize(self, node):
        return super().Unserialize(node)
