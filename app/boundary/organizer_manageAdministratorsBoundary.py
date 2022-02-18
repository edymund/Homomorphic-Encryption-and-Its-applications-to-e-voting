from distutils.log import error
from flask import render_template, flash, session
from app.controllers.projectOwner_manageAdministratorsController import projectOwner_manageAdministratorsController
from ..entity.Projectdetails import ProjectDetails

class projectOwner_manageAdministratorsBoundary:
	def __init__(self):
		pass

	def displayPage(self, projectID):
		controller = projectOwner_manageAdministratorsController()
		
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
		controller = projectOwner_manageAdministratorsController()
		
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
		controller = projectOwner_manageAdministratorsController()
		# print("Complete Constructor")
		# print("Stored Session Value is:", session['organizerID'])
		if controller.removeVerifier(projectID, session['organizerID'], administratorID):
			# print("entered1")
			return self.displayPage(projectID)
		# print("entered2")
		return self.displayError(projectID, "Failed to remove verifier")