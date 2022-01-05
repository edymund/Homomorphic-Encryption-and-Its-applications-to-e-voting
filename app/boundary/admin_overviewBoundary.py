from flask import render_template, redirect, flash, session
from app.controllers.admin_overviewController import admin_overviewController

class admin_overviewBoundary:
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		pass

	def displayPage(self):
		return render_template('admin_overview.html')

	def onSubmit(self, title, startDateTime, endDateTime, publicKey):
		userID = session['userID'];   
		controller = admin_overviewController()
		controller.addNewProj(userID, title, startDateTime, endDateTime, publicKey)
		return self.RESPONSE_SUCCESS

	#display success
	def displaySuccess(self):
		flash("Project added successfully. Please check the project in the main ballot page.", 'message')
		return redirect('/mainballot')

	def displayError(self, message):  
		return self.displayPage(message)