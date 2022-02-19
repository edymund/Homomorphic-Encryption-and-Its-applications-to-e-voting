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
	
	def getCandidateID(self):
		return self.__candidateID
	
	def getProjectID(self):
		return self.__projID
	
	def getQuestionID(self):
		return self.__questionID
	
	def getOption(self):
		return self.__option
	
	def getImageFilename(self):
		return self.__imageFilename

	def getDescription(self):
		return self.__description

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

	def getCandidateDetails(self, candidateID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if candidateID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT candidateID, questionID, candidateOption, image, description
								FROM candidates
								WHERE candidateID = (?)""", (candidateID,)).fetchone()
		dbDisconnect(connection)
		
		if result is None:
			print("Candidate is None")
			return None
		else:
			candidateDetails = {}
			candidateDetails['candidateID'] = result[0]
			candidateDetails['questionID'] = result[1]
			candidateDetails['candidateOption']  = result[2]
			candidateDetails['imageFilename'] = result[3]
			candidateDetails['description'] = result[4]
			print(candidateDetails)
			return candidateDetails
	
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
	
	def deleteCandidateByCandidateID(self, projectID, questionID, candidateID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if questionID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""DELETE FROM candidates 
								WHERE questionID = (?) AND
										projID = (?) and candidateID = (?)""", (questionID, projectID, candidateID))
		
		connection.commit()
		
		dbDisconnect(connection)
	
		return True

	def checkExists(self, projectID, questionID, candidateID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if questionID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT *
								FROM candidates
								WHERE questionID = (?)
								AND projID = (?)
								AND candidateID = (?)""", (questionID, projectID, candidateID)).fetchone()
		
		dbDisconnect(connection)

		if result is not None:
			return True
		return False

	def updateCandidate(self, candidateID, candidateName, candidateDescription, filename):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if filename is not None:
			result = db.execute("""UPDATE candidates SET candidateOption = ?, 
														image = ?, 
														description = ?
									WHERE candidateID = ?""", 
							(candidateName, filename, candidateDescription, candidateID))
		else:
			result = db.execute("""UPDATE candidates SET candidateOption = ?, 
														description = ?
									WHERE candidateID = ?""", 
							(candidateName, candidateDescription, candidateID))
		
		connection.commit()
		# Disconnect from database
		dbDisconnect(connection)

		if result.rowcount == 1:
			# print("Updated Successfully in Database")
			return True
		return False

	def addNewCandidate(self, projectID, questionID, candidateName, candidateDescription, filename):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""INSERT INTO candidates(projID, questionID, candidateOption, image, description)
								VALUES (?, ?, ?, ?, ?)""", (projectID, questionID, candidateName, filename, candidateDescription))
		
		# print("new id is ", db.lastrowid)
		# count = db.execute("""SELECT candidateID
		# 					FROM candidates
		# 					WHERE projID = (?) AND
		# 					questionID = (?) AND
		# 					candidateOption = (?) AND
		# 					image = (?) AND
		# 					description = (?)""", (projectID, questionID, candidateName, filename, candidateDescription)).fetchone()
		

		connection.commit()

		# Disconnect from database
		dbDisconnect(connection)
		
		return str(db.lastrowid)

	def getCandidateIDsByQuestion(self, questionID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		if questionID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT candidateID
								FROM candidates
								WHERE questionID = (?)
								ORDER BY candidateID ASC""", (questionID,)).fetchall()
		
		
		dbDisconnect(connection)
		
		if result is None:
			return []
		else:
			finalResult = []
			for item in result:
				finalResult.append(item[0])
			return finalResult