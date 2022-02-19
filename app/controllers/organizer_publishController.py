from ..entity.Projectdetails import ProjectDetails
from ..entity.ElectionMessage import ElectionMessage
from ..entity.Questions import Questions
from ..entity.Candidates import Candidates
from ..entity.Voter import Voter
from ..entity.ProjectRoles import ProjectRoles
from ..lib.service_email import SendEmailService
from ..lib.FHE import FHE

from flask import url_for, current_app
import random 

class organizer_publishController():
	def __init__(self):
		self.email = SendEmailService()
		self.email.setLoginDetails(current_app.config['EMAIL']['USER'], current_app.config['EMAIL']['PASSWORD'])
		self.email.setServer(current_app.config['EMAIL']['SERVER'], current_app.config['EMAIL']['PORT'])
		self.errors = []
	
	def getProjectStatus(self, projectID):
		projectDetails = ProjectDetails(projectID)
		return projectDetails.getStatus()
	
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

	def getProjectIsPendingVerification(self, projectID):
		projectDetails = ProjectDetails()
		return projectDetails.isPendingVerification(projectID)
	
	def verifyProject(self, projectID, organizerID):
		projectRoles = ProjectRoles()
		return projectRoles.setVerified(projectID, organizerID)
	
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

			# Sends notification to verifiers
			self.notify_verifier(self.get_all_verifier(projectID), projectID)

			# Attempts to publish
			self.updateProjectStatusToPublished(projectID)
			return True
		return False
		
	def updateProjectStatusToPublished(self, projectID):
		projectDetails = ProjectDetails()
		projectRoles = ProjectRoles()
		fhe = FHE()
		fhe.keyGen()

		# Check if all verifiers has approved
		if projectRoles.allVerifierApprovedProject(projectID):
			
			# Sends Email to Voters
			self.generate_inv_msg(projectID, url_for("voterLoginPage",_external=True))

			# Set public key for project
			projectDetails.updatePublicKey(projectID, fhe.getPublicKeyAsString())

			# Sends Decryption Key to Owner and Verifiers
			self.sendDecryptionKey(projectID, fhe.getPrivateKey())

			# Set Status as published
			projectDetails.setStatusAsPublished(projectID)

	def get_all_verifier(self, projectID): 
		projectOwner_entity = ProjectRoles(projectID)
		return projectOwner_entity.getVerifiersForProject(projectID)

	def generate_inv_msg(self,projectID, url):
		projDetails_entity = ProjectDetails(projectID)
		projectOwner_entity = ProjectRoles(projectID)
		electionMsg_entity = ElectionMessage(projectID)
		voter_entity = Voter(projectID)	

		proj_title = projDetails_entity.getTitle()
		proj_start_date = projDetails_entity.getStartDate()
		proj_start_time = projDetails_entity.getStartTime()
		proj_end_date = projDetails_entity.getEndDate()
		proj_end_time = projDetails_entity.getEndTime()
		
		organizer_info   = 	projectOwner_entity.get_organizer_info(projectID)
		organizer_name = f"{organizer_info[0]} {organizer_info[1]}" 
		company_name = organizer_info[2]
		
		invt_msg= electionMsg_entity.getInviteMsg()
		
		all_voters_info = voter_entity.get_all_voters_info(projectID)
		
		subject = "Invitation to participate in voting event"

		for voter_info in all_voters_info: 
			voters_email= voter_info[0]
			voters_No 	= voter_info[1]
			voters_pw 	= random.randint(0, 100000000)
			voter_entity.update_pw(voters_No, voters_email, projectID,voters_pw)
			print("url:", url)
			link = f"{url}?name={voters_No}&password={voters_pw}&projectID={projectID}"
			
			final_message = f"""
Dear Voter,

{invt_msg}

This email is to inform you that you are invited to participate in the voting event -"{proj_title}" by {organizer_name}, {company_name}.
The voting event will start from {proj_start_date},{proj_start_time} to {proj_end_date},{proj_end_time}.

Your voter ID is {voters_No}
Login link: {link}

Regards,
FYP-21-S4-03.

This is a system generated email, do not reply to this email.
"""
			

			self.email.setMessage(subject, final_message)
			self.email.setRecepientEmail(voters_email)
			self.email.sendEmail()

	def notify_verifier(self, verifier_arr, projectID):
		projectName = ProjectDetails(projectID).getTitle()
		# Set Email Message and Subject
		message = f"""
Dear verifier,

You have been added to the list of verifiers for the project "{projectName}".
Please log-in to verify the details of this project

Regards,
FYP-21-S4-03.

This is a system generated email, do not reply to this email.
"""
		subject = "Invitation to verify voting event"
		self.email.setMessage(subject, message)
		
		for verifier in verifier_arr:
			self.email.setRecepientEmail(verifier["email"])
			self.email.sendEmail()

	def notify_projectOwner(self, projectID, message):
		projectOwner_entity = ProjectRoles(projectID)
		owner = projectOwner_entity.getOwnersForProject(projectID)

		subject = "Event has been rejected by a verifier "
		self.email.setMessage(subject, message)
		self.email.setRecepientEmail(owner[2])
		self.email.sendEmail()
	
	def sendDecryptionKey(self, projectID, privateKey):
		project = ProjectDetails(projectID)
		projectRoles = ProjectRoles()

		# Get Project Details
		projectName = project.getTitle()
		projectOwner = projectRoles.getOwnersForProject(projectID)[2]
		projectVerifiers = self.get_all_verifier(projectID)
		recepients = [projectOwner]
		for verifier in projectVerifiers:
			recepients.append(verifier['email'])
		print("Recepients = ", recepients)
		subject = f"Decryption key for Voting Event - {projectName}"
		message = \
f"""
Dear Organizers

Please retain a copy of this e-mail to decrypt the voting results.

Project Name: {projectName}
Decrpytion Key: {privateKey}

We do not retain any information of the secret key.
If the decryption key is lost, we are unable to decrypt the results on your behalf.

Regards,
FYP-21-S4-03.

This is a system generated email, do not reply to this email.
"""
		self.email.setMessage(subject, message)
		self.email.setRecepientEmail(recepients)
		self.email.sendEmail()

	def return_default(self, projectID):
		projDetails_entity = ProjectDetails(projectID)
		projectOwner_entity = ProjectRoles(projectID)
		projDetails_entity.setStatusAsDraft(projectID)
		all_verifiers = projectOwner_entity.getVerifiersForProject(projectID)
		for verifier in all_verifiers:
			projectOwner_entity.default_approval(projectID,verifier['organizerID'])


