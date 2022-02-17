from app.entity.Projectdetails import ProjectDetails
from ..entity.Candidates import Candidates
from ..entity.Questions import Questions
from ..entity.Answer import Answer
from ..lib.FHE import FHE

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

	def getNumberOfQuestions(self,projID):
		questionEntity = Questions()
		questions = questionEntity.getQuestions(projID)
		
		count = 0 
		for item in questions:
			count = count + 1
		return count

	def insertVoterAns(self,answers,voterID, projectID):
		
		inserted = True
		entity = Answer()
		projectDetails = ProjectDetails(projectID)
		projectPublicKey = projectDetails.getPublicKey()
		fhe = FHE()


		for items in answers:
			if inserted == True:
				for item in items:	
					encryptedVote = FHE.encrypt(projectPublicKey, item["choice"])
					if entity.insertVoterAnswer(voterID,item["candidateID"], encryptedVote) == inserted:
						None
					else:
						inserted = False
						break
			else:
				break
		return inserted
			
					