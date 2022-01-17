from ..entity.Organizers import Organizers
import hashlib

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
		encrypted_password = self.encrypt_pw(new_password)

		# Update the password of the user
		return user.resetPassword(encrypted_password)

	def encrypt_pw(self,password):
		encoded_password = password.encode()
		encrypted_password = hashlib.sha256(encoded_password).hexdigest()
		return encrypted_password