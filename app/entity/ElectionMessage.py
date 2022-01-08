from ..dbConfig import dbConnect, dbDisconnect
class ElectionMessage:
	def __init__(self, projID= None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the NRIC is provided, fill the object with details from database
		hasResult = False

		if projID is not None: 
			result = db.execute("""
			SELECT electionMsgsID, projID, preMsg, postMsg, inviteMsg, reminderMsg
			FROM electionmsgs
			WHERE  projID = (?)
			""",(projID,)).fetchone()

			# Populate private instance variables with value or None 
			if result is not None:
				hasResult = True
				self.electionMsgsID = result[0]
				self.projID         = result[1]
				self.preMsg         = result[2]
				self.postMsg        = result[3]
				self.inviteMsg      = result[4]
				self.reminderMsg    = result[5]

		else:
			self.electionMsgsID = None
			self.projID         = None
			self.preMsg         = None
			self.postMsg        = None
			self.inviteMsg      = None
			self.reminderMsg    = None

		# Disconnect from database
		dbDisconnect(connection)

		# Accessor 
	def getElectionMsgsID(self):
		return self.electionMsgsID

	def getProjID(self):
		return self.projID

	def getPreMsg(self):
		return self.preMsg

	def getPostMsg(self):
		return self.postMsg

	def getInviteMsg(self):
		return self.inviteMsg

	def getReminderMsg(self):
		return self.reminderMsg

	# mutator
	def setPreMsg(self, preMsg):
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()
		db.execute("""
		UPDATE electionmsgs
		SET preMsg = (?)
		WHERE projID = (?)
		""",(preMsg, self.projID))
		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)

	def setPostMsg(self, postMsg):
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()
		db.execute("""
		UPDATE electionmsgs
		SET postMsg = (?)
		WHERE projID = (?)
		""",(postMsg, self.projID))
		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)

	def setInviteMsg(self, invMsg):
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()
		db.execute("""
		UPDATE electionmsgs
		SET inviteMsg = (?)
		WHERE projID = (?)
		""",(invMsg, self.projID))
		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)

	def setReminderMsg(self, rMsg):
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()
		db.execute("""
		UPDATE electionmsgs
		SET reminderMsg = (?)
		WHERE projID = (?)
		""",(rMsg, self.projID))
		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)

	def createNewRecord(self, projectID):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""INSERT INTO electionmsgs(projID)
								VALUES (?)""", (projectID,))

		connection.commit()

		# Disconnect from database
		dbDisconnect(connection)
		
		return db.lastrowid