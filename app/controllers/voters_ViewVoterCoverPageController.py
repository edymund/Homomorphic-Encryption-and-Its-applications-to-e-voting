from ..entity.Electionmsgs import Electionmsgs
from ..entity.ProjectDetails import ProjectDetails

class voters_ViewVoterCoverPageController:
	def __init__(self):
		pass

	def getElectionMsg(self,projID):
		
		# Create a Electionmsgs object containing the ID of the project
		electionDetails = Electionmsgs(projID)

		return electionDetails.preElectionMsg()

	def getElectionTitle(self,projID):

		# Create a project details object containing the ID of the project
		projectDetails = ProjectDetails(projID)

		return projectDetails.getTitle()

