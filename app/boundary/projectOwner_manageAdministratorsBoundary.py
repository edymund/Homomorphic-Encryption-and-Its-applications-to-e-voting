from flask import render_template, flash, session
from app.controllers.projectOwner_manageAdministratorsController import projectOwner_manageAdministratorsController

class projectOwner_manageAdministratorsBoundary:
	def __init__(self):
		pass

	def displayPage(self, projectID):
		controller = projectOwner_manageAdministratorsController()
		verifier = controller.getVerifier(projectID)
		return render_template('admin_manageAdministrators.html', projectID=projectID, 
																  subAdministrators=verifier,
																  userType=session['userType'])
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage)
		return self.displayPage(projectID)

	def addVerify(self, projectID, email):
		controller = projectOwner_manageAdministratorsController()
		
		# Prevents users from adding themself as sub-administrator
		if email == session['user']:
			return self.displayError(projectID, "Unable to add verifier")
		
		# Add sub admin into database
		if controller.addVerify(projectID, session['user'], email):
			return self.displayPage(projectID)
		
		return self.displayError(projectID, "Failed to add verifier")
		

	def deleteVerifier(self, projectID, administratorID):
		controller = projectOwner_manageAdministratorsController()
		
		if controller.removeVerifier(projectID, session['organizer'], administratorID):
			print("entered1")
			return self.displayPage(projectID)
		print("entered2")
		return self.displayError(projectID, "Failed to remove verifier")