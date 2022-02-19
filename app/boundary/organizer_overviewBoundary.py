from flask import render_template, redirect, flash, session
from app.controllers.organizer_overviewController import organizer_overviewController


class organizer_overviewBoundary:
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		pass

	def displayPage(self, projectID):
		controller = organizer_overviewController()
		projectDetails = controller.getProjectDetails(projectID)
		# print(projectDetails)
		return render_template('organizer_overview.html', projectID=projectID, 
													  	  projectDetails=projectDetails,
														  projectStatus=projectDetails['status'], 
													  	  userType = session['userType'])

	def onSubmit(self, projectID, title, startDateTime, endDateTime):
		organizerID = session['organizerID'];   
		controller = organizer_overviewController()
		if controller.updateProject(projectID, title, startDateTime, endDateTime):
			return self.displaySuccess(projectID)
		else:
			return self.displayError(projectID, "Failed to update details")

	#display success
	def displaySuccess(self, projectID):
		flash("Details Updated Successfully")
		return self.displayPage(projectID)

	def displayError(self, projectID, message): 
		flash(message,'error')
		return self.displayPage(projectID)

	def deleteProject(self, projectID):
		controller = organizer_overviewController()
		if controller.deleteProject(projectID):
			return redirect("/mainballot")
		else:
			self.displayError("Failed to delete project")
	
	def getProjectStatus(self,projectID):
		controller = organizer_overviewController()
		return controller.getProjectStatus(projectID)
	