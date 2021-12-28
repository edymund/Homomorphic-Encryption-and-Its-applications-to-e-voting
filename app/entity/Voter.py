from ..dbConfig import dbConnect, dbDisconnect
class Voter:
    def __init__(self, projectID = None):
        # Check email?

		# Connect to database
        connection = dbConnect()
        db = connection.cursor()
        hasResult = False

        if projectID is not None:
            result = db.execute("""
            SELECT voterID, email, projectID
            FROM voter
            WHERE projectID = (?)
            """,(projectID,)).fetchone()

            # Populate private instance variables with value or None 
            if result is not None:
                hasResult = True
                self.voterID    = result[0]
                self.email      = result[1]
                self.projectID  = result[2]


        if not hasResult:
          self.electionMsgsID = None
          self.projID         = None
          self.preMsg         = None
      
        # Disconnect from database
        dbDisconnect(connection)

    #accessor
    def get_email(self):
        return self.__email

    #insert 
    def insert_to_table(self, new_email, projectID):
        # Open connection to database
        connection = dbConnect()
        db = connection.cursor()
        db.execute("""
        INSERT INTO voter(email, projectID)
        VALUES( (?) ,(?))
        """,( new_email, projectID))
        # Commit the update to the database
        connection.commit()

        # Close the connection to the database
        dbDisconnect(connection)
        
    # functions
    def email_exist(self, projectID,try_email):
        connection = dbConnect()
        db = connection.cursor()
        result = db.execute("""
        SELECT email, projectID
        FROM voter
        WHERE projectID = (?) and email = (?) 
        """),((projectID,try_email,)).fetchone()
        if result != None:
            return True
        else:
            return False

    # def highest_voterID(self, projID):
    #     connection = dbConnect()
    #     db = connection.cursor()
    #     result = db.execute(""" 
    #     SELECT MAX(voterID)
    #     FROM Voter
    #     WHERE projectID = (?)
    #     """,(projID))
    #     if result == None:
    #         return 0
    #     else:
    #         return result

    def get_all_voters(self, projID ):
        connection = dbConnect()
        db = connection.cursor()
        result = db.execute(""" 
        SELECT email
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
