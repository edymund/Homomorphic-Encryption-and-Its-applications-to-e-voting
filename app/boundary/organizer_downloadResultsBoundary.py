from flask import render_template, redirect, session, flash


class organizer_downloadResultsBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self, projectID):
		return render_template('organizer_downloadResults.html',projectID=projectID)
	
