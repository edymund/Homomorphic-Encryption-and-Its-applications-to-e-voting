from ..entity.Candidates import Candidates
from ..entity.Questions import Questions

class voters_ViewVotingPageController:

	def __init__(self):
		pass
	
	def getCandidateDetails(self,projID):
		entity = Candidates()
		
		"""
		Gets a 2D array containing results from the database.
		returns[recordNo][columnNumber].
		Column 0: Candidate Name, 
		Column 1: Candidate Image, 
		Column 2: Candidate Descriptions
 
		"""

		return entity.getCandidateDetails(projID)
	
	def getQuestionDesc(self,projID):
		entity = Questions(projID)

		return entity.getQuestiondescription()
