from ..dbConfig import dbConnect, dbDisconnect

class Questions:
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

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
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