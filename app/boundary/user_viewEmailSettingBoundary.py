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
		return render_template('user_emailSetting.html',invMsg =json.dumps(invMsg), rmdMsg =json.dumps(rmdMsg) )
	
	def onSubmit(self,invMsg,rmdMsg):
		controller = EmailSettingsController(projID = self.getProjID())
		if controller.check_inv_msg(invMsg):
			self.invMsg = invMsg
			controller.update_inv_msg(invMsg)
		else: 
			self.invMsg = "This is a default message"
		if controller.check_rmd_msg(rmdMsg):
			self.rmdMsg = rmdMsg
			controller.update_inv_msg(rmdMsg)
		else: 
			self.invMsg = "This is a default message"

	@staticmethod
	def retrieve_proj_details_from_url(url):
		controller = EmailSettingsController()
		proj_detail= controller.retrieve_proj_detail(url)
		return proj_detail

	def send_reminder(self, msg):
		pass
			# display in text area
			# self.populateTextArea()
			# controller.insert_voter(self.projectID)
