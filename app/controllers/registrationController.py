from ..entity.Organizers import Organizers
import hashlib

class registrationController:
	def __init__(self):
		pass
			
	def addUser(self,email,password,companyName,firstName,lastName):
		user = Organizers()
		return user.addNewUser(email,password,companyName,firstName,lastName)


