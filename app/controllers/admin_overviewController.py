from ..entity.Projectdetails import ProjectDetails
from ..entity.Administrator import Administrator
import datetime

class admin_overviewController:
	def __init__(self):
		pass
	
	def getProjectDetails(self, projectID):
		projectDetails = ProjectDetails()
		return projectDetails.getProjectDetails(projectID)

	def addNewProj(self,userID, title, startDateTime, endDateTime, publicKey):
		""" 
		Returns True if successfully added
		Returns False if an error occured
		"""
		ProjectDetailsEntity = ProjectDetails()
		startDateTimeSplit = datetime.datetime.strptime(startDateTime, "%Y" + "-" + "%m" + "-" + "%d" +"T"+ "%H" + ":" + "%M")
		startDate = (startDateTimeSplit.strftime("%Y" + "-" + "%m" + "-" + "%d"))
		startTime = (startDateTimeSplit.strftime("%H" + ":" + "%M"))
		endDateTimeSplit = datetime.datetime.strptime(endDateTime, "%Y" + "-" + "%m" + "-" + "%d" +"T"+ "%H" + ":" + "%M")
		endDate = (endDateTimeSplit.strftime("%Y" + "-" + "%m" + "-" + "%d"))
		endTime = (endDateTimeSplit.strftime("%H" + ":" + "%M"))
		# Ensure that user has rights to projectID
		if userID:
			ProjectDetailsEntity.insertNewProject( userID, title, startDate, startTime, endDate, endTime, publicKey)

	def updateProject(self, projectID, organizerID, title, startDateTime, endDateTime, publicKey):
		ProjectDetailsEntity = ProjectDetails()

		startDateTimeSplit = datetime.datetime.strptime(startDateTime, "%Y" + "-" + "%m" + "-" + "%d" +"T"+ "%H" + ":" + "%M")
		startDate = (startDateTimeSplit.strftime("%Y" + "-" + "%m" + "-" + "%d"))
		startTime = (startDateTimeSplit.strftime("%H" + ":" + "%M"))
		endDateTimeSplit = datetime.datetime.strptime(endDateTime, "%Y" + "-" + "%m" + "-" + "%d" +"T"+ "%H" + ":" + "%M")
		endDate = (endDateTimeSplit.strftime("%Y" + "-" + "%m" + "-" + "%d"))
		endTime = (endDateTimeSplit.strftime("%H" + ":" + "%M"))

		return ProjectDetailsEntity.updateProject(projectID, title, "DRAFT", startDate, startTime, endDate, endTime, publicKey)
		
