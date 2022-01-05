from ..entity.ElectionMessage import ElectionMessage
from ..entity.Projectdetails import ProjectDetails

class voters_ViewVoterCoverPageController:
	def __init__(self):
		pass

	def getElectionMsg(self,projID):
		
		# Create a Electionmsgs object containing the ID of the project
		electionDetails = ElectionMessage(projID)

		return electionDetails.getPreMsg()

	def getElectionTitle(self,projID):

		# Create a project details object containing the ID of the project
		projectDetails = ProjectDetails(projID)

		return projectDetails.getTitle()

