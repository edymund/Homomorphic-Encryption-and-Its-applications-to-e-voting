from flask import render_template, redirect, session, flash
from ..controllers.organizer_emailSettingsController import organizer_emailSettingsController

class organizer_emailSettingBoundary:
	# Constructor
	def __init__(self, projectID= None):
		self.projectID = projectID

	# accessor
	def getProjID(self):
		return self.projectID

	def setProjID(self, projectID):
		self.projectID = projectID

	# Other Methods
	def displayPage(self,projectID):
		controller = organizer_emailSettingsController(projectID)
		projectStatus = controller.getProjectStatus(projectID)
		invMsg = controller.retrieve_inv_msg(projectID)
		rmdMsg = controller.retrieve_rmd_msg(projectID)
		return render_template('organizer_emailSetting.html',invMsg =invMsg, 
															rmdMsg =rmdMsg, 
															projectID = projectID,
															projectStatus=projectStatus,
															userType = session['userType'])
	
	def onSubmit(self,invMsg,rmdMsg,projectID):
		controller = organizer_emailSettingsController(projectID)
		controller.update_rmd_msg(rmdMsg,projectID)
		controller.update_inv_msg(invMsg,projectID)

	def send_reminder(self, msg,projectID):
		controller = organizer_emailSettingsController(projectID)
		if controller.check_msg(msg):
			self.rmdMsg = msg
			controller.update_rmd_msg(msg,projectID)
		else: 
			self.rmdMsg = "Remember to vote!"
			controller.update_rmd_msg(self.rmdMsg,projectID)
		controller.send_reminder(projectID)
		flash("Reminder message is sent")

	
	def getProjectStatus(self,projectID):
		controller = organizer_emailSettingsController(projectID)
		return controller.getProjectStatus(projectID)
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage,'error')
		return self.displayPage(projectID)