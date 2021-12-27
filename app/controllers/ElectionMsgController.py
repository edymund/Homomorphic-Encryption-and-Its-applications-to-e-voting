from ..entity.ElectionMessage import ElectionMessage

class ElectionMsgController:
    def __init__(self, projID = None):
        self.projID = projID

    # accessor
    def getProjID(self):
        return self.projID

    # mutator 
    def setProjID(self,projID):
        self.projID = projID

    def check_pre_election_msg(self,msg):
        pass

    def check_post_election_msg(self,msg):
        pass

    def update_pre_election_msg(self,msg):
        pass
    
    def update_post_election_msg(self,msg):
        pass
    