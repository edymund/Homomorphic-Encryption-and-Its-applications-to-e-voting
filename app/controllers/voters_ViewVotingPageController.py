from ..entity.Candidates import Candidates
from ..entity.Questions import Questions

class voters_ViewVotingPageController:

	def __init__(self):
		pass
	
	def getQuestionNCandidate(self,projID):
		questionEntity = Questions()
		CandidateEntity = Candidates()

		questions = questionEntity.getQuestions(projID)
		candidates = CandidateEntity.getCandidates(projID)

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
