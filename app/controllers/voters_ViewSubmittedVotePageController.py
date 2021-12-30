from ..entity.Electionmsgs import Electionmsgs
from ..entity.Projectdetails import Projectdetails

class voters_ViewSubmittedVotePageController:
	def __init__(self):
		pass

	def getElectionMsg(self,projID):
		entity = Electionmsgs(projID)

		return entity.postElectionMsg()

	def getElectionTitle(self,projID):
		entity = Projectdetails(projID)
		
		return entity.getElectionTitle()