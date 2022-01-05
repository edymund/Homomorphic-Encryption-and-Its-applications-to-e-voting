from ..dbConfig import dbConnect, dbDisconnect

class Answer:
	# Constructor for user
	def __init__(self):
		pass

	def getAnsNVoterInfo(self,projID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if projID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT voterID,answer.candidateID,encryptedAnswer,projID,questionID,candidateOption
									FROM answer 
									JOIN candidates
									ON answer.candidateID=candidates.candidateID
									WHERE projID = (?)
									ORDER BY voterID ASC, answer.candidateID ASC, questionID ASC""", (projID,)).fetchall()

		dbDisconnect(connection)

		if result is None:
				return []
		else:
				allResults = []
				question = None
				voter = None
				answerDetails = {}
				for items in result:
					

					if voter == items[0] and question == items[4]:
						answerDetails['encryptedAnswer'].append(items[2])
					else:
						if question != None and voter != None:
							allResults.append(answerDetails)
						
						answerDetails = {}
						answerDetails['voterID'] = items[0]
						answerDetails['candidateID'] = items[1]
						answerDetails['encryptedAnswer'] = [items[2]]
						answerDetails['projID'] = items[3]
						answerDetails['questionID'] = items[4]
						answerDetails['candidateOption'] = items[5]
					
					question = items[4]
					voter = items[0]

				allResults.append(answerDetails)
				return allResults