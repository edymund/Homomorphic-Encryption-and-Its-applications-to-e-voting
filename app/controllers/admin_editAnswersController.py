from ..entity.Candidates import Candidates
from ..entity.Projectdetails import ProjectDetails
from ..entity.Questions import Questions

class admin_editAnswersController():
	def __init__(self):
		pass

	def checkPermission(self, projectID, questionID, candidateID):
		candidates = Candidates()
		questions = Questions()
		if candidateID == 'new_candidate':
			return questions.checkQuestionIDBelongsToProject(questionID, projectID)
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
	
	def deleteCandidate(self, projectID, questionID, candidateID):
		candidates = Candidates()
		return candidates.deleteCandidateByCandidateID(projectID, questionID, candidateID)
	
	def addNewCandidate(self, projectID, questionID, candidateID, candidateName, candidateDescription, filename):
		candidates = Candidates()
		return candidates.addNewCandidate(projectID, questionID, candidateID, candidateName, candidateDescription, filename)

	def getNewCandidateID(self):
		candidates = Candidates()
		return candidates.getNewCandidateID()