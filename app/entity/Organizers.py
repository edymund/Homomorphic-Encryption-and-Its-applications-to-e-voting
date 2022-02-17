from ..dbConfig import dbConnect, dbDisconnect
from flask import session
import hashlib

class Organizers:
	# Constructor for user
	def __init__(self, username = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the username is provided, fill the object with details from database
		hasResult = False
		if username is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT organizerID, email, password, companyName, firstName,
										lastName
								FROM organizers 
								WHERE email = (?)""", (username,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__organizerID = result[0]
				self.__email = username
				self.__password = result[2]
				self.__companyName = result[3]
				self.__firstName = result[4]
				self.__lastName = result[5]
		
		if not hasResult:
				self.__organizerID = None
				self.__email = None
				self.__password = None
				self.__companyName = None
				self.__firstName = None
				self.__lastName = None

		# If the username is provided, fill the object with details from database
		if username is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT email, password
								FROM organizers 
								WHERE email = (?)""", (username,)).fetchone()

		dbDisconnect(connection)

	# Accessor Methods
	def getOrganizerID(self):
		"""Returns the NRIC of the user"""
		return self.__organizerID

	#verify login credentials
	def verifyLoginDetails(self, username, password):
		""" 
		Verify the login details against retrieved data from database
		Returns True if verified successfully
		Returns False if verification does not match
		"""
		if self.__email == username and self.__password == hashlib.sha256(password.encode()).hexdigest():
			return True
		return False

	#create user account
	def addNewUser(self,email,password,companyName,firstName,lastName):
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()
		db.execute("""INSERT INTO organizers (email, password, companyName, firstName, lastName)
		VALUES((?), (?), (?), (?), (?))""",(email,hashlib.sha256(password.encode()).hexdigest(),companyName,firstName,lastName,))
		# insert new user record
		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)

	def updatePassword(self, old_password, new_password):
		""" 
		Updates the password of the user. 
		Returns True if updated successfully
		Returns False if update failed
		"""

		#if old password is NOT equal to current password return false
		if hashlib.sha256(old_password.encode()).hexdigest() != self.__password:
			return False
		#if new password is equal to current password return same password
		elif hashlib.sha256(new_password.encode()).hexdigest() == self.__password:
			return "Same Password"
		#else if new password is unique from other password
		else:
			# Open connection to database
			connection = dbConnect()
			db = connection.cursor()

			# Update the password for the user
			db.execute("""UPDATE organizers
						SET password = (?)
						WHERE email = (?)""", (hashlib.sha256(new_password.encode()).hexdigest(), self.__email))
			
			# Commit the update to the database
			connection.commit()
			
			# Close the connection to the database
			dbDisconnect(connection)
			
			# Check if any rows have been updated successfully
			if db.rowcount != 0:
				return True
			
			# If no rows has been updated
			return False	

	def resetPassword(self, new_password):
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()

		# Update the password for the user
		db.execute("""UPDATE organizers
					SET password = (?)
					WHERE email = (?)""", (hashlib.sha256(new_password.encode()).hexdigest(), self.__email))
		
		# Commit the update to the database
		connection.commit()
		
		# Close the connection to the database
		dbDisconnect(connection)
		
		# Check if any rows have been updated successfully
		if db.rowcount != 0:
			return True
		
		# If no rows has been updated
		return False

	def updateDetails(self,first_name,last_name,email,company_name):
		"""
		Updates the details of an existing user
		Returns True if record is successfully updated in the database
		"""
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()

		if first_name == "":
			first_name = self.__firstName

		if last_name == "":
			last_name = self.__lastName

		if email == "":
			email = self.__email
		else:
			session['user'] = email

		if company_name == "":
			company_name = self.__companyName

		# Update existing user record
		db.execute("""UPDATE organizers
						SET firstName = (?), lastName = (?),
						email = (?), companyName = (?)
						WHERE organizerID = (?)""", (first_name, last_name, email,
												company_name, self.__organizerID))
		

		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)
		# Check if any rows have been updated successfully
		if db.rowcount != 0:
			return True
			
		# If no rows has been updated
		return False


	def checkEmail(self,email):
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()

		# Update the password for the user
		result = db.execute("""SELECT *
								FROM organizers 
								WHERE email = (?)""", (email,)).fetchone()

		dbDisconnect(connection)
		
		if result is not None:
			return True
		else:
			return False
		
		# Close the connection to the database

	def getUserDetails(self,username):
		connection = dbConnect()
		db = connection.cursor()
		result = db.execute("""SELECT *
								FROM organizers 
								WHERE email = (?)""", (username,)).fetchall()
		dbDisconnect(connection)
		return result