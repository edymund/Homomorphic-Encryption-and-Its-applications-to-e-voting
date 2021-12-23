from ..entity.User import User

class user_changePasswordController:
	def __init__(self):
		pass

	def updatePassword(self, email, old_password, new_password):
		"""
		Updates the mobile number of the user.
		Returns True if successfully updated.
		Returns False if unsuccessful
		"""

		# Create a user object containing details of the NRIC owner
		user = User(email)

		# Update the password of the user
		return user.updatePassword(old_password, new_password)