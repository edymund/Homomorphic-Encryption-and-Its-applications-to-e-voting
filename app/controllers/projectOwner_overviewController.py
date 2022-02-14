from ..entity.Projectdetails import ProjectDetails
from ..entity.ProjectOwner import ProjectRoles
import datetime

class projectOwner_overviewController:
	def __init__(self):
		pass
	
	def getProjectDetails(self, projectID):
		projectDetails = ProjectDetails()
		return projectDetails.getProjectDetails(projectID)

	def updateProject(self, projectID, organizerID, title, startDateTime, endDateTime, publicKey):
		ProjectDetailsEntity = ProjectDetails()
		if startDateTime == "":
			startDate = None
			startTime = None
		else:
			startDateTimeSplit = datetime.datetime.strptime(startDateTime, "%Y" + "-" + "%m" + "-" + "%d" +"T"+ "%H" + ":" + "%M")
			startDate = (startDateTimeSplit.strftime("%Y" + "-" + "%m" + "-" + "%d"))
			startTime = (startDateTimeSplit.strftime("%H" + ":" + "%M"))
		
		if endDateTime == "":
			endDate = None
			endTime = None
		else:
			endDateTimeSplit = datetime.datetime.strptime(endDateTime, "%Y" + "-" + "%m" + "-" + "%d" +"T"+ "%H" + ":" + "%M")
			endDate = (endDateTimeSplit.strftime("%Y" + "-" + "%m" + "-" + "%d"))
			endTime = (endDateTimeSplit.strftime("%H" + ":" + "%M"))

		return ProjectDetailsEntity.updateProject(projectID, title, "DRAFT", startDate, startTime, endDate, endTime, publicKey)
		
	def deleteProject(self, projectID):
		projectDetails = ProjectDetails()

		return projectDetails.deleteProject(projectID)