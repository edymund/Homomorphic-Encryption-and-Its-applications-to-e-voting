from ..entity.ElectionMessage import ElectionMessage

class EmailSettingsController:
    def __init__(self, projID = None):
        self.projID = projID
        self.invMsg = ""
        self.rmdMsg = ""

    # accessor
    def getProjID(self):
        return self.projID

    def getInvMsg(self):
        return self.invMsg

    def getRmdMsg(self):
        return self.rmdMsg

    # mutator 
    def setProjID(self,projID):
        self.projID = projID

    def check_inv_msg(self,msg):
        if msg != "":
            return True
        else:
            return False

    def check_rmd_msg(self,msg):
        if msg != "":
            return True
        else:
            return False

    def update_inv_msg(self,msg):
        pass
    
    def update_rmd_msg(self,msg):
        pass

    def retrieve_inv_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.preMsg = entity.getPreMsg()
        return self.preMsg

    def retrieve_rmd_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.postMsg = entity.getPostMsg()
        return self.postMsg
    