import sqlite3

### THIS IS TO FACILITATE THE SETTINGS OF DATABASE.
### SHOULD THERE BE A NEED TO SWITCH DATABASE. 
### IMPORT AND SETTINGS CAN BE CHANGED HERE

# Directory/name of the database
database = "./app/db.sqlite3"

# Start Connection to database (To be called only when executing a statement)
def dbConnect():
	conn = sqlite3.connect(database)
	conn.execute("PRAGMA foreign_keys = 1")
	return conn

# Close connection to database (To be called after statement execution is over)
def dbDisconnect(connection):
	connection.close()