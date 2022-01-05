from ..dbConfig import dbConnect, dbDisconnect

class ProjDetails:
	# Constructor for user
	def __init__(self, projectID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		hasResult = False
		if projectID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT *
								FROM projdetails
								WHERE projDetailsID = (?)""", (projectID,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__projDetailsID = result[0]
				self.__title = result[1]
				self.__status = result[2]
				self.__startDate = result[3]
				self.__startTime = result[4]
				self.__endDate = result[5]
				self.__endTime = result[6]
				self.__publicKey = result[7]
		
		if not hasResult:
				self.__projDetailsID = None
				self.__title = None
				self.__status = None
				self.__startDate = None
				self.__startTime = None
				self.__endDate = None
				self.__endTime = None
				self.__publicKey = None

		dbDisconnect(connection)

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

	# Verify if the user is an admin and authorized to view the page
	def insertNewProject(self,userID, title, startDate, startTime, endDate, endTime, publicKey):
		connection = dbConnect()
		db = connection.cursor()

		# Insert project details into projdetails table
		db.execute("""INSERT INTO projdetails (title, startDate, startTime, endDate, endTime, publicKey)
                        VALUES((?), (?), (?), (?), (?), (?)); """, (title,startDate,startTime,endDate,endTime,publicKey,)) 

		# select proj id
		result = db.execute("""SELECT *
							FROM projdetails
							WHERE title = (?)""", (title,)).fetchone()	
		# convert result to int variable
		projID = int(result[0])
							
		# Insert projID with userID and the adminstatus as administrator into administrator table
		db.execute("""INSERT INTO administrators (userID, projID, adminStatus)
		 				VALUES ((?), (?), (?)); """, (userID,projID,'administrator',))
		connection.commit()
		dbDisconnect(connection)