from flask import render_template, flash, session
from ..controllers.organizer_manageVerifiersController import organizer_manageVerifiersController

class organizer_manageVerifiersBoundary:
	def __init__(self):
		pass

	def displayPage(self, projectID):
		controller = organizer_manageVerifiersController()
		
		projectStatus = controller.getProjectStatus(projectID)
		verifier = controller.getVerifier(projectID)
		
		return render_template('organizer_manageVerifiers.html', projectID=projectID, 
																	  projectStatus=projectStatus,
																  	  verifiers=verifier,
																  	  userType=session['userType'])
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage,'error')
		return self.displayPage(projectID)

	def addVerify(self, projectID, email):
		controller = organizer_manageVerifiersController()
		
		# Prevents users from adding themself as verifier
		if email == session['user']:
			return self.displayError(projectID, "Unable to add verifier")
		
		# Add verifier into database
		if controller.addVerify(projectID, session['user'], email):
			return self.displayPage(projectID)
		
		return self.displayError(projectID, "Failed to add verifier")
	
	def getProjectStatus(self,projectID):
		controller = organizer_manageVerifiersController()
		return controller.getProjectStatus(projectID)


	def deleteVerifier(self, projectID, organizerID):
		# print("Entered Delete Verifier")
		controller = organizer_manageVerifiersController()
		# print("Complete Constructor")
		# print("Stored Session Value is:", session['organizerID'])
		if controller.removeVerifier(projectID, session['organizerID'], organizerID):
			# print("entered1")
			return self.displayPage(projectID)
		# print("entered2")
		return self.displayError(projectID, "Failed to remove verifier")