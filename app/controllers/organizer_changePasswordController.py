from ..entity.Organizers import Organizers
import hashlib

class organizer_changePasswordController:
	def __init__(self):
		pass

	def updatePassword(self, email, old_password, new_password):

		# Create a user object
		user = Organizers(email)
		# Encrypt passwords
		# Update the password of the user
		return user.updatePassword(old_password, new_password)