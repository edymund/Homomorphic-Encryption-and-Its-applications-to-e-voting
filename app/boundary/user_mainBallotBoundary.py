from flask import render_template, session, flash, redirect
from ..controllers.user_mainBallotController import user_mainBallotController

class user_mainBallotBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		controller = user_mainBallotController()
		user_id = session['userID']
		data = controller.getProject(user_id)
		return render_template('user_mainBallot.html',data=data)
