from ..dbConfig import dbConnect, dbDisconnect

class Administrator:
	# Constructor for user
	def __init__(self, userID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the NRIC is provided, fill the object with details from database
		hasResult = False
		if userID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT administratorsID, userID, projID, adminStatus, approval
								FROM administrators
								WHERE userID = (?)""", (userID,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__administratorsID = result[1]
				self.__userID = result[1]
				self.__projID = result[2]
				self.__adminStatus = result[3]
				self.__approval = result[4]
		
		if not hasResult:
				self.__administratorsID = None
				self.__userID = None
				self.__projID = None
				self.__adminStatus = None
				self.__approval = None

		dbDisconnect(connection)

	# Verify if the user is an admin and authorized to view the page
	def getProjectsAsAdmin(self, userID):
		connection = dbConnect()
		db = connection.cursor()

		if userID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projID
								FROM administrators
								WHERE userID = (?) AND adminStatus = 'admin' """, (userID,)).fetchall()
		
		dbDisconnect(connection)

		if result is None:
			return []
		else:
			projectID = []
			for item in result:
				projectID.append(item[0])
			return projectID

	def getProjectsAsSubadmin(self, userID):
		connection = dbConnect()
		db = connection.cursor()

		if userID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projID
								FROM administrators
								WHERE userID = (?) AND adminStatus = 'sub-admin' """, (userID,)).fetchall()
		
		dbDisconnect(connection)

		if result is None:
			return []
		else:
			projectID = []
			for item in result:
				projectID.append(item[0])
			return projectID
		
	def getProjectDetails(self,user_id):
		connection = dbConnect()
		db = connection.cursor()
		result = db.execute("""select * from administrators a 
            inner join projdetails b on a.projID = b.projDetailsID 
            where a.userID = (?)""", (user_id,)).fetchall()
		dbDisconnect(connection)
		return result
		# Result array in getProjectDetails
		# adminID = result[0]
		# userID = result[1]
		# projID = result[2]
		# adminStatus = result[3]
		# approval = result[4]
		# projDetailsID = result[5]
		# projTitle = result[6]
		# projStatus = result[7]		

