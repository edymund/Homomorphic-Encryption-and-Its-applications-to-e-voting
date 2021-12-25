from ..entity.User import User
from ..entity.Administrator import Administrator

class loginController:
	def __init__(self):
		pass

	def validateLogin(self, username, password):
		""" 
		Check if the login details provided by is a valid account 
		Returns True if validated else False
		"""

		# Create a user object containing details of the NRIC owner
		user = User(username)

		# Verify if the NRIC and password is correct
		return user.verifyLoginDetails(username, password)
	
	def getUserID(self, username):
		"""
		Check if the account type of the user
		Returns a string of the account type
		"""

		# Create a user object containing details of the NRIC owner
		user = User(username)

		# Get the type of account that is tied to the NRIC
		return user.getUserID()

	def getProjectID_Admin(self, userID):
		administrator = Administrator(userID)

		return administrator.getProjectsAsAdmin(userID)

	def getProjectID_SubAdmin(self, userID):
		administrator = Administrator(userID)

		return administrator.getProjectsAsSubadmin(userID)