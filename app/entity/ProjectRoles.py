from ..dbConfig import dbConnect, dbDisconnect

class ProjectRoles:
	# Constructor for user
	def __init__(self, organizerID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the userID is provided, fill the object with details from database
		hasResult = False
		if organizerID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projectroleID, organizerID, projID, role, approval
								FROM projectroles
								WHERE organizerID = (?)""", (organizerID,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__projectroleID = result[0]
				self.__organizerID = result[1]
				self.__projID = result[2]
				self.__role = result[3]
				self.__approval = result[4]
		
		if not hasResult:
				self.__projectroleID = None
				self.__organizerID = None
				self.__projID = None
				self.__role = None
				self.__approval = None

		dbDisconnect(connection)

	# Verify if the user is an Owner and authorized to view the page
	def getProjectsAsOwner(self, organizerID):
		connection = dbConnect()
		db = connection.cursor()

		if organizerID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projID
								FROM projectroles
								WHERE organizerID = (?) AND role = 'owner' """, (organizerID,)).fetchall()
		
		dbDisconnect(connection)

		if result is None:
			return []
		else:
			projectID = []
			for item in result:
				projectID.append(item[0])
			return projectID

	def checkUserHasOwnerRights(self, organizerID, projectID):
		connection = dbConnect()
		db = connection.cursor()

		if organizerID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projID
								FROM projectroles
								WHERE organizerID = (?) AND projID = (?) AND role = 'owner' """, (organizerID, projectID)).fetchall()
		
		dbDisconnect(connection)

		if result is None:
			return False
		else:
			return True

	def getProjectsAsVerifier(self, organizerID):
		connection = dbConnect()
		db = connection.cursor()

		if organizerID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projID
								FROM projectroles
								WHERE organizerID = (?) AND role = 'verifier' """, (organizerID,)).fetchall()
		
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
		result = db.execute("""select * from projectroles a 
            inner join projdetails b on a.projID = b.projDetailsID 
            where a.organizerID = (?)""", (organizerID,)).fetchall()
		dbDisconnect(connection)
		return result
		# Result array in getProjectDetails
		# ownerID = result[0]
		# organizerID = result[1]
		# projID = result[2]
		# role = result[3]
		# approval = result[4]
		# projDetailsID = result[5]
		# projTitle = result[6]
		# projStatus = result[7]		

	def getVerifiersForProject(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projectroles.projectroleID, projectroles.organizerID, organizers.email
								FROM projectroles
								INNER JOIN organizers ON projectroles.organizerID = organizers.organizerID
								WHERE projectroles.projID = (?) AND projectroles.role = 'verifier' 
								""", (projectID,)).fetchall()
		
		dbDisconnect(connection)


		if result is None:
			return []
		else:
			results = []
			for item in result:
				verifier = {}
				verifier['recordID'] = item[0]
				verifier['organizerID'] = item[1]
				verifier['email'] = item[2]
				results.append(verifier)
			return results

	def addVerifier(self, projectID, email):
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

			# Verify that the email provided is not a existing verifier
			result1 = db.execute("""SELECT organizerID
								FROM projectroles
								WHERE 
									organizerID = (?) AND 
									projID = (?) AND
									role = 'verifier'""", (organizerID, projectID)).fetchone()
			
			if result1 is not None:
				dbDisconnect(connection)
				return False

			# Adds the user into the list of projectroles
			result = db.execute("""INSERT INTO projectroles 
								   (organizerID, projID, role, approval) 
								   VALUES (?,?,?,?)""", (organizerID, projectID, "verifier", None))
			connection.commit()
			dbDisconnect(connection)
			return True
			
		else:
			dbDisconnect(connection)
			return False

	def deleteVerifier(self, projectID, projectroleID):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None and projectroleID is not None:
			result = db.execute("""DELETE FROM projectroles
								   WHERE 
									projectroleID = (?) AND 
									projID = (?)
								   """, (projectroleID, projectID))
		connection.commit()
		dbDisconnect(connection)

		if result.rowcount == 1:
			print("Deleted 1 record")
			return True
		else:
			print("Deleted {} records".format(result.rowcount))
			return False

	def addOwner(self, projectID, organizers_id):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None and organizers_id is not None:
			result = db.execute("""INSERT INTO projectroles 
											(organizerID, projID, role, approval) 
											VALUES (?,?,?,?)""", (organizers_id, projectID, "owner", None))
		connection.commit()
		dbDisconnect(connection)

		return db.lastrowid
	
	def setVerified(self, projectID, organizers_id):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""UPDATE projectroles SET approval = (?) 
								WHERE organizerID = (?) AND projID = (?)""", 
								(True, organizers_id, projectID))
		
		connection.commit()
		# Disconnect from database
		dbDisconnect(connection)

		if result.rowcount == 1:
			# print("Updated Successfully in Database")
			return True
		return False

	def default_approval(self, projectID, organizers_id):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""UPDATE projectroles SET approval = (?) 
								WHERE organizerID = (?) AND projID = (?)""", 
								(False, organizers_id, projectID))
		connection.commit()
		# Disconnect from database
		dbDisconnect(connection)

		if result.rowcount == 1:
			# print("Updated Successfully in Database")
			return True
		return False	

	def allVerifierApprovedProject(self, projectID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""SELECT COUNT(*)
								FROM projectroles 
								WHERE projID = (?) AND
									  role = 'verifier' AND
									  (approval IS NULL or
									  approval IS FALSE)
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
			JOIN projectroles
			on organizers.organizerID = projectroles.organizerID
			where projectroles.projID =(?) 
			and projectroles.role = 'owner'
			""",(projectID,)).fetchone()
		
		return result

	def getOwnersForProject(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		if projectID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT projectroles.projectroleID, projectroles.organizerID, organizers.email
								FROM projectroles
								INNER JOIN organizers ON projectroles.organizerID = organizers.organizerID
								WHERE projectroles.projID = (?) AND projectroles.role = 'owner' 
								""", (projectID,)).fetchone()
		
		dbDisconnect(connection)


		if result is None:
			return []
		else:
			return result