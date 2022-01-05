from ..dbConfig import dbConnect, dbDisconnect

class Questions:
	# Constructor for user
	def __init__(self, questionID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the questionID is provided, fill the object with details from database
		hasResult = False
		if questionID is not None:
			result = db.execute("""SELECT questionsID, projID, questions, questionDesc
								FROM questions
								WHERE questionsID = (?)""", (questionID,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__questionID = result[0]
				self.__projID = result[1]
				self.__questionNo = result[2]
				self.__questionDesc = result[3]
		
		if not hasResult:
				self.__questionID = None
				self.__projID = None
				self.__questionNo = None
				self.__questionDesc = None

		dbDisconnect(connection)
	
	def getQuestions(self, projectID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None:
			result = db.execute("""SELECT questionsID, questions, questionDesc
								FROM questions
								WHERE projID = (?)
								ORDER BY questions ASC""", (projectID,)).fetchall()
		
		dbDisconnect(connection)
		
		if result is None:
			return []
		else:
			allResults = []
			for items in result:
				questionDetails = {}
				questionDetails['questionID'] = items[0]
				questionDetails['questionNo'] = items[1]
				questionDetails['question']  = items[2]
				
				allResults.append(questionDetails)
			return allResults

	def getQuestion(self, questionID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if questionID is not None:
			result = db.execute("""SELECT questionsID, questions, questionDesc
								FROM questions
								WHERE questionsID = (?)""", (questionID,)).fetchone()
		
		dbDisconnect(connection)
		
		if result is None:
			return None
		else:
			questionDetails = {}
			questionDetails['questionID'] = result[0]
			questionDetails['questionNo'] = result[1]
			questionDetails['question']  = result[2]
			return questionDetails
				
	def addQuestion(self, projectID, question):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		count = db.execute("""Select COUNT(*)
							FROM questions
							WHERE projID = (?)""", (projectID, )).fetchone()
		print("Total Count is ", count[0])

		result = db.execute("""INSERT INTO questions(projID, questions, questionDesc)
								VALUES (?, ?, ?)""", (projectID, count[0]+1, question))

		connection.commit()

		# Disconnect from database
		dbDisconnect(connection)
		
		return int(count[0]) + 1

	def updateQuestion(self, projectID, questionID, question):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""UPDATE questions SET questionDesc = ?
						WHERE questionsID = ? and projID = ?""", 
						(question, questionID, projectID))
		
		connection.commit()
		# Disconnect from database
		dbDisconnect(connection)

		if result.rowcount == 1:
			# print("Updated Successfully in Database")
			return True
		return False
	
	def checkQuestionIDBelongsToProject(self, questionID, projectID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if questionID is not None:
			result = db.execute("""SELECT projID
								FROM questions
								WHERE questionsID = (?)""", (questionID,)).fetchone()

		dbDisconnect(connection)
		
		if result is None:
			return False
		else:
			return str(result[0]) == str(projectID)
	
	def deleteQuestionByQuestionID(self, projectID, questionID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if questionID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""DELETE FROM questions 
								WHERE questionsID = (?) AND
										projID = (?)""", (questionID, projectID))
		
		connection.commit()
		dbDisconnect(connection)
		return True	

		
