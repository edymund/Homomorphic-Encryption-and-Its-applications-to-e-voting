from ..entity.ElectionMessage import ElectionMessage

class ElectionMsgController:
    def __init__(self, projectID = None):
        self.projectID = projectID

    # accessor
    def getProjID(self):
        return self.projectID

    def getPreMsg(self):
        return self.preMsg

    def getPostMsg(self):
        return self.postMsg

    # mutator 
    def setProjID(self,projectID):
        self.projID = projectID

    def check_election_msg(self,msg):
        if msg == "" or msg ==None:
            return False
        elif msg != "" and msg != None:
            return True

    def update_pre_election_msg(self,msg):
        entity = ElectionMessage(projID= self.projectID)
        entity.setPreMsg(msg)
    
    def update_post_election_msg(self,msg):
        entity = ElectionMessage(projID= self.projectID)
        entity.setPostMsg(msg)

    def retrieve_pre_election_msg(self):
        entity = ElectionMessage(projID= self.projectID)
        self.preMsg = entity.getPreMsg()
        return self.preMsg

    def retrieve_post_election_msg(self):
        entity = ElectionMessage(projID= self.projectID)
        self.postMsg = entity.getPostMsg()
        return self.postMsg

    
    
    


    