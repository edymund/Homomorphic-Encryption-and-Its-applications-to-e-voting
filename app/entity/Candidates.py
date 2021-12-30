from ..dbConfig import dbConnect, dbDisconnect

class Candidates:
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