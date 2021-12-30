from ..entity.Electionmsgs import Electionmsgs
from ..entity.Projectdetails import Projectdetails

class voters_ViewVoterCoverPageController:
	def __init__(self):
		pass

	def getElectionMsg(self,projID):
		
		# Create a Electionmsgs object containing the ID of the project
		electionDetails = Electionmsgs(projID)

		return electionDetails.preElectionMsg()

	def getElectionTitle(self,projID):

		# Create a project details object containing the ID of the project
		projectDetails = Projectdetails(projID)

		return projectDetails.getElectionTitle()

