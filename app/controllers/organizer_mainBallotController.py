from ..entity.ProjectRoles import ProjectRoles
from ..entity.Projectdetails import ProjectDetails
from ..entity.ElectionMessage import ElectionMessage

class organizer_mainBallotController:
	def __init__(self):
		pass

	def getProject(self, organizers_id):
		proj = ProjectRoles(organizers_id)
		return proj.getProjectDetails(organizers_id)
	
	def addNewProject(self, organizers_id):
		projectDetails = ProjectDetails()
		projectRoles = ProjectRoles()
		electionMessage = ElectionMessage()

		projectID = projectDetails.insertNewProject()
		organizer = projectRoles.addOwner(projectID, organizers_id)
		electionMessage.createNewRecord(projectID)

		return 
		



