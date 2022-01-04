from ..entity.ProjDetails import ProjDetails
from ..entity.User import User
import datetime

class admin_overviewController:
	def __init__(self):
		pass

	def addNewProj(self,userID, title, startDateTime, endDateTime, publicKey):
		""" 
		Returns True if successfully added
		Returns False if an error occured
		"""
		projDetailsEntity = ProjDetails()
		startDateTimeSplit = datetime.datetime.strptime(startDateTime, "%Y" + "-" + "%m" + "-" + "%d" +"T"+ "%H" + ":" + "%M")
		startDate = (startDateTimeSplit.strftime("%Y" + "-" + "%m" + "-" + "%d"))
		startTime = (startDateTimeSplit.strftime("%H" + ":" + "%M"))
		endDateTimeSplit = datetime.datetime.strptime(endDateTime, "%Y" + "-" + "%m" + "-" + "%d" +"T"+ "%H" + ":" + "%M")
		endDate = (endDateTimeSplit.strftime("%Y" + "-" + "%m" + "-" + "%d"))
		endTime = (endDateTimeSplit.strftime("%H" + ":" + "%M"))
		# Ensure that user has rights to projectID
		if userID:
			projDetailsEntity.insertNewProject( userID, title, startDate, startTime, endDate, endTime, publicKey)