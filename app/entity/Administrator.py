from ..dbConfig import dbConnect, dbDisconnect

class Administrator:
	# Constructor for user
	def __init__(self, organizerID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the userID is provided, fill the object with details from database
		hasResult = False
		if organizerID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT administratorsID, organizerID, projID, adminStatus, approval
								FROM administrators
								WHERE organizerID = (?)""", (organizerID,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__administratorsID = result[0]
				self.__organizerID = result[1]
				self.__projID = result[2]
				self.__adminStatus = result[3]
				self.__approval = result[4]
		
		if not hasResult:
				self.__administratorsID = None
				self.__organizerID = None
				self.__projID = None
				self.__adminStatus = None
				self.__approval = None

		dbDisconnect(connection)

	# Verify if the user is an admin and authorized to view the page
	def getProjectsAsAdmin(self, organizerID):
		connection = dbConnect()
		db = connection.cursor()

		if organizerID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projID
								FROM administrators
								WHERE organizerID = (?) AND adminStatus = 'admin' """, (organizerID,)).fetchall()
		
		dbDisconnect(connection)

		if result is None:
			return []
		else:
			projectID = []
			for item in result:
				projectID.append(item[0])
			return projectID

	def checkUserHasAdminRights(self, organizerID, projectID):
		connection = dbConnect()
		db = connection.cursor()

		if organizerID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projID
								FROM administrators
								WHERE organizerID = (?) AND projID = (?) AND adminStatus = 'admin' """, (organizerID, projectID)).fetchall()
		
		dbDisconnect(connection)

		if result is None:
			return False
		else:
			return True

	def getProjectsAsSubadmin(self, organizerID):
		connection = dbConnect()
		db = connection.cursor()

		if organizerID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projID
								FROM administrators
								WHERE organizerID = (?) AND adminStatus = 'sub-admin' """, (organizerID,)).fetchall()
		
		dbDisconnect(connection)

		if result is None:
			return []
		else:
			projectID = []
			for item in result:
				projectID.append(item[0])
			return projectID
		

	def getProjectDetails(self,organizerID):
		connection = dbConnect()
		db = connection.cursor()
		result = db.execute("""select * from administrators a 
            inner join projdetails b on a.projID = b.projDetailsID 
            where a.organizerID = (?)""", (organizerID,)).fetchall()
		dbDisconnect(connection)
		return result
		# Result array in getProjectDetails
		# adminID = result[0]
		# organizerID = result[1]
		# projID = result[2]
		# adminStatus = result[3]
		# approval = result[4]
		# projDetailsID = result[5]
		# projTitle = result[6]
		# projStatus = result[7]		

	def getSubAdministratorsForProject(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT administrators.administratorsID, administrators.organizerID, organizers.email
								FROM administrators
								INNER JOIN organizers ON administrators.organizerID = organizers.organizerID
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
				subadmin['organizerID'] = item[1]
				subadmin['email'] = item[2]
				results.append(subadmin)
			return results

	def addSubAdministrator(self, projectID, email):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None and email is not None:
			# Verify that the email provided is a valid user and gets the ID
			result = db.execute("""SELECT organizerID
								FROM organizers
								WHERE email = (?)""", (email,)).fetchone()
			
			if result is None:
				dbDisconnect(connection)
				return False

			organizerID = result[0]

			# Verify that the email provided is not a existing sub-admin
			result1 = db.execute("""SELECT organizerID
								FROM administrators
								WHERE 
									organizerID = (?) AND 
									projID = (?) AND
									adminStatus = 'sub-admin'""", (organizerID, projectID)).fetchone()
			
			if result1 is not None:
				dbDisconnect(connection)
				return False

			# Adds the user into the list of administrators
			result = db.execute("""INSERT INTO administrators 
								   (organizerID, projID, adminStatus, approval) 
								   VALUES (?,?,?,?)""", (organizerID, projectID, "sub-admin", None))
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

	def addAdministrator(self, projectID, organizers_id):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None and organizers_id is not None:
			result = db.execute("""INSERT INTO administrators 
											(organizerID, projID, adminStatus, approval) 
											VALUES (?,?,?,?)""", (organizers_id, projectID, "admin", None))
		connection.commit()
		dbDisconnect(connection)

		return db.lastrowid
	
	def setVerified(self, projectID, organizers_id):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""UPDATE administrators SET approval = (?) 
								WHERE organizerID = (?) AND projID = (?)""", 
								(True, organizers_id, projectID))
		
		connection.commit()
		# Disconnect from database
		dbDisconnect(connection)

		if result.rowcount == 1:
			# print("Updated Successfully in Database")
			return True
		return False

	def allSubAdminApprovedProject(self, projectID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""SELECT COUNT(*)
								FROM administrators 
								WHERE projID = (?) AND
									  adminStatus = 'sub-admin' AND
									  approval IS NULL
								""", 
								(projectID, )).fetchone()
		

		# Disconnect from database
		dbDisconnect(connection)

		if result[0] == 0:
			print("True")
			return True
		else:
			print("False")
			return False
	
	def get_organizer_info(self,projectID):
		connection = dbConnect()
		db = connection.cursor()
		result = db.execute(""" 
			select firstName, lastName, companyName
			from organizers 
			JOIN administrators
			on organizers.organizerID = administrators.organizerID
			where administrators.projID =(?) 
			and administrators.adminStatus = 'admin'
			""",(projectID,)).fetchone()
		
		return result