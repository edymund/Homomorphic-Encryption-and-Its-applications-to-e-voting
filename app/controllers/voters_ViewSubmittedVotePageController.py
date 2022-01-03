from ..entity.Electionmsgs import Electionmsgs
from ..entity.ProjectDetails import ProjectDetails

class voters_ViewSubmittedVotePageController:
	def __init__(self):
		pass

	def getElectionMsg(self,projID):
		entity = Electionmsgs(projID)

		return entity.postElectionMsg()

	def getElectionTitle(self,projID):
		entity = ProjectDetails(projID)
		
		return entity.getTitle()