from ..entity.Candidates import Candidates
from ..entity.ProjDetails import ProjDetails

class admin_editAnswersController():
	def __init__(self):
		pass

	def checkPermission(self, projectID, questionID, candidateID):
		candidates = Candidates()
		return candidates.checkExists(projectID, questionID, candidateID)

	def getProjectName(self, projectID):
		projectDetails = ProjDetails(projectID)
		return projectDetails.getTitle()
	
	def getCandidateDetails(self, candidateID):
		candidates = Candidates()
		return candidates.getCandidateDetails(candidateID)
	
	def updateCandidate(self, candidateID, candidateName, candidateDescription, filename):
		candidates = Candidates()
		return candidates.updateCandidate(candidateID, candidateName, candidateDescription, filename)