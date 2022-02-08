from ..entity.Projectdetails import ProjectDetails
from ..entity.ElectionMessage import ElectionMessage
from ..entity.Questions import Questions
from ..entity.Candidates import Candidates
from ..entity.Voter import Voter
from ..entity.Administrator import Administrator
import smtplib
from email.message import EmailMessage

class admin_publishController():
	def __init__(self):
		self.errors = []
	
	def getProjectDetails(self, projectID):
		projectDetails = ProjectDetails()
		return projectDetails.getProjectDetails(projectID)
	
	def getPreElectionMessage(self, projectID):
		electionMessage = ElectionMessage(projectID)
		return electionMessage.getPreMsg()

	def getInvitationMessage(self, projectID):
		electionMessage = ElectionMessage(projectID)
		return electionMessage.getInviteMsg()

	def getVotersCount(self, projectID):
		voter = Voter()
		return voter.getVoterCount(projectID)

	def getQuestionsAndAnswers(self, projectID):
		questionEntity = Questions()
		CandidateEntity = Candidates()

		questions = questionEntity.getQuestions(projectID)
		candidates = CandidateEntity.getCandidates(projectID)

		questionArray = []
		for item in questions:
			question = {}
			question['question'] = item
			question['option'] = []
			for candidate in candidates:
				if item['questionID'] == candidate['questionID']:
					question['option'].append(candidate)
			questionArray.append(question)

		return questionArray

	def getErrorMessages(self, projectID):
		self.performChecks(projectID)
		return self.errors

		
	def performChecks(self, projectID):
		projectDetails = self.getProjectDetails(projectID)
		questionSets = self.getQuestionsAndAnswers(projectID)
		voterCount = self.getVotersCount(projectID)

		# Checks Project Details
		if projectDetails['title'] is None:
			self.errors.append("Project Name cannot be empty")
		if projectDetails['startDateTime'] is None:
			self.errors.append("Voting Start Date cannot be empty")
		if projectDetails['endDateTime'] is None:
			self.errors.append("Voting End Date cannot be empty")
		if projectDetails['publicKey'] is None:
			self.errors.append("Public Key cannot be empty")
		
		# Check Questions and Answers
		if len(questionSets) < 1:
			self.errors.append("There are no questions to be voted on")

		for questionSet in questionSets:
			if len(questionSet["option"]) < 2:
				self.errors.append("One of the questions have less than 2 candidates")
		
		# Check Voters
		if voterCount < 2:
			self.errors.append("There must be more than 1 voters")
		
		if len(self.errors) == 0:
			return True
		else:
			return False

	def requestVerification(self, projectID):
		projectDetails = ProjectDetails()
		
		# Ensure that project passed all checks first
		if not self.performChecks(projectID):
			return False
		
		# Ensure that project is Draft Mode
		if not projectDetails.isDraftMode(projectID):
			return False
		
		# Change status to pending verification
		if projectDetails.setStatusToPendingVerification(projectID):
			# Automatically publish if no sub-admin
			self.updateProjectStatusToPublished(projectID)
			return True
		return False

	def getProjectIsPendingVerification(self, projectID):
		projectDetails = ProjectDetails()
		return projectDetails.isPendingVerification(projectID)
		

	def verifyProject(self, projectID, organizerID):
		administrator = Administrator()
		return administrator.setVerified(projectID, organizerID)
	
	def updateProjectStatusToPublished(self, projectID):
		projectDetails = ProjectDetails()
		administrator = Administrator()

		if administrator.allSubAdminApprovedProject(projectID):
			projectDetails.setStatusAsPublished(projectID)
			


	def set_mail(self, sender, receiver, message,subject,email):
		email["From"] = sender
		email["To"] = receiver
		email["Subject"] = subject
		email.set_content(message)
		return email

	def send_mail(self, EMAIL_ADR, EMAIL_PW, email):
		with smtplib.SMTP("smtp.gmail.com",587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			
			smtp.login(EMAIL_ADR, EMAIL_PW)
			smtp.send_message(email)
			smtp.quit()
			del email

	def generate_inv_msg(self,projectID):
		EMAIL_PASSWORD="eccqringtcgtolnf"
		EMAIL_ADDRESS="fyp21s403@gmail.com"
		
		projDetails_entity = ProjectDetails(projectID)
		administrator_entity = Administrator(projectID)
		electionMsg_entity = ElectionMessage(projID= projectID)
		voter_entity = Voter(projectID)	

		proj_title = projDetails_entity.getTitle()
		proj_start_date = projDetails_entity.getStartDate()
		proj_start_time = projDetails_entity.getStartTime()
		proj_end_date = projDetails_entity.getEndDate()
		proj_end_time = projDetails_entity.getEndTime()
		
		admin_info   = 	administrator_entity.get_organizer_info(projectID)
		admin_name = f"{admin_info[0]} {admin_info[1]}" 
		company_name = admin_info[2]
		
		invt_msg= electionMsg_entity.getInviteMsg()
		
		all_voters_info = voter_entity.get_all_voters_info(projectID)
		
		for voter_info in all_voters_info: 
			voters_email= voter_info[0]
			voters_ID 	= voter_info[1]
			voters_pw 	= voter_info[2]
			
			link = f"http://127.0.0.1:5000/{projectID}/ViewVoterCoverPage/?voterID={voters_ID}&pw={voters_pw}"
			
			final_message = f"""
			========================SYSTEM GENERATED MESSAGE START=====================
			\nDear Voter,\n 
			{invt_msg}\n 
			This email is to inform you that you are invited to participate in the voting event,{proj_title} by {admin_name}, {company_name}.\n 
			The voting event will start from {proj_start_date},{proj_start_time} to {proj_end_date},{proj_end_time}.\n 
			Your voter ID is {voters_ID}\n
			Email link:\n
			{link}\n\n
			Regards,\n
			FYP-21-S4-03.
			========================SYSTEM GENERATED MESSAGE END=====================
			"""
			
			email_obj = EmailMessage()
			email = self.set_mail(EMAIL_ADDRESS, voters_email,final_message,"Invitation to participate in voting event", email_obj)
			self.send_mail(EMAIL_ADDRESS, EMAIL_PASSWORD, email)

	def get_all_verifier(self, projectID): 
		administrator_entity = Administrator(projectID)
		return  administrator_entity.getSubAdministratorsForProject(projectID)

	def notify_verifier(self, verifier_arr):
		EMAIL_PASSWORD="eccqringtcgtolnf"
		EMAIL_ADDRESS="fyp21s403@gmail.com"
		for verifier in verifier_arr:
			message = f"Dear verifier, do remember to verify the details of the project"
			email_obj = EmailMessage()
			email = self.set_mail(EMAIL_ADDRESS, verifier["email"],message,"Invitation to verify voting event", email_obj)
			self.send_mail(EMAIL_ADDRESS, EMAIL_PASSWORD, email)
	
	def notify_admin(self, projectID,message):
		EMAIL_PASSWORD="eccqringtcgtolnf"
		EMAIL_ADDRESS="fyp21s403@gmail.com"
		administrator_entity = Administrator(projectID)
		admin = administrator_entity.getAdministratorsForProject(projectID)
		email_obj = EmailMessage()
		email = self.set_mail(EMAIL_ADDRESS, admin[2],message,"Notify reason to reject publish", email_obj)
		self.send_mail(EMAIL_ADDRESS, EMAIL_PASSWORD, email)



