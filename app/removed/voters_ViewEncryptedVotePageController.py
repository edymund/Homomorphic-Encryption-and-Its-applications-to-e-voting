from app.entity.Candidates import Candidates
from ..entity.Answer import Answer
from ..entity.Questions import Questions
from ..entity.Candidates import Candidates

class voters_ViewEncryptedVotePageController:
	def __init__(self):
		pass

	def getVoteResults(self,projID):
		answerEntity = Answer()
		questionEntity = Questions()
		candidateEntity = Candidates()

		answers = answerEntity.getAnsNVoterInfo(projID)
		questions = questionEntity.getQuestions(projID)
		candidates = candidateEntity.getCandidates(projID)

		questionArray = []
		for item in questions:
			question = {}
			question['question'] = item
			question['info'] = []
			question['option'] = []
			for info in answers:
				if item['questionID'] == info['questionID']:
					question['info'].append(info)
			for candidate in candidates:
				if item['questionID'] == candidate['questionID']:
					question['option'].append(candidate)
			questionArray.append(question)

		return questionArray