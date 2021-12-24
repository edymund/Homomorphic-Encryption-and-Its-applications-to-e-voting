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

		# If the username is provided, fill the object with details from database
		if username is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT email, password
								FROM users 
								WHERE email = (?)""", (username,)).fetchone()

		dbDisconnect(connection)

	# Accessor Methods
	def getUserID(self):
		"""Returns the NRIC of the user"""
		return self.__userID

	#verify login credentials
	def verifyLoginDetails(self, username, password):
		""" 
		Verify the login details against retrieved data from database
		Returns True if verified successfully
		Returns False if verification does not match
		"""
		if self.__email == username and self.__password == password:
			return True
		return False

	#create user account
	def addNewUser(self,email,password,companyName,firstName,lastName):
		"""
		Returns True if record is successfully added to database
		"""
		
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()
		db.execute("""INSERT INTO users (email, password, companyName, firstName, lastName)
		VALUES((?), (?), (?), (?), (?))""",(email,password,companyName,firstName,lastName,))
		# insert new user record
		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)

	def updatePassword(self, old_pw, new_pw):
		""" 
		Updates the password of the user. 
		Returns True if updated successfully
		Returns False if update failed
		"""

		#if old password is NOT equal to database return false
		if old_pw != self.__password:
			return False
		
		else:
			# Update the object's recorded password"
			self.__password = new_pw
			# Open connection to database
			connection = dbConnect()
			db = connection.cursor()

			# Update the password for the user
			db.execute("""UPDATE users
						SET password = (?)
						WHERE email = (?)""", (new_pw, self.__email))
			
			# Commit the update to the database
			connection.commit()
			
			# Close the connection to the database
			dbDisconnect(connection)
			
			# Check if any rows have been updated successfully
			if db.rowcount != 0:
				return True
			
			# If no rows has been updated
			return False	
