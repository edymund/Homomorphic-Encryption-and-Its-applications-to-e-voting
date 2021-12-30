from ..dbConfig import dbConnect, dbDisconnect

class Projectdetails:
	# Constructor for user
	def __init__(self, projID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the projID  is provided, fill the object with details from database
		hasResult = False
		if projID  is not None:
			# Select election messages from database and populate instance variables
			result = db.execute("""SELECT  projDetailsID, title, status, startDate, startTime, endDate, endTime, publicKey
								FROM projdetails
								WHERE projDetailsID = (?)""", (projID,)).fetchone()

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

	# Accessor method

	def getElectionTitle(self):
		"""retrieve election title"""
		return self.__title