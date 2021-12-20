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

# -------------------------------------------------
#               Editable Settings
# -------------------------------------------------
# Location History Settings
CHANCE_TO_GO_OUT = 33          # In percentage (33%)
MIN_LOCATION_VISITED = 1        # No of location
MAX_LOCATION_VISITED = 3        # No of location

# Infection Setting
POPULATION_PERCENTAGE_CONFIRMED_INFECTED_DAILY = 0.01	  # In percentage (0.01%)

# Vaccination Settings (Sum to 100)
NOT_ELIGIBLE_FOR_VACCINATION = 10 							
ELIGIBLE_FOR_VACCINATION = 20
SCHEDULED_FOR_FIRST_SHOT = 30
SCHEDULED_FOR_SECOND_SHOT = 30
VACCINATION_COMPLETED = 100 - NOT_ELIGIBLE_FOR_VACCINATION - \
						ELIGIBLE_FOR_VACCINATION - \
						SCHEDULED_FOR_FIRST_SHOT - \
						SCHEDULED_FOR_SECOND_SHOT
print(VACCINATION_COMPLETED)



# Code to create and populate data

#16 ^ 3  = 4096 unique names / accounts
firstName = ['Addison', 'Bowie', 'Carter', 'Drew', 'Eden', 'Finn', 'Gabriel', 'Hayden', 'Jamie', 'Jules', 'Ripley', 'Skylar', 'Ashton', 'Caelan', 'Flynn', 'Kaden']
middleName = ['Angel', 'Asa', 'Bay', 'Blue', 'Cameron', 'Gray', 'Lee', 'Quinn', 'Rue', 'Tate', 'Banks', 'Quince', 'Finley', 'Shea', 'Pace', 'James']
lastName = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Wilson', 'Taylor', 'Moore', 'White', 'Anderson', 'Rodriguez', 'Lopez', 'Walker']
gender = ['M', 'F']

businessID = range(1, 11)
businessName = ['Bapple', 'Amazone', 'Fishbook', 'Boogle', 'McRonald\'s', '7-Melon', 'Sunbucks', 'Blokeswagon', 'Cola Coca', 'Borgar King']
branchLocation = ['Ang Mo Kio', 'Bishan', 'Choa Chu Kang', 'Woodlands', 'Punggol', 'Tampines', 'Pasir Ris', 'Yishun', 'Jurong', 'Sengkang']


# Delete existing sqlite file
if os.path.exists("app/db.sqlite3"):
  	os.remove("app/db.sqlite3")
else:
  	print("The file does not exist")
	

# Create and connect to database
connection = dbConnect()
db = connection.cursor()

# Recreate all tables again
create = ["""
			CREATE TABLE business (
				id INTEGER NOT NULL,
				name VARCHAR(50) NOT NULL,
				PRIMARY KEY (id),
				UNIQUE (name)
			)
			""",  
			"""
			CREATE TABLE organisation (
				id INTEGER NOT NULL,
				name VARCHAR(50) NOT NULL,
				PRIMARY KEY (id),
				UNIQUE (name)
			)
			""",
			"""
			CREATE TABLE user (
				id INTEGER NOT NULL,
				"NRIC" VARCHAR(10) NOT NULL,
				password VARCHAR(50) NOT NULL,
				"firstName" VARCHAR(50) NOT NULL,
				"middleName" VARCHAR(50) NOT NULL,
				"lastName" VARCHAR(50) NOT NULL,
				mobile INTEGER NOT NULL,
				gender VARCHAR(1) NOT NULL,
				"accountActive" BOOLEAN,
				"accountType" VARCHAR(50) NOT NULL,
				PRIMARY KEY (id),
				UNIQUE ("NRIC")
			)
			""",
			"""
			CREATE TABLE location (
	   			id INTEGER NOT NULL,
	   			"businessID" VARCHAR(10) NOT NULL,
	   			"locationName" VARCHAR(100) NOT NULL,
	   			PRIMARY KEY (id),
	   			FOREIGN KEY("businessID") REFERENCES business (id),
	   			UNIQUE ("locationName")
			)
			""",
			"""
			CREATE TABLE business_user (
				id INTEGER NOT NULL,
				"NRIC" VARCHAR(10) NOT NULL,
				"businessID" INTEGER NOT NULL,
				PRIMARY KEY (id),
				UNIQUE ("NRIC"),
				FOREIGN KEY("NRIC") REFERENCES user ("NRIC"),
				FOREIGN KEY("businessID") REFERENCES business (id)
			)
			""",
			"""
			CREATE TABLE health_staff_user (
				id INTEGER NOT NULL,
				"NRIC" VARCHAR(10) NOT NULL,
				"licenseNo" INTEGER NOT NULL,
				PRIMARY KEY (id),
				UNIQUE ("NRIC"),
				FOREIGN KEY("NRIC") REFERENCES user ("NRIC"),
				UNIQUE ("licenseNo")
			)
			""",
			"""
			CREATE TABLE organisation_user (
				id INTEGER NOT NULL,
				"NRIC" VARCHAR(10) NOT NULL,
				"organisationID" INTEGER NOT NULL,
				PRIMARY KEY (id),
				UNIQUE ("NRIC"),
				FOREIGN KEY("NRIC") REFERENCES user ("NRIC"),
				FOREIGN KEY("organisationID") REFERENCES organisation (id)
			)
			""",
			"""
			CREATE TABLE alert (
				id INTEGER NOT NULL,
				sent_by VARCHAR(10) NOT NULL,
				sent_on DATETIME NOT NULL,
				alert_type VARCHAR(100) NOT NULL,
				"recipient_NRIC" VARCHAR(10) NOT NULL,
				message TEXT NOT NULL,
				read_on DATETIME,
				is_read BOOLEAN,
				PRIMARY KEY (id),
				FOREIGN KEY(sent_by) REFERENCES health_staff_user ("NRIC"),
				FOREIGN KEY("recipient_NRIC") REFERENCES user ("NRIC")
			)
			""",
			"""
			CREATE TABLE infected_people (
				id INTEGER NOT NULL,
				"NRIC" VARCHAR(10) NOT NULL,
				infected_on DATETIME NOT NULL,
				PRIMARY KEY (id),
				FOREIGN KEY("NRIC") REFERENCES user ("NRIC")
			)
			""",
			"""
			CREATE TABLE vaccination_status (
				id INTEGER NOT NULL,
				"NRIC" VARCHAR(10) NOT NULL,
				"vaccinationStatus" VARCHAR(50) NOT NULL,
				"dateOfFirstShot" DATETIME,
				"dateOfSecondShot" DATETIME,
				PRIMARY KEY (id),
				FOREIGN KEY("NRIC") REFERENCES user ("NRIC")
			)
			""",
			"""
			CREATE TABLE location_history (
				id INTEGER NOT NULL,
				"NRIC" VARCHAR(10) NOT NULL,
				location_visited INTEGER,
				time_in DATETIME NOT NULL,
				time_out DATETIME NOT NULL,
				PRIMARY KEY (id),
				FOREIGN KEY("NRIC") REFERENCES user ("NRIC"),
				FOREIGN KEY(location_visited) REFERENCES location (id)
			)
			"""]

# Create all tables
for commands in create:
	db.execute(commands)

print('All tables have been created')

# Create BUSINESS record
for business in businessName:
	db.execute("INSERT INTO business(name) values (?)", (business, ))
print('All business entity has been created')

# Create ORGANISATION record
db.execute("INSERT INTO organisation(name) values (?)", ('Ministry of Health', ))
print('All organisation enity created')

# Create USER record
# All users types are added to this database, before randomly deciding if this user
# is a public, business, health staff, organisation user
count = 0
licenseNo = 10000000

# Generate Users ()
for x in firstName:
	for y in middleName:
		for z in lastName:
			count += 1

			# Generate NRIC
			NRIC = 'S'+ '{:04d}'.format(count)

			# Generate a random usertype
			mobile = 90000000 + count
			random_gender = randint(0,len(gender)-1)

			if count < 1000:
				accountType = 'Public'
			elif 1000 <= count < 2000:
				accountType = 'Health Staff'
			elif 2000 <= count < 3000:
				accountType = 'Business'
			else:
				accountType = 'Organisation'

		
			# Add User
			db.execute("""
				Insert into user(NRIC, password, firstName, 
					middleName, lastName, mobile, 
					gender, accountActive, accountType)
				VALUES( (?), (?), (?), (?), (?), (?), (?), (?), (?))""",
				(NRIC, NRIC, x, y, z, mobile, gender[random_gender], True, accountType))
			print('User added. {} new users added.'.format(count), end =' ')


			if count < 1000:
				print('Account type: Public')

			# Generate a health user
			elif 1000 <= count < 2000:
				licenseNo += 1
				db.execute("""INSERT INTO health_staff_user(NRIC, licenseNo) VALUES
								((?), (?))
							""", 
							(NRIC, licenseNo))
				print('Account type: Health Staff')

			# Generate a business user
			elif 2000 <= count < 3000:
				random_businessID = randint(1,len(businessID))
				db.execute(
					"""
						INSERT INTO business_user(NRIC, businessID) VALUES
						((?), (?))
					""", 
					(NRIC, str(random_businessID)))
				print('Account type: Business')

			# Generate a organisation user
			else:
				db.execute("""INSERT INTO organisation_user(NRIC, organisationID) VALUES
								((?), 1)
							""", 
							(NRIC, ))
				print('Account type: Organisation')

db.execute("""UPDATE user
					  SET accountActive = (?)
					  WHERE NRIC = (?)""", (False, "S0777"))

# Generate Locations (100 Locations)
count = 1
allLocations = {}
for business in businessName:
	for branch in branchLocation:
		locationName = '{} - {} Branch'.format(business, branch)
		allLocations[count] = locationName
		db.execute(
			"""
			INSERT INTO LOCATION(businessId, locationName) VALUES ((?), (?))
			""", 
			(count, locationName)
		)
		print('Location entity has been created - {}'.format(locationName))
	count += 1



# Variable Setup
totalNumberOfUsers = range(1, 4097)
numOfDays = range(31, -1, -1)
today = datetime.now()
today = today.replace(hour=0, minute=0, second=0, microsecond=0)


# Generate Location History
noOfRecords = 0
for i in numOfDays:
	for userID in totalNumberOfUsers:
		NRIC = 'S'+ '{:04d}'.format(userID)
		# Random chance to visit location
		chance = randint(0, 100)

		# if user goes out
		if chance <= CHANCE_TO_GO_OUT:

			# Randomly generate number of place visited
			numOfLocationVisited = randint(MIN_LOCATION_VISITED, MAX_LOCATION_VISITED)
			locationVisited = []

			# Add all location visited
			for location in range(numOfLocationVisited):
				visitLocation = randint(1, 100)
				while visitLocation in locationVisited:
					visitLocation = randint(1, 100)
				locationVisited.append(visitLocation)

			# Add to location history
			for location in locationVisited:
				time_in = today - timedelta(i)
				time_in_hour = randint(0, 21)
				time_in_min = randint(0, 59)
				time_in = time_in.replace(hour=time_in_hour, minute=time_in_min)
				time_out = time_in.replace(hour=time_in_hour + randint(1, 2), minute=randint(0, 59))

				db.execute(
					"""
					INSERT INTO location_history(
						NRIC, location_visited, time_in, time_out
					) VALUES ((?), (?), (?), (?))
					""",
					(NRIC, location, time_in, time_out)
				)
				noOfRecords += 1
				print('Location History Record on {}. Total Location history Record = {}'.format(time_in, noOfRecords))

# Generate Infected Record
noOfRecords = 0
for i in numOfDays:
	for userID in totalNumberOfUsers:            
		NRIC = 'S'+ '{:04d}'.format(userID)
		# Random chance to visit location
		chance = uniform(0.00, 100.00)

		#if user is infected
		if chance <= POPULATION_PERCENTAGE_CONFIRMED_INFECTED_DAILY:
			infected_on = visited_on = today - timedelta(i)
			db.execute(
				"""
				INSERT INTO infected_people(NRIC, infected_on)
				VALUES ((?), (?))
				""", 
				(NRIC, infected_on)
			)
			noOfRecords += 1
			print('Infected History Recorded on {}. Total Infected Individual Record = {}'.format(infected_on, noOfRecords))


# Generate random vaccination status
noOfRecords = 0
for userID in totalNumberOfUsers:
	NRIC = 'S'+ '{:04d}'.format(userID)
	
	# Chance for a random vaccination Status 
	chance = uniform(0.00, 100.00)
	
	# Set a status for the user
	status = None

	# If not eligible for vaccination 
	if chance <= NOT_ELIGIBLE_FOR_VACCINATION:
		status = "Not Eligible for Vaccination"
	else:
		chance -= NOT_ELIGIBLE_FOR_VACCINATION

	# if Eligible for vaccination
	if status is None and chance <= ELIGIBLE_FOR_VACCINATION:
		status = "Eligible for Vaccination"
	else:
		chance -= ELIGIBLE_FOR_VACCINATION

	# if Scheduled for first shot
	if status is None and chance <= SCHEDULED_FOR_FIRST_SHOT:
		status = "Scheduled for First Shot"
	else:
		chance -= SCHEDULED_FOR_FIRST_SHOT
	
	# if scheduled for second shot
	if status is None and chance <= SCHEDULED_FOR_SECOND_SHOT:
		status = "Scheduled for Second Shot"
	else:
		chance -= SCHEDULED_FOR_SECOND_SHOT
	
	if status is None and chance <= VACCINATION_COMPLETED: 
		status = "Vaccination Completed"

	start_date = datetime(2021, 4, 1)
	end_date = datetime.today()

	# get first random date
	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = randrange(days_between_dates)
	random_date = start_date + timedelta(days=random_number_of_days)

	# get second random date
	time_between_dates = end_date - random_date
	days_between_dates = time_between_dates.days
	random_number_of_days = randrange(days_between_dates)
	random_date1 = random_date + timedelta(days=random_number_of_days)

	date1 = None
	date2 = None

	if status == "Scheduled for Second Shot":
		date1 = random_date.strftime('%d/%m/%Y, %H:%M:%S')
	elif status == "Vaccination Completed":
		date1 = random_date.strftime('%d/%m/%Y, %H:%M:%S')
		date2 = random_date1.strftime('%d/%m/%Y, %H:%M:%S')

	db.execute(
		"""
		INSERT INTO vaccination_status(
				NRIC, vaccinationStatus, dateOfFirstShot, dateOfSecondShot
		)
		VALUES ((?), (?), (?), (?))
		""",
		(NRIC, status, date1, date2)
	)
	noOfRecords += 1
	print('Added vaccination record for {}. Total Vaccination Record = {}'.format(NRIC, noOfRecords))



# Commit the update to the database
connection.commit()

# Close the connection to the database
dbDisconnect(connection)
print('All entries committed to database')
