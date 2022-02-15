from flask import render_template, redirect, session, flash


class admin_downloadResultsBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self, projectID):
		return render_template('admin_downloadResults.html',projectID=projectID)
	
