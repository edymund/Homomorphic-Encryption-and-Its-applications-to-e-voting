from ..entity.Projectdetails import ProjectDetails
from ..entity.Questions import Questions
from ..entity.Candidates import Candidates


class organizer_editQuestionsController:
	def __init__(self):
		pass

	def getProjectName(self, projectID):
		projectDetails = ProjectDetails(projectID)
		# print(projectDetails.getTitle())
		return projectDetails.getTitle()
	
	def getProjectStatus(self, projectID):
		projectDetails = ProjectDetails(projectID)
		return projectDetails.getStatus()

	def getQuestion(self, questionID=None):
		questions = Questions()
		if questionID is None:
			return None
		else:
			# print(questions.getQuestion(questionID))
			return questions.getQuestion(questionID)

	def getCandidates(self, questionID=None): 
		candidates = Candidates()
		if questionID is None:
			return None
		else:
			# print(candidates.getCandidatesByQuestion(questionID))
			return candidates.getCandidatesByQuestion(questionID)

	def saveQuestion(self, projectID, questionID, question):
		questions = Questions()

		return questions.updateQuestion(projectID, questionID, question)

	def checkPermission(self, projectID, questionID):
		questions = Questions()
		
		return questions.checkQuestionIDBelongsToProject(questionID, projectID)

	def addQuestion(self, projectID, question):
		questions = Questions()
		return questions.addQuestion(projectID, question)
	
	def deleteCandidatesByQuestionID(self, projectID, questionID):
		candidates = Candidates()
		candidates.deleteCandidatesByQuestionID(projectID, questionID)

	def deleteQuestionByQuestionID(self, projectID, questionID):
		questions = Questions()
		questions.deleteQuestionByQuestionID(projectID, questionID)
