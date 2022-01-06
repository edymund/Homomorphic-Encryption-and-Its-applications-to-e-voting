from ..entity.Organizers import Organizers
import sys

class organizer_settingsController:
	def __init__(self):
		pass

	def updateUserDetails(self,username,first_name,last_name,email,company_name):

		# Create a user object containing details of the owner
		user = Organizers(username)

		# Update the details of the user
		return user.updateDetails(first_name,last_name,email,company_name)

	