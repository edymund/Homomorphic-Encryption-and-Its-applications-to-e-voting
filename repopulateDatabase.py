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
            userID INTEGER PRIMARY KEY AUTOINCREMENT,
            email varchar(255) NOT NULL,
            password varchar(255) NOT NULL,
            companyName varchar(255) NOT NULL,
            firstName varchar(255) NOT NULL,
            lastName varchar(255) DEFAULT NULL,
            UNIQUE (userID),
            UNIQUE (email)
            )
			""",  
			"""
			CREATE TABLE administrators (
            administratorsID INTEGER PRIMARY KEY AUTOINCREMENT,
            userID int(11) NOT NULL,
            projID int(11) NOT NULL,
            adminStatus varchar(255) NOT NULL,
            approval BOOLEAN,
            UNIQUE (administratorsID),
            FOREIGN KEY (userID) REFERENCES users (userID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID)
            ) 
			""",
            """
			CREATE TABLE projdetails (
            projDetailsID INTEGER PRIMARY KEY AUTOINCREMENT,
            title varchar(255) NOT NULL,
            status varchar(255) NOT NULL,
            startDate date NOT NULL,
            startTime time NOT NULL,
            endDate date NOT NULL,
            endTime time NOT NULL,
            publicKey varchar(255) NOT NULL,
            UNIQUE (projDetailsID)
            ) 
			""",
			"""
			CREATE TABLE voter (
            voterID INTEGER PRIMARY KEY AUTOINCREMENT,
            email varchar(255) NOT NULL,
            projectID int(11) NOT NULL,
            UNIQUE (voterID),
            FOREIGN KEY (projectID) REFERENCES projdetails (projDetailsID)
            )
			""",
			"""
			CREATE TABLE electionmsgs (
            electionMsgsID INTEGER PRIMARY KEY AUTOINCREMENT,
            projID int(11) DEFAULT NULL,
            preMsg varchar(255) NOT NULL,
            postMsg varchar(255) DEFAULT NULL,
            inviteMsg varchar(255) DEFAULT NULL,
            reminderMsg varchar(255) DEFAULT NULL,
            UNIQUE (electionMsgsID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID)
            )
			""",
			"""
			CREATE TABLE questions (
            questionsID INTEGER PRIMARY KEY AUTOINCREMENT,
            projID int(11) NOT NULL,
            questions varchar(255) NOT NULL,
            questionDesc varchar(255) NOT NULL,
            UNIQUE (questionsID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID)
            )
			""",
			"""
			CREATE TABLE candidates (
            candidateID INTEGER PRIMARY KEY AUTOINCREMENT,
            projID int(11) NOT NULL,
            questionID int(11) NOT NULL,
            candidateOption varchar(255) NOT NULL,
            image varchar(255) DEFAULT NULL,
            description varchar(255) DEFAULT NULL,
            UNIQUE (candidateID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID),
            FOREIGN KEY (questionID) REFERENCES questions (questionsID)
            ) 
			""",
			"""
			CREATE TABLE record (
            recordID INTEGER PRIMARY KEY AUTOINCREMENT,
            projID int(11) NOT NULL,
            questionID int(11) NOT NULL,
            candidateID int(11) NOT NULL,
            UNIQUE (recordID),
            FOREIGN KEY (candidateID) REFERENCES candidates (candidateID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID),
            FOREIGN KEY (questionID) REFERENCES questions (questionsID)
            )
			""",
            """
			CREATE TABLE answer (
            answerID INTEGER PRIMARY KEY AUTOINCREMENT,
            voterID int(11) NOT NULL,
            recordID int(11) NOT NULL,
            encryptedAnswer varchar(255) NOT NULL,
            UNIQUE (answerID),
            FOREIGN KEY (voterID) REFERENCES voter (voterID),
            FOREIGN KEY (recordID) REFERENCES record (recordID)
            ) 
			"""]

# Create all tables
for commands in create:
	mydb.execute(commands)

print('All tables have been created')
# userEmail=['glen@hotmail.com','john@hotmail.com']
# password=['1234','12a4']
# companyName=['abs','abs']
# firstName=['glen','john']
# lastName=['lee','']
# count = 0
# for x in userEmail:
# 			count += 1
# #Insert data for users table
# mycursor.execute("INSERT INTO users (email, password, companyName, firstName, lastName) VALUES( (?), (?), (?), (?), (?) )", (x,password,companyName,firstName,lastName))

#Insert data for users table
userInsertquery = "INSERT INTO users (email, password, companyName, firstName, lastName) VALUES (?,?,?,?,?)"
## storing values in a variable
userInsertvalues = [
    ("glen@hotmail.com","1234","abs","glen","lee"),
    ("john@hotmail.com","12a4","abs","john","NULL")
]

## executing the query with values
mycursor.executemany(userInsertquery, userInsertvalues)


#Insert data for projdetails table
projDetailsInsertquery = "INSERT INTO projdetails (title, status, startDate, startTime, endDate, endTime, publicKey) VALUES (?,?,?,?,?,?,?)"
## storing values in a variable
projDetailsInsertvalues = [
   ("foodpoll","draft","2022-01-08","09:00","2022-01-08","12:00","abababba"),
   ("president","draft","2022-01-10","10:00","2022-01-11","17:00","vavavava")
]

## executing the query with values
mycursor.executemany(projDetailsInsertquery, projDetailsInsertvalues)

#Insert data for administrators table
administratorsInsertquery = "INSERT INTO administrators (userID, projID, adminStatus, approval)  VALUES (?,?,?,?)"
## storing values in a variable
administratorsInsertvalues = [
   (1, 1, "admin",None),
   (2, 1, "sub-admin",None),
   (2, 2, "admin",None)
]

## executing the query with values
mycursor.executemany(administratorsInsertquery, administratorsInsertvalues)

#Insert data for voters table
voterInsertquery = "INSERT INTO voter (email, projectID)  VALUES (?,?)"
## storing values in a variable
voterInsertvalues = [
   ("may@gmail.com",1),
   ("angeline@gmail.com",1),
   ("jake@hotmail.com",1),
   ("emily@hotmail.com",2),
   ("yvonne@gmail.com",2),
   ("bryan@hotmail.com",2)
]

## executing the query with values
mycursor.executemany(voterInsertquery, voterInsertvalues)

#Insert data for electionmsgs table
electionmsgsInsertquery = "INSERT INTO electionmsgs (projID , preMsg, postMsg, inviteMsg, reminderMsg) VALUES (?,?,?,?,?)"
## storing values in a variable
electionmsgsInsertvalues = [
   (1,"pre/msg",None,"invitation","remember to vote")
]

## executing the query with values
mycursor.executemany(electionmsgsInsertquery, electionmsgsInsertvalues)

#Insert data for questions table
questionsInsertquery = "INSERT INTO questions (projID, questions, questionDesc) VALUES (?,?,?)"
## storing values in a variable
questionsInsertvalues = [
   (1,"Q1","Which flavours would you prefer?"),
   (1,"Q2","Can you take spice?"),
   (2,"Q1","Which president would you choose?"),
   (2,"Q2","Which vice president would you choose?")

]
## executing the query with values
mycursor.executemany(questionsInsertquery, questionsInsertvalues)

#Insert data for candidates table
candidatesInsertquery = "INSERT INTO candidates (projID, questionID, candidateOption, image, description) VALUES (?,?,?,?,?)"
## storing values in a variable
candidatesInsertvalues = [
   (1, 1, "apple", "apple.jpg", "an apple a day keeps a doctor away"),
   (1, 1, "orange", "orange.jpg", "its an orange"),
   (1, 1, "strawberry", None, None),
   (1, 2, "yes", "spicy.jpg", "very spicy"),
   (1, 2, "no", None, "not spicy"),
   (2, 1, "jane", "jane.jpg", "10 years of exp"),
   (2, 1, "mike", "mike.jpg", "won youngest entrepreneur award 2020"),
   (2, 2, "jane", "jane.jpg", "10 years of exp"),
   (2, 2, "mike", "mike.jpg", "won youngest entrepreneur award 2020"),
   (2, 2, "melissa", "melissa.jpg", "5 years of exp")
]

## executing the query with values
mycursor.executemany(candidatesInsertquery, candidatesInsertvalues)

#Insert data for record table
recordInsertquery = "INSERT INTO record (projID, questionID, candidateID)  VALUES (?,?,?)"
## storing values in a variable
recordInsertvalues = [
   (1,1,1),
   (1,1,2),
   (1,1,3),
   (1,2,4),
   (1,2,5),
   (2,3,6),
   (2,3,7),
   (2,4,6),
   (2,4,7),
   (2,4,8)
]
## executing the query with values
mycursor.executemany(recordInsertquery, recordInsertvalues)


#Insert data for answer table
answerInsertquery = "INSERT INTO answer (voterID ,recordID, encryptedAnswer) VALUES (?,?,?)"
## storing values in a variable
answerInsertvalues = [
   (1,1,'1'),
   (1,2,'0'),
   (1,3,'0'),
   (1,4,'1'),
   (1,5,'0'),
   (2,1,'0'),
   (2,2,'0'),
   (2,3,'1'),
   (2,4,'1'),
   (2,5,'0'),
   (3,1,'0'),
   (3,2,'1'),
   (3,3,'0'),
   (3,4,'0'),
   (3,5,'1'),
   (4,6,'1'),
   (4,7,'0'),
   (4,8,'0'),
   (4,9,'1'),
   (4,10,'0'),
   (5,6,'0'),
   (5,7,'1'),
   (5,8,'0'),
   (5,9,'0'),
   (5,10,'1'),
   (6,6,'0'),
   (6,7,'1'),
   (6,8,'1'),
   (6,9,'0'),
   (6,10,'0')

]
## executing the query with values
mycursor.executemany(answerInsertquery, answerInsertvalues)

# Commit the update to the database
mydb.commit()


print('All entries committed to database')
# #testing queries
# #test which project has which admin and subadmins
# mycursor.execute("SELECT projdetails.title,users.email, users.firstName,users.lastName,administrators.adminStatus FROM administrators INNER JOIN projdetails ON projdetails.projDetailsID = administrators.projID INNER JOIN users ON users.userID = administrators.userID ORDER BY administrators.projID")

# #test to see if questions and candidates are added into the correct project
# mycursor.execute("SELECT projdetails.title, questions.questions, questions.questionDesc, candidates.candidateOption, candidates.image FROM record INNER JOIN projdetails ON projdetails.projDetailsID = record.projID INNER JOIN questions ON questions.questionsID = record.questionID INNER JOIN candidates ON candidates.candidateID = record.candidateID ORDER BY record.recordID")

# #test to see what all voters vote for
mycursor.execute("SELECT t2.title,t2.questions,t2.questionDesc,t2.candidateOption,t1.email,t1.encryptedAnswer FROM (SELECT voter.email,answer.encryptedAnswer,answer.recordID FROM answer INNER JOIN voter ON voter.voterID = answer.voterID ORDER BY answer.answerID) AS t1 INNER JOIN (SELECT record.recordID,projdetails.title,questions.questions,questions.questionDesc,candidates.candidateOption FROM record INNER JOIN projdetails ON projdetails.projDetailsID = record.projID INNER JOIN questions ON questions.questionsID = record.questionID INNER JOIN candidates ON candidates.candidateID = record.candidateID) AS t2 ON t1.recordID = t2.recordID")
# mycursor.execute("SELECT * FROM users;")
# mycursor.execute("SELECT * FROM administrators;")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

  
# Close the connection to the database
dbDisconnect(mydb)