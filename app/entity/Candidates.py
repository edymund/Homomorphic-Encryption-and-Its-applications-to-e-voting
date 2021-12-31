from ..dbConfig import dbConnect, dbDisconnect

class Candidates:
<<<<<<< HEAD
	# Constructor for candidates
	def __init__(self):
		pass

	# Accessor method
	def getCandidateDetails(self,projID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the projID  is provided, fill the object with details from database
		if projID  is not None:
			# Select election messages from database and populate instance variables
			result = db.execute("""SELECT candidateOption, image, description
								FROM candidates
								WHERE projID = (?)""", (projID,)).fetchall()

		dbDisconnect(connection)

		if result is not None:
			"""
			Gets a 2D array containing results from the database.
			returns[recordNo][columnNumber].
			Column 0: Candidate Name, 
			Column 1: Candidate Image, 
			Column 2: Candidate Descriptions
	
			"""
			return result
		else:
			return []
=======
	# Constructor for user
	def __init__(self, candidateID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the NRIC is provided, fill the object with details from database
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
				
			dbDisconnect(connection)
>>>>>>> 129a775435acd1c965011b4dfa42906fae7d6274
