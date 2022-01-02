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

    def check_msg(self,msg):
        if msg == "" or msg == None:
            return False
        elif msg != "" or msg != None:
            return True

    def update_inv_msg(self,msg):
        entity = ElectionMessage(projID= self.projID)
        invMsg = entity.setInviteMsg(msg)
        self.invMsg = invMsg
    
    def update_rmd_msg(self,msg):
        entity = ElectionMessage(projID= self.projID)
        rmdMsg =entity.setReminderMsg(msg)
        self.invMsg = rmdMsg
        

    def retrieve_inv_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.invMsg = entity.getInviteMsg()
        return self.invMsg

    def retrieve_rmd_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.rmdMsg = entity.getReminderMsg()
        return self.rmdMsg
        
    