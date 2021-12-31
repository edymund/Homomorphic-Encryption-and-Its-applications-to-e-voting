from ..dbConfig import dbConnect, dbDisconnect

class Questions:
<<<<<<< HEAD
	# Constructor for questions
	def __init__(self, projID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the projID  is provided, fill the object with details from database
		hasResult = False
		if projID  is not None:
			# Select election messages from database and populate instance variables
			result = db.execute("""SELECT  questionsID, projID, questions, questionDesc
								FROM questions
								WHERE projID = (?)""", (projID,)).fetchone()
=======
	# Constructor for user
	def __init__(self, questionID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the NRIC is provided, fill the object with details from database
		hasResult = False
		if questionID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT questionsID, projID, questions, questionDesc
								FROM questions
								WHERE questionsID = (?)""", (questionID,)).fetchone()
>>>>>>> 129a775435acd1c965011b4dfa42906fae7d6274

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
<<<<<<< HEAD
				self.__questionsID = result[0]
				self.__projID = result[1]
				self.__questions = result[2]
				self.__questionDesc = result[3]

		
		if not hasResult:
				self.__questionsID = None
				self.__projID = None
				self.__questions = None
				self.__questionDesc = None


		dbDisconnect(connection)

	def getQuestiondescription(self):
		return self.__questionDesc
=======
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
			# Select User from database and populate instance variables
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

	def addQuestion(self, projectID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		count = db.execute("""Select COUNT(*)
							FROM questions
							WHERE projID = (?)""", (projectID, )).fetchone()
		print("Total Count is ", count[0])

		result = db.execute("""INSERT INTO questions(projID, questions, questionDesc)
								VALUES (?, ?, ?)""", (projectID, None, None))
		# Disconnect from database
		dbDisconnect(connection)
		
>>>>>>> 129a775435acd1c965011b4dfa42906fae7d6274
