from ..entity.ElectionMessage import ElectionMessage

class ElectionMsgController:
    def __init__(self, projectID = None):
        self.projectID = projectID

    # accessor
    def getProjID(self):
        return self.projectID

    def check_msg(self,msg):
        if msg == "" or msg == None or msg == "None":
            return False
        elif msg != "" or msg != None or msg =="None":
            return True

    def update_pre_election_msg(self,msg,projectID):
        entity = ElectionMessage(projectID)
        entity.setPreMsg(msg,projectID)
    
    def update_post_election_msg(self,msg,projectID):
        entity = ElectionMessage(projectID)
        entity.setPostMsg(msg,projectID)

    def retrieve_pre_election_msg(self,projectID):
        entity = ElectionMessage(projectID)
        return entity.getPreMsg()

    def retrieve_post_election_msg(self,projectID):
        entity = ElectionMessage(projectID)
        return entity.getPostMsg()
    
    
    


    