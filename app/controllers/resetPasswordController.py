from ..entity.User import User

class resetPasswordController:
	def __init__(self):
		pass

	def checkifEmailexists(self, email):

		# Create a user object containing details of the NRIC owner
		user = User(email)

		# Update the password of the user
		return user.checkEmail(email)

	def resetPw(self, email, new_password):

		# Create a user object containing details of the NRIC owner
		user = User(email)

		# Update the password of the user
		return user.resetPassword(new_password)