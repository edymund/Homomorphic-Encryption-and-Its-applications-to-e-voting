from ..entity.ElectionMessage import ElectionMessage
from ..entity.Voter import Voter
from ..entity.Projectdetails import ProjectDetails
from email.message import EmailMessage
from ..lib.service_email import SendEmailService
from flask import current_app

class organizer_emailSettingsController:
    def __init__(self, projID = None):
        self.projID = projID
        self.email = SendEmailService()
        self.email.setLoginDetails(current_app.config['EMAIL']['USER'], current_app.config['EMAIL']['PASSWORD'])
        self.email.setServer(current_app.config['EMAIL']['SERVER'], current_app.config['EMAIL']['PORT'])
        self.errors = []

    def check_msg(self,msg):
        if msg == "" or msg == None:
            return False
        elif msg != "" or msg != None:
            return True

    def update_inv_msg(self,msg):
        entity = ElectionMessage(projID= self.projID)
        entity.setInviteMsg(msg)
    
    def update_rmd_msg(self,msg):
        entity = ElectionMessage(projID= self.projID)
        entity.setReminderMsg(msg)
        

    def retrieve_inv_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.invMsg = entity.getInviteMsg()
        return self.invMsg

    def retrieve_rmd_msg(self):
        entity = ElectionMessage(projID= self.projID)
        self.rmdMsg = entity.getReminderMsg()
        return self.rmdMsg
        
    def send_reminder(self):
        voter_entity = Voter(self.projID)
        Election_entity = ElectionMessage(self.projID)
        proj_entity = ProjectDetails(self.projID)
        proj_title = proj_entity.getTitle()
        start_date = proj_entity.getStartDate()
        start_time = proj_entity.getStartTime()
        end_time = proj_entity.getEndTime()
        end_date =   proj_entity.getEndDate()
        compul_msg = f"\n This email is to remind you to participate in the voting event, {proj_title}."+\
            '\n'+f" Please be reminded to vote from  \nSTART: {start_date}, {start_time} \nEND:   {end_date}, {end_time}.\n\nRegards,\nFYP-21-s4-03" 
        
        #get Reminder message
        rmd_msg = Election_entity.getReminderMsg()
        all_voters = voter_entity.get_all_voters(self.projID)

        final_msg = rmd_msg+ "\n" + compul_msg

        all_email = []
        for voter_email in all_voters: 
            all_email.append(voter_email[0])

        subject = "Reminder to vote"
        self.email.setMessage(subject, final_msg)
        self.email.setRecepientEmail(all_email)
        self.email.sendEmail()
    
    
    def check_proj_status(self):
        proj_entity = ProjectDetails(self.projID)
        if proj_entity.getStatus == "ONGOING":
            return True
        else:
            return False
