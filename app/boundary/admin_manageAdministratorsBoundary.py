from flask import render_template, flash, session
from app.controllers.admin_manageAdministratorsController import admin_manageAdministratorsController

class admin_manageAdministratorsBoundary:
	def __init__(self):
		pass

	def displayPage(self, projectID):
		controller = admin_manageAdministratorsController()
		subAdministrators = controller.getSubAdministrators(projectID)
		return render_template('admin_manageAdministrators.html', projectID=projectID, subAdministrators=subAdministrators)
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage)
		return self.displayPage(projectID)

	def addSubAdministrator(self, projectID, email):
		controller = admin_manageAdministratorsController()
		
		# Prevents users from adding themself as sub-administrator
		if email == session['user']:
			return self.displayError(projectID, "Unable to add as sub-administrator")
		
		# Add sub admin into database
		if controller.addSubAdministrator(projectID, session['user'], email):
			return self.displayPage(projectID)
		
		return self.displayError(projectID, "Failed to add sub-admin")
		

	def deleteAdministrator(self, projectID, administratorID):
		controller = admin_manageAdministratorsController()
		
		if controller.removeSubAdministrator(projectID, session['user'], administratorID):
			return self.displayPage(projectID)
		
		return self.displayError(projectID, "Failed to remove sub-admin")