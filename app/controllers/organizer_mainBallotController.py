from ..entity.Administrator import Administrator
from ..entity.Projectdetails import ProjectDetails

class organizer_mainBallotController:
	def __init__(self):
		pass

	def getProject(self, organizers_id):
		proj = Administrator(organizers_id)
		return proj.getProjectDetails(organizers_id)
	
	def addNewProject(self, organizers_id):
		projectDetails = ProjectDetails()
		administrator = Administrator()
		projectID = projectDetails.insertNewProject()
		administrator = administrator.addAdministrator(projectID, organizers_id)
		return 
		



