### WARNING: ONLY USE THIS IF YOU WANT A CLEAN RESET ON THE DATABASE
###          THIS Will drop all tables and re-create them using a fresh slate
###          ANY CHANGES MADE AFTER INITIAL SETUP WILL BE LOST

# TO REPOPULATE THE DATABASE 
#   1. Copy all classes from entities.py and replace the classes below
#   2. type the following command in command prompt
#      >>> python repopulateDatabase.py

import os
from app.dbConfig import dbConnect, dbDisconnect
from random import randrange, randint, uniform
from datetime import datetime, timedelta


# Delete existing sqlite file
if os.path.exists("app/db.sqlite3"):
  	os.remove("app/db.sqlite3")
else:
  	print("The file does not exist")
	

# Create and connect to database
mydb = dbConnect()
mycursor = mydb.cursor()


#Drop all tables
mycursor.execute("DROP TABLE IF EXISTS voter;")
mycursor.execute("DROP TABLE IF EXISTS  administrators;")
mycursor.execute("DROP TABLE IF EXISTS  answer;")
mycursor.execute("DROP TABLE IF EXISTS  electionmsgs;")
mycursor.execute("DROP TABLE IF EXISTS  record;")
mycursor.execute("DROP TABLE IF EXISTS  candidates;")
mycursor.execute("DROP TABLE IF EXISTS  questions;")
mycursor.execute("DROP TABLE IF EXISTS  projdetails;")
mycursor.execute("DROP TABLE IF EXISTS  users;")

# Recreate all tables again
create = ["""
            CREATE TABLE users (
            userID int(11) NOT NULL,
            email varchar(255) NOT NULL,
            password varchar(255) NOT NULL,
            companyName varchar(255) NOT NULL,
            firstName varchar(255) NOT NULL,
            lastName varchar(255) DEFAULT NULL,
            PRIMARY KEY (userID),
            UNIQUE (userID),
            UNIQUE (email)
            )
			""",  
			"""
			CREATE TABLE administrators (
            administratorsID int(11) NOT NULL,
            userID int(11) NOT NULL,
            projID int(11) NOT NULL,
            adminStatus varchar(255) NOT NULL,
            approval BOOLEAN,
            PRIMARY KEY (administratorsID),
            UNIQUE (administratorsID),
            FOREIGN KEY (userID) REFERENCES users (userID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID)
            ) 
			""",
            """
			CREATE TABLE projdetails (
            projDetailsID int(11) NOT NULL,
            title varchar(255) NOT NULL,
            status varchar(255) NOT NULL,
            startDate date NOT NULL,
            startTime time NOT NULL,
            endDate date NOT NULL,
            endTime time NOT NULL,
            publicKey varchar(255) NOT NULL,
            PRIMARY KEY (projDetailsID),
            UNIQUE (projDetailsID)
            ) 
			""",
			"""
			CREATE TABLE voter (
            voterID int(11) NOT NULL,
            email varchar(255) NOT NULL,
            projectID int(11) NOT NULL,
            PRIMARY KEY (voterID),
            UNIQUE (voterID),
            FOREIGN KEY (projectID) REFERENCES projdetails (projDetailsID)
            )
			""",
			"""
			CREATE TABLE electionmsgs (
            electionMsgsID int(11) NOT NULL,
            projID int(11) DEFAULT NULL,
            preMsg varchar(255) NOT NULL,
            postMsg varchar(255) DEFAULT NULL,
            inviteMsg varchar(255) DEFAULT NULL,
            reminderMsg varchar(255) DEFAULT NULL,
            PRIMARY KEY (electionMsgsID),
            UNIQUE (electionMsgsID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID)
            )
			""",
			"""
			CREATE TABLE questions (
            questionsID int(11) NOT NULL,
            projID int(11) NOT NULL,
            questions varchar(255) NOT NULL,
            questionDesc varchar(255) NOT NULL,
            PRIMARY KEY (questionsID),
            UNIQUE (questionsID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID)
            )
			""",
			"""
			CREATE TABLE candidates (
            candidateID int(11) NOT NULL,
            projID int(11) NOT NULL,
            questionID int(11) NOT NULL,
            candidateOption varchar(255) NOT NULL,
            image varchar(255) DEFAULT NULL,
            description varchar(255) DEFAULT NULL,
            PRIMARY KEY (candidateID),
            UNIQUE (candidateID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID),
            FOREIGN KEY (questionID) REFERENCES questions (questionsID)
            ) 
			""",
			"""
			CREATE TABLE record (
            recordID int(11) NOT NULL,
            projID int(11) NOT NULL,
            questionID int(11) NOT NULL,
            candidateID int(11) NOT NULL,
            PRIMARY KEY (recordID),
            UNIQUE (recordID),
            FOREIGN KEY (candidateID) REFERENCES candidates (candidateID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID),
            FOREIGN KEY (questionID) REFERENCES questions (questionsID)
            )
			""",
            """
			CREATE TABLE answer (
            candidateID int(11) NOT NULL,
            projID int(11) NOT NULL,
            questionID int(11) NOT NULL,
            candidateOption varchar(255) NOT NULL,
            image varchar(255) DEFAULT NULL,
            description varchar(255) DEFAULT NULL,
            PRIMARY KEY (candidateID),
            UNIQUE (candidateID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID),
            FOREIGN KEY (questionID) REFERENCES questions (questionsID)
            ) 
			"""]

# Create all tables
for commands in create:
	mydb.execute(commands)

print('All tables have been created')
userEmail=['glen@hotmail.com','john@hotmail.com']
password=['1234','12a4']
companyName=['abs','abs']
firstName=['glen','john']
lastName=['lee','']
count = 0
for x in firstName:
			count += 1
#Insert data for users table
mycursor.execute("INSERT INTO users (email, password, companyName, firstName, lastName) VALUES (?, ?, ?, ?, ?)", (userEmail,password,companyName,firstName,lastName))



# Commit the update to the database
mydb.commit()

# Close the connection to the database
dbDisconnect(mydb)
print('All entries committed to database')
# #testing queries
# #test which project has which admin and subadmins
# mycursor.execute("SELECT projdetails.title,users.email, users.firstName,users.lastName,administrators.adminStatus FROM administrators INNER JOIN projdetails ON projdetails.projDetailsID = administrators.projID INNER JOIN users ON users.userID = administrators.userID ORDER BY administrators.projID")

# #test to see if questions and candidates are added into the correct project
# mycursor.execute("SELECT projdetails.title, questions.questions, questions.questionDesc, candidates.candidateOption, candidates.image FROM record INNER JOIN projdetails ON projdetails.projDetailsID = record.projID INNER JOIN questions ON questions.questionsID = record.questionID INNER JOIN candidates ON candidates.candidateID = record.candidateID ORDER BY record.recordID")

# #test to see what all voters vote for
mycursor.execute("SELECT t2.title,t2.questions,t2.questionDesc,t2.candidateOption,t1.email,t1.encryptedAnswer FROM (SELECT voter.email,answer.encryptedAnswer,answer.recordID FROM answer INNER JOIN voter ON voter.voterID = answer.voterID ORDER BY answer.answerID) AS t1 INNER JOIN (SELECT record.recordID,projdetails.title,questions.questions,questions.questionDesc,candidates.candidateOption FROM record INNER JOIN projdetails ON projdetails.projDetailsID = record.projID INNER JOIN questions ON questions.questionsID = record.questionID INNER JOIN candidates ON candidates.candidateID = record.candidateID) AS t2 ON t1.recordID = t2.recordID")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)