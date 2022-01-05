from ..entity.Voter import Voter
import pandas as pd
import random 

class ImportVoterListController:
    def __init__(self,voterList = [], projID = None):
        self.voterList = voterList
        self.projID = projID

    # accessor
    def getProjID(self):
        return self.projID

    # mutator 
    def setProjID(self,projID):
        self.projID = projID

    def valid_email(self, email):
        voter = Voter(self.projID)
        if voter.email_exist(self.projID,email) == False and email.find("@") > 0 :
            return True
        else:
            return False
        
    def update_voter(self, projID):
        voter = Voter(projID)
        all_id = voter.get_all_voters_id(projID)
        if len(all_id) >0:
            for id in all_id:
                for value in id:
                    voter.delete_child(value, projID)
            voter.delete_allVoters(projID)
        
        for email in self.voterList:
            password = self.get_random()
            hash = random.getrandbits(24)
            hash = str(hex(hash))[2:]
            voter.insert_to_table(hash,email, self.getProjID(),password)


    def get_random(self):
       return random.randint(0, 100000000)

    def get_all_voters_email(self):
        voter = Voter()
        list_of_voter = voter.get_all_voters(projID = self.getProjID())
        return list_of_voter
    
    def processVoterList(self,voterList):
        """
        read through the whole file and valid_email it
        if all True
        add to list
        else return to Boundary to display error
        """
        col_names=["Email"]
        datas = pd.read_csv(voterList, names = col_names)
        validity = False
        # actual code
        proc_datas = datas.Email.to_list()
        
        for data in proc_datas:
            if self.valid_email(data) == True:
                validity = True
            elif self.valid_email(data) == False:
                return False
        if validity == True:
            for data in proc_datas:
                self.voterList.append(data)
        return validity
    
    @staticmethod
    def retrieve_proj_detail(url):
        # url = "www.123/1/abc"
        for i in range(1):
            slash = url.find("/")
            new_url = url[slash+1:]
        next_slash = new_url.find("/")
        proj_details = new_url[:next_slash]
        return proj_details


        # with open ("try.txt","w") as f:
        #     proc_datas = datas.Email.to_list()
        #     for data in proc_datas:
        #         f.write(str(data).strip()) 
        #         f.write("\n")
        #     f.close()

        
