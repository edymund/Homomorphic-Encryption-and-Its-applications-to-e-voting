from ..dbConfig import dbConnect, dbDisconnect

class User:
	# Constructor for user
	def __init__(self, username = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the NRIC is provided, fill the object with details from database
		hasResult = False
		if username is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT userID, email, password, companyName, firstName,
										lastName
								FROM users 
								WHERE email = (?)""", (username,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__userID = result[0]
				self.__email = username
				self.__password = result[2]
				self.__firstName = result[3]
				self.__lastName = result[4]
		
		if not hasResult:
				self.__userID = None
				self.__email = None
				self.__password = None
				self.__firstName = None
				self.__lastName = None

		# If the NRIC is provided, fill the object with details from database
		if username is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT email, password
								FROM users 
								WHERE email = (?)""", (username,)).fetchone()

		dbDisconnect(connection)

	def verifyLoginDetails(self, username, password):
		""" 
		Verify the login details against retrieved data from database
		Returns True if verified successfully
		Returns False if verification does not match
		"""
		if self.__email == username and self.__password == password:
			return True
		return False
