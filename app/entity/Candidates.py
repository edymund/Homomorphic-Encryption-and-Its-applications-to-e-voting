from ..dbConfig import dbConnect, dbDisconnect

class Candidates:
	# Constructor for user
	def __init__(self, candidateID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the candidateID is provided, fill the object with details from database
		hasResult = False
		if candidateID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT candidateID, projID, questionID, candidateOption, image, description
								FROM candidates
								WHERE candidateID = (?)""", (candidateID,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__candidateID = result[0]
				self.__projID = result[1]
				self.__questionID = result[2]
				self.__option = result[3]
				self.__imageFilename = result[4]
				self.__description = result[5]
		
		if not hasResult:
				self.__candidateID = None
				self.__projID = None
				self.__questionID = None
				self.__option = None
				self.__imageFilename = None
				self.__description = None

		dbDisconnect(connection)

	def getCandidates(self, projectID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT candidateID, questionID, candidateOption, image, description
								FROM candidates
								WHERE projID = (?)
								ORDER BY questionID DESC""", (projectID,)).fetchall()
		dbDisconnect(connection)
		
		if result is None:
			return []
		else:
			allResults = []
			for items in result:
				candidateDetails = {}
				candidateDetails['candidateID'] = items[0]
				candidateDetails['questionID'] = items[1]
				candidateDetails['candidateOption']  = items[2]
				candidateDetails['imageFilename'] = items[3]
				candidateDetails['description'] = items[4]
				
				allResults.append(candidateDetails)
			return allResults
	
	def getCandidatesByQuestion(self, questionID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if questionID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT candidateID, questionID, candidateOption, image, description
								FROM candidates
								WHERE questionID = (?)
								ORDER BY candidateID ASC""", (questionID,)).fetchall()
		
		
		dbDisconnect(connection)
		
		if result is None:
			return []
		else:
			allResults = []
			for items in result:
				candidateDetails = {}
				candidateDetails['candidateID'] = items[0]
				candidateDetails['questionID'] = items[1]
				candidateDetails['candidateOption']  = items[2]
				candidateDetails['imageFilename'] = items[3]
				candidateDetails['description'] = items[4]
				
				allResults.append(candidateDetails)
			return allResults

	def deleteCandidatesByQuestionID(self, projectID, questionID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if questionID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""DELETE FROM candidates 
								WHERE questionID = (?) AND
										projID = (?)""", (questionID, projectID))
		
		connection.commit()
		
		dbDisconnect(connection)
	
		return True
