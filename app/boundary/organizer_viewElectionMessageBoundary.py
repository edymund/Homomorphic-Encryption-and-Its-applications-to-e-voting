from flask import render_template, flash, redirect, session
from ..entity.Projectdetails import ProjectDetails
from ..controllers.organizer_ElectionMsgController import ElectionMsgController
import json

class organizer_viewElectionMessageBoundary:
	# Constructor
	def __init__(self,projectID=None):
		self.projectID = projectID
		self.preMsg = ""
		self.postMsg = ""

	# Other Methods
	def displayPage(self,projectID):
		controller = ElectionMsgController(self.projectID)
		projectStatus = controller.getProjectStatus(projectID)
		preMsg = controller.retrieve_pre_election_msg()
		postMsg = controller.retrieve_post_election_msg()
		self.process_pre_msg(preMsg)
		self.process_post_msg(postMsg)
		return render_template('organizer_viewElectionMessage.html', preMsg = json.dumps(self.preMsg), 
																	 postMsg=json.dumps(self.postMsg), 
																	 projectID=json.dumps(int(self.projectID)),
																	 projectStatus=projectStatus,
																	 userType=session['userType'])

	def onSubmit(self, preMsg, postMsg):
		self.process_pre_msg(preMsg)
		self.process_post_msg(postMsg)

	def process_pre_msg(self, preMsg):
		controller = ElectionMsgController(projectID = self.projectID)
		if controller.check_election_msg(preMsg):
			self.preMsg = preMsg
			controller.update_pre_election_msg(preMsg)
		elif not controller.check_election_msg(preMsg):
			msg = "Enjoy your voting"
			self.preMsg = msg
			controller.update_pre_election_msg(msg)

	def process_post_msg(self, postMsg):
		controller = ElectionMsgController(projectID = self.projectID)
		if controller.check_election_msg(postMsg):
			self.postMsg = postMsg
			controller.update_post_election_msg(postMsg)
		elif not controller.check_election_msg(postMsg):
			msg = "Hope you enjoyed your vote"
			self.postMsg = msg
			controller.update_post_election_msg(msg)
	
	def getProjectStatus(self,projectID):
		controller = ProjectDetails(projectID)
		return controller.getStatus()
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage,'error')
		return self.displayPage(projectID)
