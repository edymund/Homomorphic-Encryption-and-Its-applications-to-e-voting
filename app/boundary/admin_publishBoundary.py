from flask import render_template, redirect, session, flash


class publishBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self,projectID):
		return render_template('admin_publish.html',projectID=projectID, userType = session['userType'])