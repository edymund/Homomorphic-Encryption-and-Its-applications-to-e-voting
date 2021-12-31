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
        entity = ElectionMessage(projID= self.projID)
    
    def update_rmd_msg(self,msg):
        entity = ElectionMessage(projID= self.projID)

    def retrieve_inv_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.invMsg = entity.getInviteMsg()
        # with open("invMsg.txt","w") as f:
        #     f.write(str(self.invMsg))
        #     f.close()
        return self.invMsg

    def retrieve_rmd_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.rmdMsg = entity.getReminderMsg()
        # with open("rmdMsg.txt","w") as f:
        #     f.write(str(self.rmdMsg))
        #     f.close()
        return self.rmdMsg
    
    @staticmethod
    def retrieve_proj_detail(url):
        # url = "www.123/1/abc"
        for i in range(1):
            slash = url.find("/")
            new_url = url[slash+1:]
        next_slash = new_url.find("/")
        proj_details = new_url[:next_slash]
        return proj_details
        
    