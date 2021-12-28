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

	# Other Methods
	def displayPage(self):
		controller = EmailSettingsController(projID = self.getProjID())
		invMsg = controller.retrieve_inv_msg()
		rmdMsg = controller.retrieve_rmd_msg()
		return render_template('user_emailSetting.html',invMsg =json.dumps(invMsg), rmdMsg =json.dumps(rmdMsg) )
	
	def onSubmit(self,invMsg,rmdMsg):
		controller = EmailSettingsController(projID = self.getProjID())
		if controller.check_inv_msg(invMsg):
			self.invMsg = invMsg
			controller.update_inv_msg(invMsg)
		if controller.check_rmd_msg(rmdMsg):
			self.rmdMsg = rmdMsg
			controller.update_inv_msg(rmdMsg)

	def send_reminder(self, msg):
		pass
			# display in text area
			# self.populateTextArea()
			# controller.insert_voter(self.projectID)