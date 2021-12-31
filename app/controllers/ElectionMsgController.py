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
    
    @staticmethod
    def retrieve_proj_detail(url):
	# url = "www.123/1/abc"
        for i in range(1):
            slash = url.find("/")
            new_url = url[slash+1:]
        next_slash = new_url.find("/")
        proj_details = new_url[:next_slash]
        return proj_details


    