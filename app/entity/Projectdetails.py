from ..dbConfig import dbConnect, dbDisconnect
class ProjectDetails:
	def __init__(self, projectID=None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the NRIC is provided, fill the object with details from database
		hasResult = False
		if projectID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projDetailsID, title, status, startDate, startTime, endDate, endTime, publicKey
								FROM projdetails
								WHERE projDetailsID = (?)""", (projectID,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__projectID = result[0]
				self.__title = result[1]
				self.__status = result[2]
				self.__startDate = result[3]
				self.__startTime = result[4]
				self.__endDate = result[5]
				self.__endTime = result[6]
				self.__publicKey = result[7]
		
		if not hasResult:
				self.__projectID = None
				self.__title = None
				self.__status = None
				self.__startDate = None
				self.__startTime = None
				self.__endDate = None
				self.__endTime = None
				self.__publicKey = None

		dbDisconnect(connection)
		return

	def getProjectID(self):
		return self.__projectID
	
	def getTitle(self):
		return self.__title

	def getStatus(self):
		return self.__status
	
	def getStartDate(self):
		return self.__startDate
	
	def getStartTime(self):
		return self.__startTime

	def getEndDate(self):
		return self.__endDate
	
	def getEndTime(self):
		return self.__endTime
	
	def getPublicKey(self):
		return self.__publicKey
	