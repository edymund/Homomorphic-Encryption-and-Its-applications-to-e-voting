from ..entity.ElectionMessage import ElectionMessage
from ..entity.Voter import Voter
from ..entity.Projectdetails import ProjectDetails
from ..lib.service_email import SendEmailService
from flask import current_app

class organizer_emailSettingsController:
	def __init__(self, projID = None):
		self.projID = projID
		self.email = SendEmailService()
		self.email.setLoginDetails(current_app.config['EMAIL']['USER'], current_app.config['EMAIL']['PASSWORD'])
		self.email.setServer(current_app.config['EMAIL']['SERVER'], current_app.config['EMAIL']['PORT'])
		self.errors = []
	
	def getProjectStatus(self, projectID):
		projectDetails = ProjectDetails(projectID)
		return projectDetails.getStatus()

	def check_msg(self,msg):
		if msg == "" or msg == None or msg == "None":
			return False
		elif msg != "" and msg != None and msg !="None":
			return True

	def update_inv_msg(self,msg,projectID):
		entity = ElectionMessage(projectID)
		entity.setInviteMsg(msg,projectID)
	
	def update_rmd_msg(self,msg,projectID):
		entity = ElectionMessage(projectID)
		entity.setReminderMsg(msg,projectID)

	def retrieve_inv_msg(self,projectID):
		entity = ElectionMessage(projectID)
		return entity.getInviteMsg()

	def retrieve_rmd_msg(self,projectID):
		entity = ElectionMessage(projectID)
		return entity.getReminderMsg()
		
	def send_reminder(self,projectID):
		voter_entity = Voter(projectID)
		Election_entity = ElectionMessage(projectID)
		proj_entity = ProjectDetails(projectID)
		proj_title = proj_entity.getTitle()
		start_date = proj_entity.getStartDate()
		start_time = proj_entity.getStartTime()
		end_time = proj_entity.getEndTime()
		end_date =   proj_entity.getEndDate()
		compul_msg = f"\n This email is to remind you to participate in the voting event, {proj_title}."+\
            '\n'+f" Please be reminded to vote from  \nSTART: {start_date}, {start_time} \nEND:   {end_date}, {end_time}.\n\nRegards,\nFYP-21-s4-03" 
		
		#get Reminder message
		rmd_msg = Election_entity.getReminderMsg()
		all_voters = voter_entity.get_all_voters(projectID)

		final_msg = rmd_msg+ "\n" + compul_msg

		all_email = []
		for voter_email in all_voters: 
			all_email.append(voter_email[0])

		subject = "Reminder to vote"
		self.email.setMessage(subject, final_msg)
		self.email.setRecepientEmail(all_email)
		self.email.sendEmail()
	
	