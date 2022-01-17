from ..entity.ElectionMessage import ElectionMessage

class ElectionMsgController:
    def __init__(self, projID = None):
        self.projID = projID

    # accessor
    def getProjID(self):
        return self.projID

    def getPreMsg(self):
        return self.preMsg

    def getPostMsg(self):
        return self.postMsg

    # mutator 
    def setProjID(self,projID):
        self.projID = projID

    def check_election_msg(self,msg):
        if msg == "" or msg ==None:
            return False
        elif msg != "" and msg != None:
            return True

    def update_pre_election_msg(self,msg):
        entity = ElectionMessage(projID= self.projID)
        entity.setPreMsg(msg)
    
    def update_post_election_msg(self,msg):
        entity = ElectionMessage(projID= self.projID)
        entity.setPostMsg(msg)

    def retrieve_pre_election_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.preMsg = entity.getPreMsg()
        return self.preMsg

    def retrieve_post_election_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.postMsg = entity.getPostMsg()
        return self.postMsg

    
    
    


    