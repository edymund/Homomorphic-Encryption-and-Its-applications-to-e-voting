from ..entity.User import User

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