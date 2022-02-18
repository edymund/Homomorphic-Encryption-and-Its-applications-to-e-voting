from flask import render_template, redirect, flash, session
from app.controllers.projectOwner_overviewController import projectOwner_overviewController

class admin_overviewBoundary:
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		pass

	def displayPage(self, projectID):
		controller = projectOwner_overviewController()
		projectDetails = controller.getProjectDetails(projectID)
		# print(projectDetails)
		return render_template('organizer_overview.html', projectID=projectID, 
													  projectDetails=projectDetails, 
													  userType = session['userType'])

	def onSubmit(self, projectID, title, startDateTime, endDateTime):
		organizerID = session['organizerID'];   
		controller = projectOwner_overviewController()
		if controller.updateProject(projectID, organizerID, title, startDateTime, endDateTime):
			return self.displaySuccess(projectID)
		else:
			return self.displayError(projectID, "Failed to update details")

	#display success
	def displaySuccess(self, projectID):
		flash("Details Updated Successfully")
		return self.displayPage(projectID)

	def displayError(self, projectID, message): 
		flash(message)
		return self.displayPage(projectID)

	def deleteProject(self, projectID):
		controller = projectOwner_overviewController()
		if controller.deleteProject(projectID):
			return redirect("/mainballot")
		else:
			self.displayError("Failed to delete project")