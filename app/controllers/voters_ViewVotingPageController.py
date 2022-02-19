from app.entity.Projectdetails import ProjectDetails
from ..entity.Candidates import Candidates
from ..entity.Questions import Questions
from ..entity.Answer import Answer
from ..lib.FHE import FHE

class voters_ViewVotingPageController:

	def __init__(self):
		pass
	
	def submitAnswers(self, answers, projectID, voterID):
		questions = Questions()
		candidates = Candidates()

		successfullyRecorded = True

		projectQuestions = questions.getQuestions(projectID)
		# Check if questionID is part of userSubmitted questionID
		for questionID in projectQuestions:
			questionCandidates = candidates.getCandidateIDsByQuestion(questionID['questionID'])
			try:
				questionID = str(questionID['questionID'])
				for candidateID in questionCandidates:
					# If user's answer == candidateID, count vote as 1
					if answers[questionID] == str(candidateID):
						successfullyRecorded = successfullyRecorded and self.insertVoterAns(candidateID, 1, voterID, projectID)
					# If user's anwer != candidateID, store vote as 0
					else:
						successfullyRecorded = successfullyRecorded and self.insertVoterAns(candidateID, 0, voterID, projectID)

			# If user did not submit a answer for questionID
			except:
				for candidateID in questionCandidates:
					successfullyRecorded = successfullyRecorded and self.insertVoterAns(candidateID, 0, voterID, projectID)
		
		return successfullyRecorded
	
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

	def insertVoterAns(self, candidateID, answer, voterID, projectID):
		
		entity = Answer()
		projectDetails = ProjectDetails(projectID)
		projectPublicKey = projectDetails.getPublicKey()
		fhe = FHE()

		print(f'candidateAnswer: {candidateID}, answer:{answer}')
		# Encrypt vote
		encryptedVote = FHE.encrypt(projectPublicKey, answer)

		# print(f'candidateID = {candidateID}')

		# Record Vote
		return entity.insertVoterAnswer(voterID, candidateID, encryptedVote)

