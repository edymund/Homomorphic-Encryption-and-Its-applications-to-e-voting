from ..dbConfig import dbConnect, dbDisconnect

class Electionmsgs:
	# Constructor for user
	def __init__(self, projID = None):
		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		# If the projID  is provided, fill the object with details from database
		hasResult = False
		if projID  is not None:
			# Select election messages from database and populate instance variables
			result = db.execute("""SELECT  electionMsgsID, projID, preMsg, postMsg, inviteMsg, reminderMsg
								FROM electionmsgs
								WHERE projID = (?)""", (projID,)).fetchone()

			# If a result is returned, populate object with data
			if result is not None:
				hasResult = True
				# Initialise instance variables for this object
				self.__electionMsgsID = result[0]
				self.__projID = result[1]
				self.__preMsg = result[2]
				self.__postMsg = result[3]
				self.__inviteMsg = result[4]
				self.__reminderMsg = result[5]
		
		if not hasResult:
				self.__electionMsgsID = None
				self.__projID = None
				self.__preMsg = None
				self.__postMsg = None
				self.__inviteMsg = None
				self.__reminderMsg = None

		dbDisconnect(connection)
	
	# Accessor method

	def preElectionMsg(self):
		"""retrieve pre-election message"""
		return self.__preMsg
	
	def postElectionMsg(self):
		"""retrieve Post-election message"""
		return self.__postMsg