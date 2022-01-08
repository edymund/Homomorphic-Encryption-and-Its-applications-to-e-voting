from flask import render_template, session, flash, redirect
from ..controllers.organizer_mainBallotController import organizer_mainBallotController

class organizer_mainBallotBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		controller = organizer_mainBallotController()
		organizers_id = session['organizerID']
		data = controller.getProject(organizers_id)
		return render_template('organizer_mainBallot.html',data=data)

	def addNewProject(self):
		controller = organizer_mainBallotController()
		organizers_id = session['organizerID']
		controller.addNewProject(organizers_id)
		return self.displayPage()
