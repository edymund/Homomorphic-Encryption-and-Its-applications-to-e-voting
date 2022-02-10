from flask import render_template, redirect, session, flash
from ..controllers.organizer_emailSettingsController import organizer_emailSettingsController
import json

class organizer_emailSettingBoundary:
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
		controller = organizer_emailSettingsController(projID = self.getProjID())
		invMsg = controller.retrieve_inv_msg()
		rmdMsg = controller.retrieve_rmd_msg()
		self.process_inv_msg(invMsg)
		self.process_rmd_msg(rmdMsg)
		return render_template('organizer_emailSetting.html',invMsg =json.dumps(invMsg), 
														rmdMsg =json.dumps(rmdMsg), 
														projectID = self.projectID,
														userType = session['userType'])
	
	def onSubmit(self,invMsg,rmdMsg):
		self.process_inv_msg(invMsg)
		self.process_rmd_msg(rmdMsg)

	def send_reminder(self, msg):
		controller = organizer_emailSettingsController(projID = self.getProjID())
		if controller.check_proj_status:
			if controller.check_msg(msg):
				self.rmdMsg = msg
				controller.update_rmd_msg(msg)
			else: 
				self.rmdMsg = "Remember to vote!"
				controller.update_rmd_msg(self.rmdMsg)
			controller.send_reminder()
		else:
			flash("Project status is not ongoing, unable to send reminder","error")

	# check if msg is valid
	def process_rmd_msg(self, rmdMsg):
		controller = organizer_emailSettingsController(projID = self.projectID)
		if controller.check_msg(rmdMsg):
			self.preMsg = rmdMsg
			controller.update_rmd_msg(rmdMsg)
		elif not controller.check_msg(rmdMsg):
			msg = "Remember to vote!"
			self.preMsg = msg
			controller.update_rmd_msg(msg)

	# check if msg is valid
	def process_inv_msg(self, invMsg):
		controller = organizer_emailSettingsController(projID = self.projectID)
		if controller.check_msg(invMsg):
			self.postMsg = invMsg
			controller.update_inv_msg(invMsg)
		elif not controller.check_msg(invMsg):
			msg = "You are invited!"
			self.postMsg = msg
			controller.update_inv_msg(msg)
