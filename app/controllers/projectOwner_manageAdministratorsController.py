from pickle import FALSE, TRUE
from ..entity.ProjectOwner import ProjectRoles

class projectOwner_manageAdministratorsController:
	def __init__(self):
		pass

	def getVerifier(self, projectID):
		projectOwnerEntity = ProjectRoles()
		verifier = projectOwnerEntity.getVerifiersForProject(projectID)

		return verifier

	def addVerify(self, projectID, userID ,email):
		""" 
		Returns True if successfully added
		Returns False if an error occured
		"""
		projectOwnerEntity = ProjectRoles()

		# Ensure that user has rights to projectID
		if projectOwnerEntity.checkUserHasOwnerRights(projectID, userID):
			if projectOwnerEntity.addVerifier(projectID, email):
				return True
		return False
	
	def removeVerifier(self, projectID, userID, administratorID):
		projectOwnerEntity = ProjectRoles()
		print("entered remove verifier")
		if projectOwnerEntity.checkUserHasOwnerRights(projectID, userID):
			print("TRUE")
			if projectOwnerEntity.deleteVerifier(projectID, administratorID):
				return True
		print("FALSE-----------------------")
		return False