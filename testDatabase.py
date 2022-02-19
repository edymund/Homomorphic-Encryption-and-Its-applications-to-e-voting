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
mycursor.execute("DROP TABLE IF EXISTS  projectroles;")
mycursor.execute("DROP TABLE IF EXISTS  answer;")
mycursor.execute("DROP TABLE IF EXISTS  electionmsgs;")
mycursor.execute("DROP TABLE IF EXISTS  candidates;")
mycursor.execute("DROP TABLE IF EXISTS  questions;")
mycursor.execute("DROP TABLE IF EXISTS  projdetails;")
mycursor.execute("DROP TABLE IF EXISTS  organizers;")

# Recreate all tables again
create = ["""
            CREATE TABLE organizers (
            organizerID INTEGER PRIMARY KEY AUTOINCREMENT,
            email varchar(255) NOT NULL,
            password varchar(255) NOT NULL,
            companyName varchar(255) NOT NULL,
            firstName varchar(255) NOT NULL,
            lastName varchar(255) DEFAULT NULL,
            UNIQUE (organizerID),
            UNIQUE (email)
            )
			""",  
			"""
			CREATE TABLE projectroles (
            projectroleID INTEGER PRIMARY KEY AUTOINCREMENT,
            organizerID int(11) NOT NULL,
            projID int(11) NOT NULL,
            role varchar(255) NOT NULL,
            approval BOOLEAN,
            UNIQUE (projectroleID),
            FOREIGN KEY (organizerID) REFERENCES organizers (organizerID) ON DELETE CASCADE,
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID) ON DELETE CASCADE
            ) 
			""",
            """
			CREATE TABLE projdetails (
            projDetailsID INTEGER PRIMARY KEY AUTOINCREMENT,
            title varchar(255) NOT NULL,
            status varchar(255) NOT NULL DEFAULT 'DRAFT',
            startDate date NULL,
            startTime time NULL,
            endDate date NULL,
            endTime time NULL,
            publicKey TEXT NULL,
            UNIQUE (projDetailsID)
            ) 
			""",
			"""
			CREATE TABLE voter (
            voterID INTEGER PRIMARY KEY AUTOINCREMENT,
            voterNumber varchar(255) NOT NULL,
            email varchar(255) NOT NULL,
            projectID int(11) NOT NULL,
            password varchar(255) NOT NULL,
            UNIQUE (voterID),
            FOREIGN KEY (projectID) REFERENCES projdetails (projDetailsID) ON DELETE CASCADE
            )
			""",
			"""
			CREATE TABLE electionmsgs (
            electionMsgsID INTEGER PRIMARY KEY AUTOINCREMENT,
            projID int(11) NOT NULL,
            preMsg varchar(255) DEFAULT NULL,
            postMsg varchar(255) DEFAULT NULL,
            inviteMsg varchar(255) DEFAULT NULL,
            reminderMsg varchar(255) DEFAULT NULL,
            UNIQUE (electionMsgsID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID) ON DELETE CASCADE
            )
			""",
			"""
			CREATE TABLE questions (
            questionsID INTEGER PRIMARY KEY AUTOINCREMENT,
            projID int(11) NOT NULL,
            questions varchar(255) NOT NULL,
            questionDesc varchar(255) NOT NULL,
            UNIQUE (questionsID),
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID) ON DELETE CASCADE
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
            FOREIGN KEY (projID) REFERENCES projdetails (projDetailsID) ON DELETE CASCADE,
            FOREIGN KEY (questionID) REFERENCES questions (questionsID) ON DELETE CASCADE
            ) 
			""",
            """
			CREATE TABLE answer (
            answerID INTEGER PRIMARY KEY AUTOINCREMENT,
            voterID int(11) NOT NULL,
            candidateID int(11) NOT NULL,
            encryptedAnswer varchar(255) NOT NULL,
            UNIQUE (answerID),
            FOREIGN KEY (voterID) REFERENCES voter (voterID) ON DELETE CASCADE,
            FOREIGN KEY (candidateID) REFERENCES candidates (candidateID) ON DELETE CASCADE
            ) 
			"""]

# Create all tables
for commands in create:
	mydb.execute(commands)

print('All tables have been created')
# organizerEmail=['glen@hotmail.com','john@hotmail.com']
# password=['1234','12a4']
# companyName=['abs','abs']
# firstName=['glen','john']
# lastName=['lee','']
# count = 0
# for x in organizerEmail:
# 			count += 1
# #Insert data for organizers table
# mycursor.execute("INSERT INTO organizers (email, password, companyName, firstName, lastName) VALUES( (?), (?), (?), (?), (?) )", (x,password,companyName,firstName,lastName))

#Insert data for organizers table
organizerInsertquery = "INSERT INTO organizers (email, password, companyName, firstName, lastName) VALUES (?,?,?,?,?)"
## storing values in a variable
organizerInsertvalues = [
    ("glen@hotmail.com","a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3","abs","glen","lee"),
    ("john@hotmail.com","a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3","abs","john","NULL"),
        ("abc@hotmail.com","a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3","abs","abc","abc"),
    ("abcdefg@hotmail.com","a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3","abs","abc","abc")
]

## executing the query with values
mycursor.executemany(organizerInsertquery, organizerInsertvalues)


#Insert data for projdetails table
projDetailsInsertquery = "INSERT INTO projdetails (title, status, startDate, startTime, endDate, endTime, publicKey) VALUES (?,?,?,?,?,?,?)"
## storing values in a variable
projDetailsInsertvalues = [
   ("Project Test A","DRAFT","2022-01-08","09:00","2022-01-08","12:00","aaaaaaaa"),
   ("Project Test B","DRAFT","2022-01-10","11:00","2022-01-11","17:00","bbbbbbbb"),
   ("Project Test C","ONGOING","2022-02-10","12:00","2022-03-01","19:00","cccccccc"),
   ("Project Test D","PUBLISHED","2022-02-10","15:00","2022-03-01","20:00","dddddddd"),
   ("Project Test E","ONGOING","2022-02-10","11:00","2022-03-01","17:00","eeeeeeee"),
   ("Project Test F","PUBLISHED","2022-02-10","11:30","2022-03-01","13:00","ffffffff"),
   ("Project Test G","ONGOING","2022-02-10","08:00","2022-03-01","10:00","gggggggg"),
   ("Project Test H","PUBLISHED","2022-02-10","12:00","2022-03-01","13:00","hhhhhhhh"),
   ("Project Test I","ONGOING","2022-02-10","10:00","2022-03-01","17:00","iiiiiiiii"),
   ("Project Test J","DRAFT","2022-02-10","10:00","2022-03-01","17:00","jjjjjjjjj")
]

## executing the query with values
mycursor.executemany(projDetailsInsertquery, projDetailsInsertvalues)

#Insert data for projectroles table
projectroleInsertquery = "INSERT INTO projectroles (organizerID, projID, role, approval)  VALUES (?,?,?,?)"
## storing values in a variable
projectrolesInsertvalues = [
   (1, 1, "owner",None),
   (2, 1, "verifier",None),
   (2, 2, "owner",None),
   (3, 1, "verifier",None),
   (1, 3, "owner",None),
   (1, 4, "owner",None),
   (1, 5, "owner",None),
   (1, 6, "owner",None),
   (1, 7, "owner",None),
   (1, 8, "owner",None),
   (1, 9, "owner",None),
   (2, 10, "owner",None)
]

## executing the query with values
mycursor.executemany(projectroleInsertquery, projectrolesInsertvalues)

#Insert data for voters table
voterInsertquery = "INSERT INTO voter (voterNumber, email, projectID, password)  VALUES (?,?,?,?)"
## storing values in a variable
voterInsertvalues = [
    #in Question 1: a12341,itn7 submitted blank vote and in Question 2: 213ggq submiited blank vote
   ("a12341","may@gmail.com",1,"aaa"),
   ("bhsg12","angeline@gmail.com",1,"bbb"),
   ("ajsh12","jake@hotmail.com",1,"ccc"),
   ("213ggq","emily@hotmail.com",2,"sss"),
   ("sgshh9","yvonne@gmail.com",2,"ddd"),
   ("iop905","bryan@hotmail.com",2,"eee"),
   ("itn7","7@hotmail.com",3,"ttt"),
   #in Question 1: it88 did not submit any votes
   ("it88","8@hotmail.com",3,"ttt123"),
   #in Question 2: it99 did not submit any votes
   ("it99","9@hotmail.com",4,"a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3")
]

## executing the query with values
mycursor.executemany(voterInsertquery, voterInsertvalues)

#Insert data for electionmsgs table
electionmsgsInsertquery = "INSERT INTO electionmsgs (projID , preMsg, postMsg, inviteMsg, reminderMsg) VALUES (?,?,?,?,?)"
## storing values in a variable
electionmsgsInsertvalues = [
   (1,"Do join us in this vote",None,"You are invited to vote","Remember to vote"),
   (2,"pre/msg",None,"invitation","remember to vote")
]

## executing the query with values
mycursor.executemany(electionmsgsInsertquery, electionmsgsInsertvalues)

#Insert data for questions table
questionsInsertquery = "INSERT INTO questions (projID, questions, questionDesc) VALUES (?,?,?)"
## storing values in a variable
questionsInsertvalues = [
   (1,"Q1","Testcase for P.ID 1 Q1"),
   (1,"Q2","Testcase for P.ID 1 Q2"),
   (2,"Q1","Testcase for P.ID 2 Q1"),
   (2,"Q2","Testcase for P.ID 2 Q2"),
   (3,"Q1","Testcase for P.ID 3 Q1"),
   (4,"Q1","Testcase for P.ID 4 Q1"),
   (5,"Q1","Testcase for P.ID 5 Q1"),
   (6,"Q1","Testcase for P.ID 6 Q1"),
   (7,"Q1","Testcase for P.ID 7 Q1"),
   (8,"Q1","Testcase for P.ID 8 Q1"),
   (9,"Q1","Testcase for P.ID 9 Q1"),
   (10,"Q1","Testcase for P.ID 10 Q1")

]
## executing the query with values
mycursor.executemany(questionsInsertquery, questionsInsertvalues)

#Insert data for candidates table
candidatesInsertquery = "INSERT INTO candidates (projID, questionID, candidateOption, image, description) VALUES (?,?,?,?,?)"
## storing values in a variable
candidatesInsertvalues = [
   (1, 1, "ID1_Q1C1", "ID1_Q1C1.jpg", "Project ID 1 Question 1 Candidate 1"),
   (1, 1, "ID1_Q1C2", "ID1_Q1C2.jpg", "Project ID 1 Question 1 Candidate 2"),
   (1, 1, "ID1_Q1C3", None, None),
   (1, 2, "ID1_Q2C4", "ID1_Q2C4.jpg", "Project ID 1 Question 2 Candidate 4"),
   (1, 2, "ID1_Q2C5", None, "Project ID 1 Question 2 Candidate 5"),
   (2, 3, "ID2_Q3C6", "ID2_Q3C6.jpg", "Project ID 2 Question 3 Candidate 6"),
   (2, 3, "ID2_Q3C7", "ID2_Q3C7.jpg", "Project ID 2 Question 3 Candidate 7"),
   (2, 4, "ID2_Q4C8", "ID2_Q4C8.jpg", "Project ID 2 Question 4 Candidate 8"),
   (2, 4, "ID2_Q4C9", "ID2_Q4C9.jpg", "Project ID 2 Question 4 Candidate 9"),
   (3, 5, "ID3_Q5C10", "ID3_Q5C10.jpg", "Project ID 3 Question 5 Candidate 10"),
   (3, 5, "ID3_Q5C11", "ID3_Q5C11.jpg", "Project ID 3 Question 5 Candidate 11"),
   (4, 6, "ID4_Q6C12", "ID4_Q6C12.jpg", "Project ID 4 Question 6 Candidate 12"),
   (4, 6, "ID4_Q6C13", "ID4_Q6C13.jpg", "Project ID 4 Question 6 Candidate 13")
]

## executing the query with values
mycursor.executemany(candidatesInsertquery, candidatesInsertvalues)


#Insert data for answer table
answerInsertquery = "INSERT INTO answer (voterID ,candidateID, encryptedAnswer) VALUES (?,?,?)"
## storing values in a variable
answerInsertvalues = [
    #voterid 1 is a12341, submit blank vote for question 1
   (1,1,'0'),
   (1,2,'0'),
   (1,3,'0'),
   (1,4,'0'),
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
   #voterid 4 is 213ggq, submit blank vote for question 2
   (4,6,'0'),
   (4,7,'0'),
   (4,8,'0'),
   (4,9,'0'),
   (5,6,'0'),
   (5,7,'1'),
   (5,8,'1'),
   (5,9,'0'),
   (6,6,'0'),
   (6,7,'1'),
   (6,8,'0'),
   (6,9,'1'),
   #voterid 7 is itn7, submit blank vote for question 1
   (7,1,'0'),
   (7,2,'0'),
   (7,3,'0'),
   (7,4,'0'),
   (7,5,'0'),
   #voterid 8 it88, did not submit any votes for question 1
   #voterid 9 it99, did not submit any votes for question 2

]
## executing the query with values
mycursor.executemany(answerInsertquery, answerInsertvalues)

# Commit the update to the database
mydb.commit()


print('All entries committed to database')
# #testing queries
# #test which project has which admin and subadmins
# mycursor.execute("SELECT projdetails.title,organizers.email, organizers.firstName,organizers.lastName,administrators.adminStatus FROM administrators INNER JOIN projdetails ON projdetails.projDetailsID = administrators.projID INNER JOIN organizers ON organizers.organizerID = administrators.organizerID ORDER BY administrators.projID")

# #test to see if questions and candidates are added into the correct project
# mycursor.execute("SELECT projdetails.title, questions.questions,questions.questionDesc,candidates.candidateOption FROM candidates INNER JOIN projdetails ON projdetails.projDetailsID = candidates.projID INNER JOIN questions ON questions.questionsID = candidates.questionID")

# #test to see what all voters vote for (including voter 6 digit ID)
# mycursor.execute("SELECT t2.title,t2.questions,t2.questionDesc,t2.candidateOption,t1.voterNumber,t1.email,t1.encryptedAnswer FROM (SELECT voter.voterNumber,voter.email,answer.encryptedAnswer, answer.candidateID FROM answer INNER JOIN voter ON voter.voterID = answer.voterID ORDER BY answer.answerID) AS t1 INNER JOIN (SELECT candidates.candidateID,projdetails.title, questions.questions,questions.questionDesc,candidates.candidateOption FROM candidates INNER JOIN projdetails ON projdetails.projDetailsID = candidates.projID INNER JOIN questions ON questions.questionsID = candidates.questionID) AS t2 ON t1.candidateID = t2.candidateID")
# mycursor.execute("SELECT * FROM organizers;")
# mycursor.execute("SELECT * FROM administrators;")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

  
# Close the connection to the database
dbDisconnect(mydb)