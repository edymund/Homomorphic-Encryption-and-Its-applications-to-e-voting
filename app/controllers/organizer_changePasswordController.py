from ..entity.Organizers import Organizers
import hashlib

class organizer_changePasswordController:
	def __init__(self):
		pass

	def updatePassword(self, email, old_password, new_password):

		# Create a user object
		user = Organizers(email)
		# Encrypt passwords
		encrypted_old_password = self.encrypt_pw(old_password)
		encrypted_new_password = self.encrypt_pw(new_password)
		# Update the password of the user
		return user.updatePassword(encrypted_old_password, encrypted_new_password)

	def encrypt_pw(self,password):
		encoded_password = password.encode()
		encrypted_password = hashlib.sha256(encoded_password).hexdigest()
		return encrypted_password