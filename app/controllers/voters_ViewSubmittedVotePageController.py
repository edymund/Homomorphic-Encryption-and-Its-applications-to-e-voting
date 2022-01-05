from ..entity.ElectionMessage import ElectionMessage
from ..entity.Projectdetails import ProjectDetails

class voters_ViewSubmittedVotePageController:
	def __init__(self):
		pass

	def getElectionMsg(self,projID):
		entity = ElectionMessage(projID)

		return entity.getPostMsg()

	def getElectionTitle(self,projID):
		entity = ProjectDetails(projID)
		
		return entity.getTitle()