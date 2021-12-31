from ..entity.User import User
import sys

class user_settingsController:
	def __init__(self):
		pass

	def updateUserDetails(self,username,first_name,last_name,email,company_name):

		# Create a user object containing details of the owner
		user = User(username)

		# Update the details of the user
		return user.updateDetails(first_name,last_name,email,company_name)

	