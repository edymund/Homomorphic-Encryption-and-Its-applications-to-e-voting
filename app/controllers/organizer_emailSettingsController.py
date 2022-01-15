from ..entity.ElectionMessage import ElectionMessage
from ..entity.Voter import Voter
import smtplib
from email.message import EmailMessage

class organizer_emailSettingsController:
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
        EMAIL_PASSWORD="eccqringtcgtolnf"
        EMAIL_ADDRESS="fyp21s403@gmail.com"
        voter_entity = Voter(self.projID)
        Election_entity = ElectionMessage(self.projID)
        
        #get Reminder message
        rmd_msg = Election_entity.getReminderMsg()
        all_voters = voter_entity.get_all_voters(self.projID)

        for voter_email in all_voters: 
            email = EmailMessage()
            new_email = self.set_mail(EMAIL_ADDRESS, voter_email[0],rmd_msg, email)
            self.send_mail(EMAIL_ADDRESS, EMAIL_PASSWORD, new_email)
    
    def set_mail(self, sender, receiver, message,email):
        email["From"] = sender
        email["To"] = receiver
        email["Subject"] = "Reminder message to vote"
        email.set_content(message)
        return email

    def send_mail(self, EMAIL_ADR, EMAIL_PW, email):
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            
            smtp.login(EMAIL_ADR, EMAIL_PW)
            # print(f"Message: {email.get_content()}")
            # get_picture(msg)
            smtp.send_message(email)
            smtp.quit()
            del email