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
				self.__administratorsID = result[0]
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

	def checkUserHasAdminRights(self, userID, projectID):
		connection = dbConnect()
		db = connection.cursor()

		if userID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projID
								FROM administrators
								WHERE userID = (?) AND projID = (?) AND adminStatus = 'admin' """, (userID, projectID)).fetchall()
		
		dbDisconnect(connection)

		if result is None:
			return False
		else:
			return True

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
		
	def getSubAdministratorsForProject(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT administrators.administratorsID, administrators.userID, users.email
								FROM administrators
								INNER JOIN users ON administrators.userID = users.userID
								WHERE administrators.projID = (?) AND administrators.adminStatus = 'sub-admin' 
								""", (projectID,)).fetchall()
		
		dbDisconnect(connection)

		if result is None:
			return []
		else:
			results = []
			for item in result:
				subadmin = {}
				subadmin['recordID'] = item[0]
				subadmin['userID'] = item[1]
				subadmin['email'] = item[2]
				results.append(subadmin)
			return results

	def addSubAdministrator(self, projectID, email):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None and email is not None:
			# Verify that the email provided is a valid user and gets the ID
			result = db.execute("""SELECT userID
								FROM users
								WHERE email = (?)""", (email,)).fetchone()
			
			if result is None:
				dbDisconnect(connection)
				return False

			userID = result[0]

			# Verify that the email provided is not a existing sub-admin
			result1 = db.execute("""SELECT userID
								FROM administrators
								WHERE 
									userID = (?) AND 
									projID = (?) AND
									adminStatus = 'sub-admin'""", (userID, projectID)).fetchone()
			
			if result1 is not None:
				dbDisconnect(connection)
				return False

			# Adds the user into the list of administrators
			result = db.execute("""INSERT INTO administrators 
								   (userID, projID, adminStatus, approval) 
								   VALUES (?,?,?,?)""", (userID, projectID, "sub-admin", None))
			connection.commit()
			dbDisconnect(connection)
			return True
			
		else:
			dbDisconnect(connection)
			return False

	def deleteSubAdministrator(self, projectID, administratorID):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None and administratorID is not None:
			result = db.execute("""DELETE FROM administrators
								   WHERE 
									administratorsID = (?) AND 
									projID = (?)
								   """, (administratorID, projectID))
		connection.commit()
		dbDisconnect(connection)

		if result.rowcount == 1:
			print("Deleted 1 record")
			return True
		else:
			print("Deleted {} records".format(result.rowcount))
			return False
