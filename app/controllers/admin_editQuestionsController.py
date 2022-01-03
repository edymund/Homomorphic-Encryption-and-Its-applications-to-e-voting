from ..entity.ProjectDetails import ProjectDetails
from ..entity.Questions import Questions
from ..entity.Candidates import Candidates

class admin_editQuestionsController:
	def __init__(self):
		pass

	def getProjectName(self, projectID):
		projectDetails = ProjectDetails(projectID)
		print(projectDetails.getTitle())
		return projectDetails.getTitle()

	def getQuestion(self, questionID=None):
		questions = Questions()
		if questionID is None:
			return None
		else:
			print(questions.getQuestion(questionID))
			return questions.getQuestion(questionID)

	def getCandidates(self, questionID=None): 
		candidates = Candidates()
		if questionID is None:
			return None
		else:
			print(candidates.getCandidatesByQuestion(questionID))
			return candidates.getCandidatesByQuestion(questionID)

