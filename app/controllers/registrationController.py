from ..entity.User import User

class registrationController:
	def __init__(self):
		pass
	
	def addUser(self,email,password,companyName,firstName,lastName):
		# Create user entity object
		user = User()

		# Create a new user
		return user.addNewUser(email,password,companyName,firstName,lastName)


	