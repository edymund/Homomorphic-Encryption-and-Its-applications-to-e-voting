from distutils.log import error
from flask import render_template, flash, session
from app.controllers.organizer_manageVerifiersController import organizer_manageVerifiersController
from ..entity.Projectdetails import ProjectDetails

class projectOwner_manageAdministratorsBoundary:
	def __init__(self):
		pass

	def displayPage(self, projectID):
		controller = organizer_manageVerifiersController()
		
		projectStatus = controller.getProjectStatus(projectID)
		verifier = controller.getVerifier(projectID)
		
		return render_template('organizer_manageAdministrators.html', projectID=projectID, 
																	  projectStatus=projectStatus,
																  	  subAdministrators=verifier,
																  	  userType=session['userType'])
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage,'error')
		return self.displayPage(projectID)

	def addVerify(self, projectID, email):
		controller = organizer_manageVerifiersController()
		
		# Prevents users from adding themself as sub-administrator
		if email == session['user']:
			return self.displayError(projectID, "Unable to add verifier")
		
		# Add sub admin into database
		if controller.addVerify(projectID, session['user'], email):
			return self.displayPage(projectID)
		
		return self.displayError(projectID, "Failed to add verifier")
	
	def getProjectStatus(self,projectID):
		controller = ProjectDetails(projectID)
		return controller.getStatus()


	def deleteVerifier(self, projectID, administratorID):
		# print("Entered Delete Verifier")
		controller = organizer_manageVerifiersController()
		# print("Complete Constructor")
		# print("Stored Session Value is:", session['organizerID'])
		if controller.removeVerifier(projectID, session['organizerID'], administratorID):
			# print("entered1")
			return self.displayPage(projectID)
		# print("entered2")
		return self.displayError(projectID, "Failed to remove verifier")