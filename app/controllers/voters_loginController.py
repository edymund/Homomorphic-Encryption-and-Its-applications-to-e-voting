from ..entity.Voter import Voter
from ..entity.Projectdetails import ProjectDetails
from ..entity.Answer import Answer

class voters_loginController:
	# Constructor
	def __init__(self):
		pass

	def validateLogin(self, username, password, projectID):
		voter = Voter()
		if voter.checkVoterCredentials(username, password, projectID):
			return True
		return False

	def checkProjectStatusOngoing(self, projectID):
		projectDetails = ProjectDetails()
		if projectDetails.checkProjectStatus_Ongoing(projectID):
				return True
		return False

	def getVoterID(self, voterNumber, projectID):
		voter = Voter()
		return voter.getVoterID(voterNumber, projectID)

	def checkVoterHasVoted(self, voterID):
		answer = Answer()
		return answer.hasVoted(voterID)


	# Only authorised to vote if project is ongoing and
	# Voter has not voted before
	def checkVoterAuthorised(self, voterID, projectID):
		if not self.checkProjectStatusOngoing(projectID):
			print(f"Event ID {projectID} is not LIVE")
			return False
		
		if self.checkVoterHasVoted(voterID):
			print(f"Voter ID {voterID} has voted event {projectID}")
			return False
		
		return True