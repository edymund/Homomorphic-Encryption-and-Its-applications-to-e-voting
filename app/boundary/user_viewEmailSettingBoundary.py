from flask import render_template, redirect, session
from ..controllers.emailSettingsController import EmailSettingsController
import json

class user_viewEmailSettingsBoundary:
	# Constructor
	def __init__(self, projectID= None):
		self.projectID = projectID
		self.rmdMsg = ""
		self.invMsg = ""

	# accessor
	def getProjID(self):
		return self.projectID

	def setProjID(self, projectID):
		self.projectID = projectID

	# Other Methods
	def displayPage(self):
		controller = EmailSettingsController(projID = self.getProjID())
		invMsg = controller.retrieve_inv_msg()
		rmdMsg = controller.retrieve_rmd_msg()
		return render_template('organizer_emailSetting.html',invMsg =json.dumps(invMsg), 
														rmdMsg =json.dumps(rmdMsg), 
														projectID = self.projectID,
														userType = session['userType'])
	
	def onSubmit(self,invMsg,rmdMsg):
		controller = EmailSettingsController(projID = self.getProjID())
		if controller.check_msg(invMsg):
			controller.update_inv_msg(invMsg)
		else: 
			self.invMsg = "This is a default message"
			controller.update_inv_msg(self.invMsg)

		if controller.check_msg(rmdMsg):
			self.rmdMsg = rmdMsg
			controller.update_rmd_msg(rmdMsg)
		else: 
			self.rmdMsg = "This is a default message"
			controller.update_rmd_msg(self.rmdMsg)

	def send_reminder(self, msg):
		controller = EmailSettingsController(projID = self.getProjID())
		if controller.check_msg(msg):
			self.rmdMsg = msg
			controller.update_rmd_msg(msg)
		else: 
			self.rmdMsg = "This is a default message"
			controller.update_rmd_msg(self.rmdMsg)
		controller.send_reminder()
