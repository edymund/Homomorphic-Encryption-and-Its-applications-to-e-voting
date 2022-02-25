from ..entity.Candidates import Candidates
from ..entity.Projectdetails import ProjectDetails
from ..entity.Questions import Questions

class organizer_editAnswersController():
	def __init__(self):
		pass

	def getProjectStatus(self, projectID):
		projectDetails = ProjectDetails(projectID)
		return projectDetails.getStatus()

	def checkPermission(self, projectID, questionID, candidateID):
		candidates = Candidates()
		questions = Questions()
		if candidateID == 'new_candidate':
			return questions.checkQuestionIDBelongsToProject(questionID, projectID)
		return candidates.checkExists(projectID, questionID, candidateID)

	def getProjectName(self, projectID):
		projectDetails = ProjectDetails(projectID)
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
	
	def addNewCandidate(self, projectID, questionID, candidateName, candidateDescription, filename):
		candidates = Candidates()
		return candidates.addNewCandidate(projectID, questionID, candidateName, candidateDescription, filename)