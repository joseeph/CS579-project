from Framework.GraphDataNodeBase import GraphDataNodeBase


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

        
