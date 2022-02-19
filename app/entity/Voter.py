from ..dbConfig import dbConnect, dbDisconnect
from hashlib import sha256

class Voter:
	def __init__(self, voterID = None):
		# Check email?

		# Connect to database
		connection = dbConnect()
		db = connection.cursor()
		hasResult = False

		if voterID is not None:
			result = db.execute("""
			SELECT voterID, voterNumber, email, projectID
			FROM voter
			WHERE voterID = (?)
			""",(voterID,)).fetchone()

			# Populate private instance variables with value or None 
			if result is not None:
				hasResult = True
				self.voterID    = result[0]
				self.voterNumber = result[1]
				self.email      = result[2]
				self.projectID  = result[3]
			

		if not hasResult:
			self.voterID    = None
			self.voterNumber = None
			self.email      = None
			self.projectID  = None
		
		# Disconnect from database
		dbDisconnect(connection)

	#accessor
	def get_email(self):
		return self.email

	#insert 
	def insert_to_table(self, hash,email,projectID,password=0):
		# Open connection to database
		connection = dbConnect()
		db = connection.cursor()
		db.execute("""
		INSERT INTO voter(voterNumber, email, projectID, password)
		VALUES( (?) ,(?) ,(?) ,(?))
		""",( hash, email, projectID,password))
		# Commit the update to the database
		connection.commit()
		# VoterId, Voter Number, Email, Project ID, password
		# random generate password


		# Close the connection to the database
		dbDisconnect(connection)

	# functions
	# def email_exist(self, projectID,try_email):
	# 	connection = dbConnect()
	# 	db = connection.cursor()
	# 	result = db.execute("""
	# 	SELECT count(1)
	# 	FROM voter
	# 	WHERE projectID = (?) and email = (?) 
	# 	""",(projectID,try_email,)).fetchone()
	# 	if result[0] > 0:
	# 		return True
	# 	elif result[0] <1:
	# 		return False

	def get_all_voters(self,projectID ):
		connection = dbConnect()
		db = connection.cursor()
		result = db.execute(""" 
		SELECT email
		FROM Voter
		WHERE projectID = (?)
		""",(projectID,)).fetchall()

		# Close the connection to the database
		dbDisconnect(connection)
		print(result)
		return result
		
	def get_all_voters_id(self, projID ):
		connection = dbConnect()
		db = connection.cursor()
		result = db.execute(""" 
		SELECT voterID
		FROM Voter
		WHERE projectID = (?)
		""",(projID,)).fetchall()
		return result

	def delete_allVoters(self,projID):
		connection = dbConnect()
		db = connection.cursor()
		db.execute(""" 
		DELETE FROM 
		Voter 
		WHERE 
		projectID = (?)
		""",(projID,))
		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)

	def delete_child(self,voterID,projID):
		connection = dbConnect()
		db = connection.cursor()
		db.execute(""" 
						DELETE FROM
						Answer where
						Answer.answerID in
						(select answer.answerID
						FROM answer 
						INNER JOIN voter
						ON
						answer.voterID = voter.voterID
						WHERE 
						answer.voterID = (?) and voter.projectID =(?))
						""",(voterID,projID,))

		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)

	def getVoterCount(self, projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""SELECT COUNT(*)
					  			FROM voter
					  			WHERE projectID = (?)""",(projectID,)).fetchone()

		# Commit the update to the database
		connection.commit()

		# Close the connection to the database
		dbDisconnect(connection)


		return result[0]

	def get_all_voters_info(self, projectID):
		connection = dbConnect()
		db = connection.cursor()
		result = db.execute("""
		SELECT email,voterNumber
		FROM Voter
		WHERE projectID = (?)
		""",(projectID,)).fetchall()
		dbDisconnect(connection)
		return result	

	def checkVoterCredentials(self, username, password, projectID):
		connection = dbConnect()
		db = connection.cursor()
		hash_password = sha256(password.encode()).hexdigest()

		result = db.execute("""
								SELECT *
								FROM Voter
								WHERE projectID = (?) AND
									  voterNumber = (?) AND
									  password = (?)
								""",(projectID, username, hash_password)).fetchone()

		dbDisconnect(connection)
		
		if result is not None:
			return True
		return result	

	def getVoterID(self, voterNumber, projectID):
		connection = dbConnect()
		db = connection.cursor()

		result = db.execute("""
								SELECT voterID
								FROM Voter
								WHERE projectID = (?) AND
									  voterNumber = (?)
								""",(projectID, voterNumber)).fetchone()

		dbDisconnect(connection)
		
		if result is not None:
			return result[0]
		return None

	def update_pw(self,voter_number,voters_email, projectID,voters_pw):
		connection = dbConnect()
		db = connection.cursor()
		voter_hash_pw = sha256(str(voters_pw).encode()).hexdigest()
		db.execute("""UPDATE Voter
						SET password = (?)
						WHERE 
						voterNumber = (?) and
						email = (?) and
						projectID = (?)
						""", (voter_hash_pw,voter_number,voters_email,projectID))
			
			# Commit the update to the database
		connection.commit()
			
			# Close the connection to the database
		dbDisconnect(connection)
		

