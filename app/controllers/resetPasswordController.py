from ..entity.Organizers import Organizers

class resetPasswordController:
	def __init__(self):
		pass

	def checkifEmailexists(self, email):

		# Create a user object containing details of the NRIC owner
		user = Organizers(email)

		# Update the password of the user
		return user.checkEmail(email)

	def resetPw(self, email, new_password):

		# Create a user object containing details of the NRIC owner
		user = Organizers(email)
		# encode int to string
		# Update the password of the user
		return user.resetPassword(new_password)
