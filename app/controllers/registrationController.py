from ..entity.Organizers import Organizers
import hashlib

class registrationController:
	def __init__(self):
		pass
	
	# def encrypt_pw(self,password):
	# 	encoded_password = password.encode()
	# 	encrypted_password = hashlib.sha256(encoded_password).hexdigest()
	# 	return encrypted_password
		
	def addUser(self,email,password,companyName,firstName,lastName):
		user = Organizers()
		# encrypted_password = self.encrypt_pw(password)
		encoded_password = password.encode()
		encrypted_password = hashlib.sha256(encoded_password).hexdigest()

		return user.addNewUser(email,encrypted_password,companyName,firstName,lastName)


