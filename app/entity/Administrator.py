from ..dbConfig import dbConnect, dbDisconnect

class Administrator:
	# Constructor for user
	def __init__(self, administratorID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the NRIC is provided, fill the object with details from database
		hasResult = False
		if administratorID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT administratorsID, userID, projID, adminStatus, approval
								FROM administratorsID
								WHERE administratorID = (?)""", (administratorID,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__administratorsID = administratorID
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
	def verifyPermission(self, userID, projectID):
		connection = dbConnect()
		db = connection.cursor()

		if userID is not None:
			# Select User from database and populate instance variables
			result = db.execute("""SELECT adminStatus
								FROM administratorsID
								WHERE administratorID = (?) and projID = (?)""", (userID, projectID)).fetchone()
		
		dbDisconnect(connection)

		if result is not None:
			return True
		return False

		
		

