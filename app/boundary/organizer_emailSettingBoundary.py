from flask import render_template, redirect, session, flash
from ..controllers.organizer_emailSettingsController import organizer_emailSettingsController
from ..entity.Projectdetails import ProjectDetails

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
		invMsg = controller.retrieve_inv_msg(projectID)
		rmdMsg = controller.retrieve_rmd_msg(projectID)
		self.process_inv_msg(invMsg,projectID)
		self.process_rmd_msg(rmdMsg,projectID)
		return render_template('organizer_emailSetting.html',invMsg =invMsg, 
															rmdMsg =rmdMsg, 
															projectID = projectID,
															userType = session['userType'])
	
	def onSubmit(self,invMsg,rmdMsg,projectID):
		self.process_inv_msg(invMsg,projectID)
		self.process_rmd_msg(rmdMsg,projectID)

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
			
	# check if msg is valid
	def process_rmd_msg(self, rmdMsg,projectID):
		controller = organizer_emailSettingsController(projectID)
		if controller.check_msg(rmdMsg):
			controller.update_rmd_msg(rmdMsg,projectID)
		elif not controller.check_msg(rmdMsg):
			msg = "Remember to vote!"
			controller.update_rmd_msg(msg,projectID)

	# check if msg is valid
	def process_inv_msg(self, invMsg,projectID):
		controller = organizer_emailSettingsController(projectID)
		if controller.check_msg(invMsg):
			controller.update_inv_msg(invMsg,projectID)
		elif not controller.check_msg(invMsg):
			msg = "You are invited!"
			controller.update_inv_msg(msg,projectID)

	
	def getProjectStatus(self,projectID):
		controller = ProjectDetails(projectID)
		return controller.getStatus()
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage,'error')
		return self.displayPage(projectID)