from ..entity.Questions import Questions
from ..entity.Candidates import Candidates
from ..entity.Projectdetails import ProjectDetails

class organizer_viewQuestionsController():
	def __init__(self):
		pass

	def getProjectName(self, projectID):
		projectDetails = ProjectDetails(projectID)
		return projectDetails.getTitle()
	
	def getProjectStatus(self, projectID):
		projectDetails = ProjectDetails(projectID)
		return projectDetails.getStatus()

	def getQuestionsAndAnswers(self, projectID):
		questionEntity = Questions()
		CandidateEntity = Candidates()

		questions = questionEntity.getQuestions(projectID)
		candidates = CandidateEntity.getCandidates(projectID)

		questionArray = []
		for item in questions:
			question = {}
			question['question'] = item
			question['option'] = []
			for candidate in candidates:
				if item['questionID'] == candidate['questionID']:
					question['option'].append(candidate)
			questionArray.append(question)

		return questionArray
