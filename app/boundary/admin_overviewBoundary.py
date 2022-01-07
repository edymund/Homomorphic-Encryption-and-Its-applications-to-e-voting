from flask import render_template, redirect, flash, session
from app.controllers.admin_overviewController import admin_overviewController

class admin_overviewBoundary:
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		pass

	def displayPage(self, projectID):
		controller = admin_overviewController()
		projectDetails = controller.getProjectDetails(projectID)
		print(projectDetails)
		return render_template('admin_overview.html', projectID=projectID, projectDetails=projectDetails)

	def onSubmit(self, title, startDateTime, endDateTime, publicKey):
		organizerID = session['organizerID'];   
		controller = admin_overviewController()
		controller.addNewProj(organizerID, title, startDateTime, endDateTime, publicKey)
		return self.RESPONSE_SUCCESS

	#display success
	def displaySuccess(self):
		flash("Project added successfully. Please check the project in the main ballot page.", 'message')
		return self.displayPage()

	def displayError(self, message):  
		return self.displayPage(message)