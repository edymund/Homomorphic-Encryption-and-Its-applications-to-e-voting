from ..entity.Projectdetails import ProjectDetails
from ..entity.ElectionMessage import ElectionMessage
from ..entity.Questions import Questions
from ..entity.Candidates import Candidates
from ..entity.Voter import Voter
from ..entity.Administrator import Administrator

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



