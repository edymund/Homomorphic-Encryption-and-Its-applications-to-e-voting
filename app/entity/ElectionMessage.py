from ..dbConfig import dbConnect, dbDisconnect
class ElectionMessage:
  def __init__(self, electionMsgID = None, projID= None):
		# Connect to database
        connection = dbConnect()
        db = connection.cursor()
        hasResult = False

        if electionMsgID is not None or projID is not None:
          result = db.execute("""
          SELECT electionMsgsID, projID, preMsg, postMsg, inviteMsg, reminderMsg
          FROM electionmsgs
          WHERE electionMsgID = (?) and projID = (?)
          """),((electionMsgID,projID,)).fetchone()

        # Populate private instance variables with value or None 
        if result is not None:
          hasResult = True
          self.electionMsgsID = result[0]
          self.projID         = result[1]
          self.preMsg         = result[2]
          self.postMsg        = result[3]
          self.inviteMsg      = result[4]
          self.reminderMsg    = result[5]

        if not hasResult:
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
          return self.__electionMsgsID

        def getProjID(self):
          return self.__projID

        def getPreMsg(self):
          return self.__preMsg

        def getPostMsg(self):
          return self.__postMsg

        def getInviteMsg(self):
          return self.__InviteMsg

        def getReminderMsg(self):
          return self.__reminderMsg

        # mutator
        def setPreMsg(self, preMsg):
          if hasResult == True:
            # Open connection to database
            connection = dbConnect()
            db = connection.cursor()
            db.execute("""
            UPDATE electionmsgs
            SET preMsg = (?)
            WHERE electionMsgsID = (?) and projID = (?)
            """,(preMsg, self.__electionMsgsID, self.__projID))
            # Commit the update to the database
            connection.commit()

            # Close the connection to the database
            dbDisconnect(connection)

        def setPostMsg(self, postMsg):
          if hasResult == True:
            # Open connection to database
            connection = dbConnect()
            db = connection.cursor()
            db.execute("""
            UPDATE electionmsgs
            SET postMsg = (?)
            WHERE electionMsgsID = (?) and projID = (?)
            """,(postMsg, self.__electionMsgsID, self.__projID))
            # Commit the update to the database
            connection.commit()

            # Close the connection to the database
            dbDisconnect(connection)

        def setInviteMsg(self, invMsg):
          if hasResult == True:
            # Open connection to database
            connection = dbConnect()
            db = connection.cursor()
            db.execute("""
            UPDATE electionmsgs
            SET inviteMsg = (?)
            WHERE electionMsgsID = (?) and projID = (?)
            """,(invMsg, self.__electionMsgsID, self.__projID))
            # Commit the update to the database
            connection.commit()

            # Close the connection to the database
            dbDisconnect(connection)

        def setReminderMsg(self, rMsg):
          if hasResult == True:
            # Open connection to database
            connection = dbConnect()
            db = connection.cursor()
            db.execute("""
            UPDATE electionmsgs
            SET reminderMsg = (?)
            WHERE electionMsgsID = (?) and projID = (?)
            """,(rMsg, self.__electionMsgsID, self.__projID))
            # Commit the update to the database
            connection.commit()

            # Close the connection to the database
            dbDisconnect(connection)
