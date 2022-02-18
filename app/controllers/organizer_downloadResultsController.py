from app.entity.Candidates import Candidates
from app.entity.Questions import Questions
from ..entity.Voter import Voter
from ..entity.Answer import Answer
from ..entity.Projectdetails import ProjectDetails
from ..lib.FHE import FHE
from ..lib.AES_CBC import AES_CBC
import json

class organizer_downloadResultsController:
	def __init__(self):
		pass

	def getProjectStatus(self, projectID):
		projectDetails = ProjectDetails(projectID)
		return projectDetails.getStatus()

	# Get Total Number of Voters for the project
	def getTotalNumberOfVoters(self, projectID):
		voter = Voter()
		return voter.getVoterCount(projectID)

	# Get Unique Number of People who voted for the project
	def getNumberOfVotersVoted(self, projectID):
		answer = Answer()
		return answer.getNumberOfUniqueVoter(projectID)

	def getVotingData(self, projectID):
		'''
		[ProjectName] = ?
		[questions] = array of (['question'] = ?
					  			['candidate'] = array of ([name]
														  [voteCount]))
		'''
		
		projectDetails = ProjectDetails(projectID)
		questions = Questions()
		candidates = Candidates()
		answer = Answer()
		fhe=FHE()

		projectName = projectDetails.getTitle()
		publicKey = projectDetails.getPublicKey()
		
		votingData = {}
		votingData['ProjectName'] = projectName

		# Get all Questions in project
		dataset = []
		questionList = questions.getQuestions(projectID)
		for question in questionList:
			item = {} 
			item['question'] = question['question']
			item['candidate'] = []
			# Get all candidates for question
			candidateList = candidates.getCandidatesByQuestion(question['questionID'])
			for candidate in candidateList:
				candidateData = {}
				# Store Candidate Name
				candidateData['name'] = candidate['candidateOption']
				
				# Store Total Candidate's Vote
				encryptedVotes = answer.getVotes(candidate['candidateID'])
				totalEncryptedVote = FHE.getEncryptedSum(encryptedVotes, publicKey)
				candidateData['voteCount'] = totalEncryptedVote

				# Add candidate to question
				item['candidate'].append(candidateData)

			# Add question to list of questions
			dataset.append(item)
		
		votingData['questions'] = dataset
		
		return votingData
	
	def getEncryptedVotingData(self, projectID, aes_key):
		votingData = self.getVotingData(projectID)
		votingDataAsString = json.dumps(votingData)

		aes = AES_CBC(aes_key)
		return aes.encrypt(votingDataAsString)
