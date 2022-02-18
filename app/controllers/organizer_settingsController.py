from ..entity.Organizers import Organizers

class organizer_settingsController:
	def __init__(self):
		pass

	def getUserDetails(self, username):
		getDetails = Organizers(username)
		return getDetails.getUserDetails(username)

	def updateUserDetails(self,username,first_name,last_name,email,company_name):

		# Create a user object containing details of the owner
		user = Organizers(username)

		# Update the details of the user
		return user.updateDetails(first_name,last_name,email,company_name)

	