from ..entity.Organizers import Organizers
from ..entity.ProjectRoles import ProjectRoles

class loginController:
	def __init__(self):
		pass

	def validateLogin(self, username, password):
		""" 
		Check if the login details provided by is a valid account 
		Returns True if validated else False
		"""
		# Create a user object
		user = Organizers(username)
		# Verify if the NRIC and password is correct
		return user.verifyLoginDetails(username, password)
	
	def getOrganizerID(self, username):
		"""
		Check if the account type of the user
		Returns a string of the account type
		"""

		# Create a user object containing details of the NRIC owner
		user = Organizers(username)

		# Get the type of account that is tied to the NRIC 
		return user.getOrganizerID()

	def getProjectID_Owner(self, organizerID):
		owner = ProjectRoles(organizerID)

		return owner.getProjectsAsOwner(organizerID)

	def getProjectID_Verifier(self, organizerID):
		owner = ProjectRoles(organizerID)

		return owner.getProjectsAsVerifier(organizerID)