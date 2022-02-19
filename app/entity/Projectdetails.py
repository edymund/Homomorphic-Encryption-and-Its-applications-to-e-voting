from datetime import date
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

	# Verify if the user is a verifier and authorized to view the page
	def insertNewProject(self):
		connection = dbConnect()
		db = connection.cursor()

		# Insert project details into projdetails table
		db.execute("""INSERT INTO projdetails (title, startDate, startTime, endDate, endTime, publicKey)
                        VALUES((?), (?), (?), (?), (?), (?)); """, ("New Project", None, None, None, None, None)) 

		connection.commit()
		dbDisconnect(connection)

		return db.lastrowid

	def getProjectDetails(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""SELECT projDetailsID, title, status, startDate, startTime, endDate, endTime, publicKey
								FROM projdetails
								WHERE projDetailsID = (?)""", (projectID, )).fetchone()
		
		dbDisconnect(connection)

		projectDetails = {}
		projectDetails['id'] = result[0]
		projectDetails['title'] = result[1]
		projectDetails['status'] = result[2]

		if result[3] is None or result[4] is None:
			projectDetails['startDateTime'] = None
		else:
			projectDetails['startDateTime'] = result[3] + "T" + result[4]

		if result[5] is None or result[6] is None:
			projectDetails['endDateTime'] = None
		else:
			projectDetails['endDateTime'] = result[5] + "T" + result[6]
		
		
		projectDetails['publicKey'] = result[7] if result[7] is not None else ""

		return projectDetails

	def updateProject(self, projectID, title, status, startDate, startTime, endDate, endTime, publicKey):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""UPDATE projDetails SET title = (?), 
														status = (?), 
														startDate = (?),
														startTime = (?),
														endDate = (?),
														endTime = (?),
														publicKey = (?)
								WHERE projDetailsID = (?)""", 
								(title, status, startDate, startTime, endDate, endTime, publicKey, projectID))
		
		connection.commit()
		dbDisconnect(connection)

		if db.rowcount == 1:
			return True
		return False

	def deleteProject(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""DELETE FROM projDetails 
								WHERE projDetailsID = (?)""", 
								(projectID,))
		
		connection.commit()
		dbDisconnect(connection)

		if db.rowcount == 1:
			return True
		return False

	def isDraftMode(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""SELECT status
								FROM projdetails
								WHERE projDetailsID = (?)""", 
								(projectID,)).fetchone()
		
		connection.commit()
		dbDisconnect(connection)

		if result[0] == 'DRAFT':
			return True
		else:
			return False

	def setStatusToPendingVerification(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""UPDATE projDetails SET status = 'PENDING APPROVAL'
								WHERE projDetailsID = (?)""", 
								(projectID, ))
		
		connection.commit()
		dbDisconnect(connection)

		if db.rowcount == 1:
			return True
		else:
			return False

	def isPendingVerification(projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""SELECT status
								FROM projdetails
								WHERE projDetailsID = (?)""", 
								(projectID,)).fetchone()
		
		connection.commit()
		dbDisconnect(connection)

		if result[0] == 'PENDING VERIFICATION':
			return True
		else:
			return False

	def setStatusAsPublished(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""UPDATE projDetails SET status = 'PUBLISHED'
								WHERE projDetailsID = (?)""", 
								(projectID, ))
		
		connection.commit()
		dbDisconnect(connection)

		if db.rowcount == 1:
			return True
		else:
			return False
	
	def setStatusAsDraft(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""UPDATE projDetails SET status = 'DRAFT'
								WHERE projDetailsID = (?)""", 
								(projectID, ))
		
		connection.commit()
		dbDisconnect(connection)

		if db.rowcount == 1:
			return True
		else:
			return False
		
	def updateProjectsStatus_Ongoing(self, time):
		connection = dbConnect()
		db = connection.cursor()

		currentDate = time.strftime('%Y-%m-%d')
		currentTime = time.strftime('%H:%M')
		result = db.execute("""UPDATE projDetails SET status = 'ONGOING'
							   WHERE status = 'PUBLISHED' 
							   AND (
								   (startDate = (?) AND startTime <= (?)) OR
								   (startDate < (?))
								)
							   """, 
								(currentDate, currentTime, currentDate))
		
		connection.commit()
		dbDisconnect(connection)
		return

	def updateProjectsStatus_Completed(self, time):
		connection = dbConnect()
		db = connection.cursor()

		currentDate = time.strftime('%Y-%m-%d')
		currentTime = time.strftime('%H:%M')
		result = db.execute("""UPDATE projDetails SET status = 'COMPLETED'
							   WHERE status = 'ONGOING' 
							   AND (
								   (endDate = (?) AND endTime <= (?)) OR
								   (endDate < (?))
								)
							   """, 
								(currentDate, currentTime, currentDate))
		
		connection.commit()
		dbDisconnect(connection)
		return
	
	def checkProjectStatus_Ongoing(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""SELECT *
								FROM projdetails
								WHERE projDetailsID = (?) AND
									  status = 'ONGOING'""", 
								(projectID,)).fetchone()
		
		connection.commit()
		dbDisconnect(connection)

		if result is not None:
			return True

		return False

	def updatePublicKey(self, projectID, publicKey):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""UPDATE projDetails SET publicKey = (?)
							   WHERE projDetailsID = (?)
							   """, 
								(publicKey, projectID))
		connection.commit()
		dbDisconnect(connection)
		return