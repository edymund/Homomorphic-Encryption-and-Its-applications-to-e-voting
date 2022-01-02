from ..entity.Administrator import Administrator

class admin_manageAdministratorsController:
	def __init__(self):
		pass

	def getSubAdministrators(self, projectID):
		administratorEntity = Administrator()
		subAdministrators = administratorEntity.getSubAdministratorsForProject(projectID)

		return subAdministrators

	def addSubAdministrator(self, projectID, userID ,email):
		""" 
		Returns True if successfully added
		Returns False if an error occured
		"""
		administratorEntity = Administrator()

		# Ensure that user has rights to projectID
		if administratorEntity.checkUserHasAdminRights(projectID, userID):
			if administratorEntity.addSubAdministrator(projectID, email):
				return True
		return False
	
	def removeSubAdministrator(self, projectID, userID, administratorID):
		administratorEntity = Administrator()

		if administratorEntity.checkUserHasAdminRights(projectID, userID):
			if administratorEntity.deleteSubAdministrator(projectID, administratorID):
				return True
		return False