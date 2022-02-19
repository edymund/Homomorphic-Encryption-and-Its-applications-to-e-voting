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
			result = db.execute("""SELECT voterNumber,answer.candidateID,encryptedAnswer,projID,questionID,candidateOption
									FROM answer 
									JOIN candidates
									ON answer.candidateID=candidates.candidateID
									JOIN voter
									ON answer.voterID = voter.voterID
									WHERE projID = (?)
									ORDER BY voterNumber ASC, answer.candidateID ASC, questionID ASC""", (projID,)).fetchall()

		dbDisconnect(connection)

		if result is None:
				return []
		else:
				allResults = []
				question = None
				voter = None
				answerDetails = {}
				added = False
				for items in result:
					added=False

					if voter == items[0] and question == items[4]:
						added = True
						answerDetails['encryptedAnswer'].append(items[2])
					else:
						if question != None and voter != None:
							allResults.append(answerDetails)
						added = True
						answerDetails = {}
						answerDetails['voterNumber'] = items[0]
						answerDetails['candidateID'] = items[1]
						answerDetails['encryptedAnswer'] = [items[2]]
						answerDetails['projID'] = items[3]
						answerDetails['questionID'] = items[4]
						answerDetails['candidateOption'] = items[5]
					
					question = items[4]
					voter = items[0]

				if added:
					allResults.append(answerDetails)
				return allResults

	def insertVoterAnswer(self,voterID,candidateID,encryptedAnswer):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		# Ensure that voter has not voted before
		query = db.execute("""SELECT voterID,candidateID,encryptedAnswer 
									FROM answer
									WHERE voterID = (?) AND candidateID = (?)""", (voterID,candidateID)).fetchone()
		if query is not None:
			dbDisconnect(connection)
			return False

		# Insert vote into database
		db.execute("""INSERT INTO answer(voterID, candidateID, encryptedAnswer)
							VALUES (?, ?, ?)""", (voterID, candidateID, encryptedAnswer))
		connection.commit()
		dbDisconnect(connection)
		return True

	def hasVoted(self, voterID):
		connection = dbConnect()
		db = connection.cursor()

		# Select User from database and populate instance variables
		result = db.execute("""SELECT *
								FROM answer
								WHERE voterID = (?)""", (voterID,)).fetchone()
		print("has voted", result)

		dbDisconnect(connection)
		
		if result is not None:
			return True
		return False

	# Get the unique number of people who voted in a project
	def getNumberOfUniqueVoter(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		# Select User from database and populate instance variables
		result = db.execute("""SELECT COUNT(DISTINCT voterID)
							   FROM answer
							   WHERE voterID in (
							   		SELECT voterID
							   		FROM voter
							   		WHERE projectID = (?)
							   );""", (projectID,)).fetchone()

		dbDisconnect(connection)
		
		return int(result[0])
	

	# Get all votes of a specific candidate
	def getVotes(self, candidateID):
		connection = dbConnect()
		db = connection.cursor()

		# Select User from database and populate instance variables
		result = db.execute("""SELECT encryptedAnswer
							   FROM answer
							   WHERE candidateID = (?);""", (candidateID,)).fetchall()

		dbDisconnect(connection)
		
		encryptedAnswers = []
		for row in result:
			encryptedAnswers.append(int(row[0]))
		return encryptedAnswers